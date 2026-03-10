# [redundant-numeric-union (PYI041)](#redundant-numeric-union-pyi041)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-numeric-union%27%20OR%20PYI041)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fredundant_numeric_union.rs#L55)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for parameter annotations that contain redundant unions between
builtin numeric types (e.g., `int | float`).

## [Why is this bad?](#why-is-this-bad)

The [typing specification](https://typing.python.org/en/latest/spec/special-types.html#special-cases-for-float-and-complex) states:

> Python’s numeric types `complex`, `float` and `int` are not subtypes of
> each other, but to support common use cases, the type system contains a
> straightforward shortcut: when an argument is annotated as having type
> `float`, an argument of type `int` is acceptable; similar, for an
> argument annotated as having type `complex`, arguments of type `float` or
> `int` are acceptable.

As such, a union that includes both `int` and `float` is redundant in the
specific context of a parameter annotation, as it is equivalent to a union
that only includes `float`. For readability and clarity, unions should omit
redundant elements.

## [Example](#example)

```
def foo(x: float | int | str) -> None: ...
```

Use instead:

```
def foo(x: float | str) -> None: ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the type annotation contains comments.

Note that while the fix may flatten nested unions into a single top-level union,
the semantics of the annotation will remain unchanged.

## [References](#references)

* [Python documentation: The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
* [PEP 484: The numeric tower](https://peps.python.org/pep-0484/#the-numeric-tower)