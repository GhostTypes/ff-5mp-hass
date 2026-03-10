# [cached-instance-method (B019)](#cached-instance-method-b019)

Added in [v0.0.114](https://github.com/astral-sh/ruff/releases/tag/v0.0.114) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27cached-instance-method%27%20OR%20B019)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fcached_instance_method.rs#L65)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for uses of the `functools.lru_cache` and `functools.cache`
decorators on methods.

## [Why is this bad?](#why-is-this-bad)

Using the `functools.lru_cache` and `functools.cache` decorators on methods
can lead to memory leaks, as the global cache will retain a reference to
the instance, preventing it from being garbage collected.

Instead, refactor the method to depend only on its arguments and not on the
instance of the class, or use the `@lru_cache` decorator on a function
outside of the class.

This rule ignores instance methods on enumeration classes, as enum members
are singletons.

## [Example](#example)

```
from functools import lru_cache


def square(x: int) -> int:
    return x * x


class Number:
    value: int

    @lru_cache
    def squared(self):
        return square(self.value)
```

Use instead:

```
from functools import lru_cache


@lru_cache
def square(x: int) -> int:
    return x * x


class Number:
    value: int

    def squared(self):
        return square(self.value)
```

## [References](#references)

* [Python documentation: `functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
* [Python documentation: `functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache)
* [don't lru\_cache methods!](https://www.youtube.com/watch?v=sVjtp6tGo0g)