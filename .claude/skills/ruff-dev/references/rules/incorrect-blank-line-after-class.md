# [incorrect-blank-line-after-class (D204)](#incorrect-blank-line-after-class-d204)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27incorrect-blank-line-after-class%27%20OR%20D204)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fblank_before_after_class.rs#L98)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for class methods that are not separated from the class's docstring
by a blank line.

## [Why is this bad?](#why-is-this-bad)

[PEP 257](https://peps.python.org/pep-0257/) recommends the use of a blank line to separate a class's
docstring from its methods.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the `numpy` and `pep257`
conventions, and disabled when using the `google` convention.

## [Example](#example)

```
class PhotoMetadata:
    """Metadata about a photo."""
    def __init__(self, file: Path):
        ...
```

Use instead:

```
class PhotoMetadata:
    """Metadata about a photo."""

    def __init__(self, file: Path):
        ...
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)