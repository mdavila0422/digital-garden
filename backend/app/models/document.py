from datetime import datetime
from typing import List, Optional, ClassVar, Set
from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict

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
    
