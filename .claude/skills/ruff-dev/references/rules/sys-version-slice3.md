# [sys-version-slice3 (YTT101)](#sys-version-slice3-ytt101)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-version-slice3%27%20OR%20YTT101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fsubscript.rs#L40)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for uses of `sys.version[:3]`.

## [Why is this bad?](#why-is-this-bad)

If the current major or minor version consists of multiple digits,
`sys.version[:3]` will truncate the version number (e.g., `"3.10"` would
become `"3.1"`). This is likely unintended, and can lead to subtle bugs if
the version string is used to test against a specific Python version.

Instead, use `sys.version_info` to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.

## [Example](#example)

```
import sys

sys.version[:3]  # Evaluates to "3.1" on Python 3.10.
```

Use instead:

```
import sys

sys.version_info[:2]  # Evaluates to (3, 10) on Python 3.10.
```

## [References](#references)

* [Python documentation: `sys.version`](https://docs.python.org/3/library/sys.html#sys.version)
* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)