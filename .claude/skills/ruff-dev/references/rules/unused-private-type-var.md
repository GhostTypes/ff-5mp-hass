# [unused-private-type-var (PYI018)](#unused-private-type-var-pyi018)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-private-type-var%27%20OR%20PYI018)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funused_private_type_definition.rs#L32)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of unused private `TypeVar`, `ParamSpec` or
`TypeVarTuple` declarations.

## [Why is this bad?](#why-is-this-bad)

A private `TypeVar` that is defined but not used is likely a mistake. It
should either be used, made public, or removed to avoid confusion. A type
variable is considered "private" if its name starts with an underscore.

## [Example](#example)

```
import typing
import typing_extensions

_T = typing.TypeVar("_T")
_Ts = typing_extensions.TypeVarTuple("_Ts")
```

## [Fix safety](#fix-safety)

The fix is always marked as unsafe, as it would break your code if the type
variable is imported by another module.