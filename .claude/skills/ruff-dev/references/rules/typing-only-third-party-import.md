# [typing-only-third-party-import (TC002)](#typing-only-third-party-import-tc002)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27typing-only-third-party-import%27%20OR%20TC002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Ftyping_only_runtime_import.rs#L166)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for third-party imports that are only used for type annotations, but
aren't defined in a type-checking block.

## [Why is this bad?](#why-is-this-bad)

Unused imports add a performance overhead at runtime, and risk creating
import cycles. If an import is *only* used in typing-only contexts, it can
instead be imported conditionally under an `if TYPE_CHECKING:` block to
minimize runtime overhead.

If [`lint.flake8-type-checking.quote-annotations`](../../settings/#lint_flake8-type-checking_quote-annotations) is set to `true`,
annotations will be wrapped in quotes if doing so would enable the
corresponding import to be moved into an `if TYPE_CHECKING:` block.

If a class *requires* that type annotations be available at runtime (as is
the case for Pydantic, SQLAlchemy, and other libraries), consider using
the [`lint.flake8-type-checking.runtime-evaluated-base-classes`](../../settings/#lint_flake8-type-checking_runtime-evaluated-base-classes) and
[`lint.flake8-type-checking.runtime-evaluated-decorators`](../../settings/#lint_flake8-type-checking_runtime-evaluated-decorators) settings to mark them
as such.

If [`lint.future-annotations`](../../settings/#lint_future-annotations) is set to `true`, `from __future__ import annotations` will be added if doing so would enable an import to be
moved into an `if TYPE_CHECKING:` block. This takes precedence over the
[`lint.flake8-type-checking.quote-annotations`](../../settings/#lint_flake8-type-checking_quote-annotations) setting described above if
both settings are enabled.

## [Example](#example)

```
from __future__ import annotations

import pandas as pd


def func(df: pd.DataFrame) -> int:
    return len(df)
```

Use instead:

```
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd


def func(df: pd.DataFrame) -> int:
    return len(df)
```

## [Options](#options)

* [`lint.flake8-type-checking.quote-annotations`](../../settings/#lint_flake8-type-checking_quote-annotations)
* [`lint.flake8-type-checking.runtime-evaluated-base-classes`](../../settings/#lint_flake8-type-checking_runtime-evaluated-base-classes)
* [`lint.flake8-type-checking.runtime-evaluated-decorators`](../../settings/#lint_flake8-type-checking_runtime-evaluated-decorators)
* [`lint.flake8-type-checking.strict`](../../settings/#lint_flake8-type-checking_strict)
* [`lint.typing-modules`](../../settings/#lint_typing-modules)
* [`lint.future-annotations`](../../settings/#lint_future-annotations)

## [References](#references)

* [PEP 563: Runtime annotation resolution and `TYPE_CHECKING`](https://peps.python.org/pep-0563/#runtime-annotation-resolution-and-type-checking)