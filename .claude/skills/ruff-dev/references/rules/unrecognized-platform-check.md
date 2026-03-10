# [unrecognized-platform-check (PYI007)](#unrecognized-platform-check-pyi007)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unrecognized-platform-check%27%20OR%20PYI007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funrecognized_platform.rs#L48)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Check for unrecognized `sys.platform` checks. Platform checks should be
simple string comparisons.

**Note**: this rule is only enabled in `.pyi` stub files.

## [Why is this bad?](#why-is-this-bad)

Some `sys.platform` checks are too complex for type checkers to
understand, and thus result in incorrect inferences by these tools.
`sys.platform` checks should be simple string comparisons, like
`if sys.platform == "linux"`.

## [Example](#example)

```
import sys

if sys.platform == "xunil"[::-1]:
    # Linux specific definitions
    ...
else:
    # Posix specific definitions
    ...
```

Instead, use a simple string comparison, such as `==` or `!=`:

```
import sys

if sys.platform == "linux":
    # Linux specific definitions
    ...
else:
    # Posix specific definitions
    ...
```

## [References](#references)

* [Typing documentation: Version and Platform checking](https://typing.python.org/en/latest/spec/directives.html#version-and-platform-checks)