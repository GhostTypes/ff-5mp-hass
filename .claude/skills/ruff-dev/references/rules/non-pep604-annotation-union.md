# [non-pep604-annotation-union (UP007)](#non-pep604-annotation-union-up007)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-pep604-annotation-union%27%20OR%20UP007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fuse_pep604_annotation.rs#L56)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Check for type annotations that can be rewritten based on [PEP 604](https://peps.python.org/pep-0604/) syntax.

## [Why is this bad?](#why-is-this-bad)

[PEP 604](https://peps.python.org/pep-0604/) introduced a new syntax for union type annotations based on the
`|` operator. This syntax is more concise and readable than the previous
`typing.Union` and `typing.Optional` syntaxes.

This rule is enabled when targeting Python 3.10 or later (see:
[`target-version`](../../settings/#target-version)). By default, it's *also* enabled for earlier Python
versions if `from __future__ import annotations` is present, as
`__future__` annotations are not evaluated at runtime. If your code relies
on runtime type annotations (either directly or via a library like
Pydantic), you can disable this behavior for Python versions prior to 3.10
by setting [`lint.pyupgrade.keep-runtime-typing`](../../settings/#lint_pyupgrade_keep-runtime-typing) to `true`.

## [Example](#example)

```
from typing import Union

foo: Union[int, str] = 1
```

Use instead:

```
foo: int | str = 1
```

Note that this rule only checks for usages of `typing.Union`,
while `UP045` checks for `typing.Optional`.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may lead to runtime errors when
alongside libraries that rely on runtime type annotations, like Pydantic,
on Python versions prior to Python 3.10. It may also lead to runtime errors
in unusual and likely incorrect type annotations where the type does not
support the `|` operator.

## [Options](#options)

* [`target-version`](../../settings/#target-version)
* [`lint.pyupgrade.keep-runtime-typing`](../../settings/#lint_pyupgrade_keep-runtime-typing)