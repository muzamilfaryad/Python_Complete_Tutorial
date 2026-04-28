# Pytest - Unit Testing Project

This is a complete course with projects.

A comprehensive project demonstrating unit testing and test-driven development using pytest framework.

## 📚 Overview

This project showcases:
- Unit testing with pytest
- Test-driven development (TDD)
- Mocking and fixtures
- Test organization
- Code coverage
- Testing best practices
- Service layer testing
- Database testing

## 🎯 Features

✅ Unit tests with pytest  
✅ Test fixtures and setup/teardown  
✅ Mocking external dependencies  
✅ Test organization and structure  
✅ Assertions and error testing  
✅ Database testing  
✅ Code coverage analysis  
✅ Integration tests  

## 📂 Project Structure

```
pytest/
├── main.py              # Main application code
├── service.py           # Service layer
├── db.py                # Database operations
├── test_main.py         # Tests for main.py
├── test_service.py      # Tests for service.py
├── test_db.py           # Tests for db.py
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- pytest
- pytest-mock (for mocking)
- pytest-cov (for coverage)

### Installation

1. Navigate to project:
```bash
cd pytest
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install pytest and dependencies:
```bash
pip install pytest pytest-mock pytest-cov
```

4. Run tests:
```bash
pytest
```

## 🧪 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest test_main.py
```

### Run specific test function:
```bash
pytest test_main.py::test_function_name
```

### Run with verbose output:
```bash
pytest -v
```

### Run with coverage report:
```bash
pytest --cov=. --cov-report=html
```

### Run with markers:
```bash
pytest -m unit
pytest -m integration
```

### Stop on first failure:
```bash
pytest -x
```

### Show print statements:
```bash
pytest -s
```

## 📊 Test Files Overview

### test_main.py
Tests for main application functions

**Test Examples:**
- Basic function behavior
- Input validation
- Edge cases
- Error conditions
- Return values

### test_service.py
Tests for service layer

**Test Examples:**
- Service operations
- Data transformations
- Business logic
- Error handling
- Dependencies

### test_db.py
Tests for database operations

**Test Examples:**
- Database queries
- CRUD operations
- Data integrity
- Transaction handling
- Connection management

## 🛠️ Testing Patterns

### 1. Basic Test
```python
def test_addition():
    assert 2 + 2 == 4
```

### 2. Test with Setup/Teardown
```python
@pytest.fixture
def setup_data():
    data = [1, 2, 3]
    yield data
    # Cleanup here if needed

def test_with_fixture(setup_data):
    assert len(setup_data) == 3
```

### 3. Test with Mocking
```python
def test_with_mock(mocker):
    mock_func = mocker.patch('module.function')
    mock_func.return_value = 'mocked'
    
    result = function_using_mock()
    assert result == 'mocked'
```

### 4. Parametrized Tests
```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### 5. Exception Testing
```python
def test_exception():
    with pytest.raises(ValueError):
        function_that_raises()
```

## 📚 Pytest Features

### Fixtures
Reusable test setup:
```python
@pytest.fixture
def user_data():
    return {"name": "John", "email": "john@example.com"}

def test_user(user_data):
    assert user_data["name"] == "John"
```

### Markers
Categorize and select tests:
```python
@pytest.mark.unit
def test_unit():
    pass

@pytest.mark.integration
def test_integration():
    pass
```

### Parametrization
Test multiple inputs:
```python
@pytest.mark.parametrize("x,y", [(1, 2), (2, 3), (3, 4)])
def test_add(x, y):
    assert x + y == x + y
```

### Mocking
Mock external dependencies:
```python
def test_with_mock(mocker):
    mock = mocker.patch('module.function')
    # Test with mock
```

## 🔍 Coverage Analysis

Generate coverage report:
```bash
pytest --cov=. --cov-report=html
```

View coverage:
```bash
# Open htmlcov/index.html in browser
```

