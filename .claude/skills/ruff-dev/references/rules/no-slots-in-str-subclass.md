# [no-slots-in-str-subclass (SLOT000)](#no-slots-in-str-subclass-slot000)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-slots-in-str-subclass%27%20OR%20SLOT000)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_slots%2Frules%2Fno_slots_in_str_subclass.rs#L41)

Derived from the **[flake8-slots](../#flake8-slots-slot)** linter.

## [What it does](#what-it-does)

Checks for subclasses of `str` that lack a `__slots__` definition.

## [Why is this bad?](#why-is-this-bad)

In Python, the `__slots__` attribute allows you to explicitly define the
attributes (instance variables) that a class can have. By default, Python
uses a dictionary to store an object's attributes, which incurs some memory
overhead. However, when `__slots__` is defined, Python uses a more compact
internal structure to store the object's attributes, resulting in memory
savings.

Subclasses of `str` inherit all the attributes and methods of the built-in
`str` class. Since strings are typically immutable, they don't require
additional attributes beyond what the `str` class provides. Defining
`__slots__` for subclasses of `str` prevents the creation of a dictionary
for each instance, reducing memory consumption.

## [Example](#example)

```
class Foo(str):
    pass
```

Use instead:

```
class Foo(str):
    __slots__ = ()
```

## [References](#references)

* [Python documentation: `__slots__`](https://docs.python.org/3/reference/datamodel.html#slots)