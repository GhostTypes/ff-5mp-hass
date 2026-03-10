# [implicit-optional (RUF013)](#implicit-optional-ruf013)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-optional%27%20OR%20RUF013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fimplicit_optional.rs#L86)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the use of implicit `Optional` in type annotations when the
default parameter value is `None`.

If [`lint.future-annotations`](../../settings/#lint_future-annotations) is set to `true`, `from __future__ import annotations` will be added if doing so would allow using the `|` operator on
a Python version before 3.10.

## [Why is this bad?](#why-is-this-bad)

Implicit `Optional` is prohibited by [PEP 484](https://peps.python.org/pep-0484/#union-types). It is confusing and
inconsistent with the rest of the type system.

It's recommended to use `Optional[T]` instead. For Python 3.10 and later,
you can also use `T | None`.

## [Example](#example)

```
def foo(arg: int = None):
    pass
```

Use instead:

```
from typing import Optional


def foo(arg: Optional[int] = None):
    pass
```

Or, for Python 3.10 and later:

```
def foo(arg: int | None = None):
    pass
```

If you want to use the `|` operator in Python 3.9 and earlier, you can
use future imports:

```
from __future__ import annotations


def foo(arg: int | None = None):
    pass
```

## [Limitations](#limitations)

Type aliases are not supported and could result in false negatives.
For example, the following code will not be flagged:

```
Text = str | bytes


def foo(arg: Text = None):
    pass
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)
* [`lint.future-annotations`](../../settings/#lint_future-annotations)

## [Fix safety](#fix-safety)

This fix is always marked as unsafe because it can change the behavior of code that relies on
type hints, and it assumes the default value is always appropriate—which might not be the case.