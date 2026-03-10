# [invalid-hash-return-type (PLE0309)](#invalid-hash-return-type-ple0309)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-hash-return-type%27%20OR%20PLE0309)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_hash_return.rs#L41)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__hash__` implementations that return non-integer values.

## [Why is this bad?](#why-is-this-bad)

The `__hash__` method should return an integer. Returning a different
type may cause unexpected behavior.

Note: `bool` is a subclass of `int`, so it's technically valid for `__hash__` to
return `True` or `False`. However, for consistency with other rules, Ruff will
still emit a diagnostic when `__hash__` returns a `bool`.

## [Example](#example)

```
class Foo:
    def __hash__(self):
        return "2"
```

Use instead:

```
class Foo:
    def __hash__(self):
        return 2
```

## [References](#references)

* [Python documentation: The `__hash__` method](https://docs.python.org/3/reference/datamodel.html#object.__hash__)