# [missing-terminal-punctuation (D415)](#missing-terminal-punctuation-d415)

Added in [v0.0.69](https://github.com/astral-sh/ruff/releases/tag/v0.0.69) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-terminal-punctuation%27%20OR%20D415)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fends_with_punctuation.rs#L46)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for docstrings in which the first line does not end in a punctuation
mark, such as a period, question mark, or exclamation point.

## [Why is this bad?](#why-is-this-bad)

The first line of a docstring should end with a period, question mark, or
exclamation point, for grammatical correctness and consistency.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `google`
convention, and disabled when using the `numpy` and `pep257` conventions.

## [Example](#example)

```
def average(values: list[float]) -> float:
    """Return the mean of the given values"""
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
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)