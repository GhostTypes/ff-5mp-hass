# [timeout-error-alias (UP041)](#timeout-error-alias-up041)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27timeout-error-alias%27%20OR%20UP041)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Ftimeout_error_alias.rs#L42)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of exceptions that alias `TimeoutError`.

## [Why is this bad?](#why-is-this-bad)

`TimeoutError` is the builtin error type used for exceptions when a system
function timed out at the system level.

In Python 3.10, `socket.timeout` was aliased to `TimeoutError`. In Python
3.11, `asyncio.TimeoutError` was aliased to `TimeoutError`.

These aliases remain in place for compatibility with older versions of
Python, but may be removed in future versions.

Prefer using `TimeoutError` directly, as it is more idiomatic and future-proof.

## [Example](#example)

```
import asyncio

raise asyncio.TimeoutError
```

Use instead:

```
raise TimeoutError
```

## [References](#references)

* [Python documentation: `TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError)