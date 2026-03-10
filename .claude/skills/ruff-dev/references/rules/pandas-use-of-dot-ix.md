# [pandas-use-of-dot-ix (PD007)](#pandas-use-of-dot-ix-pd007)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-ix%27%20OR%20PD007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fsubscript.rs#L42)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.ix` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

The `.ix` method is deprecated as its behavior is ambiguous. Specifically,
it's often unclear whether `.ix` is indexing by label or by ordinal position.

Instead, prefer the `.loc` method for label-based indexing, and `.iloc` for
ordinal indexing.

## [Example](#example)

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.ix[0]  # 0th row or row with label 0?
```

Use instead:

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.iloc[0]  # 0th row.
```

## [References](#references)

* [Pandas release notes: Deprecate `.ix`](https://pandas.pydata.org/pandas-docs/version/0.20/whatsnew.html#deprecate-ix)
* [Pandas documentation: `loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
* [Pandas documentation: `iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)