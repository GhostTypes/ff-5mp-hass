# [new-line-after-last-paragraph (D209)](#new-line-after-last-paragraph-d209)

Added in [v0.0.68](https://github.com/astral-sh/ruff/releases/tag/v0.0.68) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27new-line-after-last-paragraph%27%20OR%20D209)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnewline_after_last_paragraph.rs#L46)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for multi-line docstrings whose closing quotes are not on their
own line.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that the closing quotes of a multi-line docstring be
on their own line, for consistency and compatibility with documentation
tools that may need to parse the docstring.

## [Example](#example)

```
def sort_list(l: List[int]) -> List[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm."""
```

Use instead:

```
def sort_list(l: List[int]) -> List[int]:
    """Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the bubble
    sort algorithm.
    """
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)