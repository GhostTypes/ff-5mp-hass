# [mutable-contextvar-default (B039)](#mutable-contextvar-default-b039)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mutable-contextvar-default%27%20OR%20B039)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fmutable_contextvar_default.rs#L56)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for uses of mutable objects as `ContextVar` defaults.

## [Why is this bad?](#why-is-this-bad)

The `ContextVar` default is evaluated once, when the `ContextVar` is defined.

The same mutable object is then shared across all `.get()` method calls to
the `ContextVar`. If the object is modified, those modifications will persist
across calls, which can lead to unexpected behavior.

Instead, prefer to use immutable data structures. Alternatively, take
`None` as a default, and initialize a new mutable object inside for each
call using the `.set()` method.

Types outside the standard library can be marked as immutable with the
[`lint.flake8-bugbear.extend-immutable-calls`](../../settings/#lint_flake8-bugbear_extend-immutable-calls) configuration option.

## [Example](#example)

```
from contextvars import ContextVar


cv: ContextVar[list] = ContextVar("cv", default=[])
```

Use instead:

```
from contextvars import ContextVar


cv: ContextVar[list | None] = ContextVar("cv", default=None)

...

if cv.get() is None:
    cv.set([])
```

## [Options](#options)

* [`lint.flake8-bugbear.extend-immutable-calls`](../../settings/#lint_flake8-bugbear_extend-immutable-calls)

## [References](#references)

* [Python documentation: `contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html)