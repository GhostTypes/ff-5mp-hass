# [missing-required-import (I002)](#missing-required-import-i002)

Added in [v0.0.218](https://github.com/astral-sh/ruff/releases/tag/v0.0.218) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-required-import%27%20OR%20I002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fisort%2Frules%2Fadd_required_imports.rs#L41)

Derived from the **[isort](../#isort-i)** linter.

Fix is always available.

## [What it does](#what-it-does)

Adds any required imports, as specified by the user, to the top of the
file.

## [Why is this bad?](#why-is-this-bad)

In some projects, certain imports are required to be present in all
files. For example, some projects assume that
`from __future__ import annotations` is enabled,
and thus require that import to be
present in all files. Omitting a "required" import (as specified by
the user) can cause errors or unexpected behavior.

## [Example](#example)

```
import typing
```

Use instead:

```
from __future__ import annotations

import typing
```

## [Options](#options)

* [`lint.isort.required-imports`](../../settings/#lint_isort_required-imports)