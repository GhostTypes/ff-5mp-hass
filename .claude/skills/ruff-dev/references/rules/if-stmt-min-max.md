# [if-stmt-min-max (PLR1730)](#if-stmt-min-max-plr1730)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-stmt-min-max%27%20OR%20PLR1730)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fif_stmt_min_max.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` statements that can be replaced with `min()` or `max()`
calls.

## [Why is this bad?](#why-is-this-bad)

An `if` statement that selects the lesser or greater of two sub-expressions
can be replaced with a `min()` or `max()` call respectively. Where possible,
prefer `min()` and `max()`, as they're more concise and readable than the
equivalent `if` statements.

## [Example](#example)

```
if score > highest_score:
    highest_score = score
```

Use instead:

```
highest_score = max(highest_score, score)
```

## [Fix safety](#fix-safety)

This fix is marked unsafe if it would delete any comments within the replacement range.

An example to illustrate where comments are preserved and where they are not:

```
a, b = 0, 10

if a >= b: # deleted comment
    # deleted comment
    a = b # preserved comment
```

## [References](#references)

* [Python documentation: `max`](https://docs.python.org/3/library/functions.html#max)
* [Python documentation: `min`](https://docs.python.org/3/library/functions.html#min)