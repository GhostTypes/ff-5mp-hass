# [verbose-decimal-constructor (FURB157)](#verbose-decimal-constructor-furb157)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27verbose-decimal-constructor%27%20OR%20FURB157)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fverbose_decimal_constructor.rs#L50)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary string literal or float casts in `Decimal`
constructors.

## [Why is this bad?](#why-is-this-bad)

The `Decimal` constructor accepts a variety of arguments, including
integers, floats, and strings. However, it's not necessary to cast
integer literals to strings when passing them to the `Decimal`.

Similarly, `Decimal` accepts `inf`, `-inf`, and `nan` as string literals,
so there's no need to wrap those values in a `float` call when passing
them to the `Decimal` constructor.

Prefer the more concise form of argument passing for `Decimal`
constructors, as it's more readable and idiomatic.

Note that this rule does not flag quoted float literals such as `Decimal("0.1")`, which will
produce a more precise `Decimal` value than the unquoted `Decimal(0.1)`.

## [Example](#example)

```
from decimal import Decimal

Decimal("0")
Decimal(float("Infinity"))
```

Use instead:

```
from decimal import Decimal

Decimal(0)
Decimal("Infinity")
```

## [References](#references)

* [Python documentation: `decimal`](https://docs.python.org/3/library/decimal.html)