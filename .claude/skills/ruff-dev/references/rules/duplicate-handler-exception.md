# [duplicate-handler-exception (B014)](#duplicate-handler-exception-b014)

Added in [v0.0.67](https://github.com/astral-sh/ruff/releases/tag/v0.0.67) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27duplicate-handler-exception%27%20OR%20B014)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fduplicate_exceptions.rs#L90)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for exception handlers that catch duplicate exceptions.

## [Why is this bad?](#why-is-this-bad)

Including the same exception multiple times in the same handler is redundant,
as the first exception will catch the exception, making the second exception
unreachable. The same applies to exception hierarchies, as a handler for a
parent exception (like `Exception`) will also catch child exceptions (like
`ValueError`).

## [Example](#example)

```
try:
    ...
except (Exception, ValueError):  # `Exception` includes `ValueError`.
    ...
```

Use instead:

```
try:
    ...
except Exception:
    ...
```

## [References](#references)

* [Python documentation: `except` clause](https://docs.python.org/3/reference/compound_stmts.html#except-clause)
* [Python documentation: Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)