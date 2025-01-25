import pytest
import asyncio
import tempfile
import shutil
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
    print("\nDebug: Creating temp directory")  # Debug
    temp_dir = tempfile.mkdtemp()
    print(f"Debug: Created directory: {temp_dir}")  # Debug
    try:
        # Crete path with specific suffix
        file_path = Path(temp_dir) / "test_file.txt"
        print(f"Debug: Created path: {file_path}")  # Debug
        yield file_path
    except OSError as e:
        print(f"Error creating temporary file: {e}")
    finally:
        # Only clean up after test is completely done
        print(f"Debug: Cleaning up directory: {temp_dir}")  # Debug
        shutil.rmtree(temp_dir)

@pytest.fixture
def mock_document_data():
    """Generate mock data for document testing"""
    try:
        # Create mock document data
        return {
            "title": "Test Document",
            "content": "# Test Content\nThis is test content.",
            "document_type": "article",
            "created_at": "2025-01-01T12:00:00",
            "updated_at": "2025-01-01T12:00:00",
            "tags": ["test", "mock"]
        }
    except Exception as e:
        print(f"Error creating mock document data: {e}")

@pytest.fixture
def file_cleanup():
    """Cleanup utility for removing test files"""
    created_files = []
    
    def cleanup_file(file_path: Path):
        # Add file to cleanup list
        created_files.append(file_path)
        #delete immediately
        try:
            file_path.unlink(missing_ok=True)
        except OSError as e:
            pytest.warn(f"Error deleting {file_path}: {e}")
        # Return file path for convenient chaining
        return file_path
    
    yield cleanup_file
    
    # After test: Remove all created files
    for file_path in created_files:
        try:
            file_path.unlink(missing_ok=True)
        except OSError as e:
            pytest.warn(f"Error deleting {file_path}: {e}")
        

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