# [manual-dict-comprehension (PERF403)](#manual-dict-comprehension-perf403)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27manual-dict-comprehension%27%20OR%20PERF403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Fmanual_dict_comprehension.rs#L48)

Derived from the **[Perflint](../#perflint-perf)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `for` loops that can be replaced by a dictionary comprehension.

## [Why is this bad?](#why-is-this-bad)

When creating or extending a dictionary in a for-loop, prefer a dictionary
comprehension. Comprehensions are more readable and more performant.

For example, when comparing `{x: x for x in list(range(1000))}` to the `for`
loop version, the comprehension is ~10% faster on Python 3.11.

Note that, as with all `perflint` rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.

## [Example](#example)

```
pairs = (("a", 1), ("b", 2))
result = {}
for x, y in pairs:
    if y % 2:
        result[x] = y
```

Use instead:

```
pairs = (("a", 1), ("b", 2))
result = {x: y for x, y in pairs if y % 2}
```

If you're appending to an existing dictionary, use the `update` method instead:

```
pairs = (("a", 1), ("b", 2))
result.update({x: y for x, y in pairs if y % 2})
```