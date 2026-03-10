# [unnecessary-spread (PIE800)](#unnecessary-spread-pie800)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-spread%27%20OR%20PIE800)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Funnecessary_spread.rs#L30)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary dictionary unpacking operators (`**`).

## [Why is this bad?](#why-is-this-bad)

Unpacking a dictionary into another dictionary is redundant. The unpacking
operator can be removed, making the code more readable.

## [Example](#example)

```
foo = {"A": 1, "B": 2}
bar = {**foo, **{"C": 3}}
```

Use instead:

```
foo = {"A": 1, "B": 2}
bar = {**foo, "C": 3}
```

## [References](#references)

* [Python documentation: Dictionary displays](https://docs.python.org/3/reference/expressions.html#dictionary-displays)