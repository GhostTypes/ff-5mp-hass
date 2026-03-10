# [typed-argument-default-in-stub (PYI011)](#typed-argument-default-in-stub-pyi011)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27typed-argument-default-in-stub%27%20OR%20PYI011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fsimple_defaults.rs#L43)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for typed function arguments in stubs with complex default values.

## [Why is this bad?](#why-is-this-bad)

Stub (`.pyi`) files exist as "data files" for static analysis tools, and
are not evaluated at runtime. While simple default values may be useful for
some tools that consume stubs, such as IDEs, they are ignored by type
checkers.

Instead of including and reproducing a complex value, use `...` to indicate
that the assignment has a default value, but that the value is "complex" or
varies according to the current platform or Python version. For the
purposes of this rule, any default value counts as "complex" unless it is
a literal `int`, `float`, `complex`, `bytes`, `str`, `bool`, `None`, `...`,
or a simple container literal.

## [Example](#example)

```
def foo(arg: list[int] = list(range(10_000))) -> None: ...
```

Use instead:

```
def foo(arg: list[int] = ...) -> None: ...
```

## [References](#references)

* [`flake8-pyi`](https://github.com/PyCQA/flake8-pyi/blob/main/ERRORCODES.md)