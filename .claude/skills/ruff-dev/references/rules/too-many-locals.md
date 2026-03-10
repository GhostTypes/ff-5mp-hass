# [too-many-locals (PLR0914)](#too-many-locals-plr0914)

Preview (since [v0.1.9](https://github.com/astral-sh/ruff/releases/tag/v0.1.9)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-locals%27%20OR%20PLR0914)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_locals.rs#L22)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for functions that include too many local variables.

By default, this rule allows up to fifteen locals, as configured by the
[`lint.pylint.max-locals`](../../settings/#lint_pylint_max-locals) option.

## [Why is this bad?](#why-is-this-bad)

Functions with many local variables are harder to understand and maintain.

Consider refactoring functions with many local variables into smaller
functions with fewer assignments.

## [Options](#options)

* [`lint.pylint.max-locals`](../../settings/#lint_pylint_max-locals)