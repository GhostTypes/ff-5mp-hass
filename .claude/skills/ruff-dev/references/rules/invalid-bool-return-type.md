# [invalid-bool-return-type (PLE0304)](#invalid-bool-return-type-ple0304)

Preview (since [v0.3.3](https://github.com/astral-sh/ruff/releases/tag/v0.3.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-bool-return-type%27%20OR%20PLE0304)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_bool_return.rs#L37)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `__bool__` implementations that return a type other than `bool`.

## [Why is this bad?](#why-is-this-bad)

The `__bool__` method should return a `bool` object. Returning a different
type may cause unexpected behavior.

## [Example](#example)

```
class Foo:
    def __bool__(self):
        return 2
```

Use instead:

```
class Foo:
    def __bool__(self):
        return True
```

## [References](#references)

* [Python documentation: The `__bool__` method](https://docs.python.org/3/reference/datamodel.html#object.__bool__)