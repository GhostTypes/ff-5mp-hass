# [useless-object-inheritance (UP004)](#useless-object-inheritance-up004)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-object-inheritance%27%20OR%20UP004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fuseless_object_inheritance.rs#L34)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for classes that inherit from `object`.

## [Why is this bad?](#why-is-this-bad)

Since Python 3, all classes inherit from `object` by default, so `object` can
be omitted from the list of base classes.

## [Example](#example)

```
class Foo(object): ...
```

Use instead:

```
class Foo: ...
```

## [Fix safety](#fix-safety)

This fix is unsafe if it would cause comments to be deleted.

## [References](#references)

* [PEP 3115 – Metaclasses in Python 3000](https://peps.python.org/pep-3115/)