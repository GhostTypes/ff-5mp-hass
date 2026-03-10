# [wait-for-process-in-async-function (ASYNC222)](#wait-for-process-in-async-function-async222)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27wait-for-process-in-async-function%27%20OR%20ASYNC222)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_process_invocation.rs#L124)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks that async functions do not wait on processes with blocking methods.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a blocking call will block the entire
event loop, preventing it from executing other tasks while waiting for the
call to complete, negating the benefits of asynchronous programming.

Instead of making a blocking call, use an equivalent asynchronous library
or function, like [`trio.to_thread.run_sync()`](https://trio.readthedocs.io/en/latest/reference-core.html#trio.to_thread.run_sync)
or [`anyio.to_thread.run_sync()`](https://anyio.readthedocs.io/en/latest/api.html#anyio.to_thread.run_sync).

## [Example](#example)

```
import os


async def foo():
    os.waitpid(0)
```

Use instead:

```
import asyncio
import os


def wait_for_process():
    os.waitpid(0)


async def foo():
    await asyncio.loop.run_in_executor(None, wait_for_process)
```