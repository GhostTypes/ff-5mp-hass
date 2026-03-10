# [outdated-version-block (UP036)](#outdated-version-block-up036)

Added in [v0.0.240](https://github.com/astral-sh/ruff/releases/tag/v0.0.240) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27outdated-version-block%27%20OR%20UP036)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Foutdated_version_block.rs#L54)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for conditional blocks gated on `sys.version_info` comparisons
that are outdated for the minimum supported Python version.

## [Why is this bad?](#why-is-this-bad)

In Python, code can be conditionally executed based on the active
Python version by comparing against the `sys.version_info` tuple.

If a code block is only executed for Python versions older than the
minimum supported version, it should be removed.

## [Example](#example)

```
import sys

if sys.version_info < (3, 0):
    print("py2")
else:
    print("py3")
```

Use instead:

```
print("py3")
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because it will remove all code,
comments, and annotations within unreachable version blocks.

## [References](#references)

* [Python documentation: `sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info)