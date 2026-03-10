# [if-expr-min-max (FURB136)](#if-expr-min-max-furb136)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-expr-min-max%27%20OR%20FURB136)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fif_expr_min_max.rs#L33)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` expressions that can be replaced with `min()` or `max()`
calls.

## [Why is this bad?](#why-is-this-bad)

An `if` expression that selects the lesser or greater of two
sub-expressions can be replaced with a `min()` or `max()` call
respectively. When possible, prefer `min()` and `max()`, as they're more
concise and readable than the equivalent `if` expression.

## [Example](#example)

```
highest_score = score1 if score1 > score2 else score2
```

Use instead:

```
highest_score = max(score2, score1)
```

## [References](#references)

* [Python documentation: `min`](https://docs.python.org/3.11/library/functions.html#min)
* [Python documentation: `max`](https://docs.python.org/3.11/library/functions.html#max)