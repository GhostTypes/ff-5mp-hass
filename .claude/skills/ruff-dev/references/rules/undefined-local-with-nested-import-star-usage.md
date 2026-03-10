# [undefined-local-with-nested-import-star-usage (F406)](#undefined-local-with-nested-import-star-usage-f406)

Added in [v0.0.37](https://github.com/astral-sh/ruff/releases/tag/v0.0.37) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undefined-local-with-nested-import-star-usage%27%20OR%20F406)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fimports.rs#L246)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Check for the use of wildcard imports outside of the module namespace.

## [Why is this bad?](#why-is-this-bad)

The use of wildcard imports outside of the module namespace (e.g., within
functions) can lead to confusion, as the import can shadow local variables.

Though wildcard imports are discouraged by [PEP 8](https://peps.python.org/pep-0008/#imports), when necessary, they
should be placed in the module namespace (i.e., at the top-level of a
module).

## [Example](#example)

```
def foo():
    from math import *
```

Use instead:

```
from math import *


def foo(): ...
```