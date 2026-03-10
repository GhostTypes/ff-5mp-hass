# Clean Code in Python

Detailed guide to writing clean, maintainable Python code. Complements the quick-reference in SKILL.md.

## Table of Contents

1. [Naming Conventions](#1-naming-conventions)
2. [Functions](#2-functions)
3. [Data Structures](#3-data-structures)
4. [Type Hints Integration](#4-type-hints-integration)
5. [Constants and Enums](#5-constants-and-enums)
6. [Documentation](#6-documentation)
7. [Code Organization](#7-code-organization)

---

## 1. Naming Conventions

### The Philosophy

Names are documentation. Code is read more than written, so names should communicate intent.

### Naming Patterns by Type

| Type | Convention | Example |
|------|------------|---------|
| Variables | `snake_case` | `user_count`, `total_price` |
| Functions | `snake_case` | `calculate_total()`, `fetch_user()` |
| Classes | `PascalCase` | `UserAccount`, `OrderProcessor` |
| Constants | `UPPER_SNAKE` | `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT` |
| Private attributes | `_leading_underscore` | `_internal_cache`, `_validate()` |
| Name mangling | `__double_underscore` | `__private_var` (use sparingly) |

### Good vs Bad Names

```python
# BAD: Cryptic, vague, misleading
d = 86400  # What is this?
def process(x): pass  # Process what?
data = get_data()  # What data?
lst = []  # Avoid abbreviations

# GOOD: Clear, specific, self-documenting
SECONDS_PER_DAY = 86400
def calculate_order_total(items: list[OrderItem]) -> float: pass
active_users = get_active_users()
pending_orders = []
```

### Boolean Naming

```python
# GOOD: Use is_, has_, can_, should_ prefixes
is_active = True
has_permission = False
can_edit = check_permission(user)
should_retry = attempt < MAX_RETRIES

# BAD: Unclear boolean names
active = True  # Is it active? Or an active thing?
flag = False  # Flag for what?
status = 1  # What does 1 mean?
```

### Avoiding Name Shadowing

```python
# BAD: Shadows built-in
list = [1, 2, 3]  # Now you can't use list()
max = 100  # Shadows built-in max()
type = "user"  # Shadows type()

# GOOD: Use descriptive alternatives
user_list = [1, 2, 3]
max_count = 100
user_type = "user"
```

---

## 2. Functions

### Single Responsibility Principle

Each function should do ONE thing well.

```python
# BAD: Multiple responsibilities
def process_order(order):
    # Validation
    if not order.get("items"):
        raise ValueError("Empty order")
    # Business logic
    if order["customer_type"] == "premium":
        for item in order["items"]:
            item["price"] *= 0.9
    # Calculation
    total = sum(item["price"] for item in order["items"])
    # I/O
    print(f"Order: {order['id']} - Total: {total}")
    send_email(order["email"], f"Total: {total}")

# GOOD: Single responsibility
def validate_order(order: dict) -> None:
    if not order.get("items"):
        raise ValueError("Empty order")

def apply_premium_discount(order: Order) -> None:
    if order.customer_type == "premium":
        order.apply_discount(0.1)

def calculate_total(order: Order) -> float:
    return sum(item.price for item in order.items)

def send_order_confirmation(order: Order) -> None:
    notify_user(order.user_email, f"Order confirmed: {order.total}")

def process_order(order: Order) -> None:
    validate_order(order)
    apply_premium_discount(order)
    order.total = calculate_total(order)
    send_order_confirmation(order)
```

### Function Length Guidelines

- **Ideal**: 5-15 lines
- **Warning zone**: 20-30 lines
- **Refactor needed**: 40+ lines

### Parameter Guidelines

```python
# BAD: Too many parameters
def create_user(name, email, age, address, phone, role, department, manager):
    pass

# GOOD: Use dataclass/Pydantic for grouped parameters
@dataclass
class UserCreate:
    name: str
    email: str
    age: int
    address: Address | None = None
    phone: str | None = None
    role: Role = Role.VIEWER
    department: str | None = None
    manager: str | None = None

def create_user(user_data: UserCreate) -> User:
    pass
```

### Avoid Side Effects

```python
# BAD: Hidden side effect
def get_user_name(user_id: int) -> str:
    user = db.get(user_id)
    user.last_accessed = datetime.now()  # Side effect!
    db.save(user)
    return user.name

# GOOD: Explicit side effect
def get_user_name(user_id: int) -> str:
    return db.get(user_id).name

def touch_user(user_id: int) -> None:
    """Update last_accessed timestamp"""
    user = db.get(user_id)
    user.last_accessed = datetime.now()
    db.save(user)
```

---

## 3. Data Structures

### Use Dataclasses for Structured Data

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    preferences: dict = field(default_factory=dict)

    def __post_init__(self):
        self.email = self.email.lower()

# Usage
user = User(name="Alice", email="Alice@Example.com")
print(user.email)  # "alice@example.com"
```

### When to Use What

| Use Case | Recommended Type |
|----------|-----------------|
| Internal data models | `@dataclass` |
| API boundaries | Pydantic `BaseModel` |
| Configuration | Pydantic `BaseModel` or `@dataclass` |
| Simple value container | `NamedTuple` |
| Heterogeneous collection | `TypedDict` |

---

## 4. Type Hints Integration

### Public vs Private Typing

```python
# Public methods: Always type
def fetch_user(user_id: int) -> User | None:
    ...

# Private methods: Optional but encouraged
def _validate(self, data):  # OK to skip for simple private methods
    return data is not None

# All methods in library code: Always type
```

### Common Type Patterns

```python
from typing import TypeAlias, Protocol, TypeVar, Generic

# Type aliases for clarity
type UserId = int
type JsonDict = dict[str, str | int | float]

# Generic functions
T = TypeVar('T')

def first_or_none(items: list[T]) -> T | None:
    return items[0] if items else None

# Protocols for duck typing
class Serializable(Protocol):
    def to_dict(self) -> dict: ...
    def from_dict(cls, data: dict) -> "Serializable": ...
```

---

## 5. Constants and Enums

### Eliminate Magic Values

```python
# BAD: Magic numbers and strings
if status == 3:
    process()

if user.role == "admin":
    grant_access()

time.sleep(300)

# GOOD: Named constants
class OrderStatus(IntEnum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3
    CANCELLED = 4

class Role(StrEnum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

BACKOFF_DELAY_SECONDS = 300

if status == OrderStatus.COMPLETED:
    process()

if user.role == Role.ADMIN:
    grant_access()

time.sleep(BACKOFF_DELAY_SECONDS)
```

---

## 6. Documentation

### Docstring Guidelines

```python
def calculate_compound_interest(
    principal: float,
    rate: float,
    years: int,
    compounds_per_year: int = 12
) -> float:
    """Calculate compound interest over time.

    Uses the formula: A = P(1 + r/n)^(nt)

    Args:
        principal: Initial investment amount in dollars
        rate: Annual interest rate as decimal (e.g., 0.05 for 5%)
        years: Number of years to calculate
        compounds_per_year: How often interest compounds per year

    Returns:
        Final amount after compound interest

    Raises:
        ValueError: If principal, rate, or years is negative

    Example:
        >>> calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Values must be non-negative")
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
```

### When to Document

- **Always**: Public functions and classes
- **Always**: Complex algorithms
- **Always**: Non-obvious business logic
- **Optional**: Simple getters/setters
- **Avoid**: Restating what the code clearly shows

---

## 7. Code Organization

### Module Organization

```python
# Standard order in a module:
"""Module docstring."""

# 1. Future imports
from __future__ import annotations

# 2. Standard library
import os
import sys
from datetime import datetime
from typing import Protocol

# 3. Third-party
import httpx
from pydantic import BaseModel

# 4. Local imports
from myapp.config import settings
from myapp.models import User

# 5. Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# 6. Classes
class UserService:
    ...

# 7. Functions
def get_user(user_id: int) -> User | None:
    ...

# 8. Main block
if __name__ == "__main__":
    main()
```

### Avoid Deep Nesting

```python
# BAD: Deep nesting
def process_order(order):
    if order:
        if order.items:
            for item in order.items:
                if item.available:
                    if item.price > 0:
                        process(item)

# GOOD: Early returns and guards
def process_order(order):
    if not order or not order.items:
        return

    for item in order.items:
        if not item.available or item.price <= 0:
            continue
        process(item)
```

---

## Quick Reference: Clean Code Checklist

- [ ] Names are self-documenting
- [ ] Functions do one thing
- [ ] Functions are under 20 lines
- [ ] No magic numbers/strings
- [ ] Type hints on public interfaces
- [ ] No deep nesting (max 2-3 levels)
- [ ] Docstrings on public functions
- [ ] No side effects in "get" functions
- [ ] Constants extracted to module level
