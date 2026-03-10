# [sorted-min-max (FURB192)](#sorted-min-max-furb192)

Preview (since [v0.4.2](https://github.com/astral-sh/ruff/releases/tag/v0.4.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27sorted-min-max%27%20OR%20FURB192)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fsorted_min_max.rs#L49)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of `sorted()` to retrieve the minimum or maximum value in
a sequence.

## [Why is this bad?](#why-is-this-bad)

Using `sorted()` to compute the minimum or maximum value in a sequence is
inefficient and less readable than using `min()` or `max()` directly.

## [Example](#example)

```
nums = [3, 1, 4, 1, 5]
lowest = sorted(nums)[0]
highest = sorted(nums)[-1]
highest = sorted(nums, reverse=True)[0]
```

Use instead:

```
nums = [3, 1, 4, 1, 5]
lowest = min(nums)
highest = max(nums)
```

## [Fix safety](#fix-safety)

In some cases, migrating to `min` or `max` can lead to a change in behavior,
notably when breaking ties.

As an example, `sorted(data, key=itemgetter(0), reverse=True)[0]` will return
the *last* "minimum" element in the list, if there are multiple elements with
the same key. However, `min(data, key=itemgetter(0))` will return the *first*
"minimum" element in the list in the same scenario.

As such, this rule's fix is marked as unsafe when the `reverse` keyword is used.

## [References](#references)

* [Python documentation: `min`](https://docs.python.org/3/library/functions.html#min)
* [Python documentation: `max`](https://docs.python.org/3/library/functions.html#max)