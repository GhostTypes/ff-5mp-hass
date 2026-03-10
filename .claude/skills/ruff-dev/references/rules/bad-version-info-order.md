# [bad-version-info-order (PYI066)](#bad-version-info-order-pyi066)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-version-info-order%27%20OR%20PYI066)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fbad_version_info_comparison.rs#L103)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for code that branches on `sys.version_info` comparisons where
branches corresponding to older Python versions come before branches
corresponding to newer Python versions.

## [Why is this bad?](#why-is-this-bad)

As a convention, branches that correspond to newer Python versions should
come first. This makes it easier to understand the desired behavior, which
typically corresponds to the latest Python versions.

This rule enforces the convention by checking for `if` tests that compare
`sys.version_info` with `<` rather than `>=`.

By default, this rule only applies to stub files.
In [preview](https://docs.astral.sh/ruff/preview/), it will also flag this anti-pattern in non-stub files.

## [Example](#example)

```
import sys

if sys.version_info < (3, 10):
    def read_data(x, *, preserve_order=True): ...

else:
    def read_data(x): ...
```

Use instead:

```
if sys.version_info >= (3, 10):
    def read_data(x): ...

else:
    def read_data(x, *, preserve_order=True): ...
```