# [single-string-slots (PLC0205)](#single-string-slots-plc0205)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27single-string-slots%27%20OR%20PLC0205)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsingle_string_slots.rs#L50)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for single strings assigned to `__slots__`.

## [Why is this bad?](#why-is-this-bad)

In Python, the `__slots__` attribute allows you to explicitly define the
attributes (instance variables) that a class can have. By default, Python
uses a dictionary to store an object's attributes, which incurs some memory
overhead. However, when `__slots__` is defined, Python uses a more compact
internal structure to store the object's attributes, resulting in memory
savings.

Any string iterable may be assigned to `__slots__` (most commonly, a
`tuple` of strings). If a string is assigned to `__slots__`, it is
interpreted as a single attribute name, rather than an iterable of attribute
names. This can cause confusion, as users that iterate over the `__slots__`
value may expect to iterate over a sequence of attributes, but would instead
iterate over the characters of the string.

To use a single string attribute in `__slots__`, wrap the string in an
iterable container type, like a `tuple`.

## [Example](#example)

```
class Person:
    __slots__: str = "name"

    def __init__(self, name: str) -> None:
        self.name = name
```

Use instead:

```
class Person:
    __slots__: tuple[str, ...] = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name
```

## [References](#references)

* [Python documentation: `__slots__`](https://docs.python.org/3/reference/datamodel.html#slots)