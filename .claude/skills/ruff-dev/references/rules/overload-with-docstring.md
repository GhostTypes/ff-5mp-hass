# [overload-with-docstring (D418)](#overload-with-docstring-d418)

Added in [v0.0.71](https://github.com/astral-sh/ruff/releases/tag/v0.0.71) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27overload-with-docstring%27%20OR%20D418)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fif_needed.rs#L69)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for `@overload` function definitions that contain a docstring.

## [Why is this bad?](#why-is-this-bad)

The `@overload` decorator is used to define multiple compatible signatures
for a given function, to support type-checking. A series of `@overload`
definitions should be followed by a single non-decorated definition that
contains the implementation of the function.

`@overload` function definitions should not contain a docstring; instead,
the docstring should be placed on the non-decorated definition that contains
the implementation.

## [Example](#example)

```
from typing import overload


@overload
def factorial(n: int) -> int:
    """Return the factorial of n."""


@overload
def factorial(n: float) -> float:
    """Return the factorial of n."""


def factorial(n):
    """Return the factorial of n."""


factorial.__doc__  # "Return the factorial of n."
```

Use instead:

```
from typing import overload


@overload
def factorial(n: int) -> int: ...


@overload
def factorial(n: float) -> float: ...


def factorial(n):
    """Return the factorial of n."""


factorial.__doc__  # "Return the factorial of n."
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [Python documentation: `typing.overload`](https://docs.python.org/3/library/typing.html#typing.overload)