# [invalid-length-return-type (PLE0303)](#invalid-length-return-type-ple0303)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-length-return-type%27%20OR%20PLE0303)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_length_return.rs#L42)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__len__` implementations that return values that are not non-negative
integers.

## [Why is this bad?](#why-is-this-bad)

The `__len__` method should return a non-negative integer. Returning a different
value may cause unexpected behavior.

Note: `bool` is a subclass of `int`, so it's technically valid for `__len__` to
return `True` or `False`. However, for consistency with other rules, Ruff will
still emit a diagnostic when `__len__` returns a `bool`.

## [Example](#example)

```
class Foo:
    def __len__(self):
        return "2"
```

Use instead:

```
class Foo:
    def __len__(self):
        return 2
```

## [References](#references)

* [Python documentation: The `__len__` method](https://docs.python.org/3/reference/datamodel.html#object.__len__)