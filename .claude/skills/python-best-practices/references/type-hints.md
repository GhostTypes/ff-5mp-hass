# Type Hints in Python

Comprehensive guide to Python type hints for Python 3.12+. See SKILL.md for quick reference.

## Evolution of Python Typing

| Version | Feature | PEP |
|---------|---------|-----|
| 3.5 | Basic type hints | PEP 484 |
| 3.9 | Native generics (`list[str]`) | PEP 585 |
| 3.10 | Union syntax (`str \| int`) | PEP 604 |
| 3.11 | `Self`, `TypeVarTuple` | PEP 673, 646 |
| 3.12 | `@override`, `type` alias | PEP 698, 695 |
| 3.13 | `TypeForm` | PEP 747 |

## Modern Type Syntax (3.10+)

### Union Types

```python
# OLD (pre-3.10)
from typing import Union, Optional
def foo(x: Union[str, int]) -> Optional[User]: ...

# NEW (3.10+)
def foo(x: str | int) -> User | None: ...
```

### Generic Collections

```python
# OLD
from typing import List, Dict, Set, Tuple
def process(items: List[str]) -> Dict[str, int]: ...

# NEW (3.9+)
def process(items: list[str]) -> dict[str, int]: ...
```

### Type Aliases

```python
# OLD
from typing import TypeAlias
UserId: TypeAlias = int

# NEW (3.12+)
type UserId = int
type JsonDict = dict[str, str | int | float]
type Point = tuple[float, float]
```

## Generics

### Generic Functions

```python
from typing import TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T | None:
    return items[0] if items else None

# Usage
name = first(["Alice", "Bob"])  # Inferred as str | None
count = first([1, 2, 3])  # Inferred as int | None
```

### Generic Classes

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T | None:
        return self._items.pop() if self._items else None

# Usage
int_stack: Stack[int] = Stack()
int_stack.push(1)
value = int_stack.pop()  # int | None
```

### Bounded Type Variables

```python
from typing import TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self, other: Any) -> bool: ...

def find_max(items: list[T]) -> T | None:
    if not items:
        return None
    maximum = items[0]
    for item in items[1:]:
        if item > maximum:
            maximum = item
    return maximum
```

## Protocols (Structural Typing)

Use protocols for duck typing - check behavior, not inheritance.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

def render(shape: Drawable) -> None:
    shape.draw()

# Works with any class that has draw()
render(Circle())  # OK
render(Square())  # OK
```

### Protocol with Properties

```python
class Named(Protocol):
    @property
    def name(self) -> str: ...

def greet(entity: Named) -> str:
    return f"Hello, {entity.name}"
```

## Special Types

### Any vs object

```python
# Any: Escape hatch - disables type checking
def unsafe(x: Any) -> Any:
    return x.whatever()  # No error

# object: Most general safe type
def safe(x: object) -> object:
    return x.whatever()  # Error: object has no attribute 'whatever'
```

### Never and NoReturn

```python
from typing import Never, NoReturn

def never_returns() -> NoReturn:
    raise Exception("Always fails")

def assert_never(value: Never) -> Never:
    raise AssertionError(f"Unexpected value: {value}")

# Usage in match exhaustiveness
def handle_status(status: Status) -> str:
    match status:
        case Status.ACTIVE:
            return "active"
        case Status.INACTIVE:
            return "inactive"
        case _:
            assert_never(status)  # Type error if cases missing
```

### Self for Method Chaining

```python
from typing import Self

class Builder:
    def __init__(self) -> None:
        self._value: str = ""

    def set_name(self, name: str) -> Self:
        self._value = name
        return self

    def build(self) -> str:
        return self._value

# Works with subclasses too
```

## Type Guards

```python
from typing import TypeGuard

def is_string_list(values: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(v, str) for v in values)

def process(values: list[object]) -> None:
    if is_string_list(values):
        # values is now known to be list[str]
        for v in values:
            print(v.upper())
```

## Overriding and Overloading

### @override Decorator (3.12+)

```python
from typing import override

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    @override
    def speak(self) -> str:
        return "Woof!"

# Type checker will warn if speak() doesn't exist in parent
```

### Function Overloading

```python
from typing import overload

@overload
def process(data: str) -> str: ...
@overload
def process(data: bytes) -> int: ...
def process(data: str | bytes) -> str | int:
    if isinstance(data, str):
        return data.upper()
    return len(data)

# Type checker knows the return type based on input
result1: str = process("hello")  # OK
result2: int = process(b"hello")  # OK
```

## Common Patterns

### Callable Types

```python
from typing import Callable

# Function taking two ints, returning bool
Comparator = Callable[[int, int], bool]

def sort_with(items: list[int], compare: Comparator) -> list[int]:
    return sorted(items, key=lambda x: x)

# Generic callable
Handler = Callable[[T], None]
```

### TypedDict

```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    email: NotRequired[str]  # Optional field (3.11+)

user: UserDict = {"name": "Alice", "age": 30}
```

### Final Values

```python
from typing import final, Final

# Final variable
MAX_SIZE: Final = 100

# Final method (cannot be overridden)
class Base:
    @final
    def cannot_override(self) -> None: ...

# Final class (cannot be subclassed)
@final
class CannotBeSubclassed: ...
```

## Best Practices

1. **Type all public interfaces** - Functions, methods, class attributes
2. **Use modern syntax** - `list[str]` not `List[str]`, `str | int` not `Union[str, int]`
3. **Avoid Any** - Use `object` or proper types
4. **Use TypeGuard** for type narrowing
5. **Use Protocol** for duck typing
6. **Use @override** when overriding methods
7. **Keep private methods optionally typed** - Focus on public API

## Quick Reference

| Use Case | Type |
|----------|------|
| Optional value | `T \| None` |
| List of strings | `list[str]` |
| Dict with string keys | `dict[str, T]` |
| Function type | `Callable[[Arg], Return]` |
| Any value (escape) | `Any` |
| Any value (safe) | `object` |
| Never returns | `NoReturn` |
| Self reference | `Self` |
| Type alias | `type Name = ...` |
