# [pandas-use-of-inplace-argument (PD002)](#pandas-use-of-inplace-argument-pd002)

Added in [v0.0.188](https://github.com/astral-sh/ruff/releases/tag/v0.0.188) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pandas-use-of-inplace-argument%27%20OR%20PD002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpandas_vet%2Frules%2Finplace_argument.rs#L37)

Derived from the **[pandas-vet](../#pandas-vet-pd)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `inplace=True` usages in `pandas` function and method
calls.

## [Why is this bad?](#why-is-this-bad)

Using `inplace=True` encourages mutation rather than immutable data,
which is harder to reason about and may cause bugs. It also removes the
ability to use the method chaining style for `pandas` operations.

Further, in many cases, `inplace=True` does not provide a performance
benefit, as `pandas` will often copy `DataFrames` in the background.

## [Example](#example)

```
df.sort_values("col1", inplace=True)
```

Use instead:

```
sorted_df = df.sort_values("col1")
```

## [References](#references)

* [*Why You Should Probably Never Use pandas `inplace=True`*](https://towardsdatascience.com/why-you-should-probably-never-use-pandas-inplace-true-9f9f211849e4)