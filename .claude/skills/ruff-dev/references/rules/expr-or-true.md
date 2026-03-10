# [expr-or-true (SIM222)](#expr-or-true-sim222)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27expr-or-true%27%20OR%20SIM222)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L216)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `or` expressions that contain truthy values.

## [Why is this bad?](#why-is-this-bad)

If the expression is used as a condition, it can be replaced in-full with
`True`.

In other cases, the expression can be short-circuited to the first truthy
value.

By using `True` (or the first truthy value), the code is more concise
and easier to understand, since it no longer contains redundant conditions.

## [Example](#example)

```
if x or [1] or y:
    pass

a = x or [1] or y
```

Use instead:

```
if True:
    pass

a = x or [1]
```