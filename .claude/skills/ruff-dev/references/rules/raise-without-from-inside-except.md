# [raise-without-from-inside-except (B904)](#raise-without-from-inside-except-b904)

Added in [v0.0.138](https://github.com/astral-sh/ruff/releases/tag/v0.0.138) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-without-from-inside-except%27%20OR%20B904)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fraise_without_from_inside_except.rs#L49)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `raise` statements in exception handlers that lack a `from`
clause.

## [Why is this bad?](#why-is-this-bad)

In Python, `raise` can be used with or without an exception from which the
current exception is derived. This is known as exception chaining. When
printing the stack trace, chained exceptions are displayed in such a way
so as make it easier to trace the exception back to its root cause.

When raising an exception from within an `except` clause, always include a
`from` clause to facilitate exception chaining. If the exception is not
chained, it will be difficult to trace the exception back to its root cause.

## [Example](#example)

```
try:
    ...
except FileNotFoundError:
    if ...:
        raise RuntimeError("...")
    else:
        raise UserWarning("...")
```

Use instead:

```
try:
    ...
except FileNotFoundError as exc:
    if ...:
        raise RuntimeError("...") from None
    else:
        raise UserWarning("...") from exc
```

## [References](#references)

* [Python documentation: `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)