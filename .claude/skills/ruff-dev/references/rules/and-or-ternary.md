# [and-or-ternary (PLR1706)](#and-or-ternary-plr1706)

Removed (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27and-or-ternary%27%20OR%20PLR1706)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fand_or_ternary.rs#L31)

Derived from the **[Pylint](../#pylint-pl)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removal](#removal)

This rule was removed from Ruff because it was common for it to introduce behavioral changes.
See [#9007](https://github.com/astral-sh/ruff/issues/9007) for more information.

## [What it does](#what-it-does)

Checks for uses of the known pre-Python 2.5 ternary syntax.

## [Why is this bad?](#why-is-this-bad)

Prior to the introduction of the if-expression (ternary) operator in Python
2.5, the only way to express a conditional expression was to use the `and`
and `or` operators.

The if-expression construct is clearer and more explicit, and should be
preferred over the use of `and` and `or` for ternary expressions.

## [Example](#example)

```
x, y = 1, 2
maximum = x >= y and x or y
```

Use instead:

```
x, y = 1, 2
maximum = x if x >= y else y
```