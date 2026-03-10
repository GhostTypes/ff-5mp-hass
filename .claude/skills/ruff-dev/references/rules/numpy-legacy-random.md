# [numpy-legacy-random (NPY002)](#numpy-legacy-random-npy002)

Added in [v0.0.248](https://github.com/astral-sh/ruff/releases/tag/v0.0.248) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27numpy-legacy-random%27%20OR%20NPY002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fnumpy%2Frules%2Flegacy_random.rs#L48)

## [What it does](#what-it-does)

Checks for the use of legacy `np.random` function calls.

## [Why is this bad?](#why-is-this-bad)

According to the NumPy documentation's [Legacy Random Generation](https://numpy.org/doc/stable/reference/random/legacy.html#legacy):

> The `RandomState` provides access to legacy generators... This class
> should only be used if it is essential to have randoms that are
> identical to what would have been produced by previous versions of
> NumPy.

The members exposed directly on the `random` module are convenience
functions that alias to methods on a global singleton `RandomState`
instance. NumPy recommends using a dedicated `Generator` instance
rather than the random variate generation methods exposed directly on
the `random` module, as the new `Generator` is both faster and has
better statistical properties.

See the documentation on [Random Sampling](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start) and [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html) for further
details.

## [Example](#example)

```
import numpy as np

np.random.seed(1337)
np.random.normal()
```

Use instead:

```
rng = np.random.default_rng(1337)
rng.normal()
```