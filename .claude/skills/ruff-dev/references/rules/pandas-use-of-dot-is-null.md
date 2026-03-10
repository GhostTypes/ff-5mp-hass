# [pandas-use-of-dot-is-null (PD003)](#pandas-use-of-dot-is-null-pd003)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-is-null%27%20OR%20PD003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fcall.rs#L42)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.isnull` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

In the Pandas API, `.isna` and `.isnull` are equivalent. For consistency,
prefer `.isna` over `.isnull`.

As a name, `.isna` more accurately reflects the behavior of the method,
since these methods check for `NaN` and `NaT` values in addition to `None`
values.

## [Example](#example)

```
import pandas as pd

animals_df = pd.read_csv("animals.csv")
pd.isnull(animals_df)
```

Use instead:

```
import pandas as pd

animals_df = pd.read_csv("animals.csv")
pd.isna(animals_df)
```

## [References](#references)

* [Pandas documentation: `isnull`](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html#pandas.isnull)
* [Pandas documentation: `isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna)