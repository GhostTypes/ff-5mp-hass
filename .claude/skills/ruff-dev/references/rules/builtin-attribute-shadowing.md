# [builtin-attribute-shadowing (A003)](#builtin-attribute-shadowing-a003)

Added in [v0.0.48](https://github.com/astral-sh/ruff/releases/tag/v0.0.48) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-attribute-shadowing%27%20OR%20A003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_builtins%2Frules%2Fbuiltin_attribute_shadowing.rs#L59)

Derived from the **[flake8-builtins](../#flake8-builtins-a)** linter.

## [What it does](#what-it-does)

Checks for class attributes and methods that use the same names as
Python builtins.

## [Why is this bad?](#why-is-this-bad)

Reusing a builtin name for the name of an attribute increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the attribute for the
builtin and vice versa.

Since methods and class attributes typically cannot be referenced directly
from outside the class scope, this rule only applies to those methods
and attributes that both shadow a builtin *and* are referenced from within
the class scope, as in the following example, where the `list[int]` return
type annotation resolves to the `list` method, rather than the builtin:

```
class Class:
    @staticmethod
    def list() -> None:
        pass

    @staticmethod
    def repeat(value: int, times: int) -> list[int]:
        return [value] * times
```

Builtins can be marked as exceptions to this rule via the
[`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist) configuration option, or
converted to the appropriate dunder method. Methods decorated with
`@typing.override` or `@typing_extensions.override` are also
ignored.

## [Example](#example)

```
class Class:
    @staticmethod
    def list() -> None:
        pass

    @staticmethod
    def repeat(value: int, times: int) -> list[int]:
        return [value] * times
```

## [Options](#options)

* [`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist)