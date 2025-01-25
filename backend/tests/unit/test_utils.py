import pytest
import json
from pathlib import Path

def test_document_file_operations(temp_file_path: Path, mock_document_data: dict, file_cleanup: callable):
    """Test document file operations using all utility fixtures"""
    # Test file creation and deletion
    try:
        # 1. Setup
        test_file = temp_file_path
        print(f"Debug: Starting test with file: {test_file}")
        
        # 2. Ensure parent directory exists
        test_file.parent.mkdir(parents=True, exist_ok=True)
        
        # 3. Write operation
        with open(test_file, "w") as f:
            json.dump(mock_document_data, f)
            f.flush()  # Force write to disk
            print("Debug: Write operation complete")
        
        print("Debug: File handle closed")
        print(f"Debug: Checking existence after write: {test_file.exists()}")
        
        # 4. Verify file exists
        assert test_file.exists(), "File should exist after writing"
        assert test_file.stat().st_size > 0, "File should have content"
        
        # 5. Read and verify content
        with open(test_file, "r") as f:
            loaded_data = json.load(f)
            print("Debug: Successfully read file")
        
        # 6. Verify data
        assert loaded_data["title"] == mock_document_data["title"]
        assert loaded_data["content"] == mock_document_data["content"]
        assert loaded_data["tags"] == mock_document_data["tags"]
        print("Debug: Data verification complete")
        
        # 7. Cleanup
        file_cleanup(test_file)
        #test_file.unlink(missing_ok=True)
        assert not test_file.exists(), "File should be cleaned up"
        
    except Exception as e:
        print(f"Debug: Test failed with error: {str(e)}")
        pytest.fail(f"Test failed: {str(e)}")