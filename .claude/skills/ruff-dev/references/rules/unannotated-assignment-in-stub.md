# [unannotated-assignment-in-stub (PYI052)](#unannotated-assignment-in-stub-pyi052)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unannotated-assignment-in-stub%27%20OR%20PYI052)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fsimple_defaults.rs#L156)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for unannotated assignments in stub (`.pyi`) files.

## [Why is this bad?](#why-is-this-bad)

Stub files exist to provide type hints, and are never executed. As such,
all assignments in stub files should be annotated with a type.