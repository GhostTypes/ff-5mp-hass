# [lru-cache-without-parameters (UP011)](#lru-cache-without-parameters-up011)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27lru-cache-without-parameters%27%20OR%20UP011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Flru_cache_without_parameters.rs#L41)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary parentheses on `functools.lru_cache` decorators.

## [Why is this bad?](#why-is-this-bad)

Since Python 3.8, `functools.lru_cache` can be used as a decorator without
trailing parentheses, as long as no arguments are passed to it.

## [Example](#example)

```
import functools


@functools.lru_cache()
def foo(): ...
```

Use instead:

```
import functools


@functools.lru_cache
def foo(): ...
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
* [Let lru\_cache be used as a decorator with no arguments](https://github.com/python/cpython/issues/80953)