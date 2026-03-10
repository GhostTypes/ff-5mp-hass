# Data Validation

Guide to data validation with Pydantic and dataclasses. See SKILL.md for quick reference.

## When to Use What

| Use Case | Tool |
|----------|------|
| API boundaries | Pydantic `BaseModel` |
| Configuration | Pydantic `BaseModel` |
| External data (JSON, forms) | Pydantic `BaseModel` |
| Internal data structures | `@dataclass` |
| Simple value containers | `NamedTuple` |

## Pydantic for External Boundaries

### Basic Model

```python
from pydantic import BaseModel, EmailStr, HttpUrl, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr                    # Validates email format
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)     # 0 <= age <= 150
    website: HttpUrl | None = None     # Validates URL format

class User(UserCreate):
    id: int
    created_at: datetime

# Usage
user = UserCreate(email="test@example.com", name="Alice", age=30)
invalid = UserCreate(email="not-an-email", name="", age=-1)  # ValidationError
```

### Custom Validators

```python
from pydantic import BaseModel, field_validator, model_validator
import re

class UserCreate(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain uppercase letter')
        return v

    @model_validator(mode='after')
    def passwords_match(self) -> 'UserCreate':
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self
```

### Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str

class User(BaseModel):
    name: str
    address: Address  # Nested model, validated recursively

# Usage
user = User(
    name="Alice",
    address={
        "street": "123 Main St",
        "city": "Boston",
        "country": "USA",
        "postal_code": "02101"
    }
)
```

### JSON Parsing

```python
from pydantic import BaseModel

class Config(BaseModel):
    database_url: str
    debug: bool = False

# From JSON string
json_data = '{"database_url": "postgresql://localhost/db", "debug": true}'
config = Config.model_validate_json(json_data)

# From dict
dict_data = {"database_url": "postgresql://localhost/db"}
config = Config.model_validate(dict_data)
```

## Dataclasses for Internal Models

### Basic Dataclass

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    name: str
    email: str
    age: int
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        # Normalize email after initialization
        self.email = self.email.lower()

# Usage
user = User(name="Alice", email="Alice@Example.com", age=30)
print(user.email)  # "alice@example.com"
```

### Frozen Dataclasses (Immutable)

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
p1.x = 5  # Error: cannot assign to frozen field
```

### Dataclass with Methods

```python
@dataclass
class Money:
    amount: float
    currency: str

    def __post_init__(self):
        self.amount = round(self.amount, 2)

    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"

# Usage
price1 = Money(10.50, "USD")
price2 = Money(5.25, "USD")
total = price1 + price2  # Money(15.75, "USD")
```

## Validate at Boundaries

### Early Validation Pattern

```python
from pydantic import BaseModel, ValidationError
from dataclasses import dataclass

# External model (API)
class UserCreateRequest(BaseModel):
    email: str
    name: str
    age: int

# Internal model
@dataclass
class User:
    id: int
    email: str
    name: str
    age: int

def create_user(data: dict) -> User:
    # Validate at boundary
    validated = UserCreateRequest.model_validate(data)

    # Create internal model (already validated)
    user = User(
        id=generate_id(),
        email=validated.email,
        name=validated.name,
        age=validated.age
    )

    return save_user(user)
```

### Type Guards

```python
from typing import TypeGuard, TypedDict

class UserDict(TypedDict):
    id: int
    email: str
    name: str

def is_valid_user(data: dict) -> TypeGuard[UserDict]:
    """Check if dict has required user fields."""
    required = {'id', 'email', 'name'}
    return (
        required.issubset(data.keys()) and
        isinstance(data['id'], int) and
        isinstance(data['email'], str) and
        isinstance(data['name'], str)
    )

def process_user(data: dict) -> None:
    if is_valid_user(data):
        # data is now typed as UserDict
        print(data['email'])
```

## Conversion Between Types

### Pydantic to Dataclass

```python
from pydantic import BaseModel
from dataclasses import dataclass, asdict

@dataclass
class UserInternal:
    name: str
    email: str

class UserAPI(BaseModel):
    name: str
    email: str

    def to_internal(self) -> UserInternal:
        return UserInternal(**self.model_dump())

# Usage
api_user = UserAPI(name="Alice", email="alice@example.com")
internal_user = api_user.to_internal()
```

## Quick Reference

### Pydantic Features

| Feature | Example |
|---------|---------|
| Email validation | `email: EmailStr` |
| URL validation | `url: HttpUrl` |
| Range constraints | `age: int = Field(ge=0, le=150)` |
| Length constraints | `name: str = Field(min_length=1, max_length=100)` |
| Optional fields | `bio: str \| None = None` |
| Default factory | `tags: list = Field(default_factory=list)` |

### Dataclass Features

| Feature | Example |
|---------|---------|
| Default values | `is_active: bool = True` |
| Default factory | `tags: list = field(default_factory=list)` |
| Frozen | `@dataclass(frozen=True)` |
| Post-init | `def __post_init__(self):` |
| Convert to dict | `asdict(user)` |

### Decision Matrix

```
External data (API, JSON, forms)?
    → YES: Use Pydantic
    → NO: Internal only?

Internal only?
    → YES: Use dataclass
    → NO: Mixed sources?

Mixed sources?
    → Validate at boundary with Pydantic
    → Use dataclass internally
```
