# [singledispatchmethod-function (PLE1520)](#singledispatchmethod-function-ple1520)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27singledispatchmethod-function%27%20OR%20PLE1520)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsingledispatchmethod_function.rs#L43)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for non-method functions decorated with `@singledispatchmethod`.

## [Why is this bad?](#why-is-this-bad)

The `@singledispatchmethod` decorator is intended for use with methods, not
functions.

Instead, use the `@singledispatch` decorator.

## [Example](#example)

```
from functools import singledispatchmethod


@singledispatchmethod
def func(arg): ...
```

Use instead:

```
from functools import singledispatch


@singledispatch
def func(arg): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as migrating from `@singledispatchmethod` to
`@singledispatch` may change the behavior of the code.