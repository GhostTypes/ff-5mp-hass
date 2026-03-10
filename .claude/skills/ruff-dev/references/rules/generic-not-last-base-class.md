# [generic-not-last-base-class (PYI059)](#generic-not-last-base-class-pyi059)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27generic-not-last-base-class%27%20OR%20PYI059)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fgeneric_not_last_base_class.rs#L86)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for classes inheriting from `typing.Generic[]` where `Generic[]` is
not the last base class in the bases tuple.

## [Why is this bad?](#why-is-this-bad)

If `Generic[]` is not the final class in the bases tuple, unexpected
behaviour can occur at runtime (See [this CPython issue](https://github.com/python/cpython/issues/106102) for an example).

The rule is also applied to stub files, where it won't cause issues at
runtime. This is because type checkers may not be able to infer an
accurate [MRO](https://docs.python.org/3/glossary.html#term-method-resolution-order) for the class, which could lead to unexpected or
inaccurate results when they analyze your code.

For example:

```
from collections.abc import Container, Iterable, Sized
from typing import Generic, TypeVar


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class LinkedList(Generic[T], Sized):
    def push(self, item: T) -> None:
        self._items.append(item)


class MyMapping(
    Generic[K, V],
    Iterable[tuple[K, V]],
    Container[tuple[K, V]],
):
    ...
```

Use instead:

```
from collections.abc import Container, Iterable, Sized
from typing import Generic, TypeVar


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class LinkedList(Sized, Generic[T]):
    def push(self, item: T) -> None:
        self._items.append(item)


class MyMapping(
    Iterable[tuple[K, V]],
    Container[tuple[K, V]],
    Generic[K, V],
):
    ...
```

## [Fix safety](#fix-safety)

This rule's fix is always unsafe because reordering base classes can change
the behavior of the code by modifying the class's MRO. The fix will also
delete trailing comments after the `Generic` base class in multi-line base
class lists, if any are present.

## [Fix availability](#fix-availability)

This rule's fix is only available when there are no `*args` present in the base class list.

## [References](#references)

* [`typing.Generic` documentation](https://docs.python.org/3/library/typing.html#typing.Generic)