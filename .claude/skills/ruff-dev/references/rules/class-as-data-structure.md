# [class-as-data-structure (B903)](#class-as-data-structure-b903)

Preview (since [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27class-as-data-structure%27%20OR%20B903)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fclass_as_data_structure.rs#L36)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for classes that only have a public `__init__` method,
without base classes and decorators.

## [Why is this bad?](#why-is-this-bad)

Classes with just an `__init__` are possibly better off
being a dataclass or a namedtuple, which have less boilerplate.

## [Example](#example)

```
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
```

Use instead:

```
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
```