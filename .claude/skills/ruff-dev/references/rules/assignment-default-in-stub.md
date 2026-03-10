# [assignment-default-in-stub (PYI015)](#assignment-default-in-stub-pyi015)

Added in [v0.0.260](https://github.com/astral-sh/ruff/releases/tag/v0.0.260) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assignment-default-in-stub%27%20OR%20PYI015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fsimple_defaults.rs#L135)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for assignments in stubs with default values that are not "simple"
(i.e., `int`, `float`, `complex`, `bytes`, `str`, `bool`, `None`, `...`, or
simple container literals).

## [Why is this bad?](#why-is-this-bad)

Stub (`.pyi`) files exist to define type hints, and are not evaluated at
runtime. As such, assignments in stub files should not include values,
as they are ignored by type checkers.

However, the use of such values may be useful for IDEs and other consumers
of stub files, and so "simple" values may be worth including and are
permitted by this rule.

Instead of including and reproducing a complex value, use `...` to indicate
that the assignment has a default value, but that the value is non-simple
or varies according to the current platform or Python version.

## [Example](#example)

```
foo: str = bar()
```

Use instead:

```
foo: str = ...
```

## [References](#references)

* [`flake8-pyi`](https://github.com/PyCQA/flake8-pyi/blob/main/ERRORCODES.md)