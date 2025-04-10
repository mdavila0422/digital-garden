import pytest
from datetime import datetime
from app.models.document import Document
from app.services.validation_service import DocumentValidationService

def test_invalid_document():
    """
    Test invalid document with a long title name
    """
    doc = Document(
        title="T" * 201,
        content="This is a test document",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        tags=["test", "documentation"],
        document_type="article"
    )
    
    formatted_result = DocumentValidationService.validate_single_document(doc)
    
    assert formatted_result.valid_items == []
    assert formatted_result.invalid_items == [doc]
    assert formatted_result.errors == [
        "Title error. String should have at most 200 characters"
    ]
    
    print(formatted_result)
    
    