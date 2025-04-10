# System Component Requirements Template

## Initial Understanding Check
I am writing a validation service that will check whether documents have been filled in correctly and will provide a user friendly error message when there is an error.

### What is it?
The validation service is a series of methods that will check each field in the document, or documents in the case of bulk uploads, and will return all the error messages that are found. 

### What does it do?
The validation service handles occasions when a single document is uploaded, when multiple documents are uploaded at once and when a document is modified. The service will gather all errors found and return a user friendly error message to notify users about the errors in their documentation and how to fix it.

### Why is it needed?
I am trying to maintain strict formats for my documents so I need to enforce these document rules and I need to communicate with users what is allowed and what isn't.

## Technical Requirements

### Core Functionality
- Primary Functions:
  * Single document error handling
  * Bulk document upload handling
  * Document modification error handling
  * Error Formatting
  * Collect all errors instead of stopping at first error
- Input Requirements:
  * Document objects
  * Document formats expected
- Output Requirements:
  * TODO - Define [What comes out]
  * TODO - Define [Required formats]

### Integration Points
- Upstream Dependencies:
  * A filled in Document object is fed to the validation service
  * Document class object is required
- Downstream Consumers:
  * React will use this but not sure if other parts of the backend need to be involved.
  * The error messages should be displayed to the users through the UI so these messages need to be passed over to React 

### Constraints & Limitations
- Technical Constraints:
  * Using python pydantic library for ValidationError
  * Should be fairly quick
- Business Constraints:
  * [Time limitations]
  * [Resource constraints]
- Known Limitations:
  * [What it won't do]
  * [Accepted trade-offs]

## Assumption Testing

### Core Assumptions
[List each assumption about how the component should work]
1. [Assumption 1]
   - Why I believe this
   - How to validate
2. [Assumption 2]
   - Why I believe this
   - How to validate

### Knowledge Gaps
[List areas where you need more information]
1. How will we pass this error message to the user on the front end?
   - Understanding how this validation service outputs error messages will inform our design of the error messaging display in React UI. 
   - Research how the python backend communicates with a React frontend
2. How will we handle multiple error messages across multiple documents during bulk upload?
   - The bulk upload of documents will likely be a common user experience and when multiple documents are uploaded at once the likelihood of an error in the document goes up. That means this will be a common 
   - How to investigate

## Implementation Planning

### Development Approach
- Component Structure:
  * [High-level design]
  * [Key classes/functions]
- Testing Strategy:
  * [Test requirements]
  * [Validation approach]

### Risk Assessment
- Technical Risks:
  * [What could go wrong]
  * [Mitigation strategies]
- Integration Risks:
  * [Potential system impacts]
  * [Mitigation strategies]

## Ready to Code Checklist
□ Core purpose clearly understood
□ Main functionalities defined
□ Integration points identified
□ Key assumptions documented
□ Knowledge gaps addressed
□ Basic structure outlined
□ Risks considered
□ Test strategy defined

## Notes
- Questions that arose during planning:
  1. How will multiple errors be displayed?
  1. What exactly is the output of the validation service?
    1. Should the output be a list of dictionaries or a list of error strings?
    1. When there are multiple errors we need to organize the error messages appropriately so that users will know which field went wrong and which document produced the error.
  1. How will we pass this error message to the user on the front end?
  1. How will we handle multiple error messages across multiple documents during bulk upload?
- Ideas for future enhancement:
- Related components to consider:
  1. Could I not just provide an error message on the React Frontend for each individual document field as it's being filled out? Although this would not be available for bulk updates.


Remember: The goal is to surface assumptions and gaps before coding begins. Take time to question your understanding and validate your assumptions.