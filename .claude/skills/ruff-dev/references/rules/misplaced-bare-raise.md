# [misplaced-bare-raise (PLE0704)](#misplaced-bare-raise-ple0704)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27misplaced-bare-raise%27%20OR%20PLE0704)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fmisplaced_bare_raise.rs#L43)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for bare `raise` statements outside of exception handlers.

## [Why is this bad?](#why-is-this-bad)

A bare `raise` statement without an exception object will re-raise the last
exception that was active in the current scope, and is typically used
within an exception handler to re-raise the caught exception.

If a bare `raise` is used outside of an exception handler, it will generate
an error due to the lack of an active exception.

Note that a bare `raise` within a `finally` block will work in some cases
(namely, when the exception is raised within the `try` block), but should
be avoided as it can lead to confusing behavior.

## [Example](#example)

```
from typing import Any


def is_some(obj: Any) -> bool:
    if obj is None:
        raise
```

Use instead:

```
from typing import Any


def is_some(obj: Any) -> bool:
    if obj is None:
        raise ValueError("`obj` cannot be `None`")
```