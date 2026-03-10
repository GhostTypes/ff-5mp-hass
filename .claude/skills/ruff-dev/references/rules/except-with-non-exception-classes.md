# [except-with-non-exception-classes (B030)](#except-with-non-exception-classes-b030)

Added in [v0.0.255](https://github.com/astral-sh/ruff/releases/tag/v0.0.255) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27except-with-non-exception-classes%27%20OR%20B030)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fexcept_with_non_exception_classes.rs#L37)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for exception handlers that catch non-exception classes.

## [Why is this bad?](#why-is-this-bad)

Catching classes that do not inherit from `BaseException` will raise a
`TypeError`.

## [Example](#example)

```
try:
    1 / 0
except 1:
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
* [Python documentation: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)