# [wrong-tuple-length-version-comparison (PYI005)](#wrong-tuple-length-version-comparison-pyi005)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27wrong-tuple-length-version-comparison%27%20OR%20PYI005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funrecognized_version_info.rs#L112)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for Python version comparisons that compare against a tuple of the
wrong length.

## [Why is this bad?](#why-is-this-bad)

Stub files support simple conditionals to test for differences in Python
versions and platforms. When comparing against `sys.version_info`, avoid
comparing against tuples of the wrong length, which can lead to unexpected
behavior.

## [Example](#example)

```
import sys

if sys.version_info[:2] == (3,): ...
```

Use instead:

```
import sys

if sys.version_info[0] == 3: ...
```

## [References](#references)

* [Typing documentation: Version and Platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)