# [non-pep695-type-alias (UP040)](#non-pep695-type-alias-up040)

Added in [v0.0.283](https://github.com/astral-sh/ruff/releases/tag/v0.0.283) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-pep695-type-alias%27%20OR%20UP040)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fpep695%2Fnon_pep695_type_alias.rs#L86)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for use of `TypeAlias` annotations and `TypeAliasType` assignments
for declaring type aliases.

## [Why is this bad?](#why-is-this-bad)

The `type` keyword was introduced in Python 3.12 by [PEP 695](https://peps.python.org/pep-0695/) for defining
type aliases. The `type` keyword is easier to read and provides cleaner
support for generics.

## [Known problems](#known-problems)

[PEP 695](https://peps.python.org/pep-0695/) uses inferred variance for type parameters, instead of the
`covariant` and `contravariant` keywords used by `TypeVar` variables. As
such, rewriting a type alias using a PEP-695 `type` statement may change
the variance of the alias's type parameters.

Unlike type aliases that use simple assignments, definitions created using
[PEP 695](https://peps.python.org/pep-0695/) `type` statements cannot be used as drop-in replacements at
runtime for the value on the right-hand side of the statement. This means
that while for some simple old-style type aliases you can use them as the
second argument to an `isinstance()` call (for example), doing the same
with a [PEP 695](https://peps.python.org/pep-0695/) `type` statement will always raise `TypeError` at
runtime.

## [Example](#example)

```
from typing import Annotated, TypeAlias, TypeAliasType
from annotated_types import Gt

ListOfInt: TypeAlias = list[int]
PositiveInt = TypeAliasType("PositiveInt", Annotated[int, Gt(0)])
```

Use instead:

```
from typing import Annotated
from annotated_types import Gt

type ListOfInt = list[int]
type PositiveInt = Annotated[int, Gt(0)]
```

## [Fix safety](#fix-safety)

This fix is marked unsafe for `TypeAlias` assignments outside of stub files because of the
runtime behavior around `isinstance()` calls noted above. The fix is also unsafe for
`TypeAliasType` assignments if there are any comments in the replacement range that would be
deleted.

## [See also](#see-also)

This rule only applies to `TypeAlias`es and `TypeAliasType`s. See
[`non-pep695-generic-class`](https://docs.astral.sh/ruff/rules/non-pep695-generic-class/) and [`non-pep695-generic-function`](https://docs.astral.sh/ruff/rules/non-pep695-generic-function/) for similar
transformations for generic classes and functions.

This rule replaces standalone type variables in aliases but doesn't remove the corresponding
type variables even if they are unused after the fix. See [`unused-private-type-var`](https://docs.astral.sh/ruff/rules/unused-private-type-var/)
for a rule to clean up unused private type variables.

This rule will not rename private type variables to remove leading underscores, even though the
new type parameters are restricted in scope to their associated aliases. See
[`private-type-parameter`](https://docs.astral.sh/ruff/rules/private-type-parameter/) for a rule to update these names.