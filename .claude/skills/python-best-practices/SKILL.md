---
name: python-best-practices
description: Production-ready Python DOs and DON'Ts for engineers. Covers code quality, type hints, error handling, async patterns, testing, security, performance, logging, and data validation. Use when writing Python code that needs to be production-ready, reviewing Python code, refactoring legacy Python, or answering questions about Python best practices. Targets Python 3.12+.
---

# Python Best Practices (Production-Ready)

Production-grade DOs and DON'Ts for Python 3.12+.

## Quick Reference

| Topic | Key Principle |
|-------|---------------|
| [Code Quality](#1-code-quality--style) | Readable > clever |
| [Type Hints](#2-type-hints) | Type everything public |
| [Error Handling](#3-error-handling) | Catch specific, never silent |
| [Async/Await](#4-asyncawait) | Never block the event loop |
| [Testing](#5-testing) | Test behavior, not implementation |
| [Security](#6-security) | Never trust input |
| [Project Structure](#7-project-structure) | Use src layout |
| [Performance](#8-performance) | Measure first, optimize bottlenecks |
| [Logging](#9-logging) | Structured logs, appropriate levels |
| [Data Validation](#10-data-validation) | Validate at boundaries |
| [Code Review](#11-code-review-checklist) | Blockers vs improvements |

---

## 1. Code Quality & Style

**Core Principle:** Code is read more than written. Optimize for readability.

### DO

```python
# Descriptive names
def calculate_discounted_price(original_price: float, discount_rate: float) -> float:
    return original_price * (1 - discount_rate)

# Dataclasses for structured data
@dataclass
class User:
    name: str
    email: str
    created_at: datetime

# Early returns reduce nesting
def get_user(user_id: int) -> User | None:
    if not user_id:
        return None
    return database.get_user(user_id)

# Context managers for resources
with open("file.txt") as f:
    content = f.read()
```

### DON'T

```python
def calc(a, b):  # Cryptic name
    return a * b

user = {"nme": "Alice"}  # Typos silently fail

f = open("file.txt")  # Never closed
content = f.read()
```

**See `references/clean-code.md`**

---

## 2. Type Hints

**Core Principle:** Type all public interfaces.

### DO

```python
def fetch_user(user_id: int) -> User | None: ...

type UserId = int
type JsonDict = dict[str, str | int | float]

def get_items[T](items: list[T]) -> list[T]: ...

class Renderable(Protocol):
    def render(self) -> str: ...
```

### DON'T

```python
def process(data: Any) -> Any: ...  # Useless

from typing import Union
def old(x: Union[str, int]): ...  # Use str | int
```

**See `references/type-hints.md`**

---

## 3. Error Handling

**Core Principle:** Catch specific exceptions, never silent failures.

### DO

```python
try:
    result = divide(a, b)
except ZeroDivisionError:
    logger.error("Division by zero")
    return None

class InsufficientFundsError(Exception):
    def __init__(self, balance: float, required: float):
        self.balance = balance
        self.required = required

# Chain exceptions
except FileNotFoundError as e:
    raise ConfigError(f"Not found: {path}") from e
```

### DON'T

```python
try:
    do_something()
except:  # NEVER bare except!
    pass

try:
    risky_operation()
except SomeError:
    pass  # Silent failure - at least log it!
```

**See `references/error-handling.md`**

---

## 4. Async/Await

**Core Principle:** Never block the event loop.

### DO

```python
async def fetch_user(user_id: int) -> User:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"/users/{user_id}") as response:
            return await response.json()

# Concurrent operations
async def fetch_all(user_ids: list[int]) -> list[User]:
    tasks = [fetch_user(id) for id in user_ids]
    return await asyncio.gather(*tasks)

# Offload blocking work
async def process_file(path: str) -> Result:
    content = await asyncio.to_thread(read_file, path)
    return process(content)
```

### DON'T

```python
async def bad():
    time.sleep(5)  # Blocks entire event loop!
    requests.get(url)  # Also blocks!

async def broken():
    result = fetch_user(1)  # Missing await!
    return result
```

**See `references/async-patterns.md`**

---

## 5. Testing

**Core Principle:** Test behavior, not implementation.

### DO

```python
def test_user_creation_sets_email():
    user = User(email="test@example.com")
    assert user.email == "test@example.com"

@pytest.fixture
def user():
    return User(email="test@example.com", balance=100)

@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"), ("WORLD", "WORLD"), ("", ""),
])
def test_uppercase(input: str, expected: str):
    assert input.upper() == expected
```

### DON'T

```python
def test_user_has_internal_dict():
    assert user._data == {}  # Tests private implementation

def test_create_user():
    global created_user
    created_user = User()  # Shared state is fragile
```

**See `references/testing.md`**

---

## 6. Security

**Core Principle:** Never trust input. Validate at boundaries.

### DO

```python
# Parameterized queries
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Secure random
import secrets
token = secrets.token_urlsafe(32)

# Environment variables for secrets
api_key = os.environ["API_KEY"]
```

### DON'T

```python
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection!

token = str(random.random())  # Predictable!

API_KEY = "sk-abc123..."  # Hardcoded secret!

result = eval(user_expression)  # Arbitrary code execution!
```

**See `references/security.md`**

---

## 7. Project Structure

**Core Principle:** Use src layout. Organize by feature.

### DO

```
my-project/
├── src/mypackage/
│   ├── __init__.py
│   ├── core/service.py
│   ├── api/routes.py
│   └── models/user.py
├── tests/
│   └── test_service.py
├── pyproject.toml
└── README.md
```

### DON'T

```
my-project/
├── mypackage.py       # Single file for everything
├── tests.py           # Tests mixed with source
└── utils/             # Junk drawer
```

**See `references/project-structure.md`**

---

## 8. Performance

**Core Principle:** Measure first. Optimize only proven bottlenecks.

### DO

```python
# Profile first
import cProfile
cProfile.run('my_function()')

# Generators for large data
def read_large_file(path: str):
    with open(path) as f:
        for line in f:
            yield line.strip()

# Built-in functions (C-optimized)
total = sum(item.price for item in items)

# Cache expensive work
@lru_cache(maxsize=128)
def expensive_computation(n: int) -> int: ...
```

### DON'T

```python
result = ""
for s in strings:
    result += s  # O(n²) - use "".join(strings)

if item in my_list:  # O(n) - use set for O(1)
```

**See `references/performance.md`**

---

## 9. Logging

**Core Principle:** Structured logs, appropriate levels.

### DO

```python
logger = logging.getLogger(__name__)

logger.info("User logged in", extra={"user_id": user.id})

# Structured logging
import structlog
logger = structlog.get_logger()
logger.info("order_placed", order_id=123, total=99.99)
```

### DON'T

```python
print(f"User {user_id} logged in")  # Use logger

logger.info(f"Password: {password}")  # NEVER log secrets!

logger.debug(f"Result: {expensive()}")  # Always runs - use lazy eval
```

**See `references/logging.md`**

---

## 10. Data Validation

**Core Principle:** Validate at boundaries. Pydantic for external, dataclasses for internal.

### DO

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    age: int

@dataclass
class User:
    id: int
    email: str

# Validate early
def process_request(data: dict) -> Response:
    validated = UserCreate(**data)  # Fails if invalid
    return create_user(validated)
```

### DON'T

```python
def unsafe_process(data: dict):
    email = data["email"]  # KeyError if missing!

config = json.load(f)  # Untyped - use Pydantic
```

**See `references/data-validation.md`**

---

## 11. Code Review Checklist

### Blockers (Must Fix)

- [ ] **Security**: No SQL injection, hardcoded secrets, eval on user input
- [ ] **Correctness**: Logic correct, edge cases handled
- [ ] **Error Handling**: No bare except, no silent failures
- [ ] **Type Safety**: Public interfaces typed
- [ ] **Tests**: New code tested, tests pass

### Improvements (Nice to Have)

- [ ] **Naming**: Clear, reveals intent
- [ ] **Functions**: Single responsibility
- [ ] **Documentation**: Complex logic commented
- [ ] **Performance**: No obvious inefficiencies
- [ ] **DRY**: No duplicated logic

**See `references/code-review.md`**

---

## Reference Files Index

| File | Content |
|------|---------|
| `references/clean-code.md` | Naming, functions, dataclasses |
| `references/type-hints.md` | Generics, protocols, modern syntax |
| `references/error-handling.md` | Custom exceptions, cleanup |
| `references/async-patterns.md` | Event loop, TaskGroup, patterns |
| `references/testing.md` | Pytest, fixtures, mocking |
| `references/security.md` | Input validation, crypto, OWASP |
| `references/project-structure.md` | Src layout, organization |
| `references/performance.md` | Profiling, optimization |
| `references/logging.md` | Structured logging, levels |
| `references/data-validation.md` | Pydantic, dataclasses |
| `references/code-review.md` | Full checklist |
| `references/anti-patterns.md` | Common mistakes |
