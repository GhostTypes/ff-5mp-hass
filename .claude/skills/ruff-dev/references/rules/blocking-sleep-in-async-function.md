# [blocking-sleep-in-async-function (ASYNC251)](#blocking-sleep-in-async-function-async251)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blocking-sleep-in-async-function%27%20OR%20ASYNC251)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_sleep.rs#L37)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks that async functions do not call `time.sleep`.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a `time.sleep` call will block the entire
event loop, preventing it from executing other tasks while waiting for the
`time.sleep`, negating the benefits of asynchronous programming.

Instead of `time.sleep`, use `asyncio.sleep`.

## [Example](#example)

```
import time


async def fetch():
    time.sleep(1)
```

Use instead:

```
import asyncio


async def fetch():
    await asyncio.sleep(1)
```