# Digital Garden

A personal digital garden for knowledge management and learning documentation. This system serves as an evolving platform for documenting personal learning journeys, connecting knowledge across different domains, and sharing insights.

## Project Overview

The Digital Garden is designed to:
- Document personal and technical learning journeys
- Enable discovery of connections between different knowledge areas
- Showcase project development and growth
- Serve as a reference for future learning
- Facilitate knowledge sharing

## Technical Stack

- Frontend: React
- Backend: Python/FastAPI
- Database: PostgreSQL

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   .\venv\Scripts\activate
   
   # Unix or MacOS
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Testing

### Local Testing Setup

1. Ensure you're in the backend directory:
   ```bash
   cd backend
   ```

2. Install test dependencies:
   ```bash
   pip install pytest pytest-cov
   ```

3. Run tests:
   - Run all tests:
     ```bash
     pytest
     ```
   - Run with verbose output:
     ```bash
     pytest -v
     ```
   - Run with coverage report:
     ```bash
     pytest -v --cov=.
     ```
   - Run specific test file:
     ```bash
     pytest tests/unit/test_utils.py
     ```

### Test Structure
```
backend/
└── tests/
    ├── conftest.py          # Shared fixtures
    └── unit/
        ├── test_basic.py    # Basic test examples
        ├── test_document_models.py  # Document model tests
        └── test_utils.py    # Utility function tests
```

### Continuous Integration

Tests are automatically run via GitHub Actions when:
- Creating a pull request to the main branch
- Pushing to the main branch
- Manually triggering the workflow

The CI pipeline:
- Runs tests against Python 3.10, 3.11, and 3.12
- Generates test coverage reports
- Uploads coverage data to Codecov

### Adding New Tests

1. Create new test files in the appropriate directory under `tests/`
2. Use existing fixtures from `conftest.py` or add new ones as needed
3. Run tests locally to verify before pushing
4. Ensure test names are descriptive and follow the `test_*` pattern

## Project Structure

```
digital-garden/
├── backend/               # Python/FastAPI backend
│   ├── app/
│   ├── tests/
│   └── main.py
├── frontend/             # React frontend
└── docs/                 # Project documentation
```

## Contributing

1. Create a feature branch from main
2. Make your changes
3. Run tests locally to verify changes
4. Create a pull request to main
5. Ensure all CI checks pass