# [runtime-cast-value (TC006)](#runtime-cast-value-tc006)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27runtime-cast-value%27%20OR%20TC006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Fruntime_cast_value.rs#L45)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unquoted type expressions in `typing.cast()` calls.

## [Why is this bad?](#why-is-this-bad)

This rule helps enforce a consistent style across your codebase.

It's often necessary to quote the first argument passed to `cast()`,
as type expressions can involve forward references, or references
to symbols which are only imported in `typing.TYPE_CHECKING` blocks.
This can lead to a visual inconsistency across different `cast()` calls,
where some type expressions are quoted but others are not. By enabling
this rule, you ensure that all type expressions passed to `cast()` are
quoted, enforcing stylistic consistency across all of your `cast()` calls.

In some cases where `cast()` is used in a hot loop, this rule may also
help avoid overhead from repeatedly evaluating complex type expressions at
runtime.

## [Example](#example)

```
from typing import cast

x = cast(dict[str, int], foo)
```

Use instead:

```
from typing import cast

x = cast("dict[str, int]", foo)
```

## [Fix safety](#fix-safety)

This fix is safe as long as the type expression doesn't span multiple
lines and includes comments on any of the lines apart from the last one.