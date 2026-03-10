# Error Handling in Python

Comprehensive guide to exception handling best practices. See SKILL.md for quick reference.

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── TypeError
    ├── ValueError
    └── ... (your custom exceptions)
```

## The try-except Pattern

### Basic Structure

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except SpecificException as e:
    # Handle specific exception
    logger.error(f"Operation failed: {e}")
    result = fallback_value
else:
    # Runs if no exception (optional)
    logger.info("Success!")
finally:
    # Always runs (cleanup)
    cleanup_resources()
```

### Catching Specific Exceptions

```python
# GOOD: Catch specific exceptions
try:
    file = open(path)
    data = file.read()
except FileNotFoundError:
    logger.error(f"File not found: {path}")
    return None
except PermissionError:
    logger.error(f"Permission denied: {path}")
    return None

# BAD: Bare except catches everything (including KeyboardInterrupt!)
try:
    do_something()
except:
    pass  # NEVER do this

# BAD: Catching Exception is too broad
try:
    do_something()
except Exception:
    pass  # Silently swallows most errors
```

### Multiple Exception Handlers

```python
# Group related exceptions
try:
    connect_to_database()
except (ConnectionError, TimeoutError) as e:
    logger.warning(f"Connection failed: {e}")
    retry_later()
except AuthenticationError as e:
    logger.error(f"Auth failed: {e}")
    raise  # Re-raise - caller should handle
```

## Custom Exceptions

### Creating Custom Exceptions

```python
# Simple custom exception
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

# With additional context
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, required: float):
        self.balance = balance
        self.required = required
        super().__init__(
            f"Insufficient funds: have ${balance:.2f}, need ${required:.2f}"
        )

# Exception hierarchy
class AppError(Exception):
    """Base exception for application errors."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class ConnectionError(DatabaseError):
    """Connection to database failed."""
    pass
```

### When to Create Custom Exceptions

```python
# DO: For domain-specific errors
class PaymentDeclinedError(Exception):
    def __init__(self, reason: str, retry_after: int | None = None):
        self.reason = reason
        self.retry_after = retry_after

# DON'T: When built-in exceptions work fine
# Just use ValueError for invalid input
def set_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be negative")
```

## Exception Chaining

```python
# Use 'raise ... from' to preserve context
def load_config(path: str) -> Config:
    try:
        with open(path) as f:
            return parse_config(f.read())
    except FileNotFoundError as e:
        raise ConfigError(f"Config file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config: {path}") from e

# Use 'from None' to hide implementation details
def get_user(user_id: int) -> User:
    try:
        return database.query(User).get(user_id)
    except SQLAlchemyError as e:
        raise UserNotFoundError(user_id) from None
```

## Context Managers for Cleanup

### Using with Statements

```python
# Automatic resource cleanup
with open("file.txt") as f:
    content = f.read()
# File automatically closed, even if exception raised

# Database transactions
with database.transaction():
    db.insert(user)
    db.insert(profile)
    # Auto-rollback on exception, auto-commit on success
```

### Creating Custom Context Managers

```python
from contextlib import contextmanager

@contextmanager
def timer(name: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        logger.info(f"{name} took {elapsed:.2f}s")

# Usage
with timer("database_query"):
    results = db.query("SELECT * FROM users")
```

## Re-raising Exceptions

```python
# Log and re-raise
try:
    process_data(data)
except ProcessingError as e:
    logger.error(f"Failed to process: {e}")
    raise  # Re-raise the same exception

# Wrap and re-raise
try:
    response = requests.get(url)
except requests.RequestException as e:
    raise ApiError(f"API call failed: {url}") from e
```

## Anti-Patterns to Avoid

### 1. Silent Failures

```python
# BAD: Silent failure
try:
    save_to_database(data)
except Exception:
    pass  # Data lost silently!

# GOOD: At least log it
try:
    save_to_database(data)
except DatabaseError as e:
    logger.error(f"Failed to save: {e}")
    raise
```

### 2. Catching Too Broad

```python
# BAD
try:
    complex_operation()
except Exception:  # Catches way too much
    pass

# GOOD
try:
    complex_operation()
except (ValueError, KeyError) as e:
    handle_known_error(e)
```

### 3. Using Exceptions for Flow Control

```python
# BAD: Using exceptions for normal flow
def find_user(user_id: int) -> User:
    try:
        return database.get(User, user_id)
    except NotFoundError:
        return None

# GOOD: Use explicit checks
def find_user(user_id: int) -> User | None:
    return database.get(User, user_id)  # Returns None if not found
```

### 4. Finally with Return

```python
# BAD: finally overrides return
def bad():
    try:
        return "from try"
    finally:
        return "from finally"  # This is returned!

# GOOD: Avoid return in finally
def good():
    try:
        return "from try"
    finally:
        cleanup()  # Just cleanup, no return
```

## Best Practices Summary

| Practice | Example |
|----------|---------|
| Catch specific | `except ValueError` not `except Exception` |
| Never bare except | Always specify exception type |
| Log exceptions | `logger.error(f"Failed: {e}")` |
| Chain with context | `raise NewError() from original_error` |
| Use finally for cleanup | `finally: close_connection()` |
| Create domain exceptions | `class PaymentError(Exception): pass` |
| Re-raise when appropriate | `except Error as e: log(e); raise` |
| Use context managers | `with open(path) as f:` |
