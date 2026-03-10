# [pandas-use-of-dot-pivot-or-unstack (PD010)](#pandas-use-of-dot-pivot-or-unstack-pd010)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-pivot-or-unstack%27%20OR%20PD010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fcall.rs#L120)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.pivot` or `.unstack` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

Prefer `.pivot_table` to `.pivot` or `.unstack`. `.pivot_table` is more general
and can be used to implement the same behavior as `.pivot` and `.unstack`.

## [Example](#example)

```
import pandas as pd

df = pd.read_csv("cities.csv")
df.pivot(index="city", columns="year", values="population")
```

Use instead:

```
import pandas as pd

df = pd.read_csv("cities.csv")
df.pivot_table(index="city", columns="year", values="population")
```

## [References](#references)

* [Pandas documentation: Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)
* [Pandas documentation: `pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html#pandas.pivot_table)