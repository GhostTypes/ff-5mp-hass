# [unnecessary-builtin-import (UP029)](#unnecessary-builtin-import-up029)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-builtin-import%27%20OR%20UP029)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funnecessary_builtin_import.rs#L48)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary imports of builtins.

## [Why is this bad?](#why-is-this-bad)

Builtins are always available. Importing them is unnecessary and should be
removed to avoid confusion.

## [Example](#example)

```
from builtins import str

str(1)
```

Use instead:

```
str(1)
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe because removing the import
may change program behavior. For example, in the following
situation:

```
def str(x):
    return x


from builtins import str

str(1)  # `"1"` with the import, `1` without
```

## [References](#references)

* [Python documentation: The Python Standard Library](https://docs.python.org/3/library/index.html)