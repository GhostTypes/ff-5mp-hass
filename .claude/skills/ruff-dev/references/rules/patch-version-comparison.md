# [patch-version-comparison (PYI004)](#patch-version-comparison-pyi004)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27patch-version-comparison%27%20OR%20PYI004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funrecognized_version_info.rs#L75)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for Python version comparisons in stubs that compare against patch
versions (e.g., Python 3.8.3) instead of major and minor versions (e.g.,
Python 3.8).

## [Why is this bad?](#why-is-this-bad)

Stub files support simple conditionals to test for differences in Python
versions and platforms. However, type checkers only understand a limited
subset of these conditionals. In particular, type checkers don't support
patch versions (e.g., Python 3.8.3), only major and minor versions (e.g.,
Python 3.8). Therefore, version checks in stubs should only use the major
and minor versions.

## [Example](#example)

```
import sys

if sys.version_info >= (3, 4, 3): ...
```

Use instead:

```
import sys

if sys.version_info >= (3, 4): ...
```

## [References](#references)

* [Typing documentation: Version and Platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)