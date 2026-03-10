# [blank-line-before-function (D201)](#blank-line-before-function-d201)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blank-line-before-function%27%20OR%20D201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fblank_before_after_function.rs#L40)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for docstrings on functions that are separated by one or more blank
lines from the function definition.

## [Why is this bad?](#why-is-this-bad)

Remove any blank lines between the function definition and its docstring,
for consistency.

## [Example](#example)

```
def average(values: list[float]) -> float:

    """Return the mean of the given values."""
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