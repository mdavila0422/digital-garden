# Implement Document Models using Pydantic

Implement core document models and schemas for the Digital Garden backend.

## Technical Requirements
- Pydantic v2.x
- Python type hints
- FastAPI model integration
- JSON Schema support
- Markdown content handling

## Learning Goals
- Master Pydantic model design and validation
- Understand type hints and their benefits
- Learn model inheritance and composition
- Understand FastAPI's data validation
- Learn about JSON Schema and OpenAPI integration

## Tasks
- [x] Create base models
  - Create BaseDocument model
  - Implement metadata fields
  - Add timestamp handling
  - Set up version control fields
  
- [ ] Implement content models
  - Create Markdown content model
  - Add content validation
  - Implement content parsing utilities
  - Add content type enumeration
  
- [ ] Create relationship models
  - Implement document references
  - Create tag model
  - Add category model
  - Implement relationship types
  
- [ ] Add input/output schemas
  - Create document creation schema
  - Implement update schemas
  - Add response models
  - Create list response schemas
  
- [ ] Implement validation rules
  - Add custom validators
  - Implement field constraints
  - Create validation error messages
  - Add example values

## Definition of Done
- [ ] All models implemented and tested
- [ ] Custom validators working correctly
- [ ] JSON Schema generation verified
- [ ] OpenAPI documentation updated
- [ ] Example usage documented
- [ ] Type hints properly implemented
- [ ] Model relationships tested
- [ ] Input/output schemas validated

## Resources
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Data Declaration](https://fastapi.tiangolo.com/tutorial/body/)
- [Python Type Hints Guide](https://docs.python.org/3/library/typing.html)
- [JSON Schema Reference](https://json-schema.org/)


## Resources
<!-- Add helpful links and references -->
- [Link to relevant documentation]
- [Tutorial references]
- [Related issues/PRs]
- [pytest-best practices](https://pytest-with-eric.com/pytest-best-practices/pytest-ini/)

## Learning Notes
<!-- Use this section to document learnings as you work -->
### Challenges Encountered
- Challenges reconciling differences between different document model implementations
- Challenge coming up with validators for relationship models

### Key Insights
- Bulk operations and validation features two main approaches
  - Stop processing immediately when you find the first error
  - Continue processing and collect all the errors
- UUIDs benefits
  - practically unique across space and time
  - Extremely low collision probability
  - Can be generated before DB insertion
  - Works well in distributed systems
  - No need to query database to ensure uniqueness
    - Create complete objects in memory before saving them
    - Reference objects before they're stored in the database
    - Handle distributed systems more easily since each part can create valid IDs independently
    - Avoid database roundtrips just to get the next available ID
- Bulk processing of validators stores outcomes of each validation and returns complete results showing both successes and failures
- Services directory is the brain of the application
- Several key points where you'd want to validate documents:
  1. During Document Creation
  1. During Document Updates
  1. During Relationship Creation
  1. During Bulk Operations
- Common Validation Errors:
  1. Format Issues
    - Users trying to create documents with empty titles or content
    - Invalid document types
    - Malformed tags
  1. Relationship Issues:
    - Trying to create relationships to non-existant documents
    - Circular references (document A refert to B which refers back to A)
    - Invalid relationship types
  1. Temporal Issues
    - Updated timestamps that come before creation timestamps
    - Future dates in created_at or updated_at fields
    - Last accessed dates that don't make logical sense





### Questions to Research
- How are UUIDs implemented?