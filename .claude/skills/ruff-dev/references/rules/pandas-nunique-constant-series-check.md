# [pandas-nunique-constant-series-check (PD101)](#pandas-nunique-constant-series-check-pd101)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-nunique-constant-series-check%27%20OR%20PD101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fnunique_constant_series_check.rs#L53)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Check for uses of `.nunique()` to check if a Pandas Series is constant
(i.e., contains only one unique value).

## [Why is this bad?](#why-is-this-bad)

`.nunique()` is computationally inefficient for checking if a Series is
constant.

Consider, for example, a Series of length `n` that consists of increasing
integer values (e.g., 1, 2, 3, 4). The `.nunique()` method will iterate
over the entire Series to count the number of unique values. But in this
case, we can detect that the Series is non-constant after visiting the
first two values, which are non-equal.

In general, `.nunique()` requires iterating over the entire Series, while a
more efficient approach allows short-circuiting the operation as soon as a
non-equal value is found.

Instead of calling `.nunique()`, convert the Series to a NumPy array, and
check if all values in the array are equal to the first observed value.

## [Example](#example)

```
import pandas as pd

data = pd.Series(range(1000))
if data.nunique() <= 1:
    print("Series is constant")
```

Use instead:

```
import pandas as pd

data = pd.Series(range(1000))
array = data.to_numpy()
if array.shape[0] == 0 or (array[0] == array).all():
    print("Series is constant")
```

## [References](#references)

* [Pandas Cookbook: "Constant Series"](https://pandas.pydata.org/docs/user_guide/cookbook.html#constant-series)
* [Pandas documentation: `nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html)