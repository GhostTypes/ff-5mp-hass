# [non-pep646-unpack (UP044)](#non-pep646-unpack-up044)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-pep646-unpack%27%20OR%20UP044)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fnon_pep646_unpack.rs#L38)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `Unpack[]` on Python 3.11 and above, and suggests
using `*` instead.

## [Why is this bad?](#why-is-this-bad)

[PEP 646](https://peps.python.org/pep-0646/) introduced a new syntax for unpacking sequences based on the `*`
operator. This syntax is more concise and readable than the previous
`Unpack[]` syntax.

## [Example](#example)

```
from typing import Unpack


def foo(*args: Unpack[tuple[int, ...]]) -> None:
    pass
```

Use instead:

```
def foo(*args: *tuple[int, ...]) -> None:
    pass
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as `Unpack[T]` and `*T` are considered
different values when introspecting types at runtime. However, in most cases,
the fix should be safe to apply.