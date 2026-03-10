# [unnecessary-range-start (PIE808)](#unnecessary-range-start-pie808)

Added in [v0.0.286](https://github.com/astral-sh/ruff/releases/tag/v0.0.286) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-range-start%27%20OR%20PIE808)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Funnecessary_range_start.rs#L29)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `range` calls with an unnecessary `start` argument.

## [Why is this bad?](#why-is-this-bad)

`range(0, x)` is equivalent to `range(x)`, as `0` is the default value for
the `start` argument. Omitting the `start` argument makes the code more
concise and idiomatic.

## [Example](#example)

```
range(0, 3)
```

Use instead:

```
range(3)
```

## [References](#references)

* [Python documentation: `range`](https://docs.python.org/3/library/stdtypes.html#range)