### Coverage Metrics
- **Line Coverage**: Percentage of executed lines
- **Branch Coverage**: Percentage of conditional branches tested
- **Function Coverage**: Percentage of functions tested

## 🎓 Testing Best Practices

### Naming Conventions
- Test functions start with `test_`
- Test files start with `test_` or end with `_test.py`
- Descriptive test names

### Test Structure (AAA Pattern)
```python
def test_feature():
    # Arrange - setup test data
    data = [1, 2, 3]
    
    # Act - perform action
    result = process(data)
    
    # Assert - verify result
    assert result == expected
```

### Test Isolation
- Each test is independent
- No shared state between tests
- Clean setup and teardown

### Assertion Messages
```python
assert user.age == 21, "User age should be 21"
```

### Avoid Common Mistakes
- Don't test implementation details
- Don't create test interdependencies
- Don't skip assertions
- Don't hardcode values unnecessarily

## 📖 Code Examples

### Testing Main Functions
```python
# main.py
def add(a, b):
    return a + b

# test_main.py
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

### Testing with Fixtures
```python
@pytest.fixture
def db():
    # Setup
    database = Database()
    yield database
    # Teardown
    database.close()

def test_db_query(db):
    result = db.query("SELECT * FROM users")
    assert len(result) > 0
```

### Testing Exceptions
```python
def test_invalid_input():
    with pytest.raises(ValueError):
        parse_int("not a number")
```

## 🚀 Common Commands

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run specific test
pytest test_main.py::test_function

# Run tests matching name
pytest -k "test_add"

# Generate coverage
pytest --cov=.

# Generate HTML coverage report
pytest --cov=. --cov-report=html

# Run tests with markers
pytest -m unit
```

## 🧪 Test Organization

```
pytest/
├── test_main.py          # Unit tests
├── test_service.py       # Service tests
├── test_db.py            # Database tests
├── conftest.py           # Shared fixtures (optional)
└── fixtures/             # Test data files
    └── sample_data.json
```

## 🔧 Configuration (pytest.ini)

```ini
[pytest]
testpaths = .
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

## 📊 Test Types

### Unit Tests
- Test individual functions
- Fast and isolated
- No external dependencies

### Integration Tests
- Test components together
- Include database, APIs
- Slower than unit tests

### Fixture vs Mock
- **Fixture**: Real test data/setup
- **Mock**: Simulated dependencies

## 🎯 Testing Workflow

1. **Write Test First** (TDD)
2. **Run Test** (should fail)
3. **Write Code** (make test pass)
4. **Refactor** (improve code)
5. **Run All Tests** (ensure nothing broke)

## 📈 Coverage Goals

- **Line Coverage**: 80%+ minimum
- **Branch Coverage**: 75%+ minimum
- **Critical Code**: 100% coverage

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| pytest not found | Install: `pip install pytest` |
| Import errors | Add project to PYTHONPATH |
| Fixture not found | Define in same file or conftest.py |
| Mock not working | Check patch target path |

## 📚 Resources

- Pytest Documentation: https://docs.pytest.org/
- Testing with pytest: https://pragprog.com/titles/bopytest/python-testing-with-pytest/
- Real Python: https://realpython.com/pytest-python-testing/

## 🎓 Learning Topics

✅ Pytest basics  
✅ Test organization  
✅ Fixtures and setup  
✅ Mocking and patching  
✅ Assertions  
✅ Exception testing  
✅ Parametrization  
✅ Coverage analysis  
✅ Test-driven development  
✅ Integration testing  

## 🚀 Next Steps

1. Run existing tests: `pytest`
2. Read test files to understand patterns
3. Write new tests for features
4. Use mocking for external dependencies
5. Generate coverage reports
6. Aim for high coverage
7. Practice TDD approach

## 📝 Notes

- Pytest is powerful and flexible
- Use fixtures for test setup
- Mock external dependencies
- Keep tests focused and simple
- Test both happy and error paths
- Maintain test independence

---

**Happy Testing! ✅**
