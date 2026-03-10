# [missing-blank-line-after-summary (D205)](#missing-blank-line-after-summary-d205)

Added in [v0.0.68](https://github.com/astral-sh/ruff/releases/tag/v0.0.68) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-blank-line-after-summary%27%20OR%20D205)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fblank_after_summary.rs#L43)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for docstring summary lines that are not separated from the docstring
description by one blank line.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that multi-line docstrings consist of "a summary line
just like a one-line docstring, followed by a blank line, followed by a
more elaborate description."

## [Example](#example)

```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.
    Sort the list in ascending order and return a copy of the
    result using the bubble sort algorithm.
    """
```

Use instead:

```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the
    result using the bubble sort algorithm.
    """
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)