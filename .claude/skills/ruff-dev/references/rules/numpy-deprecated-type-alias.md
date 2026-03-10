# [numpy-deprecated-type-alias (NPY001)](#numpy-deprecated-type-alias-npy001)

Added in [v0.0.247](https://github.com/astral-sh/ruff/releases/tag/v0.0.247) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27numpy-deprecated-type-alias%27%20OR%20NPY001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fnumpy%2Frules%2Fdeprecated_type_alias.rs#L33)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for deprecated NumPy type aliases.

## [Why is this bad?](#why-is-this-bad)

NumPy's `np.int` has long been an alias of the builtin `int`; the same
is true of `np.float` and others. These aliases exist primarily
for historic reasons, and have been a cause of frequent confusion
for newcomers.

These aliases were deprecated in 1.20, and removed in 1.24.
Note, however, that `np.bool` and `np.long` were reintroduced in 2.0 with
different semantics, and are thus omitted from this rule.

## [Example](#example)

```
import numpy as np

np.int
```

Use instead:

```
int
```