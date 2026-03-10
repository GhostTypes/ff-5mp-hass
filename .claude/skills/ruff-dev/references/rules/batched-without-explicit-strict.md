# [batched-without-explicit-strict (B911)](#batched-without-explicit-strict-b911)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27batched-without-explicit-strict%27%20OR%20B911)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fbatched_without_explicit_strict.rs#L51)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `itertools.batched` calls without an explicit `strict` parameter.

## [Why is this bad?](#why-is-this-bad)

By default, if the length of the iterable is not divisible by
the second argument to `itertools.batched`, the last batch
will be shorter than the rest.

In Python 3.13, a `strict` parameter was added which allows controlling if the batches must be of uniform length.
Pass `strict=True` to raise a `ValueError` if the batches are of non-uniform length.
Otherwise, pass `strict=False` to make the intention explicit.

## [Example](#example)

```
import itertools

itertools.batched(iterable, n)
```

Use instead if the batches must be of uniform length:

```
import itertools

itertools.batched(iterable, n, strict=True)
```

Or if the batches can be of non-uniform length:

```
import itertools

itertools.batched(iterable, n, strict=False)
```

## [Known deviations](#known-deviations)

Unlike the upstream `B911`, this rule will not report infinite iterators
(e.g., `itertools.cycle(...)`).

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `batched`](https://docs.python.org/3/library/itertools.html#batched)