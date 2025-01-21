import pytest
from datetime import datetime
from app.models.document import Document

@pytest.fixture
def minimal_valid_document():
    """
    The absolute minimum valid document - useful for testing basic validation
    Only includes required fields with valid minimal content
    """
    fixed_time = datetime(2025, 1, 1, 12, 0, 0)
    return Document(
        title="Test",  # Minimal valid title
        content="Content",  # Minimal valid content
        document_type="article",
        created_at=fixed_time,
        updated_at=fixed_time,
        tags=[]  # Empty tags are valid
    )
    
@pytest.fixture
def maximum_document():
    """
    Document with maximum allowed values - tests upper boundaries
    Like a book that's right at the library's size limit
    """
    fixed_time = datetime(2025, 1, 1, 12, 0, 0)
    return Document(
        title="T" * 200,  # Maximum title length
        content="C" * 10000,  # Maximum content length
        document_type="article",
        created_at=fixed_time,
        updated_at=fixed_time,
        tags=["tag1", "tag2", "tag3", "tag4", "tag5"]  # Maximum tags
    )
    
@pytest.fixture
def special_characters_document():
    """
    Document with special characters - tests text handling
    Like a book with unusual characters in its title
    """
    fixed_time = datetime(2025, 1, 1, 12, 0, 0)
    return Document(
        title="Test's Document with «special» characters!",
        content="Content with émojis 🌟 and unicode characters ©",
        document_type="article",
        created_at=fixed_time,
        updated_at=fixed_time,
        tags=["special!", "test&", "unicode©"]
    )