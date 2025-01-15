Set up testing infrastructure for the project.

## Technical Requirements
- pytest framework
- pytest-cov for coverage reporting
- pytest-asyncio for async testing
- GitHub Actions for CI
- Test data generation tools

## Learning Goals
- Understanding pytest configuration and best practices
- Test fixture creation and management
- CI/CD concepts and implementation
- Test coverage analysis
- Async testing patterns in FastAPI

## Tasks
- [X] Install pytest and related packages
  - Install pytest
  - Install pytest-cov
  - Install pytest-asyncio
  - Update requirements.txt
- [X] Set up test directory structure
  - Create tests/ directory
  - Set up conftest.py
  - Create separate directories for different test types (unit, integration)
- [X] Create initial test configuration
  - Configure pytest.ini
  - Set up coverage configuration
  - Add async test support
- [ ] Add test data fixtures
  - Create basic document fixtures
  - Set up mock data generation
  - Create utility fixtures
- [ ] Set up CI workflow for tests
  - Create GitHub Actions workflow file
  - Configure test automation
  - Set up coverage reporting

## Definition of Done
- [ ] pytest and related packages have been installed successfully
- [ ] Testing directory structure created and documented
- [ ] Initial test configuration created and working
- [ ] Test data fixtures added and documented
- [ ] CI workflow documented and operational
- [ ] Minimum test coverage requirements established
- [ ] Sample tests created for each test type
- [ ] README updated with testing instructions

## Resources
- [pytest Documentation](https://docs.pytest.org/)
- [FastAPI Testing Guide](https://fastapi.tiangolo.com/tutorial/testing/)
- [GitHub Actions for Python Testing](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [pytest-asyncio Documentation](https://pytest-asyncio.readthedocs.io/)

## Resources
<!-- Add helpful links and references -->
- [Link to relevant documentation]
- [Tutorial references]
- [Related issues/PRs]
- [pytest-best practices](https://pytest-with-eric.com/pytest-best-practices/pytest-ini/)

## Learning Notes
<!-- Use this section to document learnings as you work -->
### Challenges Encountered
- Unkown pytest.mark.unit
  - pytest.ini was in the wrong directory (child of backend)
  - Need to be in backend directory to run tests
- Finding uniqueness in a list
- Creating test cases for tag list manipulation
  - Checking tag uniqueness
  - Checking tags are lowercase w/ no spaces
  - Verify you can have multiple tags
  - Check that tags aren't empty strings
- ModuleNotFoundError: No module named 'app'
  - Python doesn't know where to find the app module
- Pydantic v2 field validation
  - v2 validator function now gets ValidationInfo object instead of raw dict
  - Now need to access values usnig values.data instead of directly from values
- bitwise AND operator vs logical AND operator
  - '&' bitwise operator converts numbers into binary and compares them bit by bit
  - 'and' logical operator compare boolean values

### Key Insights
- Unit tests: Test individual functions/components in isolation
- Integration Tests: Test how components work together
- pytest.ini configuration file for pytest
- Controls pytest behavior like:
  - Test discovery patterns
  - Warning settings
  - plugins configuration
  - Custom markers
  - test timeout settings
- Fixtures
  - They're reusable - write setup once, use in many tests
  - They can be scoped (how long they last):
  - function: Fresh setup for each test (default)
  - class: Once per test class
  - module: Once per test file
  - session: Once per test run
  - They can depend on other fixtures
  - They go in conftest.py if you want to share them across multiple test files
- Model Fields (instance attributes)
  - Like having your own personal notebook
  - In our Document class, title and content are model fields bc each doc needs its own unique title and content
- Class Variable (shared across all instances)
  - Like having one whiteboard shared with the entire class
  - Writing on the board makes it visible to all instances 
- ClassVar[Set[str]] versus ClassVar[set[str]]
  - Set[str] is the formal type hint that tells type checkers "this is a set of strings"
  - set[str] is the runtime implementation
- Double underscore (dunder) methods are part of Python's protocol system

### Questions to Research
- What is a decorator?
- What is a pydantic validator?
