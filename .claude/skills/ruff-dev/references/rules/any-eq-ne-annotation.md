# [any-eq-ne-annotation (PYI032)](#any-eq-ne-annotation-pyi032)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27any-eq-ne-annotation%27%20OR%20PYI032)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fany_eq_ne_annotation.rs#L46)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `__eq__` and `__ne__` implementations that use `typing.Any` as
the type annotation for their second parameter.

## [Why is this bad?](#why-is-this-bad)

The Python documentation recommends the use of `object` to "indicate that a
value could be any type in a typesafe manner". `Any`, on the other hand,
should be seen as an "escape hatch when you need to mix dynamically and
statically typed code". Since using `Any` allows you to write highly unsafe
code, you should generally only use `Any` when the semantics of your code
would otherwise be inexpressible to the type checker.

The expectation in Python is that a comparison of two arbitrary objects
using `==` or `!=` should never raise an exception. This contract can be
fully expressed in the type system and does not involve requesting unsound
behaviour from a type checker. As such, `object` is a more appropriate
annotation than `Any` for the second parameter of the methods implementing
these comparison operators -- `__eq__` and `__ne__`.

## [Example](#example)

```
from typing import Any

class Foo:
    def __eq__(self, obj: Any) -> bool: ...
```

Use instead:

```
class Foo:
    def __eq__(self, obj: object) -> bool: ...
```

## [References](#references)

* [Python documentation: The `Any` type](https://docs.python.org/3/library/typing.html#the-any-type)
* [Mypy documentation: Any vs. object](https://mypy.readthedocs.io/en/latest/dynamic_typing.html#any-vs-object)