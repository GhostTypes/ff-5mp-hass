# [numpy2-deprecation (NPY201)](#numpy2-deprecation-npy201)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27numpy2-deprecation%27%20OR%20NPY201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fnumpy%2Frules%2Fnumpy_2_0_deprecation.rs#L52)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of NumPy functions and constants that were removed from
the main namespace in NumPy 2.0.

## [Why is this bad?](#why-is-this-bad)

NumPy 2.0 includes an overhaul of NumPy's Python API, intended to remove
redundant aliases and routines, and establish unambiguous mechanisms for
accessing constants, dtypes, and functions.

As part of this overhaul, a variety of deprecated NumPy functions and
constants were removed from the main namespace.

The majority of these functions and constants can be automatically replaced
by other members of the NumPy API or by equivalents from the Python
standard library. With the exception of renaming `numpy.byte_bounds` to
`numpy.lib.array_utils.byte_bounds`, all such replacements are backwards
compatible with earlier versions of NumPy.

This rule flags all uses of removed members, along with automatic fixes for
any backwards-compatible replacements.

## [Example](#example)

```
import numpy as np

arr1 = [np.Infinity, np.NaN, np.nan, np.PINF, np.inf]
arr2 = [np.float_(1.5), np.float64(5.1)]
np.round_(arr2)
```

Use instead:

```
import numpy as np

arr1 = [np.inf, np.nan, np.nan, np.inf, np.inf]
arr2 = [np.float64(1.5), np.float64(5.1)]
np.round(arr2)
```