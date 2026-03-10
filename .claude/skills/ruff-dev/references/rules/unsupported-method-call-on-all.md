# [unsupported-method-call-on-all (PYI056)](#unsupported-method-call-on-all-pyi056)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unsupported-method-call-on-all%27%20OR%20PYI056)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Funsupported_method_call_on_all.rs#L43)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks that `append`, `extend` and `remove` methods are not called on
`__all__`.

## [Why is this bad?](#why-is-this-bad)

Different type checkers have varying levels of support for calling these
methods on `__all__`. Instead, use the `+=` operator to add items to
`__all__`, which is known to be supported by all major type checkers.

## [Example](#example)

```
import sys

__all__ = ["A", "B"]

if sys.version_info >= (3, 10):
    __all__.append("C")

if sys.version_info >= (3, 11):
    __all__.remove("B")
```

Use instead:

```
import sys

__all__ = ["A"]

if sys.version_info < (3, 11):
    __all__ += ["B"]

if sys.version_info >= (3, 10):
    __all__ += ["C"]
```