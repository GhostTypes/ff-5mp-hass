# [pandas-use-of-dot-not-null (PD004)](#pandas-use-of-dot-not-null-pd004)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-not-null%27%20OR%20PD004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fcall.rs#L83)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.notnull` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

In the Pandas API, `.notna` and `.notnull` are equivalent. For consistency,
prefer `.notna` over `.notnull`.

As a name, `.notna` more accurately reflects the behavior of the method,
since these methods check for `NaN` and `NaT` values in addition to `None`
values.

## [Example](#example)

```
import pandas as pd

animals_df = pd.read_csv("animals.csv")
pd.notnull(animals_df)
```

Use instead:

```
import pandas as pd

animals_df = pd.read_csv("animals.csv")
pd.notna(animals_df)
```

## [References](#references)

* [Pandas documentation: `notnull`](https://pandas.pydata.org/docs/reference/api/pandas.notnull.html#pandas.notnull)
* [Pandas documentation: `notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna)