# [unnecessary-from-float (FURB164)](#unnecessary-from-float-furb164)

Preview (since [v0.3.5](https://github.com/astral-sh/ruff/releases/tag/v0.3.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-from-float%27%20OR%20FURB164)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Funnecessary_from_float.rs#L62)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for unnecessary `from_float` and `from_decimal` usages to construct
`Decimal` and `Fraction` instances.

## [Why is this bad?](#why-is-this-bad)

Since Python 3.2, the `Fraction` and `Decimal` classes can be constructed
by passing float or decimal instances to the constructor directly. As such,
the use of `from_float` and `from_decimal` methods is unnecessary, and
should be avoided in favor of the more concise constructor syntax.

However, there are important behavioral differences between the `from_*` methods
and the constructors:

* The `from_*` methods validate their argument types and raise `TypeError` for invalid types
* The constructors accept broader argument types without validation
* The `from_*` methods have different parameter names than the constructors

## [Example](#example)

```
from decimal import Decimal
from fractions import Fraction

Decimal.from_float(4.2)
Decimal.from_float(float("inf"))
Fraction.from_float(4.2)
Fraction.from_decimal(Decimal("4.2"))
```

Use instead:

```
from decimal import Decimal
from fractions import Fraction

Decimal(4.2)
Decimal("inf")
Fraction(4.2)
Fraction(Decimal("4.2"))
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe by default because:

* The `from_*` methods provide type validation that the constructors don't
* Removing type validation can change program behavior
* The parameter names are different between methods and constructors

The fix is marked as safe only when:

* The argument type is known to be valid for the target constructor
* No keyword arguments are used, or they match the constructor's parameters

## [References](#references)

* [Python documentation: `decimal`](https://docs.python.org/3/library/decimal.html)
* [Python documentation: `fractions`](https://docs.python.org/3/library/fractions.html)