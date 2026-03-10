# [too-many-nested-blocks (PLR1702)](#too-many-nested-blocks-plr1702)

Preview (since [v0.1.15](https://github.com/astral-sh/ruff/releases/tag/v0.1.15)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-nested-blocks%27%20OR%20PLR1702)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_nested_blocks.rs#L21)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for functions or methods with too many nested blocks.

By default, this rule allows up to five nested blocks.
This can be configured using the [`lint.pylint.max-nested-blocks`](../../settings/#lint_pylint_max-nested-blocks) option.

## [Why is this bad?](#why-is-this-bad)

Functions or methods with too many nested blocks are harder to understand
and maintain.

## [Options](#options)

* [`lint.pylint.max-nested-blocks`](../../settings/#lint_pylint_max-nested-blocks)