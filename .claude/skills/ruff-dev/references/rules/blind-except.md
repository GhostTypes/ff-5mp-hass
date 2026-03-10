# [blind-except (BLE001)](#blind-except-ble001)

Added in [v0.0.127](https://github.com/astral-sh/ruff/releases/tag/v0.0.127) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blind-except%27%20OR%20BLE001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_blind_except%2Frules%2Fblind_except.rs#L65)

Derived from the **[flake8-blind-except](../#flake8-blind-except-ble)** linter.

## [What it does](#what-it-does)

Checks for `except` clauses that catch all exceptions. This includes
`except BaseException` and `except Exception`.

## [Why is this bad?](#why-is-this-bad)

Overly broad `except` clauses can lead to unexpected behavior, such as
catching `KeyboardInterrupt` or `SystemExit` exceptions that prevent the
user from exiting the program.

Instead of catching all exceptions, catch only those that are expected to
be raised in the `try` block.

## [Example](#example)

```
try:
    foo()
except BaseException:
    ...
```

Use instead:

```
try:
    foo()
except FileNotFoundError:
    ...
```

Exceptions that are re-raised will *not* be flagged, as they're expected to
be caught elsewhere:

```
try:
    foo()
except BaseException:
    raise
```

Exceptions that are logged via `logging.exception()` or are logged via
`logging.error()` or `logging.critical()` with `exc_info` enabled will
*not* be flagged, as this is a common pattern for propagating exception
traces:

```
try:
    foo()
except BaseException:
    logging.exception("Something went wrong")
```

## [References](#references)

* [Python documentation: The `try` statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
* [Python documentation: Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [PEP 8: Programming Recommendations on bare `except`](https://peps.python.org/pep-0008/#programming-recommendations)