# [future-required-type-annotation (FA102)](#future-required-type-annotation-fa102)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27future-required-type-annotation%27%20OR%20FA102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_future_annotations%2Frules%2Ffuture_required_type_annotation.rs#L51)

Derived from the **[flake8-future-annotations](../#flake8-future-annotations-fa)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of PEP 585- and PEP 604-style type annotations in Python
modules that lack the required `from __future__ import annotations` import
for compatibility with older Python versions.

## [Why is this bad?](#why-is-this-bad)

Using PEP 585 and PEP 604 style annotations without a `from __future__ import annotations` import will cause runtime errors on Python versions prior to
3.9 and 3.10, respectively.

By adding the `__future__` import, the interpreter will no longer interpret
annotations at evaluation time, making the code compatible with both past
and future Python versions.

This rule respects the [`target-version`](../../settings/#target-version) setting. For example, if your
project targets Python 3.10 and above, adding `from __future__ import annotations`
does not impact your ability to leverage PEP 604-style unions (e.g., to
convert `Optional[str]` to `str | None`). As such, this rule will only
flag such usages if your project targets Python 3.9 or below.

## [Example](#example)

```
def func(obj: dict[str, int | None]) -> None: ...
```

Use instead:

```
from __future__ import annotations


def func(obj: dict[str, int | None]) -> None: ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as adding `from __future__ import annotations`
may change the semantics of the program.

## [Options](#options)

* [`target-version`](../../settings/#target-version)