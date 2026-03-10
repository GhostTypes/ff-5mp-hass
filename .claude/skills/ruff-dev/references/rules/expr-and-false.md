# [expr-and-false (SIM223)](#expr-and-false-sim223)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27expr-and-false%27%20OR%20SIM223)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L269)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `and` expressions that contain falsey values.

## [Why is this bad?](#why-is-this-bad)

If the expression is used as a condition, it can be replaced in-full with
`False`.

In other cases, the expression can be short-circuited to the first falsey
value.

By using `False` (or the first falsey value), the code is more concise
and easier to understand, since it no longer contains redundant conditions.

## [Example](#example)

```
if x and [] and y:
    pass

a = x and [] and y
```

Use instead:

```
if False:
    pass

a = x and []
```