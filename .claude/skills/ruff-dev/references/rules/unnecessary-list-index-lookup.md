# [unnecessary-list-index-lookup (PLR1736)](#unnecessary-list-index-lookup-plr1736)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-list-index-lookup%27%20OR%20PLR1736)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funnecessary_list_index_lookup.rs#L34)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for index-based list accesses during `enumerate` iterations.

## [Why is this bad?](#why-is-this-bad)

When iterating over a list with `enumerate`, the current item is already
available alongside its index. Using the index to look up the item is
unnecessary.

## [Example](#example)

```
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(letters[index])
```

Use instead:

```
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(letter)
```