# [pass-in-class-body (PYI012)](#pass-in-class-body-pyi012)

Added in [v0.0.260](https://github.com/astral-sh/ruff/releases/tag/v0.0.260) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pass-in-class-body%27%20OR%20PYI012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fpass_in_class_body.rs#L29)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the presence of the `pass` statement in non-empty class bodies
in `.pyi` files.

## [Why is this bad?](#why-is-this-bad)

The `pass` statement is always unnecessary in non-empty class bodies in
stubs.

## [Example](#example)

```
class MyClass:
    x: int
    pass
```

Use instead:

```
class MyClass:
    x: int
```