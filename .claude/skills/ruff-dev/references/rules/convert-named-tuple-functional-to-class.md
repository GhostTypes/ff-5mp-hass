# [convert-named-tuple-functional-to-class (UP014)](#convert-named-tuple-functional-to-class-up014)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27convert-named-tuple-functional-to-class%27%20OR%20UP014)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fconvert_named_tuple_functional_to_class.rs#L52)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `NamedTuple` declarations that use functional syntax.

## [Why is this bad?](#why-is-this-bad)

`NamedTuple` subclasses can be defined either through a functional syntax
(`Foo = NamedTuple(...)`) or a class syntax (`class Foo(NamedTuple): ...`).

The class syntax is more readable and generally preferred over the
functional syntax, which exists primarily for backwards compatibility
with `collections.namedtuple`.

## [Example](#example)

```
from typing import NamedTuple

Foo = NamedTuple("Foo", [("a", int), ("b", str)])
```

Use instead:

```
from typing import NamedTuple


class Foo(NamedTuple):
    a: int
    b: str
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there are any comments within the
range of the `NamedTuple` definition, as these will be dropped by the
autofix.

## [References](#references)

* [Python documentation: `typing.NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple)