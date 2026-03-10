# [useless-class-metaclass-type (UP050)](#useless-class-metaclass-type-up050)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-class-metaclass-type%27%20OR%20UP050)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fuseless_class_metaclass_type.rs#L31)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `metaclass=type` in class definitions.

## [Why is this bad?](#why-is-this-bad)

Since Python 3, the default metaclass is `type`, so specifying it explicitly is redundant.

Even though `__prepare__` is not required, the default metaclass (`type`) implements it,
for the convenience of subclasses calling it via `super()`.

## [Example](#example)

```
class Foo(metaclass=type): ...
```

Use instead:

```
class Foo: ...
```

## [References](#references)

* [PEP 3115 – Metaclasses in Python 3000](https://peps.python.org/pep-3115/)