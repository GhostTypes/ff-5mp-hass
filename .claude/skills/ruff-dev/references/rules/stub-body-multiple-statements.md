# [stub-body-multiple-statements (PYI048)](#stub-body-multiple-statements-pyi048)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27stub-body-multiple-statements%27%20OR%20PYI048)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fstub_body_multiple_statements.rs#L31)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for functions in stub (`.pyi`) files that contain multiple
statements.

## [Why is this bad?](#why-is-this-bad)

Stub files are never executed, and are only intended to define type hints.
As such, functions in stub files should not contain functional code, and
should instead contain only a single statement (e.g., `...`).

## [Example](#example)

```
def function():
    x = 1
    y = 2
    return x + y
```

Use instead:

```
def function(): ...
```