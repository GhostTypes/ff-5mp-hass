# [type-comparison (E721)](#type-comparison-e721)

Added in [v0.0.39](https://github.com/astral-sh/ruff/releases/tag/v0.0.39) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-comparison%27%20OR%20E721)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ftype_comparison.rs#L51)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for object type comparisons using `==` and other comparison
operators.

## [Why is this bad?](#why-is-this-bad)

Unlike a direct type comparison, `isinstance` will also check if an object
is an instance of a class or a subclass thereof.

If you want to check for an exact type match, use `is` or `is not`.

## [Known problems](#known-problems)

When using libraries that override the `==` (`__eq__`) operator (such as NumPy,
Pandas, and SQLAlchemy), this rule may produce false positives, as converting
from `==` to `is` or `is not` will change the behavior of the code.

For example, the following operations are *not* equivalent:

```
import numpy as np

np.array([True, False]) == False
# array([False,  True])

np.array([True, False]) is False
# False
```

## [Example](#example)

```
if type(obj) == type(1):
    pass

if type(obj) == int:
    pass
```

Use instead:

```
if isinstance(obj, int):
    pass
```