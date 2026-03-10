# [redundant-literal-union (PYI051)](#redundant-literal-union-pyi051)

Added in [v0.0.283](https://github.com/astral-sh/ruff/releases/tag/v0.0.283) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-literal-union%27%20OR%20PYI051)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fredundant_literal_union.rs#L39)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for redundant unions between a `Literal` and a builtin supertype of
that `Literal`.

## [Why is this bad?](#why-is-this-bad)

Using a `Literal` type in a union with its builtin supertype is redundant,
as the supertype will be strictly more general than the `Literal` type.
For example, `Literal["A"] | str` is equivalent to `str`, and
`Literal[1] | int` is equivalent to `int`, as `str` and `int` are the
supertypes of `"A"` and `1` respectively.

## [Example](#example)

```
from typing import Literal

x: Literal["A", b"B"] | str
```

Use instead:

```
from typing import Literal

x: Literal[b"B"] | str
```