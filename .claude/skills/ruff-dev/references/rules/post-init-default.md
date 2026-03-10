# [post-init-default (RUF033)](#post-init-default-ruf033)

Added in [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27post-init-default%27%20OR%20RUF033)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fpost_init_default.rs#L76)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `__post_init__` dataclass methods with parameter defaults.

## [Why is this bad?](#why-is-this-bad)

Adding a default value to a parameter in a `__post_init__` method has no
impact on whether the parameter will have a default value in the dataclass's
generated `__init__` method. To create an init-only dataclass parameter with
a default value, you should use an `InitVar` field in the dataclass's class
body and give that `InitVar` field a default value.

As the [documentation](https://docs.python.org/3/library/dataclasses.html#init-only-variables) states:

> Init-only fields are added as parameters to the generated `__init__()`
> method, and are passed to the optional `__post_init__()` method. They are
> not otherwise used by dataclasses.

## [Example](#example)

```
from dataclasses import InitVar, dataclass


@dataclass
class Foo:
    bar: InitVar[int] = 0

    def __post_init__(self, bar: int = 1, baz: int = 2) -> None:
        print(bar, baz)


foo = Foo()  # Prints '0 2'.
```

Use instead:

```
from dataclasses import InitVar, dataclass


@dataclass
class Foo:
    bar: InitVar[int] = 1
    baz: InitVar[int] = 2

    def __post_init__(self, bar: int, baz: int) -> None:
        print(bar, baz)


foo = Foo()  # Prints '1 2'.
```

## [Fix safety](#fix-safety)

This fix is always marked as unsafe because, although switching to `InitVar` is usually correct,
it is incorrect when the parameter is not intended to be part of the public API or when the value
is meant to be shared across all instances.

## [References](#references)

* [Python documentation: Post-init processing](https://docs.python.org/3/library/dataclasses.html#post-init-processing)
* [Python documentation: Init-only variables](https://docs.python.org/3/library/dataclasses.html#init-only-variables)