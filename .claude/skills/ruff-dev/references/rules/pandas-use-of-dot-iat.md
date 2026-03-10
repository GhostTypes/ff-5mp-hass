# [pandas-use-of-dot-iat (PD009)](#pandas-use-of-dot-iat-pd009)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-iat%27%20OR%20PD009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fsubscript.rs#L137)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.iat` on Pandas objects.

## [Why is this bad?](#why-is-this-bad)

The `.iat` method selects a single value from a `DataFrame` or Series based
on an ordinal index, and is slightly faster than using `.iloc`. However,
`.iloc` is more idiomatic and versatile, as it can be used to select
multiple values at once.

If performance is an important consideration, convert the object to a NumPy
array, which will provide a much greater performance boost than using `.iat`
over `.iloc`.

## [Example](#example)

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.iat[0]
```

Use instead:

```
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.iloc[0]
```

Or, using NumPy:

```
import numpy as np
import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.to_numpy()[0]
```

## [References](#references)

* [Pandas documentation: `iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
* [Pandas documentation: `iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html)