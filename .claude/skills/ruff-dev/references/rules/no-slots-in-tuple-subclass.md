# [no-slots-in-tuple-subclass (SLOT001)](#no-slots-in-tuple-subclass-slot001)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-slots-in-tuple-subclass%27%20OR%20SLOT001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_slots%2Frules%2Fno_slots_in_tuple_subclass.rs#L42)

Derived from the **[flake8-slots](../#flake8-slots-slot)** linter.

## [What it does](#what-it-does)

Checks for subclasses of `tuple` that lack a `__slots__` definition.

## [Why is this bad?](#why-is-this-bad)

In Python, the `__slots__` attribute allows you to explicitly define the
attributes (instance variables) that a class can have. By default, Python
uses a dictionary to store an object's attributes, which incurs some memory
overhead. However, when `__slots__` is defined, Python uses a more compact
internal structure to store the object's attributes, resulting in memory
savings.

Subclasses of `tuple` inherit all the attributes and methods of the
built-in `tuple` class. Since tuples are typically immutable, they don't
require additional attributes beyond what the `tuple` class provides.
Defining `__slots__` for subclasses of `tuple` prevents the creation of a
dictionary for each instance, reducing memory consumption.

## [Example](#example)

```
class Foo(tuple):
    pass
```

Use instead:

```
class Foo(tuple):
    __slots__ = ()
```

## [References](#references)

* [Python documentation: `__slots__`](https://docs.python.org/3/reference/datamodel.html#slots)