# [unrecognized-version-info-check (PYI003)](#unrecognized-version-info-check-pyi003)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unrecognized-version-info-check%27%20OR%20PYI003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funrecognized_version_info.rs#L35)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for problematic `sys.version_info`-related conditions in stubs.

## [Why is this bad?](#why-is-this-bad)

Stub files support simple conditionals to test for differences in Python
versions using `sys.version_info`. However, there are a number of common
mistakes involving `sys.version_info` comparisons that should be avoided.
For example, comparing against a string can lead to unexpected behavior.

## [Example](#example)

```
import sys

if sys.version_info[0] == "2": ...
```

Use instead:

```
import sys

if sys.version_info[0] == 2: ...
```

## [References](#references)

* [Typing documentation: Version and Platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)