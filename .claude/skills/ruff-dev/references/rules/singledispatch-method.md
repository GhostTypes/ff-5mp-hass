# [singledispatch-method (PLE1519)](#singledispatch-method-ple1519)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27singledispatch-method%27%20OR%20PLE1519)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsingledispatch_method.rs#L45)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for methods decorated with `@singledispatch`.

## [Why is this bad?](#why-is-this-bad)

The `@singledispatch` decorator is intended for use with functions, not methods.

Instead, use the `@singledispatchmethod` decorator, or migrate the method to a
standalone function.

## [Example](#example)

```
from functools import singledispatch


class Class:
    @singledispatch
    def method(self, arg): ...
```

Use instead:

```
from functools import singledispatchmethod


class Class:
    @singledispatchmethod
    def method(self, arg): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as migrating from `@singledispatch` to
`@singledispatchmethod` may change the behavior of the code.