# [escape-sequence-in-docstring (D301)](#escape-sequence-in-docstring-d301)

Added in [v0.0.172](https://github.com/astral-sh/ruff/releases/tag/v0.0.172) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27escape-sequence-in-docstring%27%20OR%20D301)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fbackslashes.rs#L44)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for docstrings that include backslashes, but are not defined as
raw string literals.

## [Why is this bad?](#why-is-this-bad)

In Python, backslashes are typically used to escape characters in strings.
In raw strings (those prefixed with an `r`), however, backslashes are
treated as literal characters.

[PEP 257](https://peps.python.org/pep-0257/#what-is-a-docstring) recommends
the use of raw strings (i.e., `r"""raw triple double quotes"""`) for
docstrings that include backslashes. The use of a raw string ensures that
any backslashes are treated as literal characters, and not as escape
sequences, which avoids confusion.

## [Example](#example)

```
def foobar():
    """Docstring for foo\bar."""


foobar.__doc__  # "Docstring for foar."
```

Use instead:

```
def foobar():
    r"""Docstring for foo\bar."""


foobar.__doc__  # "Docstring for foo\bar."
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [Python documentation: String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)