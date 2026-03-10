# [pandas-use-of-dot-read-table (PD012)](#pandas-use-of-dot-read-table-pd012)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-read-table%27%20OR%20PD012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fread_table.rs#L38)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `pd.read_table` to read CSV files.

## [Why is this bad?](#why-is-this-bad)

In the Pandas API, `pd.read_csv` and `pd.read_table` are equivalent apart
from their default separator: `pd.read_csv` defaults to a comma (`,`),
while `pd.read_table` defaults to a tab (`\t`) as the default separator.

Prefer `pd.read_csv` over `pd.read_table` when reading comma-separated
data (like CSV files), as it is more idiomatic.

## [Example](#example)

```
import pandas as pd

cities_df = pd.read_table("cities.csv", sep=",")
```

Use instead:

```
import pandas as pd

cities_df = pd.read_csv("cities.csv")
```

## [References](#references)

* [Pandas documentation: `read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv)
* [Pandas documentation: `read_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table)