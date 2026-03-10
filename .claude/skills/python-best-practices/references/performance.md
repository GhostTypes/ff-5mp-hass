# Performance Optimization

Guide to writing performant Python code. See SKILL.md for quick reference.

## Core Principle

> "Premature optimization is the root of all evil" - Donald Knuth

**Measure first, optimize only proven bottlenecks.**

## Profiling

### Quick Timing

```python
import time

start = time.perf_counter()
result = expensive_function()
elapsed = time.perf_counter() - start
print(f" Took {elapsed:.3f}s")
```

### cProfile

```python
import cProfile

# Profile a function
cProfile.run('my_function()')

# Profile with sorting
cProfile.run('my_function()', sort='cumulative')
```

### Line Profiler

```python
# Install: pip install line_profiler

from line_profiler import LineProfiler

lp = LineProfiler()
lp.add_function(my_function)
lp.enable()

result = my_function()

lp.print_stats()
```

## Common Optimizations

### Use Built-in Functions

```python
# BAD: Manual loop
total = 0
for item in items:
    total += item.price

# GOOD: Built-in sum (C-optimized)
total = sum(item.price for item in items)
```

### List/Dict Comprehensions

```python
# BAD: Append in loop
result = []
for x in range(1000):
    result.append(x ** 2)

# GOOD: List comprehension
result = [x ** 2 for x in range(1000)]

# GOOD: Dict comprehension
lookup = {item.id: item for item in items}
```

### Generators for Large Data

```python
# BAD: Load everything into memory
def read_file(path: str) -> list[str]:
    with open(path) as f:
        return f.readlines()  # Loads entire file

# GOOD: Generator (lazy evaluation)
def read_file(path: str):
    with open(path) as f:
        for line in f:
            yield line.strip()

# Usage: Memory efficient
for line in read_file("huge_file.txt"):
    process(line)
```

### String Concatenation

```python
# BAD: O(n²) complexity
result = ""
for s in strings:
    result += s

# GOOD: O(n) with join
result = "".join(strings)

# GOOD: For building with separators
result = ", ".join(strings)
```

### Membership Testing

```python
# BAD: O(n) for lists
if item in my_list:  # Scans entire list

# GOOD: O(1) for sets
my_set = set(my_list)
if item in my_set:

# GOOD: O(1) for dict keys
if key in my_dict:
```

### Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Custom cache
def expensive_computation(n: int, _cache: dict = {}) -> int:
    if n not in _cache:
        _cache[n] = heavy_work(n)
    return _cache[n]
```

## Algorithmic Complexity

### Choose the Right Data Structure

| Operation | list | set | dict |
|-----------|------|-----|------|
| Lookup by value | O(n) | O(1) | - |
| Lookup by key | - | - | O(1) |
| Insert | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |
| Iteration | O(n) | O(n) | O(n) |

### Common Patterns

```python
# Finding duplicates - O(n²) vs O(n)
# BAD
def has_duplicates(items: list) -> bool:
    for i, item in enumerate(items):
        if item in items[i + 1:]:  # O(n) lookup each time
            return True
    return False

# GOOD
def has_duplicates(items: list) -> bool:
    seen = set()
    for item in items:
        if item in seen:  # O(1) lookup
            return True
        seen.add(item)
    return False

# BETTER (if order doesn't matter)
def has_duplicates(items: list) -> bool:
    return len(items) != len(set(items))
```

## Memory Optimization

### Slots

```python
# Without __slots__: uses dict per instance
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# With __slots__: uses tuple-like storage
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Benefit: ~40% less memory per instance
```

### Generators vs Lists

```python
import sys

# List: All in memory
numbers_list = [i for i in range(1000000)]
print(sys.getsizeof(numbers_list))  # ~8MB

# Generator: Only one item at a time
numbers_gen = (i for i in range(1000000))
print(sys.getsizeof(numbers_gen))  # ~200 bytes
```

## I/O Performance

### Batch Operations

```python
# BAD: Many small I/O operations
for item in items:
    db.insert(item)

# GOOD: Batch insert
db.insert_all(items)
```

### Async I/O

```python
import asyncio
import aiohttp

async def fetch_all(urls: list[str]) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

## When to Consider Alternatives

| Scenario | Consider |
|----------|----------|
| Heavy number crunching | NumPy, Pandas |
| CPU-bound parallelism | multiprocessing, Cython |
| Real-time requirements | PyPy, Cython, Rust |
| Large datasets | Dask, Polars |

## Quick Reference

### Before Optimizing

1. Profile to find bottlenecks
2. Check if algorithm is the problem
3. Consider if optimization is worth it

### Quick Wins

| Change | Speedup |
|--------|---------|
| List comprehension vs loop | ~30% |
| Built-in sum vs manual | ~50% |
| Set lookup vs list | ~100x |
| join vs += for strings | ~10x |
| @lru_cache | Depends on cache hits |

### Don't Optimize

- Code that runs once
- Code that's already fast enough
- Readability for minor gains
- Before measuring
