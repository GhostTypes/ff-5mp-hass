# [non-pep604-isinstance (UP038)](#non-pep604-isinstance-up038)

Removed (since [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-pep604-isinstance%27%20OR%20UP038)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fuse_pep604_isinstance.rs#L74)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

Fix is always available.

## [Removed](#removed)

This rule was removed as using [PEP 604](https://peps.python.org/pep-0604/) syntax in `isinstance` and `issubclass` calls
isn't recommended practice, and it incorrectly suggests that other typing syntaxes like [PEP 695](https://peps.python.org/pep-0695/)
would be supported by `isinstance` and `issubclass`. Using the [PEP 604](https://peps.python.org/pep-0604/) syntax
is also slightly slower.

## [What it does](#what-it-does)

Checks for uses of `isinstance` and `issubclass` that take a tuple
of types for comparison.

## [Why is this bad?](#why-is-this-bad)

Since Python 3.10, `isinstance` and `issubclass` can be passed a
`|`-separated union of types, which is consistent
with the union operator introduced in [PEP 604](https://peps.python.org/pep-0604/).

Note that this results in slower code. Ignore this rule if the
performance of an `isinstance` or `issubclass` check is a
concern, e.g., in a hot loop.

## [Example](#example)

```
isinstance(x, (int, float))
```

Use instead:

```
isinstance(x, int | float)
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)
* [Python documentation: `issubclass`](https://docs.python.org/3/library/functions.html#issubclass)