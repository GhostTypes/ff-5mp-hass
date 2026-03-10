# [sys-version-slice1 (YTT303)](#sys-version-slice1-ytt303)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-version-slice1%27%20OR%20YTT303)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fsubscript.rs#L163)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for uses of `sys.version[:1]`.

## [Why is this bad?](#why-is-this-bad)

If the major version number consists of more than one digit, this will
select the first digit of the major version number only (e.g., `"10.0"`
would evaluate to `"1"`). This is likely unintended, and can lead to subtle
bugs in future versions of Python if the version string is used to test
against a specific major version number.

Instead, use `sys.version_info.major` to access the current major version
number.

## [Example](#example)

```
import sys

sys.version[:1]  # If using Python 10, this evaluates to "1".
```

Use instead:

```
import sys

f"{sys.version_info.major}"  # If using Python 10, this evaluates to "10".
```

## [References](#references)

* [Python documentation: `sys.version`](https://docs.python.org/3/library/sys.html#sys.version)
* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)