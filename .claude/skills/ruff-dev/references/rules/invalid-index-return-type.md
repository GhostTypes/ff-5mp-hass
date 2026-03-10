# [invalid-index-return-type (PLE0305)](#invalid-index-return-type-ple0305)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-index-return-type%27%20OR%20PLE0305)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_index_return.rs#L43)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__index__` implementations that return non-integer values.

## [Why is this bad?](#why-is-this-bad)

The `__index__` method should return an integer. Returning a different
type may cause unexpected behavior.

Note: `bool` is a subclass of `int`, so it's technically valid for `__index__` to
return `True` or `False`. However, a `DeprecationWarning` (`DeprecationWarning: __index__ returned non-int (type bool)`) for such cases was already introduced,
thus this is a conscious difference between the original pylint rule and the
current ruff implementation.

## [Example](#example)

```
class Foo:
    def __index__(self):
        return "2"
```

Use instead:

```
class Foo:
    def __index__(self):
        return 2
```

## [References](#references)

* [Python documentation: The `__index__` method](https://docs.python.org/3/reference/datamodel.html#object.__index__)