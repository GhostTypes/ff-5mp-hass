# [f-string-docstring (B021)](#f-string-docstring-b021)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27f-string-docstring%27%20OR%20B021)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Ff_string_docstring.rs#L33)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for docstrings that are written via f-strings.

## [Why is this bad?](#why-is-this-bad)

Python will interpret the f-string as a joined string, rather than as a
docstring. As such, the "docstring" will not be accessible via the
`__doc__` attribute, nor will it be picked up by any automated
documentation tooling.

## [Example](#example)

```
def foo():
    f"""Not a docstring."""
```

Use instead:

```
def foo():
    """A docstring."""
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [Python documentation: Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)