# [yield-from-in-async-function (PLE1700)](#yield-from-in-async-function-ple1700)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27yield-from-in-async-function%27%20OR%20PLE1700)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fyield_from_in_async_function.rs#L26)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of `yield from` in async functions.

## [Why is this bad?](#why-is-this-bad)

Python doesn't support the use of `yield from` in async functions, and will
raise a `SyntaxError` in such cases.

Instead, considering refactoring the code to use an `async for` loop instead.

## [Example](#example)

```
async def numbers():
    yield from [1, 2, 3, 4, 5]
```

Use instead:

```
async def numbers():
    async for number in [1, 2, 3, 4, 5]:
        yield number
```