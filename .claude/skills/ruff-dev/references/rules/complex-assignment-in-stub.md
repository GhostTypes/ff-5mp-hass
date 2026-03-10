# [complex-assignment-in-stub (PYI017)](#complex-assignment-in-stub-pyi017)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27complex-assignment-in-stub%27%20OR%20PYI017)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fcomplex_assignment_in_stub.rs#L44)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for assignments with multiple or non-name targets in stub files.

## [Why is this bad?](#why-is-this-bad)

In general, stub files should be thought of as "data files" for a type
checker, and are not intended to be executed. As such, it's useful to
enforce that only a subset of Python syntax is allowed in a stub file, to
ensure that everything in the stub is unambiguous for the type checker.

The need to perform multi-assignment, or assignment to a non-name target,
likely indicates a misunderstanding of how stub files are intended to be
used.

## [Example](#example)

```
from typing import TypeAlias

a = b = int

class Klass: ...

Klass.X: TypeAlias = int
```

Use instead:

```
from typing import TypeAlias

a: TypeAlias = int
b: TypeAlias = int

class Klass:
    X: TypeAlias = int
```