# [redeclared-assigned-name (PLW0128)](#redeclared-assigned-name-plw0128)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redeclared-assigned-name%27%20OR%20PLW0128)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fredeclared_assigned_name.rs#L30)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for declared assignments to the same variable multiple times
in the same assignment.

## [Why is this bad?](#why-is-this-bad)

Assigning a variable multiple times in the same assignment is redundant,
as the final assignment to the variable is what the value will be.

## [Example](#example)

```
a, b, a = (1, 2, 3)
print(a)  # 3
```

Use instead:

```
# this is assuming you want to assign 3 to `a`
_, b, a = (1, 2, 3)
print(a)  # 3
```