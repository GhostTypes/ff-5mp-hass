# Async/Await Patterns in Python

Comprehensive guide to async programming patterns. See SKILL.md for quick reference.

## Core Concepts

### When to Use Async

| Use Case | Async? | Reason |
|----------|--------|--------|
| HTTP requests | YES | Network I/O bound |
| Database queries | YES | I/O bound |
| File I/O | YES | I/O bound |
| CPU-heavy computation | NO | Use ProcessPoolExecutor |
| Simple scripts | NO | Overhead not worth it |

### The Event Loop

```python
import asyncio

# The event loop runs one coroutine at a time
# When a coroutine awaits, the loop runs other coroutines

async def main():
    result = await some_async_operation()

# Run the async code
asyncio.run(main())
```

## Basic Patterns

### Defining Async Functions

```python
# Async function (coroutine)
async def fetch_user(user_id: int) -> User:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"/users/{user_id}") as response:
            return await response.json()

# Calling async functions
async def main():
    user = await fetch_user(1)  # Must await
    print(user)
```

### Running Concurrent Operations

```python
import asyncio

# Run multiple operations concurrently
async def fetch_all_users(user_ids: list[int]) -> list[User]:
    tasks = [fetch_user(id) for id in user_ids]
    return await asyncio.gather(*tasks)

# With error handling
async def fetch_all_safe(user_ids: list[int]) -> list[User | None]:
    async def safe_fetch(user_id: int) -> User | None:
        try:
            return await fetch_user(user_id)
        except Exception as e:
            logger.error(f"Failed to fetch {user_id}: {e}")
            return None

    tasks = [safe_fetch(id) for id in user_ids]
    return await asyncio.gather(*tasks)
```

### Timeouts

```python
# Add timeout to prevent hanging
async def fetch_with_timeout(url: str, timeout: float = 30.0) -> Response:
    async with asyncio.timeout(timeout):
        return await fetch(url)

# Python 3.10+ style
async def fetch_with_timeout(url: str) -> Response:
    async with asyncio.timeout(30):
        return await fetch(url)

# Older style
async def fetch_with_timeout(url: str) -> Response:
    return await asyncio.wait_for(fetch(url), timeout=30.0)
```

## Blocking the Event Loop

### NEVER Block in Async

```python
# BAD: Blocks entire event loop
async def bad_example():
    time.sleep(5)  # NO! Everything stops
    requests.get(url)  # NO! Synchronous HTTP

# GOOD: Use async equivalents
async def good_example():
    await asyncio.sleep(5)  # Non-blocking
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

### Offloading Blocking Operations

```python
# Use asyncio.to_thread for blocking I/O
async def read_large_file(path: str) -> str:
    # Runs in thread pool
    return await asyncio.to_thread(sync_read_file, path)

# For CPU-bound work
async def process_large_data(data: list) -> Result:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,  # Default executor
        heavy_computation,
        data
    )
```

## Task Management

### Creating and Tracking Tasks

```python
# BAD: Fire-and-forget can leak tasks
async def leaky():
    asyncio.create_task(background_work())  # Can be lost
    return "done"

# GOOD: Keep reference or use TaskGroup
async def tracked():
    task = asyncio.create_task(background_work())
    # ... do other work ...
    await task  # Ensure completion

# Python 3.11+: TaskGroup (recommended)
async def with_task_group():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_user(1))
        task2 = tg.create_task(fetch_user(2))
        task3 = tg.create_task(fetch_user(3))
    # All tasks completed here
    return [task1.result(), task2.result(), task3.result()]
```

### Cancelling Tasks

```python
async def cancellable_operation():
    task = asyncio.create_task(long_running_work())
    try:
        await asyncio.wait_for(task, timeout=10.0)
    except asyncio.TimeoutError:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            logger.info("Task was cancelled")
```

## Async Context Managers

```python
# Built-in async context managers
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()

# Custom async context manager
from contextlib import asynccontextmanager

@asynccontextmanager
async def database_transaction():
    conn = await get_connection()
    try:
        yield conn
        await conn.commit()
    except Exception:
        await conn.rollback()
        raise
    finally:
        await conn.close()

# Usage
async def save_user(user: User):
    async with database_transaction() as conn:
        await conn.execute("INSERT INTO users ...", user)
```

## Async Iterators

```python
# Async generator
async def fetch_pages(url: str) -> AsyncIterator[Page]:
    page = 1
    while True:
        response = await fetch(f"{url}?page={page}")
        if not response.data:
            break
        yield response
        page += 1

# Usage
async def process_all_pages():
    async for page in fetch_pages("/api/data"):
        process(page)
```

## Common Patterns

### Rate Limiting

```python
class RateLimiter:
    def __init__(self, rate: float):
        self.rate = rate
        self.last_call = 0.0

    async def acquire(self):
        now = asyncio.get_event_loop().time()
        wait_time = self.last_call + (1 / self.rate) - now
        if wait_time > 0:
            await asyncio.sleep(wait_time)
        self.last_call = asyncio.get_event_loop().time()

# Usage
limiter = RateLimiter(rate=10)  # 10 requests per second

async def fetch_with_rate_limit(url: str) -> Response:
    await limiter.acquire()
    return await fetch(url)
```

### Connection Pooling

```python
# Reuse session for connection pooling
class HttpClient:
    def __init__(self):
        self._session: aiohttp.ClientSession | None = None

    async def get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def fetch(self, url: str) -> dict:
        session = await self.get_session()
        async with session.get(url) as response:
            return await response.json()

    async def close(self):
        if self._session:
            await self._session.close()
```

### Retry Pattern

```python
async def retry_with_backoff(
    func: Callable[..., Awaitable[T]],
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> T:
    for attempt in range(max_retries):
        try:
            return await func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {delay}s")
            await asyncio.sleep(delay)
```

## Debugging Async

```python
# Enable debug mode
asyncio.run(main(), debug=True)

# Check for never-awaited coroutines
import warnings
warnings.filterwarnings("error", category=RuntimeWarning)
```

## Quick Reference

| Pattern | Code |
|---------|------|
| Basic async | `async def foo(): await bar()` |
| Sleep | `await asyncio.sleep(1)` |
| Timeout | `async with asyncio.timeout(30):` |
| Gather | `await asyncio.gather(*tasks)` |
| TaskGroup | `async with asyncio.TaskGroup() as tg:` |
| Offload blocking | `await asyncio.to_thread(func, arg)` |
| Cancel | `task.cancel()` |
