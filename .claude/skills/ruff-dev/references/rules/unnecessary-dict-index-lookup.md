# [unnecessary-dict-index-lookup (PLR1733)](#unnecessary-dict-index-lookup-plr1733)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-dict-index-lookup%27%20OR%20PLR1733)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funnecessary_dict_index_lookup.rs#L33)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for key-based dict accesses during `.items()` iterations.

## [Why is this bad?](#why-is-this-bad)

When iterating over a dict via `.items()`, the current value is already
available alongside its key. Using the key to look up the value is
unnecessary.

## [Example](#example)

```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}

for fruit_name, fruit_count in FRUITS.items():
    print(FRUITS[fruit_name])
```

Use instead:

```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}

for fruit_name, fruit_count in FRUITS.items():
    print(fruit_count)
```