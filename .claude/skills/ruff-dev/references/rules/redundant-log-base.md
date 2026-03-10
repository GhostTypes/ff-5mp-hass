# [redundant-log-base (FURB163)](#redundant-log-base-furb163)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-log-base%27%20OR%20FURB163)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fredundant_log_base.rs#L53)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `math.log` calls with a redundant base.

## [Why is this bad?](#why-is-this-bad)

The default base of `math.log` is `e`, so specifying it explicitly is
redundant.

Instead of passing 2 or 10 as the base, use `math.log2` or `math.log10`
respectively, as these dedicated variants are typically more accurate
than `math.log`.

## [Example](#example)

```
import math

math.log(4, math.e)
math.log(4, 2)
math.log(4, 10)
```

Use instead:

```
import math

math.log(4)
math.log2(4)
math.log10(4)
```

## [Fix safety](#fix-safety)

This fix is marked unsafe when the argument is a starred expression, as this changes
the call semantics and may raise runtime errors. It is also unsafe if comments are
present within the call, as they will be removed. Additionally, `math.log(x, base)`
and `math.log2(x)` / `math.log10(x)` may differ due to floating-point rounding, so
the fix is also unsafe when making this transformation.

## [References](#references)

* [Python documentation: `math.log`](https://docs.python.org/3/library/math.html#math.log)
* [Python documentation: `math.log2`](https://docs.python.org/3/library/math.html#math.log2)
* [Python documentation: `math.log10`](https://docs.python.org/3/library/math.html#math.log10)
* [Python documentation: `math.e`](https://docs.python.org/3/library/math.html#math.e)