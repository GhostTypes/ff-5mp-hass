# [non-unique-enums (PIE796)](#non-unique-enums-pie796)

Added in [v0.0.224](https://github.com/astral-sh/ruff/releases/tag/v0.0.224) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-unique-enums%27%20OR%20PIE796)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Fnon_unique_enums.rs#L43)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

## [What it does](#what-it-does)

Checks for enums that contain duplicate values.

## [Why is this bad?](#why-is-this-bad)

Enum values should be unique. Non-unique values are redundant and likely a
mistake.

## [Example](#example)

```
from enum import Enum


class Foo(Enum):
    A = 1
    B = 2
    C = 1
```

Use instead:

```
from enum import Enum


class Foo(Enum):
    A = 1
    B = 2
    C = 3
```

## [References](#references)

* [Python documentation: `enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)