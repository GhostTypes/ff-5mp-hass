# [try-consider-else (TRY300)](#try-consider-else-try300)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27try-consider-else%27%20OR%20TRY300)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Ftry_consider_else.rs#L53)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

## [What it does](#what-it-does)

Checks for `return` statements in `try` blocks.

## [Why is this bad?](#why-is-this-bad)

The `try`-`except` statement has an `else` clause for code that should
run *only* if no exceptions were raised. Returns in `try` blocks may
exhibit confusing or unwanted behavior, such as being overridden by
control flow in `except` and `finally` blocks, or unintentionally
suppressing an exception.

## [Example](#example)

```
import logging


def reciprocal(n):
    try:
        rec = 1 / n
        print(f"reciprocal of {n} is {rec}")
        return rec
    except ZeroDivisionError:
        logging.exception("Exception occurred")
        raise
```

Use instead:

```
import logging


def reciprocal(n):
    try:
        rec = 1 / n
    except ZeroDivisionError:
        logging.exception("Exception occurred")
        raise
    else:
        print(f"reciprocal of {n} is {rec}")
        return rec
```

## [References](#references)

* [Python documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)