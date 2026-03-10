# [multi-line-summary-first-line (D212)](#multi-line-summary-first-line-d212)

Added in [v0.0.69](https://github.com/astral-sh/ruff/releases/tag/v0.0.69) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multi-line-summary-first-line%27%20OR%20D212)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fmulti_line_summary_start.rs#L63)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for docstring summary lines that are not positioned on the first
physical line of the docstring.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257) recommends that multi-line docstrings consist of "a summary line
just like a one-line docstring, followed by a blank line, followed by a
more elaborate description."

The summary line should be located on the first physical line of the
docstring, immediately after the opening quotes.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `google`
convention, and disabled when using the `numpy` and `pep257` conventions.

For an alternative, see [D213](https://docs.astral.sh/ruff/rules/multi-line-summary-second-line).

## [Example](#example)

```
def sort_list(l: list[int]) -> list[int]:
    """
    Return a sorted copy of the list.

    Sort the list in ascending order and return a copy of the result using the
    bubble sort algorithm.
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

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)