# [banned-api (TID251)](#banned-api-tid251)

Added in [v0.0.201](https://github.com/astral-sh/ruff/releases/tag/v0.0.201) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27banned-api%27%20OR%20TID251)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_tidy_imports%2Frules%2Fbanned_api.rs#L27)

Derived from the **[flake8-tidy-imports](../#flake8-tidy-imports-tid)** linter.

## [What it does](#what-it-does)

Checks for banned imports.

## [Why is this bad?](#why-is-this-bad)

Projects may want to ensure that specific modules or module members are
not imported or accessed.

Security or other company policies may be a reason to impose
restrictions on importing external Python libraries. In some cases,
projects may adopt conventions around the use of certain modules or
module members that are not enforceable by the language itself.

This rule enforces certain import conventions project-wide automatically.

## [Options](#options)

* [`lint.flake8-tidy-imports.banned-api`](../../settings/#lint_flake8-tidy-imports_banned-api)