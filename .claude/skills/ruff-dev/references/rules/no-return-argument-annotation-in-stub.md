# [no-return-argument-annotation-in-stub (PYI050)](#no-return-argument-annotation-in-stub-pyi050)

Added in [v0.0.272](https://github.com/astral-sh/ruff/releases/tag/v0.0.272) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-return-argument-annotation-in-stub%27%20OR%20PYI050)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fno_return_argument_annotation.rs#L43)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for uses of `typing.NoReturn` (and `typing_extensions.NoReturn`) for
parameter annotations.

## [Why is this bad?](#why-is-this-bad)

Prefer `Never` over `NoReturn` for parameter annotations. `Never` has a
clearer name in these contexts, since it makes little sense to talk about a
parameter annotation "not returning".

This is a purely stylistic lint: the two types have identical semantics for
type checkers. Both represent Python's "[bottom type](https://en.wikipedia.org/wiki/Bottom_type)" (a type that has no
members).

## [Example](#example)

```
from typing import NoReturn

def foo(x: NoReturn): ...
```

Use instead:

```
from typing import Never

def foo(x: Never): ...
```

## [References](#references)

* [Python documentation: `typing.Never`](https://docs.python.org/3/library/typing.html#typing.Never)
* [Python documentation: `typing.NoReturn`](https://docs.python.org/3/library/typing.html#typing.NoReturn)