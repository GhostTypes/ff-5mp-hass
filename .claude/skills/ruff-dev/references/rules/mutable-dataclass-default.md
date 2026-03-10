# [mutable-dataclass-default (RUF008)](#mutable-dataclass-default-ruf008)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mutable-dataclass-default%27%20OR%20RUF008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fmutable_dataclass_default.rs#L57)

## [What it does](#what-it-does)

Checks for mutable default values in dataclass attributes.

## [Why is this bad?](#why-is-this-bad)

Mutable default values share state across all instances of the dataclass.
This can lead to bugs when the attributes are changed in one instance, as
those changes will unexpectedly affect all other instances.

Instead of sharing mutable defaults, use the `field(default_factory=...)`
pattern.

If the default value is intended to be mutable, it must be annotated with
`typing.ClassVar`; otherwise, a `ValueError` will be raised.

## [Example](#example)

```
from dataclasses import dataclass


@dataclass
class A:
    # A list without a `default_factory` or `ClassVar` annotation
    # will raise a `ValueError`.
    mutable_default: list[int] = []
```

Use instead:

```
from dataclasses import dataclass, field


@dataclass
class A:
    mutable_default: list[int] = field(default_factory=list)
```

Or:

```
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class A:
    mutable_default: ClassVar[list[int]] = []
```