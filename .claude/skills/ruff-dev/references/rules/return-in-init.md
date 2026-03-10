# [return-in-init (PLE0101)](#return-in-init-ple0101)

Added in [v0.0.248](https://github.com/astral-sh/ruff/releases/tag/v0.0.248) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27return-in-init%27%20OR%20PLE0101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Freturn_in_init.rs#L37)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `__init__` methods that return values.

## [Why is this bad?](#why-is-this-bad)

The `__init__` method is the constructor for a given Python class,
responsible for initializing, rather than creating, new objects.

The `__init__` method has to return `None`. Returning any value from
an `__init__` method will result in a runtime error.

## [Example](#example)

```
class Example:
    def __init__(self):
        return []
```

Use instead:

```
class Example:
    def __init__(self):
        self.value = []
```

## [References](#references)

* [CodeQL: `py-explicit-return-in-init`](https://codeql.github.com/codeql-query-help/python/py-explicit-return-in-init/)