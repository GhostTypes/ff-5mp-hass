# [future-rewritable-type-annotation (FA100)](#future-rewritable-type-annotation-fa100)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27future-rewritable-type-annotation%27%20OR%20FA100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_future_annotations%2Frules%2Ffuture_rewritable_type_annotation.rs#L70)

Derived from the **[flake8-future-annotations](../#flake8-future-annotations-fa)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for missing `from __future__ import annotations` imports upon
detecting type annotations that can be written more succinctly under
PEP 563.

## [Why is this bad?](#why-is-this-bad)

PEP 585 enabled the use of a number of convenient type annotations, such as
`list[str]` instead of `List[str]`. However, these annotations are only
available on Python 3.9 and higher, *unless* the `from __future__ import annotations`
import is present.

Similarly, PEP 604 enabled the use of the `|` operator for unions, such as
`str | None` instead of `Optional[str]`. However, these annotations are only
available on Python 3.10 and higher, *unless* the `from __future__ import annotations`
import is present.

By adding the `__future__` import, the pyupgrade rules can automatically
migrate existing code to use the new syntax, even for older Python versions.
This rule thus pairs well with pyupgrade and with Ruff's pyupgrade rules.

This rule respects the [`target-version`](../../settings/#target-version) setting. For example, if your
project targets Python 3.10 and above, adding `from __future__ import annotations`
does not impact your ability to leverage PEP 604-style unions (e.g., to
convert `Optional[str]` to `str | None`). As such, this rule will only
flag such usages if your project targets Python 3.9 or below.

## [Example](#example)

```
from typing import List, Dict, Optional


def func(obj: Dict[str, Optional[int]]) -> None: ...
```

Use instead:

```
from __future__ import annotations

from typing import List, Dict, Optional


def func(obj: Dict[str, Optional[int]]) -> None: ...
```

After running the additional pyupgrade rules:

```
from __future__ import annotations


def func(obj: dict[str, int | None]) -> None: ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as adding `from __future__ import annotations`
may change the semantics of the program.

## [Options](#options)

* [`target-version`](../../settings/#target-version)