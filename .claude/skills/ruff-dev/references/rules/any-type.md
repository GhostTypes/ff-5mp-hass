# [any-type (ANN401)](#any-type-ann401)

Added in [v0.0.108](https://github.com/astral-sh/ruff/releases/tag/v0.0.108) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27any-type%27%20OR%20ANN401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_annotations%2Frules%2Fdefinition.rs#L523)

Derived from the **[flake8-annotations](../#flake8-annotations-ann)** linter.

## [What it does](#what-it-does)

Checks that function arguments are annotated with a more specific type than
`Any`.

## [Why is this bad?](#why-is-this-bad)

`Any` is a special type indicating an unconstrained type. When an
expression is annotated with type `Any`, type checkers will allow all
operations on it.

It's better to be explicit about the type of an expression, and to use
`Any` as an "escape hatch" only when it is really needed.

## [Example](#example)

```
from typing import Any


def foo(x: Any): ...
```

Use instead:

```
def foo(x: int): ...
```

## [Known problems](#known-problems)

Type aliases are unsupported and can lead to false positives.
For example, the following will trigger this rule inadvertently:

```
from typing import Any

MyAny = Any


def foo(x: MyAny): ...
```

## [Options](#options)

* [`lint.flake8-annotations.allow-star-arg-any`](../../settings/#lint_flake8-annotations_allow-star-arg-any)

## [References](#references)

* [Typing spec: `Any`](https://typing.python.org/en/latest/spec/special-types.html#any)
* [Python documentation: `typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any)
* [Mypy documentation: The Any type](https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-any-type)