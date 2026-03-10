# [unused-loop-control-variable (B007)](#unused-loop-control-variable-b007)

Added in [v0.0.84](https://github.com/astral-sh/ruff/releases/tag/v0.0.84) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-loop-control-variable%27%20OR%20B007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Funused_loop_control_variable.rs#L37)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unused variables in loops (e.g., `for` and `while` statements).

## [Why is this bad?](#why-is-this-bad)

Defining a variable in a loop statement that is never used can confuse
readers.

If the variable is intended to be unused (e.g., to facilitate
destructuring of a tuple or other object), prefix it with an underscore
to indicate the intent. Otherwise, remove the variable entirely.

## [Example](#example)

```
for i, j in foo:
    bar(i)
```

Use instead:

```
for i, _j in foo:
    bar(i)
```

## [References](#references)

* [PEP 8: Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)