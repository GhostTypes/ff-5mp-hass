# [non-pep695-generic-class (UP046)](#non-pep695-generic-class-up046)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-pep695-generic-class%27%20OR%20UP046)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fpep695%2Fnon_pep695_generic_class.rs#L88)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for use of standalone type variables and parameter specifications in generic classes.

## [Why is this bad?](#why-is-this-bad)

Special type parameter syntax was introduced in Python 3.12 by [PEP 695](https://peps.python.org/pep-0695/) for defining generic
classes. This syntax is easier to read and provides cleaner support for generics.

## [Known problems](#known-problems)

The rule currently skips generic classes nested inside of other functions or classes. It also
skips type parameters with the `default` argument introduced in [PEP 696](https://peps.python.org/pep-0696/) and implemented in
Python 3.13.

This rule can only offer a fix if all of the generic types in the class definition are defined
in the current module. For external type parameters, a diagnostic is emitted without a suggested
fix.

Not all type checkers fully support PEP 695 yet, so even valid fixes suggested by this rule may
cause type checking to [fail](https://github.com/python/mypy/issues/18507).

## [Fix safety](#fix-safety)

This fix is marked as unsafe, as [PEP 695](https://peps.python.org/pep-0695/) uses inferred variance for type parameters, instead
of the `covariant` and `contravariant` keywords used by `TypeVar` variables. As such, replacing
a `TypeVar` variable with an inline type parameter may change its variance.

## [Example](#example)

```
from typing import Generic, TypeVar

T = TypeVar("T")


class GenericClass(Generic[T]):
    var: T
```

Use instead:

```
class GenericClass[T]:
    var: T
```

## [See also](#see-also)

This rule replaces standalone type variables in classes but doesn't remove
the corresponding type variables even if they are unused after the fix. See
[`unused-private-type-var`](https://docs.astral.sh/ruff/rules/unused-private-type-var/) for a rule to clean up unused
private type variables.

This rule will not rename private type variables to remove leading underscores, even though the
new type parameters are restricted in scope to their associated class. See
[`private-type-parameter`](https://docs.astral.sh/ruff/rules/private-type-parameter/) for a rule to update these names.

This rule will correctly handle classes with multiple base classes, as long as the single
`Generic` base class is at the end of the argument list, as checked by
[`generic-not-last-base-class`](https://docs.astral.sh/ruff/rules/generic-not-last-base-class/). If a `Generic` base class is
found outside of the last position, a diagnostic is emitted without a suggested fix.

This rule only applies to generic classes and does not include generic functions. See
[`non-pep695-generic-function`](https://docs.astral.sh/ruff/rules/non-pep695-generic-function/) for the function version.