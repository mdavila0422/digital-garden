import pytest
import asyncio
from pathlib import Path
from datetime import datetime
from app.models.document import Document

#Async Support Fixtures
@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for each test case"""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def async_client():
    """Create async test client for FastAPI app testing"""
    from main import app
    from httpx import AsyncClient
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

#Utility Fixtures
@pytest.fixture
def temp_file_path():
    """Create a temporary file path for testing file operations"""
    pass

@pytest.fixture
def mock_document_data():
    """Generate mock data for document testing"""
    pass

@pytest.fixture
def file_cleanup():
    """Cleanup utility for removing test files"""
    pass

#Document Fixtures
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