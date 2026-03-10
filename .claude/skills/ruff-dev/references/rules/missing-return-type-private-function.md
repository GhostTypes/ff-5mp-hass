# [missing-return-type-private-function (ANN202)](#missing-return-type-private-function-ann202)

Added in [v0.0.105](https://github.com/astral-sh/ruff/releases/tag/v0.0.105) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-return-type-private-function%27%20OR%20ANN202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_annotations%2Frules%2Fdefinition.rs#L297)

Derived from the **[flake8-annotations](../#flake8-annotations-ann)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks that private functions and methods have return type annotations.

## [Why is this bad?](#why-is-this-bad)

Type annotations are a good way to document the return types of functions. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any returned values, and the types expected by callers, match expectation.

## [Example](#example)

```
def _add(a, b):
    return a + b
```

Use instead:

```
def _add(a: int, b: int) -> int:
    return a + b
```

## [Availability](#availability)

Because this rule relies on the third-party `typing_extensions` module for some Python versions,
its diagnostic will not be emitted, and no fix will be offered, if `typing_extensions` imports
have been disabled by the [`lint.typing-extensions`](../../settings/#lint_typing-extensions) linter option.

## [Options](#options)

* [`lint.typing-extensions`](../../settings/#lint_typing-extensions)