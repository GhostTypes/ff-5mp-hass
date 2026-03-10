# Python Anti-Patterns

Common mistakes to avoid in Python. See SKILL.md for DOs and DON'Ts.

## Correctness Anti-Patterns

### Mutable Default Arguments

```python
# BAD: Default is shared across all calls
def add_item(item: str, items: list = []):
    items.append(item)
    return items

add_item("a")  # ["a"]
add_item("b")  # ["a", "b"]  ← Surprise!

# GOOD: Use None as default
def add_item(item: str, items: list | None = None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Modifying List While Iterating

```python
# BAD: Skips elements
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
# Result: [1, 3, 5] (4 was skipped!)

# GOOD: Create new list
numbers = [n for n in numbers if n % 2 != 0]

# GOOD: Iterate copy
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)
```

### Late Binding Closures

```python
# BAD: All lambdas use final value of i
functions = [lambda: i for i in range(3)]
for f in functions:
    print(f())  # 2, 2, 2

# GOOD: Capture value with default argument
functions = [lambda i=i: i for i in range(3)]
for f in functions:
    print(f())  # 0, 1, 2
```

### Comparing with is Instead of ==

```python
# BAD: is for value comparison
if x is 5:  # Works sometimes, not guaranteed
    ...

# GOOD: Use == for values
if x == 5:
    ...

# CORRECT use of is
if x is None:  # Only use is for None and singletons
if x is not None:
```

## Error Handling Anti-Patterns

### Bare except

```python
# BAD: Catches everything including KeyboardInterrupt
try:
    do_something()
except:
    pass

# GOOD: Catch specific exception
try:
    do_something()
except ValueError as e:
    logger.error(f"Failed: {e}")
```

### Silent Failures

```python
# BAD: Silent failure
try:
    save_to_database(data)
except DatabaseError:
    pass  # Data lost!

# GOOD: At least log
try:
    save_to_database(data)
except DatabaseError as e:
    logger.error(f"Failed to save: {e}")
    raise
```

### Using Exceptions for Flow Control

```python
# BAD: Exception for normal flow
def is_numeric(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

# GOOD: Check directly
def is_numeric(s: str) -> bool:
    return s.isdigit() or (s[0] == '-' and s[1:].isdigit())
```

## Performance Anti-Patterns

### String Concatenation in Loops

```python
# BAD: O(n²)
result = ""
for s in strings:
    result += s

# GOOD: O(n)
result = "".join(strings)
```

### List Membership Testing

```python
# BAD: O(n) for each lookup
if item in my_list:  # Scans entire list

# GOOD: O(1) with set
my_set = set(my_list)
if item in my_set:
```

### Not Using Built-in Functions

```python
# BAD: Manual loop
total = 0
for item in items:
    total += item.price

# GOOD: Built-in sum
total = sum(item.price for item in items)
```

## Security Anti-Patterns

### SQL Injection

```python
# BAD
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# GOOD
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### Command Injection

```python
# BAD
os.system(f"ping {host}")

# GOOD
subprocess.run(["ping", host], check=True)
```

### Using random for Security

```python
# BAD: Predictable
import random
token = str(random.random())

# GOOD: Cryptographically secure
import secrets
token = secrets.token_urlsafe(32)
```

### Hardcoded Secrets

```python
# BAD
API_KEY = "sk-abc123..."

# GOOD
import os
API_KEY = os.environ["API_KEY"]
```

## Code Quality Anti-Patterns

### Unpythonic Loops

```python
# BAD: Using index when you don't need it
for i in range(len(items)):
    print(items[i])

# GOOD: Direct iteration
for item in items:
    print(item)

# If you need both index and value:
for i, item in enumerate(items):
    print(i, item)
```

### Not Using Context Managers

```python
# BAD: Resource leak possible
f = open("file.txt")
content = f.read()
# If exception occurs, file never closed

# GOOD: Automatic cleanup
with open("file.txt") as f:
    content = f.read()
```

### Wildcard Imports

```python
# BAD: Pollutes namespace
from module import *

# GOOD: Import what you need
from module import specific_function
import module
```

### Comparing to True/False

```python
# BAD
if is_valid == True:
    ...

if is_empty == False:
    ...

# GOOD
if is_valid:
    ...

if not is_empty:
    ...
```

### Type Checking with type()

```python
# BAD: Doesn't handle subclasses
if type(obj) == MyClass:
    ...

# GOOD: Use isinstance
if isinstance(obj, MyClass):
    ...
```

## Async Anti-Patterns

### Blocking the Event Loop

```python
# BAD: Blocks everything
async def fetch():
    time.sleep(5)  # NO!
    requests.get(url)  # NO!

# GOOD: Use async equivalents
async def fetch():
    await asyncio.sleep(5)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

### Forgetting to Await

```python
# BAD: Returns coroutine, not result
async def fetch():
    result = async_function()  # Missing await!
    return result

# GOOD
async def fetch():
    result = await async_function()
    return result
```

## Quick Reference

| Anti-Pattern | Correct Pattern |
|--------------|-----------------|
| `def f(x=[])` | `def f(x=None): if x is None: x = []` |
| `except:` | `except SpecificError:` |
| `result += s` in loop | `"".join(strings)` |
| `if x is 5:` | `if x == 5:` |
| `if x == True:` | `if x:` |
| `for i in range(len(l)):` | `for item in l:` |
| `type(x) == T` | `isinstance(x, T)` |
| `f"SELECT * WHERE id={id}"` | `cursor.execute("... WHERE id=%s", (id,))` |
| `random.random()` for tokens | `secrets.token_urlsafe()` |
| `time.sleep()` in async | `await asyncio.sleep()` |

## Priority for Fixing

| Priority | Anti-Pattern Type |
|----------|------------------|
| Critical | Security (SQL injection, secrets) |
| Critical | Data loss (silent failures) |
| High | Correctness (mutable defaults) |
| Medium | Performance (string concat, list search) |
| Low | Style (unpythonic patterns) |
