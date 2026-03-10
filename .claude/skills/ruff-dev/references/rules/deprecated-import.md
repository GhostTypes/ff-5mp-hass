# [deprecated-import (UP035)](#deprecated-import-up035)

Added in [v0.0.239](https://github.com/astral-sh/ruff/releases/tag/v0.0.239) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27deprecated-import%27%20OR%20UP035)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fdeprecated_import.rs#L66)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of deprecated imports based on the minimum supported
Python version.

## [Why is this bad?](#why-is-this-bad)

Deprecated imports may be removed in future versions of Python, and
should be replaced with their new equivalents.

Note that, in some cases, it may be preferable to continue importing
members from `typing_extensions` even after they're added to the Python
standard library, as `typing_extensions` can backport bugfixes and
optimizations from later Python versions. This rule thus avoids flagging
imports from `typing_extensions` in such cases.

## [Example](#example)

```
from collections import Sequence
```

Use instead:

```
from collections.abc import Sequence
```