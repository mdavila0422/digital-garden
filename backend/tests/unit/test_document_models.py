import pytest
from datetime import datetime
from app.models.document import Document   # We'll create this next

def test_document_creation():
    """Test basic document creation and validation"""
    doc = Document(
        title="Test Document",
        content="This is a test document",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        tags=["test", "documentation"],
        document_type="article"
    )
    
    assert doc.title == "Test Document"
    assert "test" in doc.tags
    assert doc.document_type == "article"
    assert len(doc.title) <= 200  and len(doc.title) > 0
    assert doc.updated_at >= doc.created_at
    assert doc.content.__len__() > 0
    assert doc.document_type in doc.VALID_DOCUMENT_TYPES
    assert len(doc.tags) == len(set(doc.tags))
    assert all(tag == tag.lower().strip() for tag in doc.tags)
    assert len(doc.tags) >= 0
    assert all(len(tag.strip()) > 0 for tag in doc.tags)

def test_document_invalid_type():
    """Test document creation with invalid type raises error"""
    with pytest.raises(ValueError):
        Document(
            title="Test Document",
            content="This is a test document",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            tags=["test"],
            document_type="invalid_type"  # This should raise an error
        )
    