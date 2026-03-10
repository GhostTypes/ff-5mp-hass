# [yield-in-init (PLE0100)](#yield-in-init-ple0100)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27yield-in-init%27%20OR%20PLE0100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fyield_in_init.rs#L31)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__init__` methods that are turned into generators by the
inclusion of `yield` or `yield from` expressions.

## [Why is this bad?](#why-is-this-bad)

The `__init__` method is the constructor for a given Python class,
responsible for initializing, rather than creating, new objects.

The `__init__` method has to return `None`. By including a `yield` or
`yield from` expression in an `__init__`, the method will return a
generator object when called at runtime, resulting in a runtime error.

## [Example](#example)

```
class InitIsGenerator:
    def __init__(self, i):
        yield i
```

## [References](#references)

* [CodeQL: `py-init-method-is-generator`](https://codeql.github.com/codeql-query-help/python/py-init-method-is-generator/)