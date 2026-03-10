# [for-loop-set-mutations (FURB142)](#for-loop-set-mutations-furb142)

Preview (since [v0.3.5](https://github.com/astral-sh/ruff/releases/tag/v0.3.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27for-loop-set-mutations%27%20OR%20FURB142)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Ffor_loop_set_mutations.rs#L46)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for code that updates a set with the contents of an iterable by
using a `for` loop to call `.add()` or `.discard()` on each element
separately.

## [Why is this bad?](#why-is-this-bad)

When adding or removing a batch of elements to or from a set, it's more
idiomatic to use a single method call rather than adding or removing
elements one by one.

## [Example](#example)

```
s = set()

for x in (1, 2, 3):
    s.add(x)

for x in (1, 2, 3):
    s.discard(x)
```

Use instead:

```
s = set()

s.update((1, 2, 3))
s.difference_update((1, 2, 3))
```

## [Fix safety](#fix-safety)

The fix will be marked as unsafe if applying the fix would delete any comments.
Otherwise, it is marked as safe.

## [References](#references)

* [Python documentation: `set`](https://docs.python.org/3/library/stdtypes.html#set)