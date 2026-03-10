# [unprefixed-type-param (PYI001)](#unprefixed-type-param-pyi001)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unprefixed-type-param%27%20OR%20PYI001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fprefix_type_params.rs#L48)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks that type `TypeVar`s, `ParamSpec`s, and `TypeVarTuple`s in stubs
have names prefixed with `_`.

## [Why is this bad?](#why-is-this-bad)

Prefixing type parameters with `_` avoids accidentally exposing names
internal to the stub.

## [Example](#example)

```
from typing import TypeVar

T = TypeVar("T")
```

Use instead:

```
from typing import TypeVar

_T = TypeVar("_T")
```