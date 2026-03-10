# [delete-full-slice (FURB131)](#delete-full-slice-furb131)

Preview (since [v0.0.287](https://github.com/astral-sh/ruff/releases/tag/v0.0.287)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27delete-full-slice%27%20OR%20FURB131)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fdelete_full_slice.rs#L46)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `del` statements that delete the entire slice of a list or
dictionary.

## [Why is this bad?](#why-is-this-bad)

It is faster and more succinct to remove all items via the `clear()`
method.

## [Known problems](#known-problems)

This rule is prone to false negatives due to type inference limitations,
as it will only detect lists and dictionaries that are instantiated as
literals or annotated with a type annotation.

## [Example](#example)

```
names = {"key": "value"}
nums = [1, 2, 3]

del names[:]
del nums[:]
```

Use instead:

```
names = {"key": "value"}
nums = [1, 2, 3]

names.clear()
nums.clear()
```

## [References](#references)

* [Python documentation: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html?highlight=list#mutable-sequence-types)
* [Python documentation: `dict.clear()`](https://docs.python.org/3/library/stdtypes.html?highlight=list#dict.clear)