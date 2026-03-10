# [undefined-local-with-import-star (F403)](#undefined-local-with-import-star-f403)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undefined-local-with-import-star%27%20OR%20F403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fimports.rs#L120)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for the use of wildcard imports.

## [Why is this bad?](#why-is-this-bad)

Wildcard imports (e.g., `from module import *`) make it hard to determine
which symbols are available in the current namespace, and from which module
they were imported. They're also discouraged by [PEP 8](https://peps.python.org/pep-0008/#imports).

## [Example](#example)

```
from math import *


def area(radius):
    return pi * radius**2
```

Use instead:

```
from math import pi


def area(radius):
    return pi * radius**2
```