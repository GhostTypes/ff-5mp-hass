# [reimplemented-container-builtin (PIE807)](#reimplemented-container-builtin-pie807)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27reimplemented-container-builtin%27%20OR%20PIE807)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Freimplemented_container_builtin.rs#L40)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for lambdas that can be replaced with the `list` or `dict` builtins.

## [Why is this bad?](#why-is-this-bad)

Using container builtins are more succinct and idiomatic than wrapping
the literal in a lambda.

## [Example](#example)

```
from dataclasses import dataclass, field


@dataclass
class Foo:
    bar: list[int] = field(default_factory=lambda: [])
```

Use instead:

```
from dataclasses import dataclass, field


@dataclass
class Foo:
    bar: list[int] = field(default_factory=list)
    baz: dict[str, int] = field(default_factory=dict)
```

## [References](#references)

* [Python documentation: `list`](https://docs.python.org/3/library/functions.html#func-list)