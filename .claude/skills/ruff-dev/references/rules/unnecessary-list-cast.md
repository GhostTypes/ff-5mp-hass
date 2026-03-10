# [unnecessary-list-cast (PERF101)](#unnecessary-list-cast-perf101)

Added in [v0.0.276](https://github.com/astral-sh/ruff/releases/tag/v0.0.276) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-list-cast%27%20OR%20PERF101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Funnecessary_list_cast.rs#L53)

Derived from the **[Perflint](../#perflint-perf)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for explicit casts to `list` on for-loop iterables.

## [Why is this bad?](#why-is-this-bad)

Using a `list()` call to eagerly iterate over an already-iterable type
(like a tuple, list, or set) is inefficient, as it forces Python to create
a new list unnecessarily.

Removing the `list()` call will not change the behavior of the code, but
may improve performance.

Note that, as with all `perflint` rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.

## [Example](#example)

```
items = (1, 2, 3)
for i in list(items):
    print(i)
```

Use instead:

```
items = (1, 2, 3)
for i in items:
    print(i)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there's comments in the
`list()` call, as comments may be removed.

For example, the fix would be marked as unsafe in the following case:

```
items = (1, 2, 3)
for i in list(  # comment
    items
):
    print(i)
```