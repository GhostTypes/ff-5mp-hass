# [signature-in-docstring (D402)](#signature-in-docstring-d402)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27signature-in-docstring%27%20OR%20D402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fno_signature.rs#L43)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for function docstrings that include the function's signature in
the summary line.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends against including a function's signature in its
docstring. Instead, consider using type annotations as a form of
documentation for the function's parameters and return value.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `google` and
`pep257` conventions, and disabled when using the `numpy` convention.

## [Example](#example)

```
def foo(a, b):
    """foo(a: int, b: int) -> list[int]"""
```

Use instead:

```
def foo(a: int, b: int) -> list[int]:
    """Return a list of a and b."""
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)