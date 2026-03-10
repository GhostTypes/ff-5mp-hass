# [class-with-mixed-type-vars (RUF053)](#class-with-mixed-type-vars-ruf053)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27class-with-mixed-type-vars%27%20OR%20RUF053)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fclass_with_mixed_type_vars.rs#L64)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for classes that have [PEP 695](https://docs.python.org/3/reference/compound_stmts.html#type-params)
while also inheriting from `typing.Generic` or `typing_extensions.Generic`.

## [Why is this bad?](#why-is-this-bad)

Such classes cause errors at runtime:

```
from typing import Generic, TypeVar

U = TypeVar("U")

# TypeError: Cannot inherit from Generic[...] multiple times.
class C[T](Generic[U]): ...
```

## [Example](#example)

```
from typing import Generic, ParamSpec, TypeVar, TypeVarTuple

U = TypeVar("U")
P = ParamSpec("P")
Ts = TypeVarTuple("Ts")


class C[T](Generic[U, P, *Ts]): ...
```

Use instead:

```
class C[T, U, **P, *Ts]: ...
```

## [Fix safety](#fix-safety)

As the fix changes runtime behaviour, it is always marked as unsafe.
Additionally, comments within the fix range will not be preserved.

## [References](#references)

* [Python documentation: User-defined generic types](https://docs.python.org/3/library/typing.html#user-defined-generic-types)
* [Python documentation: type parameter lists](https://docs.python.org/3/reference/compound_stmts.html#type-params)
* [PEP 695 - Type Parameter Syntax](https://peps.python.org/pep-0695/)