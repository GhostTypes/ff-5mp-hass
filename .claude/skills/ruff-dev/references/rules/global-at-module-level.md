# [global-at-module-level (PLW0604)](#global-at-module-level-plw0604)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27global-at-module-level%27%20OR%20PLW0604)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fglobal_at_module_level.rs#L17)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of the `global` keyword at the module level.

## [Why is this bad?](#why-is-this-bad)

The `global` keyword is used within functions to indicate that a name
refers to a global variable, rather than a local variable.

At the module level, all names are global by default, so the `global`
keyword is redundant.