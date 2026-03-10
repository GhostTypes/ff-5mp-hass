# [pandas-use-of-dot-at (PD008)](#pandas-use-of-dot-at-pd008)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-at%27%20OR%20PD008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fsubscript.rs#L85)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.at` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

The `.at` method selects a single value from a `DataFrame` or Series based on
a label index, and is slightly faster than using `.loc`. However, `.loc` is
more idiomatic and versatile, as it can be used to select multiple values at
once.

If performance is an important consideration, convert the object to a NumPy
array, which will provide a much greater performance boost than using `.at`
over `.loc`.

## [Example](#example)

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.at["Maria"]
```

Use instead:

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.loc["Maria"]
```

## [References](#references)

* [Pandas documentation: `loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
* [Pandas documentation: `at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html)