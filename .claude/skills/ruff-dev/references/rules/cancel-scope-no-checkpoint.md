# [cancel-scope-no-checkpoint (ASYNC100)](#cancel-scope-no-checkpoint-async100)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27cancel-scope-no-checkpoint%27%20OR%20ASYNC100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fcancel_scope_no_checkpoint.rs#L47)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks for timeout context managers which do not contain a checkpoint.

For the purposes of this check, `yield` is considered a checkpoint,
since checkpoints may occur in the caller to which we yield.

## [Why is this bad?](#why-is-this-bad)

Some asynchronous context managers, such as `asyncio.timeout` and
`trio.move_on_after`, have no effect unless they contain a checkpoint.
The use of such context managers without an `await`, `async with` or
`async for` statement is likely a mistake.

## [Example](#example)

```
import asyncio


async def func():
    async with asyncio.timeout(2):
        do_something()
```

Use instead:

```
import asyncio


async def func():
    async with asyncio.timeout(2):
        do_something()
        await awaitable()
```

## [References](#references)

* [`asyncio` timeouts](https://docs.python.org/3/library/asyncio-task.html#timeouts)
* [`anyio` timeouts](https://anyio.readthedocs.io/en/stable/cancellation.html)
* [`trio` timeouts](https://trio.readthedocs.io/en/stable/reference-core.html#cancellation-and-timeouts)