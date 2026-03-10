# [zip-without-explicit-strict (B905)](#zip-without-explicit-strict-b905)

Added in [v0.0.167](https://github.com/astral-sh/ruff/releases/tag/v0.0.167) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27zip-without-explicit-strict%27%20OR%20B905)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fzip_without_explicit_strict.rs#L41)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `zip` calls without an explicit `strict` parameter when called with two or more iterables, or any starred argument.

## [Why is this bad?](#why-is-this-bad)

By default, if the iterables passed to `zip` are of different lengths, the
resulting iterator will be silently truncated to the length of the shortest
iterable. This can lead to subtle bugs.

Pass `strict=True` to raise a `ValueError` if the iterables are of
non-uniform length. Alternatively, if the iterables are deliberately of
different lengths, pass `strict=False` to make the intention explicit.

## [Example](#example)

```
zip(a, b)
```

Use instead:

```
zip(a, b, strict=True)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe. While adding `strict=False` preserves
the runtime behavior, it can obscure situations where the iterables are of
unequal length. Ruff prefers to alert users so they can choose the intended
behavior themselves.

## [References](#references)

* [Python documentation: `zip`](https://docs.python.org/3/library/functions.html#zip)