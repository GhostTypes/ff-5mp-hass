# [if-with-same-arms (SIM114)](#if-with-same-arms-sim114)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-with-same-arms%27%20OR%20SIM114)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fif_with_same_arms.rs#L38)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` branches with identical arm bodies.

## [Why is this bad?](#why-is-this-bad)

If multiple arms of an `if` statement have the same body, using `or`
better signals the intent of the statement.

## [Example](#example)

```
if x == 1:
    print("Hello")
elif x == 2:
    print("Hello")
```

Use instead:

```
if x == 1 or x == 2:
    print("Hello")
```