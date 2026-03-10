# [under-indentation (D207)](#under-indentation-d207)

Added in [v0.0.75](https://github.com/astral-sh/ruff/releases/tag/v0.0.75) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27under-indentation%27%20OR%20D207)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Findent.rs#L103)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for under-indented docstrings.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that docstrings be indented to the same level as their
opening quotes. Avoid under-indenting docstrings, for consistency.

## [Example](#example)

```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.

Sort the list in ascending order and return a copy of the result using the bubble sort
algorithm.
    """
```

Use instead:

```
def sort_list(l: list[int]) -> list[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter/). The
formatter enforces consistent indentation, making the rule redundant.

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)