# [eq-without-hash (PLW1641)](#eq-without-hash-plw1641)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27eq-without-hash%27%20OR%20PLW1641)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Feq_without_hash.rs#L66)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for classes that implement `__eq__` but not `__hash__`.

## [Why is this bad?](#why-is-this-bad)

A class that implements `__eq__` but not `__hash__` will have its hash
method implicitly set to `None`, regardless of if a superclass defines
`__hash__`. This will cause the class to be unhashable, which will in turn
cause issues when using instances of the class as keys in a dictionary or
members of a set.

## [Example](#example)

```
class Person:
    def __init__(self):
        self.name = "monty"

    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name
```

Use instead:

```
class Person:
    def __init__(self):
        self.name = "monty"

    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name

    def __hash__(self):
        return hash(self.name)
```

In general, it is unsound to inherit a `__hash__` implementation from a parent class while
overriding the `__eq__` implementation because the two must be kept in sync. However, an easy
way to resolve this error in cases where it *is* sound is to explicitly set `__hash__` to the
parent class's implementation:

```
class Developer(Person):
    def __init__(self): ...

    def __eq__(self, other): ...

    __hash__ = Person.__hash__
```

## [References](#references)

* [Python documentation: `object.__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)
* [Python glossary: hashable](https://docs.python.org/3/glossary.html#term-hashable)