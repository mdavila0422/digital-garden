from typing import List, Dict, Optional, Any
from datetime import datetime
from uuid import UUID
from pydantic import ValidationError
from dataclasses import dataclass
from utils.string_utils import string_truncator

#First, let's import your Document model
from app.models.document import Document

@dataclass
class ValidationResult:
    """
    Stores the results of validating one or more documents.add()
    Think of this as a report card - it tells us what passed, what failed,
    and what went wrong
    """
    valid_items: List[Document]         # Documents that passed validation
    invalid_items: List[Dict[str, Any]] # Original data for failed docs
    errors: List[Dict[str, Any]]        # Detailed error information
    
class DocumentValidationService:
    """
    Handles validation of documents and their relationships
    This is like a quality control department that checks documents
    before they're allowed into our digital garden
    """
    
    def validate_single_document(self, document_data: Dict[str, Any]) -> ValidationResult:
        """
        Validates a single document
        This is used when creating or updating one document at a time
        """
        try:
            # Attempt to create a Document model from the data
            # If successful, all validation rules pass
            valid_document = Document(**document_data)
            
            #If we get here, validation passed
            return ValidationResult(
                valid_items = [valid_document], # List with our one valid document
                invalid_items = [], # Empty since nothing failed
                errors =  [] # Empty since no errors occurred
            )
            
        except ValidationError as e:
            # If we get here, validation failed
            # The ValidationError object has details about what went wrong
            formatted_error = self._format_validation_error(e)
            
            ValidationResult(
                valid_items = [], # Empty since nothing passed
                invalid_items = [document_data], # Original data that failed
                errors = [formatted_error] # What went wrong
            )
        
        
    
    def validate_documents(self, documents: List[Dict[str, Any]]) -> ValidationResult:
        """
        Validates multiple documents at once
        Used for bulk operations like importing multiple documents
        """
        pass
    
    def validate_document_update(
        self,
        document_id: UUID,
        update_date: Dict[str, Any]
    ) -> ValidationResult:
        """
        Validates updates to an existing document
        Checks if the updates would create an invalid state
        """
        pass
    
    def _format_validation_error(self, error: ValidationError) -> Dict[str, Any]:
        """
        Formats a Pydantic validation error into a more useful structure
        This helps us give clear feedback about what went wrong
        """
        def field_formatter(field: str) -> str:
            """
            Helper function to format field names
            """
            if isinstance(field, list):
                #if field exists format it
                field_name = field[0]
                if field_name == "title":
                    string_truncator(field_name, 20)
                
    
                
            #if field doesn't exist return default  
            if field is None:
                return "Missing error field"
            
                
            return string_truncator(field, 20)
        
        list_error = error.errors()
        formatted_errors = []
        
        # We can loop through the list of errors
        for error in list_error:
            error_field = error.get("loc", "Missing error field")
            error_input = error.get("input", "Missing input value")
            error_type = error["type"].replace('_', ' ')
            error_msg = error.get("msg", "Missing error message")
            error_msg = error["msg"] = f"{error_field} error. {error_msg}."

                            
            # We can use the error dict to create a formatted error message
            formatted_error = {
                "field": error["loc"][0], # Field that failed validation
                "error": error_msg, # Error message
            }
            formatted_errors.append(formatted_error)
            
        # Return a list of formatted errors
        return formatted_errors