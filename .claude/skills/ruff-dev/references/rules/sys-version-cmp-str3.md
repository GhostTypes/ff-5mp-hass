# [sys-version-cmp-str3 (YTT103)](#sys-version-cmp-str3-ytt103)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sys-version-cmp-str3%27%20OR%20YTT103)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fcompare.rs#L43)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for comparisons that test `sys.version` against string literals,
such that the comparison will evaluate to `False` on Python 3.10 or later.

## [Why is this bad?](#why-is-this-bad)

Comparing `sys.version` to a string is error-prone and may cause subtle
bugs, as the comparison will be performed lexicographically, not
semantically. For example, `sys.version > "3.9"` will evaluate to `False`
when using Python 3.10, as `"3.10"` is lexicographically "less" than
`"3.9"`.

Instead, use `sys.version_info` to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.

## [Example](#example)

```
import sys

sys.version > "3.9"  # `False` on Python 3.10.
```

Use instead:

```
import sys

sys.version_info > (3, 9)  # `True` on Python 3.10.
```

## [References](#references)

* [Python documentation: `sys.version`](https://docs.python.org/3/library/sys.html#sys.version)
* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)