from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict, Optional, Any
from enum import Enum

class RelationshipStrength(float, Enum):
    """
    Enumerated values for relationship strength, making ti easier to
    categorize and understand the importance of connections
    """
    STRONG = 1.0    # Direct, crucial connection
    MEDIUM = 0.6    # Important, but not crucial
    WEAK = 0.3      # Tangential connection
    ARCHIVED = 0.1  # Historical connection, kept for reference
    
class RelationshipType(str, Enum):
    """
    Standard relationship types to ensure consistencey across the garden
    """
    PREREQUISITE = "prerequisite"
    BUILDS_UPON = "builds_upon"
    REFERENCES = "references"
    INSPIRED_BY = "inspired_by"
    CONTRADICTS = "contradicts"

class DocumentReference(BaseModel):
    """
    Represents a relationship betwen documents
    Example: Document A is 'prerequisite' for Document B
    """
    document_id: str
    relationship_type: RelationshipType #prerequisite, builds_upon, references
    description: Optional[str] = None
    relevance_score: float = Field(
        default=RelationshipStrength.WEAK.value,
        ge=0.0,
        le=1.0
    )
    created_at: datetime = Field(default_factory=datetime.now)
    last_accessed: datetime = Field(default_factory=datetime.now)
    is_archived: bool = False
    access_count: int = 0 #Track how often this relationship is traversed
    
class RelationshipMetrics(BaseModel):
    """
    Metrics to help manage and understand relationship growth
    """
    direct_connections_count: int = 0
    archived_connections_count: int = 0
    last_pruning_date: Optional[datetime] = None
    average_rlevance_score: Optional[RelationshipType] = None
    last_relationship_update: datetime = Field(default_factory=datetime.now)
    
class DocumentBase(BaseModel):
    
    title: str
    content: str
    type: str #article, learning_note, project_overview
    tags: List[str] = []
    category: Optional[str] = None
    
class Document(DocumentBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    #Dictionary where keys are relationship types and values are lists of related document Ids
    relationships: Dict[RelationshipType, List[DocumentReference]] = {}
    relationship_metrics: RelationshipMetrics = Field(default_factory=RelationshipMetrics)
    max_relationship_depth: int = 2 #Default depth limit for relationship traversal
    
    def get_related_documents(self, max_depth: int = None, min_relvance: float = 0.3):
        """
        Fetch related documents up to a certain depth, filtered by minimum relevance
        Like exploring branches of a tree, we only follow strong enough connections
        """
        depth_limit = max_depth or self.max_relationship_depth
        related_docs = {
            "direct": [],   # Depth 1 connections
            "indirect": [], # Depth 2 connections
            "archived": []  # Archived connections
        }
    
        def traverse_relationships(current_id: str, current_depth: int, visited: set):
            if current_depth > depth_limit or current_id in visited:
                return
            
            visited.add(current_id)
            for rel_type, references in self.relationships.items():
                for ref in references:
                    if ref.relevance_score >= min_relvance:
                        if current_depth == 1:
                            related_docs["direct"].append(ref)
                        else:
                            related_docs["indirect"].append(ref)
                        
                        # Recursively explore deeper connections
                        traverse_relationships(ref.document_id, current_depth + 1, visited)
            
            traverse_relationships(self.id, 1, set())
            return related_docs
    
    def update_relvance_scores(self):
        """
        Automatically update the relevance scores based on usage paterns
        This implements a "use it or lose it" approach, similar to human memory
        """
        current_time = datetime.now()
        for references in self.relationships.values():
            for ref in references:
                #Factor in recency and frequency of access
                time_factor = (current_time - ref.last_accessed).days / 365.0
                frequency_factor = min(ref.access_count / 100.0, 1.0)
                
                #Update relevance score
                ref.relevance_score = max(
                    RelationshipStrength.WEAK.value,
                    ref.relevance_score * (1.0 - time_factor) * (0.5 + 0.5 * frequency_factor)
                )
    
    def prune_relationships(self, archive_threshold: float = 0.2):
        """
        Manage relationship growth by archiving less relevant connections
        Rather than deleting, we preserve them in an archived state for potential future value.
        """
        for rel_type in RelationshipType:
            if rel_type not in self.relationships:
                continue
            
            active_relationships = []
            archived_count = 0
            
            for ref in self.relationships[rel_type]:
                if ref.relevance_score <= archive_threshold and not ref.is_archived:
                    ref.is_archived = True
                    archived_count += 1
                active_relationships.append(ref)
            
            self.relationships[rel_type] = active_relationships
            self.relationship_metrics.archived_connections_count += archived_count
            self.relationship_metrics.last_pruning_date = datetime.now()
        
                