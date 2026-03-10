# [blocking-open-call-in-async-function (ASYNC230)](#blocking-open-call-in-async-function-async230)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blocking-open-call-in-async-function%27%20OR%20ASYNC230)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_async%2Frules%2Fblocking_open_call.rs#L36)

Derived from the **[flake8-async](../#flake8-async-async)** linter.

## [What it does](#what-it-does)

Checks that async functions do not open files with blocking methods like `open`.

## [Why is this bad?](#why-is-this-bad)

Blocking an async function via a blocking call will block the entire
event loop, preventing it from executing other tasks while waiting for the
call to complete, negating the benefits of asynchronous programming.

Instead of making a blocking call, use an equivalent asynchronous library
or function.

## [Example](#example)

```
async def foo():
    with open("bar.txt") as f:
        contents = f.read()
```

Use instead:

```
import anyio


async def foo():
    async with await anyio.open_file("bar.txt") as f:
        contents = await f.read()
```