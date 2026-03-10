# [unassigned-special-variable-in-stub (PYI035)](#unassigned-special-variable-in-stub-pyi035)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unassigned-special-variable-in-stub%27%20OR%20PYI035)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fsimple_defaults.rs#L188)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks that `__all__`, `__match_args__`, and `__slots__` variables are
assigned to values when defined in stub files.

## [Why is this bad?](#why-is-this-bad)

Special variables like `__all__` have the same semantics in stub files
as they do in Python modules, and so should be consistent with their
runtime counterparts.

## [Example](#example)

```
__all__: list[str]
```

Use instead:

```
__all__: list[str] = ["foo", "bar"]
```