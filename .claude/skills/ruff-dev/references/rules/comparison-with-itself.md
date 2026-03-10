# [comparison-with-itself (PLR0124)](#comparison-with-itself-plr0124)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27comparison-with-itself%27%20OR%20PLR0124)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fcomparison_with_itself.rs#L33)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for operations that compare a name to itself.

## [Why is this bad?](#why-is-this-bad)

Comparing a name to itself always results in the same value, and is likely
a mistake.

## [Example](#example)

```
foo == foo
```

In some cases, self-comparisons are used to determine whether a float is
NaN. Instead, prefer `math.isnan`:

```
import math

math.isnan(foo)
```

## [References](#references)

* [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)