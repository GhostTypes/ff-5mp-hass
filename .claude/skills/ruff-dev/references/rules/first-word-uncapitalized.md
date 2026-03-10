# [first-word-uncapitalized (D403)](#first-word-uncapitalized-d403)

Added in [v0.0.69](https://github.com/astral-sh/ruff/releases/tag/v0.0.69) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27first-word-uncapitalized%27%20OR%20D403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fcapitalized.rs#L32)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for docstrings that do not start with a capital letter.

## [Why is this bad?](#why-is-this-bad)

The first non-whitespace character in a docstring should be
capitalized for grammatical correctness and consistency.

## [Example](#example)

```
def average(values: list[float]) -> float:
    """return the mean of the given values."""
```

Use instead:

```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)