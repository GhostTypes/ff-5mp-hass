# [docstring-starts-with-this (D404)](#docstring-starts-with-this-d404)

Added in [v0.0.71](https://github.com/astral-sh/ruff/releases/tag/v0.0.71) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-starts-with-this%27%20OR%20D404)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fstarts_with_this.rs#L42)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for docstrings that start with `This`.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that the first line of a docstring be written in the
imperative mood, for consistency.

Hint: to rewrite the docstring in the imperative, phrase the first line as
if it were a command.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `numpy`
convention,, and disabled when using the `google` and `pep257` conventions.

## [Example](#example)

```
def average(values: list[float]) -> float:
    """This function returns the mean of the given values."""
```

Use instead:

```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)