# [run-process-in-async-function (ASYNC221)](#run-process-in-async-function-async221)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27run-process-in-async-function%27%20OR%20ASYNC221)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_process_invocation.rs#L79)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks that async functions do not run processes with blocking methods.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a blocking call will block the entire
event loop, preventing it from executing other tasks while waiting for the
call to complete, negating the benefits of asynchronous programming.

Instead of making a blocking call, use an equivalent asynchronous library
or function, like [`trio.run_process()`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.run_process)
or [`anyio.run_process()`](https://anyio.readthedocs.io/en/latest/api.html#anyio.run_process).

## [Example](#example)

```
import subprocess


async def foo():
    subprocess.run(cmd)
```

Use instead:

```
import asyncio


async def foo():
    asyncio.create_subprocess_shell(cmd)
```