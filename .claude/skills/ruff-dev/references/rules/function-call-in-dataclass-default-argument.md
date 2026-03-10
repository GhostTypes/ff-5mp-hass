# [function-call-in-dataclass-default-argument (RUF009)](#function-call-in-dataclass-default-argument-ruf009)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27function-call-in-dataclass-default-argument%27%20OR%20RUF009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Ffunction_call_in_dataclass_default.rs#L63)

## [What it does](#what-it-does)

Checks for function calls in dataclass attribute defaults.

## [Why is this bad?](#why-is-this-bad)

Function calls are only performed once, at definition time. The returned
value is then reused by all instances of the dataclass. This can lead to
unexpected behavior when the function call returns a mutable object, as
changes to the object will be shared across all instances.

If a field needs to be initialized with a mutable object, use the
`field(default_factory=...)` pattern.

Attributes whose default arguments are `NewType` calls
where the original type is immutable are ignored.

## [Example](#example)

```
from dataclasses import dataclass


def simple_list() -> list[int]:
    return [1, 2, 3, 4]


@dataclass
class A:
    mutable_default: list[int] = simple_list()
```

Use instead:

```
from dataclasses import dataclass, field


def creating_list() -> list[int]:
    return [1, 2, 3, 4]


@dataclass
class A:
    mutable_default: list[int] = field(default_factory=creating_list)
```

## [Options](#options)

* [`lint.flake8-bugbear.extend-immutable-calls`](../../settings/#lint_flake8-bugbear_extend-immutable-calls)