# [error-instead-of-exception (TRY400)](#error-instead-of-exception-try400)

Added in [v0.0.236](https://github.com/astral-sh/ruff/releases/tag/v0.0.236) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27error-instead-of-exception%27%20OR%20TRY400)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Ferror_instead_of_exception.rs#L54)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `logging.error` instead of `logging.exception` when
logging an exception.

## [Why is this bad?](#why-is-this-bad)

`logging.exception` logs the exception and the traceback, while
`logging.error` only logs the exception. The former is more appropriate
when logging an exception, as the traceback is often useful for debugging.

## [Example](#example)

```
import logging


def func():
    try:
        raise NotImplementedError
    except NotImplementedError:
        logging.error("Exception occurred")
```

Use instead:

```
import logging


def func():
    try:
        raise NotImplementedError
    except NotImplementedError:
        logging.exception("Exception occurred")
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe when run against `logging.error` calls,
but unsafe when marked against other logger-like calls (e.g.,
`logger.error`), since the rule is prone to false positives when detecting
logger-like calls outside of the `logging` module.

## [References](#references)

* [Python documentation: `logging.exception`](https://docs.python.org/3/library/logging.html#logging.exception)