# [useless-contextlib-suppress (B022)](#useless-contextlib-suppress-b022)

Added in [v0.0.118](https://github.com/astral-sh/ruff/releases/tag/v0.0.118) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-contextlib-suppress%27%20OR%20B022)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fuseless_contextlib_suppress.rs#L39)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `contextlib.suppress` without arguments.

## [Why is this bad?](#why-is-this-bad)

`contextlib.suppress` is a context manager that suppresses exceptions. It takes,
as arguments, the exceptions to suppress within the enclosed block. If no
exceptions are specified, then the context manager won't suppress any
exceptions, and is thus redundant.

Consider adding exceptions to the `contextlib.suppress` call, or removing the
context manager entirely.

## [Example](#example)

```
import contextlib

with contextlib.suppress():
    foo()
```

Use instead:

```
import contextlib

with contextlib.suppress(Exception):
    foo()
```

## [References](#references)

* [Python documentation: `contextlib.suppress`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress)