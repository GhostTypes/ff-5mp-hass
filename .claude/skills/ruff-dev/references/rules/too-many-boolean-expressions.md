# [too-many-boolean-expressions (PLR0916)](#too-many-boolean-expressions-plr0916)

Preview (since [v0.1.1](https://github.com/astral-sh/ruff/releases/tag/v0.1.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-boolean-expressions%27%20OR%20PLR0916)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_boolean_expressions.rs#L28)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for too many Boolean expressions in an `if` statement.

By default, this rule allows up to 5 expressions. This can be configured
using the [`lint.pylint.max-bool-expr`](../../settings/#lint_pylint_max-bool-expr) option.

## [Why is this bad?](#why-is-this-bad)

`if` statements with many Boolean expressions are harder to understand
and maintain. Consider assigning the result of the Boolean expression,
or any of its sub-expressions, to a variable.

## [Example](#example)

```
if a and b and c and d and e and f and g and h:
    ...
```

## [Options](#options)

* [`lint.pylint.max-bool-expr`](../../settings/#lint_pylint_max-bool-expr)