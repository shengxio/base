# Sample Python Application with Docker

This is a sample Python application that demonstrates a standard project structure with Docker deployment and comprehensive testing suite using pytest.

## Project Structure

```
.
├── Dockerfile              # Docker image definition
├── docker-compose.yml     # Docker compose configuration
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── .gitignore           # Git ignore patterns
├── .dockerignore        # Docker ignore patterns
├── .cursorignore        # Cursor Pro ignore patterns
├── src/                 # Source code directory
│   ├── __init__.py
│   └── app.py          # Main application code
└── tests/              # Test directory
    ├── __init__.py
    ├── conftest.py     # Shared pytest fixtures
    ├── test_app.py     # API endpoint tests
    ├── test_calculations.py  # Unit tests
    └── test_integration.py   # Integration tests
```

## Features

- Flask-based REST API
- Docker containerization
- Comprehensive test suite:
  - Unit tests
  - Integration tests
  - API endpoint tests
  - Performance benchmarks
  - Load testing
- Code coverage reporting
- Proper ignore files for Git, Docker, and Cursor Pro

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /sum/<int:a>/<int:b>` - Calculate sum of two numbers

## Getting Started

### Running with Docker

1. Build and run the application:
```bash
docker-compose up --build
```

2. Run tests in Docker:
```bash
docker-compose run app pytest
```

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/app.py
```

4. Run tests:
```bash
# Run all tests
pytest

# Run specific test types
pytest -m "not slow"  # Skip slow tests
pytest -m regression  # Run only regression tests
pytest -m benchmark  # Run only benchmark tests

# Run with coverage
pytest --cov=src

# Run tests in parallel
pytest -n auto

# Generate HTML coverage report
pytest --cov=src --cov-report=html
```

## Testing

The project includes a comprehensive test suite:

### Unit Tests (`test_calculations.py`)
- Normal case testing
- Edge case handling
- Type error validation
- Mathematical property verification
- Performance benchmarking

### API Tests (`test_app.py`)
- Endpoint testing
- HTTP method validation
- Input validation
- Response structure verification
- Error handling

### Integration Tests (`test_integration.py`)
- Complete workflow testing
- Concurrent request handling
- Load testing
- Error recovery testing
- Response header validation

## Project Configuration

### Ignore Files
- `.gitignore`: Excludes build artifacts, virtual environments, and local development files
- `.dockerignore`: Optimizes Docker builds by excluding unnecessary files
- `.cursorignore`: Prevents Cursor Pro from indexing out-of-scope content

### Test Configuration
- `pytest.ini`: Configures test discovery, markers, and reporting
- Coverage reporting enabled by default
- Benchmark configuration included
- Custom markers for test categorization

## Dependencies

- Flask 3.0.2
- pytest 8.0.0
- pytest-cov 4.1.0
- pytest-benchmark 4.0.0
- pytest-xdist 3.5.0
- pytest-timeout 2.2.0
- gunicorn 21.2.0
- requests 2.31.0

## Development Best Practices

1. Always run tests before committing:
```bash
pytest
```

2. Check code coverage:
```bash
pytest --cov=src --cov-report=term-missing
```

3. Run performance benchmarks:
```bash
pytest -m benchmark
```

4. Format code before committing:
```bash
black src tests
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run the test suite
4. Submit a pull request

## License

This project is open-source and available under the MIT License. 