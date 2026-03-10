# [unnecessary-multiline-docstring (D200)](#unnecessary-multiline-docstring-d200)

Added in [v0.0.68](https://github.com/astral-sh/ruff/releases/tag/v0.0.68) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-multiline-docstring%27%20OR%20D200)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fone_liner.rs#L39)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for single-line docstrings that are broken across multiple lines.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends that docstrings that *can* fit on one line should be
formatted on a single line, for consistency and readability.

## [Example](#example)

```
def average(values: list[float]) -> float:
    """
    Return the mean of the given values.
    """
```

Use instead:

```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```

## [Fix safety](#fix-safety)

The fix is marked as unsafe because it could affect tools that parse docstrings,
documentation generators, or custom introspection utilities that rely on
specific docstring formatting.

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)