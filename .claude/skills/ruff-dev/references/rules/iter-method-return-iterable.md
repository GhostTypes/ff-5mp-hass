# [iter-method-return-iterable (PYI045)](#iter-method-return-iterable-pyi045)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27iter-method-return-iterable%27%20OR%20PYI045)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fiter_method_return_iterable.rs#L71)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for `__iter__` methods in stubs that return `Iterable[T]` instead
of an `Iterator[T]`.

## [Why is this bad?](#why-is-this-bad)

`__iter__` methods should always should return an `Iterator` of some kind,
not an `Iterable`.

In Python, an `Iterable` is an object that has an `__iter__` method; an
`Iterator` is an object that has `__iter__` and `__next__` methods. All
`__iter__` methods are expected to return `Iterator`s. Type checkers may
not always recognize an object as being iterable if its `__iter__` method
does not return an `Iterator`.

Every `Iterator` is an `Iterable`, but not every `Iterable` is an `Iterator`.
For example, `list` is an `Iterable`, but not an `Iterator`; you can obtain
an iterator over a list's elements by passing the list to `iter()`:

```
>>> import collections.abc
>>> x = [42]
>>> isinstance(x, collections.abc.Iterable)
True
>>> isinstance(x, collections.abc.Iterator)
False
>>> next(x)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
>>> y = iter(x)
>>> isinstance(y, collections.abc.Iterable)
True
>>> isinstance(y, collections.abc.Iterator)
True
>>> next(y)
42
```

Using `Iterable` rather than `Iterator` as a return type for an `__iter__`
methods would imply that you would not necessarily be able to call `next()`
on the returned object, violating the expectations of the interface.

## [Example](#example)

```
import collections.abc


class Klass:
    def __iter__(self) -> collections.abc.Iterable[str]: ...
```

Use instead:

```
import collections.abc


class Klass:
    def __iter__(self) -> collections.abc.Iterator[str]: ...
```