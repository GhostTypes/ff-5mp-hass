# [unused-private-protocol (PYI046)](#unused-private-protocol-pyi046)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-private-protocol%27%20OR%20PYI046)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funused_private_type_definition.rs#L89)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for the presence of unused private `typing.Protocol` definitions.

## [Why is this bad?](#why-is-this-bad)

A private `typing.Protocol` that is defined but not used is likely a
mistake. It should either be used, made public, or removed to avoid
confusion.

## [Example](#example)

```
import typing

class _PrivateProtocol(typing.Protocol):
    foo: int
```

Use instead:

```
import typing

class _PrivateProtocol(typing.Protocol):
    foo: int

def func(arg: _PrivateProtocol) -> None: ...
```