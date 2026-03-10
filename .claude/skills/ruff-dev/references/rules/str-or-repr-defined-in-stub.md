# [str-or-repr-defined-in-stub (PYI029)](#str-or-repr-defined-in-stub-pyi029)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27str-or-repr-defined-in-stub%27%20OR%20PYI029)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fstr_or_repr_defined_in_stub.rs#L26)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for redundant definitions of `__str__` or `__repr__` in stubs.

## [Why is this bad?](#why-is-this-bad)

Defining `__str__` or `__repr__` in a stub is almost always redundant,
as the signatures are almost always identical to those of the default
equivalent, `object.__str__` and `object.__repr__`, respectively.

## [Example](#example)

```
class Foo:
    def __repr__(self) -> str: ...
```