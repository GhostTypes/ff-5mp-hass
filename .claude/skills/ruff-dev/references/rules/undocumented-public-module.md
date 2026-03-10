# [undocumented-public-module (D100)](#undocumented-public-module-d100)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-public-module%27%20OR%20D100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnot_missing.rs#L63)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for undocumented public module definitions.

## [Why is this bad?](#why-is-this-bad)

Public modules should be documented via docstrings to outline their purpose
and contents.

Generally, module docstrings should describe the purpose of the module and
list the classes, exceptions, functions, and other objects that are exported
by the module, alongside a one-line summary of each.

If the module is a script, the docstring should be usable as its "usage"
message.

If the codebase adheres to a standard format for module docstrings, follow
that format for consistency.

## [Example](#example)

```
class FasterThanLightError(ZeroDivisionError): ...


def calculate_speed(distance: float, time: float) -> float: ...
```

Use instead:

```
"""Utility functions and classes for calculating speed.

This module provides:
- FasterThanLightError: exception when FTL speed is calculated;
- calculate_speed: calculate speed given distance and time.
"""


class FasterThanLightError(ZeroDivisionError): ...


def calculate_speed(distance: float, time: float) -> float: ...
```

## [Notebook behavior](#notebook-behavior)

This rule is ignored for Jupyter Notebooks.

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)