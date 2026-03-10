# [unnecessary-default-type-args (UP043)](#unnecessary-default-type-args-up043)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-default-type-args%27%20OR%20UP043)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funnecessary_default_type_args.rs#L65)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary default type arguments for `Generator` and
`AsyncGenerator` on Python 3.13+.
In [preview](https://docs.astral.sh/ruff/preview/), this rule will also apply to stub files.

## [Why is this bad?](#why-is-this-bad)

Python 3.13 introduced the ability for type parameters to specify default
values. Following this change, several standard-library classes were
updated to add default values for some of their type parameters. For
example, `Generator[int]` is now equivalent to
`Generator[int, None, None]`, as the second and third type parameters of
`Generator` now default to `None`.

Omitting type arguments that match the default values can make the code
more concise and easier to read.

## [Example](#example)

```
from collections.abc import Generator, AsyncGenerator


def sync_gen() -> Generator[int, None, None]:
    yield 42


async def async_gen() -> AsyncGenerator[int, None]:
    yield 42
```

Use instead:

```
from collections.abc import Generator, AsyncGenerator


def sync_gen() -> Generator[int]:
    yield 42


async def async_gen() -> AsyncGenerator[int]:
    yield 42
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the type annotation contains comments.

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [PEP 696 – Type Defaults for Type Parameters](https://peps.python.org/pep-0696/)
* [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
* [Python documentation: `typing.Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)
* [Python documentation: `typing.AsyncGenerator`](https://docs.python.org/3/library/typing.html#typing.AsyncGenerator)