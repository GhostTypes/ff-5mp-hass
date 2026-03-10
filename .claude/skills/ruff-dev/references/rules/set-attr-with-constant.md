# [set-attr-with-constant (B010)](#set-attr-with-constant-b010)

Added in [v0.0.111](https://github.com/astral-sh/ruff/releases/tag/v0.0.111) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27set-attr-with-constant%27%20OR%20B010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fsetattr_with_constant.rs#L51)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `setattr` that take a constant attribute value as an
argument (e.g., `setattr(obj, "foo", 42)`).

## [Why is this bad?](#why-is-this-bad)

`setattr` is used to set attributes dynamically. If the attribute is
defined as a constant, it is no safer than a typical property access. When
possible, prefer property access over `setattr` calls, as the former is
more concise and idiomatic.

## [Example](#example)

```
setattr(obj, "foo", 42)
```

Use instead:

```
obj.foo = 42
```

## [Fix safety](#fix-safety)

The fix is marked as unsafe for attribute names that are not in NFKC (Normalization Form KC)
normalization. Python normalizes identifiers using NFKC when using attribute access syntax
(e.g., `obj.attr = value`), but does not normalize string arguments passed to `setattr`.
Rewriting `setattr(obj, "ſ", 1)` to `obj.ſ = 1` would be interpreted as `obj.s = 1` at
runtime, changing behavior.

For example, the long s character `"ſ"` normalizes to `"s"` under NFKC, so:

```
# This creates an attribute with the exact name "ſ"
setattr(obj, "ſ", 1)
getattr(obj, "ſ")  # Returns 1

# But this would normalize to "s" and set a different attribute
obj.ſ = 1  # This is interpreted as obj.s = 1, not obj.ſ = 1
```

## [References](#references)

* [Python documentation: `setattr`](https://docs.python.org/3/library/functions.html#setattr)