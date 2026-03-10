# [manual-list-copy (PERF402)](#manual-list-copy-perf402)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27manual-list-copy%27%20OR%20PERF402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Fmanual_list_copy.rs#L37)

Derived from the **[Perflint](../#perflint-perf)** linter.

## [What it does](#what-it-does)

Checks for `for` loops that can be replaced by a making a copy of a list.

## [Why is this bad?](#why-is-this-bad)

When creating a copy of an existing list using a for-loop, prefer
`list` or `list.copy` instead. Making a direct copy is more readable and
more performant.

Using the below as an example, the `list`-based copy is ~2x faster on
Python 3.11.

Note that, as with all `perflint` rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.

## [Example](#example)

```
original = list(range(10000))
filtered = []
for i in original:
    filtered.append(i)
```

Use instead:

```
original = list(range(10000))
filtered = list(original)
```