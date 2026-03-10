# [empty-type-checking-block (TC005)](#empty-type-checking-block-tc005)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27empty-type-checking-block%27%20OR%20TC005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Fempty_type_checking_block.rs#L35)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for an empty type-checking block.

## [Why is this bad?](#why-is-this-bad)

The type-checking block does not do anything and should be removed to avoid
confusion.

## [Example](#example)

```
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

print("Hello, world!")
```

Use instead:

```
print("Hello, world!")
```

## [References](#references)

* [PEP 563: Runtime annotation resolution and `TYPE_CHECKING`](https://peps.python.org/pep-0563/#runtime-annotation-resolution-and-type-checking)