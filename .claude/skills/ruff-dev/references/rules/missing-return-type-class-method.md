# [missing-return-type-class-method (ANN206)](#missing-return-type-class-method-ann206)

Added in [v0.0.105](https://github.com/astral-sh/ruff/releases/tag/v0.0.105) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-return-type-class-method%27%20OR%20ANN206)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_annotations%2Frules%2Fdefinition.rs#L450)

Derived from the **[flake8-annotations](../#flake8-annotations-ann)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks that class methods have return type annotations.

## [Why is this bad?](#why-is-this-bad)

Type annotations are a good way to document the return types of functions. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any returned values, and the types expected by callers, match expectation.

## [Example](#example)

```
class Foo:
    @classmethod
    def bar(cls):
        return 1
```

Use instead:

```
class Foo:
    @classmethod
    def bar(cls) -> int:
        return 1
```