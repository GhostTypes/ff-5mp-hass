# [pandas-use-of-dot-stack (PD013)](#pandas-use-of-dot-stack-pd013)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-stack%27%20OR%20PD013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fcall.rs#L158)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.stack` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

Prefer `.melt` to `.stack`, which has the same functionality but with
support for direct column renaming and no dependence on `MultiIndex`.

## [Example](#example)

```
import pandas as pd

cities_df = pd.read_csv("cities.csv")
cities_df.set_index("city").stack()
```

Use instead:

```
import pandas as pd

cities_df = pd.read_csv("cities.csv")
cities_df.melt(id_vars="city")
```

## [References](#references)

* [Pandas documentation: `melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
* [Pandas documentation: `stack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html)