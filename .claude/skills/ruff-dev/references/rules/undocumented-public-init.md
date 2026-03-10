# [undocumented-public-init (D107)](#undocumented-public-init-d107)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-public-init%27%20OR%20D107)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnot_missing.rs#L537)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for public `__init__` method definitions that are missing
docstrings.

## [Why is this bad?](#why-is-this-bad)

Public `__init__` methods are used to initialize objects. `__init__`
methods should be documented via docstrings to describe the method's
behavior, arguments, side effects, exceptions, and any other information
that may be relevant to the user.

If the codebase adheres to a standard format for `__init__` method docstrings,
follow that format for consistency.

## [Example](#example)

```
class City:
    def __init__(self, name: str, population: int) -> None:
        self.name: str = name
        self.population: int = population
```

Use instead:

```
class City:
    def __init__(self, name: str, population: int) -> None:
        """Initialize a city with a name and population."""
        self.name: str = name
        self.population: int = population
```

## [Options](#options)

* [`lint.pydocstyle.ignore-decorators`](../../settings/#lint_pydocstyle_ignore-decorators)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)