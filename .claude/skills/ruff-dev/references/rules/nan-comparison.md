# [nan-comparison (PLW0177)](#nan-comparison-plw0177)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27nan-comparison%27%20OR%20PLW0177)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnan_comparison.rs#L35)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for comparisons against NaN values.

## [Why is this bad?](#why-is-this-bad)

Comparing against a NaN value can lead to unexpected results. For example,
`float("NaN") == float("NaN")` will return `False` and, in general,
`x == float("NaN")` will always return `False`, even if `x` is `NaN`.

To determine whether a value is `NaN`, use `math.isnan` or `np.isnan`
instead of comparing against `NaN` directly.

## [Example](#example)

```
if x == float("NaN"):
    pass
```

Use instead:

```
import math

if math.isnan(x):
    pass
```