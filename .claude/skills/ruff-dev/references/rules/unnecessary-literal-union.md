# [unnecessary-literal-union (PYI030)](#unnecessary-literal-union-pyi030)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-literal-union%27%20OR%20PYI030)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funnecessary_literal_union.rs#L49)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of multiple literal types in a union.

## [Why is this bad?](#why-is-this-bad)

`Literal["foo", 42]` has identical semantics to
`Literal["foo"] | Literal[42]`, but is clearer and more concise.

## [Example](#example)

```
from typing import Literal

field: Literal[1] | Literal[2] | str
```

Use instead:

```
from typing import Literal

field: Literal[1, 2] | str
```

## [Fix safety](#fix-safety)

This fix is marked unsafe if it would delete any comments within the replacement range.

An example to illustrate where comments are preserved and where they are not:

```
from typing import Literal

field: (
    # deleted comment
    Literal["a", "b"]  # deleted comment
    # deleted comment
    | Literal["c", "d"]  # preserved comment
)
```

## [References](#references)

* [Python documentation: `typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)