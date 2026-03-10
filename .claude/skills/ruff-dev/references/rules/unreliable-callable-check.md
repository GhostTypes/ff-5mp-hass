# [unreliable-callable-check (B004)](#unreliable-callable-check-b004)

Added in [v0.0.106](https://github.com/astral-sh/ruff/releases/tag/v0.0.106) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unreliable-callable-check%27%20OR%20B004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Funreliable_callable_check.rs#L69)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `hasattr` to test if an object is callable (e.g.,
`hasattr(obj, "__call__")`).

## [Why is this bad?](#why-is-this-bad)

Using `hasattr` is an unreliable mechanism for testing if an object is
callable. If `obj` implements a custom `__getattr__`, or if its `__call__`
is itself not callable, you may get misleading results.

Instead, use `callable(obj)` to test if `obj` is callable.

## [Example](#example)

```
hasattr(obj, "__call__")
```

Use instead:

```
callable(obj)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because the replacement may not be semantically
equivalent to the original expression, potentially changing the behavior of the code.

For example, an imported module may have a `__call__` attribute but is not considered
a callable object:

```
import operator

assert hasattr(operator, "__call__")
assert callable(operator) is False
```

Additionally, `__call__` may be defined only as an instance method:

```
class A:
    def __init__(self):
        self.__call__ = None


assert hasattr(A(), "__call__")
assert callable(A()) is False
```

Additionally, if there are comments in the `hasattr` call expression, they may be removed:

```
hasattr(
    # comment 1
    obj,  # comment 2
    # comment 3
    "__call__",  # comment 4
    # comment 5
)
```

## [References](#references)

* [Python documentation: `callable`](https://docs.python.org/3/library/functions.html#callable)
* [Python documentation: `hasattr`](https://docs.python.org/3/library/functions.html#hasattr)
* [Python documentation: `__getattr__`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__)
* [Python documentation: `__call__`](https://docs.python.org/3/reference/datamodel.html#object.__call__)