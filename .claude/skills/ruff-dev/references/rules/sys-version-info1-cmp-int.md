# [sys-version-info1-cmp-int (YTT203)](#sys-version-info1-cmp-int-ytt203)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-version-info1-cmp-int%27%20OR%20YTT203)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fcompare.rs#L141)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for comparisons that test `sys.version_info[1]` against an integer.

## [Why is this bad?](#why-is-this-bad)

Comparisons based on the current minor version number alone can cause
subtle bugs and would likely lead to unintended effects if the Python
major version number were ever incremented (e.g., to Python 4).

Instead, compare `sys.version_info` to a tuple, including the major and
minor version numbers, to future-proof the code.

## [Example](#example)

```
import sys

if sys.version_info[1] < 7:
    print("Python 3.6 or earlier.")  # This will be printed on Python 4.0.
```

Use instead:

```
import sys

if sys.version_info < (3, 7):
    print("Python 3.6 or earlier.")
```

## [References](#references)

* [Python documentation: `sys.version`](https://docs.python.org/3/library/sys.html#sys.version)
* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)