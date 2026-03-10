# [sys-version-cmp-str10 (YTT302)](#sys-version-cmp-str10-ytt302)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-version-cmp-str10%27%20OR%20YTT302)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fcompare.rs#L228)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for comparisons that test `sys.version` against string literals,
such that the comparison would fail if the major version number were
ever incremented to Python 10 or higher.

## [Why is this bad?](#why-is-this-bad)

Comparing `sys.version` to a string is error-prone and may cause subtle
bugs, as the comparison will be performed lexicographically, not
semantically.

Instead, use `sys.version_info` to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.

## [Example](#example)

```
import sys

sys.version >= "3"  # `False` on Python 10.
```

Use instead:

```
import sys

sys.version_info >= (3,)  # `True` on Python 10.
```

## [References](#references)

* [Python documentation: `sys.version`](https://docs.python.org/3/library/sys.html#sys.version)
* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)