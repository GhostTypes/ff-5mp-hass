# [self-assigning-variable (PLW0127)](#self-assigning-variable-plw0127)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27self-assigning-variable%27%20OR%20PLW0127)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fself_assigning_variable.rs#L26)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for self-assignment of variables.

## [Why is this bad?](#why-is-this-bad)

Self-assignment of variables is redundant and likely a mistake.

## [Example](#example)

```
country = "Poland"
country = country
```

Use instead:

```
country = "Poland"
```