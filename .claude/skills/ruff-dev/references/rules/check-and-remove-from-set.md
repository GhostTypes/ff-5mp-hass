# [check-and-remove-from-set (FURB132)](#check-and-remove-from-set-furb132)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27check-and-remove-from-set%27%20OR%20FURB132)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fcheck_and_remove_from_set.rs#L42)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `set.remove` that can be replaced with `set.discard`.

## [Why is this bad?](#why-is-this-bad)

If an element should be removed from a set if it is present, it is more
succinct and idiomatic to use `discard`.

## [Known problems](#known-problems)

This rule is prone to false negatives due to type inference limitations,
as it will only detect sets that are instantiated as literals or annotated
with a type annotation.

## [Example](#example)

```
nums = {123, 456}

if 123 in nums:
    nums.remove(123)
```

Use instead:

```
nums = {123, 456}

nums.discard(123)
```

## [References](#references)

* [Python documentation: `set.discard()`](https://docs.python.org/3/library/stdtypes.html?highlight=list#frozenset.discard)