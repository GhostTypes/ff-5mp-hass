# [surrounding-whitespace (D210)](#surrounding-whitespace-d210)

Added in [v0.0.68](https://github.com/astral-sh/ruff/releases/tag/v0.0.68) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27surrounding-whitespace%27%20OR%20D210)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fno_surrounding_whitespace.rs#L34)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for surrounding whitespace in docstrings.

## [Why is this bad?](#why-is-this-bad)

Remove surrounding whitespace from the docstring, for consistency.

## [Example](#example)

```
def factorial(n: int) -> int:
    """ Return the factorial of n. """
```

Use instead:

```
def factorial(n: int) -> int:
    """Return the factorial of n."""
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)