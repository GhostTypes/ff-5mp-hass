# [replace-str-enum (UP042)](#replace-str-enum-up042)

Preview (since [v0.3.6](https://github.com/astral-sh/ruff/releases/tag/v0.3.6)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27replace-str-enum%27%20OR%20UP042)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Freplace_str_enum.rs#L79)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for classes that inherit from both `str` and `enum.Enum`.

## [Why is this bad?](#why-is-this-bad)

Python 3.11 introduced `enum.StrEnum`, which is preferred over inheriting
from both `str` and `enum.Enum`.

## [Example](#example)

```
import enum


class Foo(str, enum.Enum): ...
```

Use instead:

```
import enum


class Foo(enum.StrEnum): ...
```

## [Fix safety](#fix-safety)

Python 3.11 introduced a [breaking change](https://blog.pecar.me/python-enum) for enums that inherit from both
`str` and `enum.Enum`. Consider the following enum:

```
from enum import Enum


class Foo(str, Enum):
    BAR = "bar"
```

In Python 3.11, the formatted representation of `Foo.BAR` changed as
follows:

```
# Python 3.10
f"{Foo.BAR}"  # > bar
# Python 3.11
f"{Foo.BAR}"  # > Foo.BAR
```

Migrating from `str` and `enum.Enum` to `enum.StrEnum` will restore the
previous behavior, such that:

```
from enum import StrEnum


class Foo(StrEnum):
    BAR = "bar"


f"{Foo.BAR}"  # > bar
```

As such, migrating to `enum.StrEnum` will introduce a behavior change for
code that relies on the Python 3.11 behavior.

## [References](#references)

* [enum.StrEnum](https://docs.python.org/3/library/enum.html#enum.StrEnum)