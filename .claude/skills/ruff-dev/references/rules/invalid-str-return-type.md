# [invalid-str-return-type (PLE0307)](#invalid-str-return-type-ple0307)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-str-return-type%27%20OR%20PLE0307)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_str_return.rs#L37)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__str__` implementations that return a type other than `str`.

## [Why is this bad?](#why-is-this-bad)

The `__str__` method should return a `str` object. Returning a different
type may cause unexpected behavior.

## [Example](#example)

```
class Foo:
    def __str__(self):
        return True
```

Use instead:

```
class Foo:
    def __str__(self):
        return "Foo"
```

## [References](#references)

* [Python documentation: The `__str__` method](https://docs.python.org/3/reference/datamodel.html#object.__str__)