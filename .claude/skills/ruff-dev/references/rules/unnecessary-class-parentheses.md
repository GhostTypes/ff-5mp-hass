# [unnecessary-class-parentheses (UP039)](#unnecessary-class-parentheses-up039)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-class-parentheses%27%20OR%20UP039)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funnecessary_class_parentheses.rs#L27)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for class definitions that include unnecessary parentheses after
the class name.

## [Why is this bad?](#why-is-this-bad)

If a class definition doesn't have any bases, the parentheses are
unnecessary.

## [Example](#example)

```
class Foo():
    ...
```

Use instead:

```
class Foo:
    ...
```