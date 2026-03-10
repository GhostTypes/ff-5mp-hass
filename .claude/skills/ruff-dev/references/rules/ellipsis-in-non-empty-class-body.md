# [ellipsis-in-non-empty-class-body (PYI013)](#ellipsis-in-non-empty-class-body-pyi013)

Added in [v0.0.270](https://github.com/astral-sh/ruff/releases/tag/v0.0.270) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ellipsis-in-non-empty-class-body%27%20OR%20PYI013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fellipsis_in_non_empty_class_body.rs#L30)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Removes ellipses (`...`) in otherwise non-empty class bodies.

## [Why is this bad?](#why-is-this-bad)

An ellipsis in a class body is only necessary if the class body is
otherwise empty. If the class body is non-empty, then the ellipsis
is redundant.

## [Example](#example)

```
class Foo:
    ...
    value: int
```

Use instead:

```
class Foo:
    value: int
```