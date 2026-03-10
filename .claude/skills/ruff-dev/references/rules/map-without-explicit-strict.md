# [map-without-explicit-strict (B912)](#map-without-explicit-strict-b912)

Preview (since [0.13.2](https://github.com/astral-sh/ruff/releases/tag/0.13.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27map-without-explicit-strict%27%20OR%20B912)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fmap_without_explicit_strict.rs#L45)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `map` calls without an explicit `strict` parameter when called with two or more iterables, or any starred argument.

This rule applies to Python 3.14 and later, where `map` accepts a `strict` keyword
argument. For details, see: [What’s New in Python 3.14](https://docs.python.org/dev/whatsnew/3.14.html).

## [Why is this bad?](#why-is-this-bad)

By default, if the iterables passed to `map` are of different lengths, the
resulting iterator will be silently truncated to the length of the shortest
iterable. This can lead to subtle bugs.

Pass `strict=True` to raise a `ValueError` if the iterables are of
non-uniform length. Alternatively, if the iterables are deliberately of
different lengths, pass `strict=False` to make the intention explicit.

## [Example](#example)

```
map(f, a, b)
```

Use instead:

```
map(f, a, b, strict=True)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe. While adding `strict=False` preserves
the runtime behavior, it can obscure situations where the iterables are of
unequal length. Ruff prefers to alert users so they can choose the intended
behavior themselves.

## [References](#references)

* [Python documentation: `map`](https://docs.python.org/3/library/functions.html#map)
* [What’s New in Python 3.14](https://docs.python.org/dev/whatsnew/3.14.html)