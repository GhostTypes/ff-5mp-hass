# [numpy-deprecated-function (NPY003)](#numpy-deprecated-function-npy003)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27numpy-deprecated-function%27%20OR%20NPY003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fnumpy%2Frules%2Fdeprecated_function.rs#L33)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of deprecated NumPy functions.

## [Why is this bad?](#why-is-this-bad)

When NumPy functions are deprecated, they are usually replaced with
newer, more efficient versions, or with functions that are more
consistent with the rest of the NumPy API.

Prefer newer APIs over deprecated ones.

## [Example](#example)

```
import numpy as np

np.alltrue([True, False])
```

Use instead:

```
import numpy as np

np.all([True, False])
```