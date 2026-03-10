# [banned-import-from (ICN003)](#banned-import-from-icn003)

Added in [v0.0.263](https://github.com/astral-sh/ruff/releases/tag/v0.0.263) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27banned-import-from%27%20OR%20ICN003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_import_conventions%2Frules%2Fbanned_import_from.rs#L35)

Derived from the **[flake8-import-conventions](../#flake8-import-conventions-icn)** linter.

## [What it does](#what-it-does)

Checks for member imports that should instead be accessed by importing the
module.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.

For example, it's common to import `pandas` as `pd`, and then access
members like `Series` via `pd.Series`, rather than importing `Series`
directly.

## [Example](#example)

```
from pandas import Series
```

Use instead:

```
import pandas as pd

pd.Series
```

## [Options](#options)

* [`lint.flake8-import-conventions.banned-from`](../../settings/#lint_flake8-import-conventions_banned-from)