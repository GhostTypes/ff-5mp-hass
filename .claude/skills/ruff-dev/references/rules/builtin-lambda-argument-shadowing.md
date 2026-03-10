# [builtin-lambda-argument-shadowing (A006)](#builtin-lambda-argument-shadowing-a006)

Added in [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-lambda-argument-shadowing%27%20OR%20A006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_builtins%2Frules%2Fbuiltin_lambda_argument_shadowing.rs#L23)

Derived from the **[flake8-builtins](../#flake8-builtins-a)** linter.

## [What it does](#what-it-does)

Checks for lambda arguments that use the same names as Python builtins.

## [Why is this bad?](#why-is-this-bad)

Reusing a builtin name for the name of a lambda argument increases the
difficulty of reading and maintaining the code and can cause
non-obvious errors. Readers may mistake the variable for the
builtin, and vice versa.

Builtins can be marked as exceptions to this rule via the
[`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist) configuration option.

## [Options](#options)

* [`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist)