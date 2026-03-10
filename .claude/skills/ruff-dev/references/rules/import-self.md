# [import-self (PLW0406)](#import-self-plw0406)

Added in [v0.0.265](https://github.com/astral-sh/ruff/releases/tag/v0.0.265) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27import-self%27%20OR%20PLW0406)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fimport_self.rs#L25)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for import statements that import the current module.

## [Why is this bad?](#why-is-this-bad)

Importing a module from itself is a circular dependency and results
in an `ImportError` exception.

## [Example](#example)

```
# file: this_file.py
from this_file import foo


def foo(): ...
```