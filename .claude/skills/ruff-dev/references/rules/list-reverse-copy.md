# [list-reverse-copy (FURB187)](#list-reverse-copy-furb187)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27list-reverse-copy%27%20OR%20FURB187)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Flist_reverse_copy.rs#L49)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for list reversals that can be performed in-place in lieu of
creating a new list.

## [Why is this bad?](#why-is-this-bad)

When reversing a list, it's more efficient to use the in-place method
`.reverse()` instead of creating a new list, if the original list is
no longer needed.

## [Example](#example)

```
l = [1, 2, 3]
l = reversed(l)

l = [1, 2, 3]
l = list(reversed(l))

l = [1, 2, 3]
l = l[::-1]
```

Use instead:

```
l = [1, 2, 3]
l.reverse()
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as calling `.reverse()` on a list
will mutate the list in-place, unlike `reversed`, which creates a new list
and leaves the original list unchanged.

If the list is referenced elsewhere, this could lead to unexpected
behavior.

## [References](#references)

* [Python documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)