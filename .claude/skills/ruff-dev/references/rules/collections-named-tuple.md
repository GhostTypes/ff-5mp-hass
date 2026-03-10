# [collections-named-tuple (PYI024)](#collections-named-tuple-pyi024)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27collections-named-tuple%27%20OR%20PYI024)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fcollections_named_tuple.rs#L38)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for uses of `collections.namedtuple` in stub files.

## [Why is this bad?](#why-is-this-bad)

`typing.NamedTuple` is the "typed version" of `collections.namedtuple`.

Inheriting from `typing.NamedTuple` creates a custom `tuple` subclass in
the same way as using the `collections.namedtuple` factory function.
However, using `typing.NamedTuple` allows you to provide a type annotation
for each field in the class. This means that type checkers will have more
information to work with, and will be able to analyze your code more
precisely.

## [Example](#example)

```
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
```

Use instead:

```
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
```