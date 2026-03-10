# [non-imperative-mood (D401)](#non-imperative-mood-d401)

Added in [v0.0.228](https://github.com/astral-sh/ruff/releases/tag/v0.0.228) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-imperative-mood%27%20OR%20D401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnon_imperative_mood.rs#L53)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for docstring first lines that are not in an imperative mood.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that the first line of a docstring be written in the
imperative mood, for consistency.

Hint: to rewrite the docstring in the imperative, phrase the first line as
if it were a command.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `numpy` and
`pep257` conventions, and disabled when using the `google` conventions.

## [Example](#example)

```
def average(values: list[float]) -> float:
    """Returns the mean of the given values."""
```

Use instead:

```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)
* [`lint.pydocstyle.property-decorators`](../../settings/#lint_pydocstyle_property-decorators)
* [`lint.pydocstyle.ignore-decorators`](../../settings/#lint_pydocstyle_ignore-decorators)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)