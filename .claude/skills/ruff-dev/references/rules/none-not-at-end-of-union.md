# [none-not-at-end-of-union (RUF036)](#none-not-at-end-of-union-ruf036)

Preview (since [0.7.4](https://github.com/astral-sh/ruff/releases/tag/0.7.4)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27none-not-at-end-of-union%27%20OR%20RUF036)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fnone_not_at_end_of_union.rs#L32)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for type annotations where `None` is not at the end of an union.

## [Why is this bad?](#why-is-this-bad)

Type annotation unions are commutative, meaning that the order of the elements
does not matter. The `None` literal represents the absence of a value. For
readability, it's preferred to write the more informative type expressions first.

## [Example](#example)

```
def func(arg: None | int): ...
```

Use instead:

```
def func(arg: int | None): ...
```

## [References](#references)

* [Python documentation: Union type](https://docs.python.org/3/library/stdtypes.html#types-union)
* [Python documentation: `typing.Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)
* [Python documentation: `None`](https://docs.python.org/3/library/constants.html#None)