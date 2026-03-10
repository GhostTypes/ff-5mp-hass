# [unrecognized-platform-name (PYI008)](#unrecognized-platform-name-pyi008)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unrecognized-platform-name%27%20OR%20PYI008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funrecognized_platform.rs#L87)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Check for unrecognized platform names in `sys.platform` checks.

**Note**: this rule is only enabled in `.pyi` stub files.

## [Why is this bad?](#why-is-this-bad)

If a `sys.platform` check compares to a platform name outside of a
small set of known platforms (e.g. "linux", "win32", etc.), it's likely
a typo or a platform name that is not recognized by type checkers.

The list of known platforms is: "linux", "win32", "cygwin", "darwin".

## [Example](#example)

```
import sys

if sys.platform == "linus": ...
```

Use instead:

```
import sys

if sys.platform == "linux": ...
```

## [References](#references)

* [Typing documentation: Version and Platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)