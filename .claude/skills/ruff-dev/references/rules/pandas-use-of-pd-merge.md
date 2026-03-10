# [pandas-use-of-pd-merge (PD015)](#pandas-use-of-pd-merge-pd015)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-pd-merge%27%20OR%20PD015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fpd_merge.rs#L46)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `pd.merge` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

In Pandas, the `.merge` method (exposed on, e.g., `DataFrame` objects) and
the `pd.merge` function (exposed on the Pandas module) are equivalent.

For consistency, prefer calling `.merge` on an object over calling
`pd.merge` on the Pandas module, as the former is more idiomatic.

Further, `pd.merge` is not a method, but a function, which prohibits it
from being used in method chains, a common pattern in Pandas code.

## [Example](#example)

```
import pandas as pd

cats_df = pd.read_csv("cats.csv")
dogs_df = pd.read_csv("dogs.csv")
rabbits_df = pd.read_csv("rabbits.csv")
pets_df = pd.merge(pd.merge(cats_df, dogs_df), rabbits_df)  # Hard to read.
```

Use instead:

```
import pandas as pd

cats_df = pd.read_csv("cats.csv")
dogs_df = pd.read_csv("dogs.csv")
rabbits_df = pd.read_csv("rabbits.csv")
pets_df = cats_df.merge(dogs_df).merge(rabbits_df)
```

## [References](#references)

* [Pandas documentation: `merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)
* [Pandas documentation: `pd.merge`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge)