# [except-with-empty-tuple (B029)](#except-with-empty-tuple-b029)

Added in [v0.0.250](https://github.com/astral-sh/ruff/releases/tag/v0.0.250) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27except-with-empty-tuple%27%20OR%20B029)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fexcept_with_empty_tuple.rs#L36)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for exception handlers that catch an empty tuple.

## [Why is this bad?](#why-is-this-bad)

An exception handler that catches an empty tuple will not catch anything,
and is indicative of a mistake. Instead, add exceptions to the `except`
clause.

## [Example](#example)

```
try:
    1 / 0
except ():
    ...
```

Use instead:

```
try:
    1 / 0
except ZeroDivisionError:
    ...
```

## [References](#references)

* [Python documentation: `except` clause](https://docs.python.org/3/reference/compound_stmts.html#except-clause)