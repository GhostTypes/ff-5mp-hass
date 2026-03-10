# [loop-variable-overrides-iterator (B020)](#loop-variable-overrides-iterator-b020)

Added in [v0.0.121](https://github.com/astral-sh/ruff/releases/tag/v0.0.121) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27loop-variable-overrides-iterator%27%20OR%20B020)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Floop_variable_overrides_iterator.rs#L39)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for loop control variables that override the loop iterable.

## [Why is this bad?](#why-is-this-bad)

Loop control variables should not override the loop iterable, as this can
lead to confusing behavior.

Instead, use a distinct variable name for any loop control variables.

## [Example](#example)

```
items = [1, 2, 3]

for items in items:
    print(items)
```

Use instead:

```
items = [1, 2, 3]

for item in items:
    print(item)
```

## [References](#references)

* [Python documentation: The `for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)