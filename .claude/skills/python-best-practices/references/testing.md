# Testing Best Practices

Comprehensive guide to testing Python code with pytest. See SKILL.md for quick reference.

## Test Organization

### Directory Structure

```
project/
├── src/
│   └── mypackage/
│       └── module.py
└── tests/
    ├── __init__.py
    ├── conftest.py           # Shared fixtures
    ├── test_module.py        # Tests for module.py
    └── integration/
        └── test_api.py       # Integration tests
```

### Naming Conventions

```python
# Test files: test_*.py or *_test.py
# Test classes: Test*
# Test functions: test_*

def test_user_creation():
    ...

class TestUserService:
    def test_create_user(self):
        ...

    def test_delete_user(self):
        ...
```

## Writing Good Tests

### Test Structure: Arrange-Act-Assert

```python
def test_transfer_between_accounts():
    # Arrange: Set up test data
    source = Account(balance=100)
    destination = Account(balance=50)
    amount = 30

    # Act: Execute the behavior
    source.transfer_to(destination, amount)

    # Assert: Verify the outcome
    assert source.balance == 70
    assert destination.balance == 80
```

### One Assertion Per Test (Guideline)

```python
# GOOD: Focused test
def test_user_email_is_lowercase():
    user = User(email="Test@Example.com")
    assert user.email == "test@example.com"

# Also OK: Related assertions
def test_user_creation():
    user = User(name="Alice", email="alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.created_at is not None
```

### Descriptive Test Names

```python
# BAD: Vague name
def test_user():
    ...

# GOOD: Describes behavior
def test_create_user_with_valid_email_succeeds():
    ...

def test_create_user_with_invalid_email_raises_validation_error():
    ...

def test_transfer_insufficient_funds_raises_error():
    ...
```

## Fixtures

### Basic Fixtures

```python
import pytest

@pytest.fixture
def user():
    return User(email="test@example.com", balance=100)

def test_user_has_balance(user):
    assert user.balance == 100

def test_user_can_spend(user):
    assert user.can_spend(50)
```

### Fixture with Cleanup

```python
@pytest.fixture
def temp_file():
    path = "/tmp/test_file.txt"
    with open(path, "w") as f:
        f.write("test content")
    yield path  # Provide to test
    # Cleanup after test
    os.remove(path)

def test_read_file(temp_file):
    content = read_file(temp_file)
    assert content == "test content"
```

### Fixture Scopes

```python
@pytest.fixture(scope="function")  # Default: new each test
def fresh_database():
    return create_test_database()

@pytest.fixture(scope="class")  # One per test class
def class_data():
    return load_test_data()

@pytest.fixture(scope="module")  # One per module
def api_client():
    return TestClient()

@pytest.fixture(scope="session")  # One per test session
def test_config():
    return load_config()
```

### Fixture Factories

```python
@pytest.fixture
def make_user():
    def _make_user(email="test@example.com", balance=100):
        return User(email=email, balance=balance)
    return _make_user

def test_with_custom_user(make_user):
    user = make_user(email="custom@example.com", balance=500)
    assert user.balance == 500
```

## Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("WORLD", "WORLD"),
    ("", ""),
    ("123", "123"),
])
def test_uppercase(input: str, expected: str):
    assert input.upper() == expected

@pytest.mark.parametrize("balance,amount,can_afford", [
    (100, 50, True),
    (100, 100, True),
    (100, 150, False),
    (0, 1, False),
])
def test_can_afford(balance: float, amount: float, can_afford: bool):
    user = User(balance=balance)
    assert user.can_afford(amount) == can_afford
```

## Mocking

### Basic Mocking

```python
from unittest.mock import Mock, patch

def test_send_notification():
    # Create mock
    mailer = Mock()
    mailer.send.return_value = True

    # Use mock
    service = NotificationService(mailer)
    result = service.notify_user(user_id=1, message="Hello")

    # Verify interactions
    assert result is True
    mailer.send.assert_called_once_with(
        to="user@example.com",
        subject="Notification",
        body="Hello"
    )
```

### Patching

```python
# Patch a function
@patch('mymodule.requests.get')
def test_fetch_user(mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "Alice"}

    user = fetch_user(1)

    assert user.name == "Alice"
    mock_get.assert_called_once_with("https://api.example.com/users/1")

# Patch as context manager
def test_with_context():
    with patch('mymodule.database.query') as mock_query:
        mock_query.return_value = [User(id=1)]
        result = get_all_users()
        assert len(result) == 1
```

### Patch Object Attributes

```python
def test_with_patch_object():
    service = UserService()

    with patch.object(service, '_send_email', return_value=True):
        result = service.register_user(email="test@example.com")

    assert result.success
```

## Testing Exceptions

```python
def test_invalid_input_raises_error():
    with pytest.raises(ValueError, match="cannot be negative"):
        create_user(age=-1)

def test_specific_exception():
    with pytest.raises(InsufficientFundsError) as exc_info:
        account.withdraw(amount=1000)
    assert exc_info.value.balance == 100
    assert exc_info.value.required == 1000
```

## Test Organization Tips

### Skip and XFail

```python
@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    ...

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_modern_syntax():
    ...

@pytest.mark.xfail(reason="Known bug #123")
def test_known_failing():
    ...
```

### Test Markers

```python
# In pytest.ini or pyproject.toml
# [tool.pytest.ini_options]
# markers = "slow: marks tests as slow"

@pytest.mark.slow
def test_integration():
    ...

# Run only fast tests: pytest -m "not slow"
```

## Best Practices Summary

| Practice | Example |
|----------|---------|
| One concept per test | `test_user_creation_sets_email()` |
| Use fixtures for setup | `@pytest.fixture def user():` |
| Mock external dependencies | `@patch('module.external_call')` |
| Test edge cases | Empty, None, negative, max |
| Parametrize similar tests | `@pytest.mark.parametrize` |
| Descriptive names | `test_X_given_Y_returns_Z()` |
| Don't test implementation | Test behavior, not internals |
| Keep tests isolated | No shared mutable state |

## Common Anti-Patterns

```python
# DON'T: Test private methods directly
def test_internal_validation():
    assert service._validate(data)  # Test public interface instead

# DON'T: Depend on test order
created_id = None
def test_create():
    global created_id
    created_id = create_user().id

def test_delete():
    delete_user(created_id)  # Fails if run out of order

# DON'T: Use production data
def test_with_real_db():
    user = db.get(1)  # What if user doesn't exist?

# DO: Use factories
def test_delete(make_user):
    user = make_user()
    delete_user(user.id)
    assert get_user(user.id) is None
```
