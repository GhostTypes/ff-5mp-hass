# [type-param-name-mismatch (PLC0132)](#type-param-name-mismatch-plc0132)

Added in [v0.0.277](https://github.com/astral-sh/ruff/releases/tag/v0.0.277) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-param-name-mismatch%27%20OR%20PLC0132)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftype_param_name_mismatch.rs#L41)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `TypeVar`, `TypeVarTuple`, `ParamSpec`, and `NewType`
definitions in which the name of the type parameter does not match the name
of the variable to which it is assigned.

## [Why is this bad?](#why-is-this-bad)

When defining a `TypeVar` or a related type parameter, Python allows you to
provide a name for the type parameter. According to [PEP 484](https://peps.python.org/pep-0484/#generics), the name
provided to the `TypeVar` constructor must be equal to the name of the
variable to which it is assigned.

## [Example](#example)

```
from typing import TypeVar

T = TypeVar("U")
```

Use instead:

```
from typing import TypeVar

T = TypeVar("T")
```

## [References](#references)

* [Python documentation: `typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
* [PEP 484 – Type Hints: Generics](https://peps.python.org/pep-0484/#generics)