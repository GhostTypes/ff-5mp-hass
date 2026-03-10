# [type-name-incorrect-variance (PLC0105)](#type-name-incorrect-variance-plc0105)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-name-incorrect-variance%27%20OR%20PLC0105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftype_name_incorrect_variance.rs#L45)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for type names that do not match the variance of their associated
type parameter.

## [Why is this bad?](#why-is-this-bad)

[PEP 484](https://peps.python.org/pep-0484/) recommends the use of the `_co` and `_contra` suffixes for
covariant and contravariant type parameters, respectively (while invariant
type parameters should not have any such suffix).

## [Example](#example)

```
from typing import TypeVar

T = TypeVar("T", covariant=True)
U = TypeVar("U", contravariant=True)
V_co = TypeVar("V_co")
```

Use instead:

```
from typing import TypeVar

T_co = TypeVar("T_co", covariant=True)
U_contra = TypeVar("U_contra", contravariant=True)
V = TypeVar("V")
```

## [References](#references)

* [Python documentation: `typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
* [PEP 483 – The Theory of Type Hints: Covariance and Contravariance](https://peps.python.org/pep-0483/#covariance-and-contravariance)
* [PEP 484 – Type Hints: Covariance and contravariance](https://peps.python.org/pep-0484/#covariance-and-contravariance)