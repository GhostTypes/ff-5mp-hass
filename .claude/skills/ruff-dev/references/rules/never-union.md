# [never-union (RUF020)](#never-union-ruf020)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27never-union%27%20OR%20RUF020)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fnever_union.rs#L37)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `typing.NoReturn` and `typing.Never` in union types.

## [Why is this bad?](#why-is-this-bad)

`typing.NoReturn` and `typing.Never` are special types, used to indicate
that a function never returns, or that a type has no values.

Including `typing.NoReturn` or `typing.Never` in a union type is redundant,
as, e.g., `typing.Never | T` is equivalent to `T`.

## [Example](#example)

```
from typing import Never


def func() -> Never | int: ...
```

Use instead:

```
def func() -> int: ...
```

## [References](#references)

* [Python documentation: `typing.Never`](https://docs.python.org/3/library/typing.html#typing.Never)
* [Python documentation: `typing.NoReturn`](https://docs.python.org/3/library/typing.html#typing.NoReturn)