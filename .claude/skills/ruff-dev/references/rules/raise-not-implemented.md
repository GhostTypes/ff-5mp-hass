# [raise-not-implemented (F901)](#raise-not-implemented-f901)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-not-implemented%27%20OR%20F901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fraise_not_implemented.rs#L37)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `raise` statements that raise `NotImplemented`.

## [Why is this bad?](#why-is-this-bad)

`NotImplemented` is an exception used by binary special methods to indicate
that an operation is not implemented with respect to a particular type.

`NotImplemented` should not be raised directly. Instead, raise
`NotImplementedError`, which is used to indicate that the method is
abstract or not implemented in the derived class.

## [Example](#example)

```
class Foo:
    def bar(self):
        raise NotImplemented
```

Use instead:

```
class Foo:
    def bar(self):
        raise NotImplementedError
```

## [References](#references)

* [Python documentation: `NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented)
* [Python documentation: `NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError)