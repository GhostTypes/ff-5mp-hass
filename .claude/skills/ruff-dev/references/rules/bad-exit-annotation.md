# [bad-exit-annotation (PYI036)](#bad-exit-annotation-pyi036)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-exit-annotation%27%20OR%20PYI036)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fexit_annotations.rs#L49)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for incorrect function signatures on `__exit__` and `__aexit__`
methods.

## [Why is this bad?](#why-is-this-bad)

Improperly annotated `__exit__` and `__aexit__` methods can cause
unexpected behavior when interacting with type checkers.

## [Example](#example)

```
from types import TracebackType

class Foo:
    def __exit__(
        self, typ: BaseException, exc: BaseException, tb: TracebackType
    ) -> None: ...
```

Use instead:

```
from types import TracebackType

class Foo:
    def __exit__(
        self,
        typ: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
```