# [duplicate-isinstance-call (SIM101)](#duplicate-isinstance-call-sim101)

Added in [v0.0.212](https://github.com/astral-sh/ruff/releases/tag/v0.0.212) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27duplicate-isinstance-call%27%20OR%20SIM101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L47)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for multiple `isinstance` calls on the same target.

## [Why is this bad?](#why-is-this-bad)

To check if an object is an instance of any one of multiple types
or classes, it is unnecessary to use multiple `isinstance` calls, as
the second argument of the `isinstance` built-in function accepts a
tuple of types and classes.

Using a single `isinstance` call implements the same behavior with more
concise code and clearer intent.

## [Example](#example)

```
if isinstance(obj, int) or isinstance(obj, float):
    pass
```

Use instead:

```
if isinstance(obj, (int, float)):
    pass
```

## [References](#references)

* [Python documentation: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)