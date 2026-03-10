# [bad-version-info-comparison (PYI006)](#bad-version-info-comparison-pyi006)

Added in [v0.0.254](https://github.com/astral-sh/ruff/releases/tag/v0.0.254) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-version-info-comparison%27%20OR%20PYI006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fbad_version_info_comparison.rs#L53)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for uses of comparators other than `<` and `>=` for
`sys.version_info` checks. All other comparators, such
as `>`, `<=`, and `==`, are banned.

## [Why is this bad?](#why-is-this-bad)

Comparing `sys.version_info` with `==` or `<=` has unexpected behavior
and can lead to bugs.

For example, `sys.version_info > (3, 8, 1)` will resolve to `True` if your
Python version is 3.8.1; meanwhile, `sys.version_info <= (3, 8)` will *not*
resolve to `True` if your Python version is 3.8.10:

```
>>> import sys
>>> print(sys.version_info)
sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0)
>>> print(sys.version_info > (3, 8))
True
>>> print(sys.version_info == (3, 8))
False
>>> print(sys.version_info <= (3, 8))
False
>>> print(sys.version_info in (3, 8))
False
```

## [Example](#example)

```
import sys

if sys.version_info > (3, 8): ...
```

Use instead:

```
import sys

if sys.version_info >= (3, 9): ...
```