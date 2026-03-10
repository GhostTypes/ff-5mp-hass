# [if-else-block-instead-of-if-exp (SIM108)](#if-else-block-instead-of-if-exp-sim108)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-else-block-instead-of-if-exp%27%20OR%20SIM108)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fif_else_block_instead_of_if_exp.rs#L63)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Check for `if`-`else`-blocks that can be replaced with a ternary
or binary operator.

The lint is suppressed if the suggested replacement would exceed
the maximum line length configured in [pycodestyle.max-line-length](https://docs.astral.sh/ruff/settings/#lint_pycodestyle_max-line-length).

## [Why is this bad?](#why-is-this-bad)

`if`-`else`-blocks that assign a value to a variable in both branches can
be expressed more concisely by using a ternary or binary operator.

## [Example](#example)

```
if foo:
    bar = x
else:
    bar = y
```

Use instead:

```
bar = x if foo else y
```

Or:

```
if cond:
    z = cond
else:
    z = other_cond
```

Use instead:

```
z = cond or other_cond
```

## [Known issues](#known-issues)

This is an opinionated style rule that may not always be to everyone's
taste, especially for code that makes use of complex `if` conditions.
Ternary operators can also make it harder to measure [code coverage](https://github.com/nedbat/coveragepy/issues/509)
with tools that use line profiling.

## [References](#references)

* [Python documentation: Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)