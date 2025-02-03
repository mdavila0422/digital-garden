from datetime import datetime
from typing import List, Optional, ClassVar, Set, Any
from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict
from enum import Enum
from uuid import UUID, uuid4

class RelationshipStrength(float, Enum):
    """
    Defines the strength of connections between documents
    Using float values allows for more nuanced relationship scoring
    """
    STRONG = 1.0    # Direct, crucial connection
    MEDIUM = 0.6    # Important, but not crucial
    WEAK = 0.3      # Tangential connection
    ARCHIVED = 0.1  # Historical connection, kept for reference

class RelationshipType(str, Enum):
    """
    Defines the type of relationship between documents
    Using string enum makes these easy to serialize and understand
    """
    PREREQUISITE = "prerequisite"
    BUILDS_UPON = "builds_upon"
    REFERENCES = "references"
    INSPIRED_BY = "inspired_by"
    CONTRADICTS = "contradicts"
    
class DocumentReference(BaseModel):
    """
    Represents a connection between documents
    Think of this like a bridge between two documents with properties
    describing the nature of their connection.
    """
    document_id: str
    relationship_type: RelationshipType #prerequisite, builds_upon, references
    description: Optional[str] = Field(default=None, max_length=1000)
    relevance_score: float = Field(
        default=RelationshipStrength.WEAK.value,
        ge=0.0,
        le=1.0
    )
    created_at: datetime = Field(default_factory=datetime.now)
    last_accessed: datetime = Field(default_factory=datetime.now)
    is_archived: bool = False
    access_count: int = 0 #Track how often this relationship is traversed
    
    @field_validator("document_id")
    def validate_document_id(cls, v):
        if v == "":
            raise ValueError("Document ID cannot be empty")
        return v
    
    @field_validator("relationship_type")
    def validate_relationship_type(cls, v):
        if v == "":
            raise ValueError("Relationship type cannot be empty")
        return v
    
    @field_validator("description")
    def validate_description(cls, v):
        if v is not None and len(v) > 1000:
            raise ValueError(
                f"Description length ({len(v)} characters) cannot exceed 1000 characters. "
                "Please shorten your description."
                )
        return v
    
    @field_validator("relevance_score")
    def validate_relevance_score(cls, v):
        if v < 0 or v > 1:
            raise ValueError("Relevance score must be between 0 and 1")
        return v
    
    @field_validator("created_at")
    def validate_created_at(cls, v):
        if v == "":
            raise ValueError("Created at cannot be empty")
        if v > datetime.now():
            raise ValueError("Created at cannot be in the future")
        return v
    
    @field_validator("last_accessed")
    def validate_last_accessed(cls, v):
        if v == "":
            raise ValueError("Last accessed cannot be empty")
        if v > datetime.now():
            raise ValueError("Last accessed cannot be in the future")
        if v < ValidationInfo.data["created_at"]:
            raise ValueError("Last accessed cannot be before created at")
        return v
    
    @field_validator("access_count")
    def validate_access_count(cls, v):
        if v < 0:
            raise ValueError("Access count cannot be negative")
        return v
    
class RelationshipMetrics(BaseModel):
    """
    Tracks metadata about document relationships
    This is like a dashboard showing the health and state of document connections.
    """
    direct_connections_count: int = 0
    archived_connections_count: int = 0
    last_pruning_date: Optional[datetime] = None
    average_relevance_score: Optional[float] = None
    last_relationship_update: datetime = Field(default_factory=datetime.now)
    
    @field_validator("direct_connections_count")
    def validate_direct_connections_count(cls, v):
        if v < 0:
            raise ValueError("Direct connections count cannot be negative")
        return v
    
    @field_validator("archived_connections_count")
    def validate_archived_connections_count(cls, v):
        if v < 0:
            raise ValueError("Archived connections count cannot be negative")
        return v
    
    @field_validator("last_pruning_date")
    def validate_last_pruning_date(cls, v):
        if v > datetime.now():
            raise ValueError("Last pruning date cannot be in the future")
        if v < ValidationInfo.data["created_at"]:
            raise ValueError("Last pruning date cannot be before created at")
        return v
    
    @field_validator("average_relevance_score")
    def validate_average_relevance_score(cls, v):
        if v < 0 or v > 1:
            raise ValueError("Average relevance score must be between 0 and 1")
        return v    
    
    @field_validator("last_relationship_update")
    def validate_last_relationship_update(cls, v):
        if v == "":
            raise ValueError("Last relationship update cannot be empty")
        if v > datetime.now():
            raise ValueError("Last relationship update cannot be in the future")
        return v


class Document(BaseModel):
    """
    Docment model representing a single document in the digital garden.
    
    Atrributes:
        title: The title of the document
        content: The content of the document
        created_at: The timestamp the document was created
        updated_at: The timestamp the document was last updated
        tags: A list of tags associated with the document
        document_type: The type of the document (article, note, etc.)
    """
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    tags: List[str] = Field(default_factory=list)
    document_type: str
    
    Config: ClassVar[ConfigDict] = ConfigDict(
        json = {
            "encoders" : {
                datetime: lambda v: v.isoformat()
            }
        }
    )
    
    #Define valid document types
    VALID_DOCUMENT_TYPES: ClassVar[Set[str]] = {"article", "note", "journal", "project"}

    @field_validator("document_type")
    def validate_document_type(cls, value):
        """Ensure document_type is one of the valid types"""
        if value not in cls.VALID_DOCUMENT_TYPES:
            raise ValueError(f"Invalid document type: {cls.VALID_DOCUMENT_TYPES}")
        return value
    
    @field_validator("updated_at")
    def validate_updated_at(cls, v, values: ValidationInfo):
        """Ensure updated_at is not before created_at"""
        if 'created_at' in values.data and v < values.data['created_at']:
            raise ValueError("updated_at cannot be before created_at")
        return v
    
    @field_validator("tags")
    def validate_tags(cls, v):
        """Ensure tags are unique, lowercase and stripped"""
        stripped = [tag.strip().lower() for tag in v]
        if any(tag == "" for tag in stripped):
            raise ValueError("Tags cannot be empty")
        if len(set(stripped)) != len(stripped):
            raise ValueError("Tags must be unique")
        return stripped
    
