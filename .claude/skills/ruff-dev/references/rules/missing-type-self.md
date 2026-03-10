# [missing-type-self (ANN101)](#missing-type-self-ann101)

Removed (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-type-self%27%20OR%20ANN101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_annotations%2Frules%2Fdefinition.rs#L153)

Derived from the **[flake8-annotations](../#flake8-annotations-ann)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule has been removed because type checkers can infer this type without annotation.

## [What it does](#what-it-does)

Checks that instance method `self` arguments have type annotations.

## [Why is this bad?](#why-is-this-bad)

Type annotations are a good way to document the types of function arguments. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any provided arguments match expectation.

Note that many type checkers will infer the type of `self` automatically, so this
annotation is not strictly necessary.

## [Example](#example)

```
class Foo:
    def bar(self): ...
```

Use instead:

```
class Foo:
    def bar(self: "Foo"): ...
```