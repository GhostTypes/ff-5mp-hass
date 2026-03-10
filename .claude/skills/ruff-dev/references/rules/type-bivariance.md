# [type-bivariance (PLC0131)](#type-bivariance-plc0131)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-bivariance%27%20OR%20PLC0131)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftype_bivariance.rs#L56)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `TypeVar` and `ParamSpec` definitions in which the type is
both covariant and contravariant.

## [Why is this bad?](#why-is-this-bad)

By default, Python's generic types are invariant, but can be marked as
either covariant or contravariant via the `covariant` and `contravariant`
keyword arguments. While the API does allow you to mark a type as both
covariant and contravariant, this is not supported by the type system,
and should be avoided.

Instead, change the variance of the type to be either covariant,
contravariant, or invariant. If you want to describe both covariance and
contravariance, consider using two separate type parameters.

For context: an "invariant" generic type only accepts values that exactly
match the type parameter; for example, `list[Dog]` accepts only `list[Dog]`,
not `list[Animal]` (superclass) or `list[Bulldog]` (subclass). This is
the default behavior for Python's generic types.

A "covariant" generic type accepts subclasses of the type parameter; for
example, `Sequence[Animal]` accepts `Sequence[Dog]`. A "contravariant"
generic type accepts superclasses of the type parameter; for example,
`Callable[Dog]` accepts `Callable[Animal]`.

## [Example](#example)

```
from typing import TypeVar

T = TypeVar("T", covariant=True, contravariant=True)
```

Use instead:

```
from typing import TypeVar

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)
```

## [References](#references)

* [Python documentation: `typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
* [PEP 483 – The Theory of Type Hints: Covariance and Contravariance](https://peps.python.org/pep-0483/#covariance-and-contravariance)
* [PEP 484 – Type Hints: Covariance and contravariance](https://peps.python.org/pep-0484/#covariance-and-contravariance)