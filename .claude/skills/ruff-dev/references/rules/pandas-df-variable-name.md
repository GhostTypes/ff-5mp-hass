# [pandas-df-variable-name (PD901)](#pandas-df-variable-name-pd901)

Removed (since [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-df-variable-name%27%20OR%20PD901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Fassignment_to_df.rs#L34)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule has been removed as it's highly opinionated and overly strict in most cases.

## [What it does](#what-it-does)

Checks for assignments to the variable `df`.

## [Why is this bad?](#why-is-this-bad)

Although `df` is a common variable name for a Pandas `DataFrame`, it's not a
great variable name for production code, as it's non-descriptive and
prone to name conflicts.

Instead, use a more descriptive variable name.

## [Example](#example)

```
import pandas as pd

df = pd.read_csv("animals.csv")
```

Use instead:

```
import pandas as pd

animals = pd.read_csv("animals.csv")
```