# [jump-statement-in-finally (B012)](#jump-statement-in-finally-b012)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27jump-statement-in-finally%27%20OR%20B012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fjump_statement_in_finally.rs#L43)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `break`, `continue`, and `return` statements in `finally`
blocks.

## [Why is this bad?](#why-is-this-bad)

The use of `break`, `continue`, and `return` statements in `finally` blocks
can cause exceptions to be silenced.

`finally` blocks execute regardless of whether an exception is raised. If a
`break`, `continue`, or `return` statement is reached in a `finally` block,
any exception raised in the `try` or `except` blocks will be silenced.

## [Example](#example)

```
def speed(distance, time):
    try:
        return distance / time
    except ZeroDivisionError:
        raise ValueError("Time cannot be zero")
    finally:
        return 299792458  # `ValueError` is silenced
```

Use instead:

```
def speed(distance, time):
    try:
        return distance / time
    except ZeroDivisionError:
        raise ValueError("Time cannot be zero")
```

## [References](#references)

* [Python documentation: The `try` statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)