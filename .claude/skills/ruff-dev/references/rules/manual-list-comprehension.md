# [manual-list-comprehension (PERF401)](#manual-list-comprehension-perf401)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27manual-list-comprehension%27%20OR%20PERF401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Fmanual_list_comprehension.rs#L51)

Derived from the **[Perflint](../#perflint-perf)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `for` loops that can be replaced by a list comprehension.

## [Why is this bad?](#why-is-this-bad)

When creating a transformed list from an existing list using a for-loop,
prefer a list comprehension. List comprehensions are more readable and
more performant.

Using the below as an example, the list comprehension is ~10% faster on
Python 3.11, and ~25% faster on Python 3.10.

Note that, as with all `perflint` rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.

## [Example](#example)

```
original = list(range(10000))
filtered = []
for i in original:
    if i % 2:
        filtered.append(i)
```

Use instead:

```
original = list(range(10000))
filtered = [x for x in original if x % 2]
```

If you're appending to an existing list, use the `extend` method instead:

```
original = list(range(10000))
filtered.extend(x for x in original if x % 2)
```