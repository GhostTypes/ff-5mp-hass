# [magic-value-comparison (PLR2004)](#magic-value-comparison-plr2004)

Added in [v0.0.221](https://github.com/astral-sh/ruff/releases/tag/v0.0.221) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27magic-value-comparison%27%20OR%20PLR2004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fmagic_value_comparison.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for the use of unnamed numerical constants ("magic") values in
comparisons.

## [Why is this bad?](#why-is-this-bad)

The use of "magic" values can make code harder to read and maintain, as
readers will have to infer the meaning of the value from the context.
Such values are discouraged by [PEP 8](https://peps.python.org/pep-0008/#constants).

For convenience, this rule excludes a variety of common values from the
"magic" value definition, such as `0`, `1`, `""`, and `"__main__"`.

## [Example](#example)

```
def apply_discount(price: float) -> float:
    if price <= 100:
        return price / 2
    else:
        return price
```

Use instead:

```
MAX_DISCOUNT = 100


def apply_discount(price: float) -> float:
    if price <= MAX_DISCOUNT:
        return price / 2
    else:
        return price
```

## [Options](#options)

* [`lint.pylint.allow-magic-value-types`](../../settings/#lint_pylint_allow-magic-value-types)