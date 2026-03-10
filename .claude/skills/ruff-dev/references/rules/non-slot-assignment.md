# [non-slot-assignment (PLE0237)](#non-slot-assignment-ple0237)

Added in [v0.1.15](https://github.com/astral-sh/ruff/releases/tag/v0.1.15) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-slot-assignment%27%20OR%20PLE0237)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnon_slot_assignment.rs#L49)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for assignments to attributes that are not defined in `__slots__`.

## [Why is this bad?](#why-is-this-bad)

When using `__slots__`, only the specified attributes are allowed.
Attempting to assign to an attribute that is not defined in `__slots__`
will result in an `AttributeError` at runtime.

## [Known problems](#known-problems)

This rule can't detect `__slots__` implementations in superclasses, and
so limits its analysis to classes that inherit from (at most) `object`.

## [Example](#example)

```
class Student:
    __slots__ = ("name",)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  # [assigning-non-slot]
        self.setup()

    def setup(self):
        pass
```

Use instead:

```
class Student:
    __slots__ = ("name", "surname")

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.setup()

    def setup(self):
        pass
```