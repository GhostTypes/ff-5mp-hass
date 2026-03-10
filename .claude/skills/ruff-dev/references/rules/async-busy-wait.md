# [async-busy-wait (ASYNC110)](#async-busy-wait-async110)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27async-busy-wait%27%20OR%20ASYNC110)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fasync_busy_wait.rs#L44)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks for the use of an async sleep function in a `while` loop.

## [Why is this bad?](#why-is-this-bad)

Instead of sleeping in a `while` loop, and waiting for a condition
to become true, it's preferable to `await` on an `Event` object such
as: `asyncio.Event`, `trio.Event`, or `anyio.Event`.

## [Example](#example)

```
import asyncio

DONE = False


async def func():
    while not DONE:
        await asyncio.sleep(1)
```

Use instead:

```
import asyncio

DONE = asyncio.Event()


async def func():
    await DONE.wait()
```

## [References](#references)

* [`asyncio` events](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event)
* [`anyio` events](https://anyio.readthedocs.io/en/latest/api.html#anyio.Event)
* [`trio` events](https://trio.readthedocs.io/en/latest/reference-core.html#trio.Event)