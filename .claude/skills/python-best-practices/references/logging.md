# Logging Best Practices

Guide to effective logging in Python. See SKILL.md for quick reference.

## Basic Logging

### Module-Level Logger

```python
import logging

# Use __name__ for automatic hierarchy
logger = logging.getLogger(__name__)

def process_user(user_id: int) -> None:
    logger.info(f"Processing user {user_id}")
    try:
        user = fetch_user(user_id)
        logger.debug(f"Found user: {user.email}")
    except Exception as e:
        logger.error(f"Failed to fetch user {user_id}: {e}")
        raise
```

### Log Levels

| Level | When to Use |
|-------|-------------|
| DEBUG | Detailed diagnostic information |
| INFO | Normal operation events |
| WARNING | Unexpected but recoverable |
| ERROR | Error requiring investigation |
| CRITICAL | System-wide failure |

```python
logger.debug("Detailed state: %s", state)      # Dev only
logger.info("User logged in: %s", user_id)     # Normal ops
logger.warning("Rate limit approaching")        # Concern
logger.error("Database connection failed")      # Error
logger.critical("System out of memory")         # Emergency
```

## Structured Logging

### Using structlog

```python
import structlog

logger = structlog.get_logger()

# Structured logs with context
logger.info("user_logged_in", user_id=123, ip="192.168.1.1")
logger.error("payment_failed", order_id=456, error="insufficient_funds")

# Output (JSON in production):
# {"event": "user_logged_in", "user_id": 123, "ip": "192.168.1.1", "level": "info"}
```

### Configuration

```python
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer()  # Use JSONRenderer in production
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)
```

## Context and Correlation

### Request Context

```python
import structlog

def middleware(request):
    # Bind context for all logs in this request
    structlog.contextvars.bind_contextvars(
        request_id=request.headers.get("X-Request-ID"),
        user_id=request.user.id if request.user else None,
    )
    return request

# All logs in this request include context
logger.info("order_created", order_id=123)
# {"event": "order_created", "order_id": 123, "request_id": "abc", "user_id": 1}
```

### Bounded Loggers

```python
import structlog

# Create logger with bound context
log = logger.bind(user_id=123, session_id="abc")
log.info("action_performed", action="checkout")
```

## What to Log

### DO Log

```python
# Business events
logger.info("order_placed", order_id=123, total=99.99, items=5)

# State changes
logger.info("user_role_changed", user_id=1, old_role="viewer", new_role="admin")

# External integrations
logger.info("api_call", service="stripe", endpoint="charges", duration_ms=150)

# Errors with context
logger.error("payment_failed", order_id=456, reason="card_declined", amount=50.00)
```

### DON'T Log

```python
# BAD: Sensitive data
logger.info("user_login", email=user.email, password="...")  # NEVER!

# BAD: Personal identifiable information
logger.info("customer", ssn="123-45-6789", credit_card="4111...")  # NEVER!

# BAD: Authentication tokens
logger.debug("api_request", token=api_key)  # NEVER!

# BAD: Huge payloads
logger.debug("response", data=huge_json_response)  # Too much noise
```

## Performance Considerations

### Lazy Evaluation

```python
# BAD: Always evaluates expensive_operation()
logger.debug(f"Result: {expensive_operation()}")

# GOOD: Only evaluates if DEBUG is enabled
logger.debug("Result: %s", expensive_operation)

# With structlog (lazy by default)
logger.debug("result", value=lambda: expensive_operation())
```

### Conditional Logging

```python
# For expensive operations
if logger.isEnabledFor(logging.DEBUG):
    logger.debug(f"Detailed state: {expensive_serialization()}")
```

## Exception Logging

```python
try:
    risky_operation()
except SpecificError as e:
    # Include full traceback
    logger.exception("Operation failed")  # Automatically includes stack trace
    raise

# Or with structlog
except Exception as e:
    logger.error("operation_failed", error=str(e), exc_info=True)
```

## Configuration

### Basic Configuration

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Console
        logging.FileHandler("app.log"),  # File
    ]
)
```

### Production Configuration (JSON)

```python
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

## Quick Reference

### Log Level Guidelines

| Environment | Default Level |
|-------------|---------------|
| Development | DEBUG |
| Staging | INFO |
| Production | INFO or WARNING |

### Log Format (Production)

```json
{
  "timestamp": "2025-01-15T10:30:00Z",
  "level": "info",
  "logger": "myapp.service",
  "message": "order_placed",
  "request_id": "abc-123",
  "user_id": 1,
  "order_id": 456,
  "duration_ms": 150
}
```

### Checklist

- [ ] Use module-level loggers (`getLogger(__name__)`)
- [ ] Never log sensitive data
- [ ] Use structured logging in production
- [ ] Include correlation IDs for tracing
- [ ] Use lazy evaluation for expensive operations
- [ ] Configure appropriate log levels per environment
- [ ] Never use `print()` for logging
