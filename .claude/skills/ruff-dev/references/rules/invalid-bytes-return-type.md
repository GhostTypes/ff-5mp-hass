# [invalid-bytes-return-type (PLE0308)](#invalid-bytes-return-type-ple0308)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-bytes-return-type%27%20OR%20PLE0308)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_bytes_return.rs#L37)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__bytes__` implementations that return types other than `bytes`.

## [Why is this bad?](#why-is-this-bad)

The `__bytes__` method should return a `bytes` object. Returning a different
type may cause unexpected behavior.

## [Example](#example)

```
class Foo:
    def __bytes__(self):
        return 2
```

Use instead:

```
class Foo:
    def __bytes__(self):
        return b"2"
```

## [References](#references)

* [Python documentation: The `__bytes__` method](https://docs.python.org/3/reference/datamodel.html#object.__bytes__)