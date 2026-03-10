# [pandas-use-of-dot-values (PD011)](#pandas-use-of-dot-values-pd011)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-dot-values%27%20OR%20PD011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fattr.rs#L36)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

## [What it does](#what-it-does)

Checks for uses of `.values` on Pandas Series and Index objects.

## [Why is this bad?](#why-is-this-bad)

The `.values` attribute is ambiguous as its return type is unclear. As
such, it is no longer recommended by the Pandas documentation.

Instead, use `.to_numpy()` to return a NumPy array, or `.array` to return a
Pandas `ExtensionArray`.

## [Example](#example)

```
import pandas as pd

animals = pd.read_csv("animals.csv").values  # Ambiguous.
```

Use instead:

```
import pandas as pd

animals = pd.read_csv("animals.csv").to_numpy()  # Explicit.
```

## [References](#references)

* [Pandas documentation: Accessing the values in a Series or Index](https://pandas.pydata.org/pandas-docs/stable/whatsnew/v0.24.0.html#accessing-the-values-in-a-series-or-index)