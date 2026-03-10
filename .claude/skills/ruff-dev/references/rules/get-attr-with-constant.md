# [get-attr-with-constant (B009)](#get-attr-with-constant-b009)

Added in [v0.0.110](https://github.com/astral-sh/ruff/releases/tag/v0.0.110) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27get-attr-with-constant%27%20OR%20B009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fgetattr_with_constant.rs#L50)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `getattr` that take a constant attribute value as an
argument (e.g., `getattr(obj, "foo")`).

## [Why is this bad?](#why-is-this-bad)

`getattr` is used to access attributes dynamically. If the attribute is
defined as a constant, it is no safer than a typical property access. When
possible, prefer property access over `getattr` calls, as the former is
more concise and idiomatic.

## [Example](#example)

```
getattr(obj, "foo")
```

Use instead:

```
obj.foo
```

## [Fix safety](#fix-safety)

The fix is marked as unsafe for attribute names that are not in NFKC (Normalization Form KC)
normalization. Python normalizes identifiers using NFKC when using attribute access syntax
(e.g., `obj.attr`), but does not normalize string arguments passed to `getattr`. Rewriting
`getattr(obj, "ſ")` to `obj.ſ` would be interpreted as `obj.s` at runtime, changing behavior.

For example, the long s character `"ſ"` normalizes to `"s"` under NFKC, so:

```
# This accesses an attribute with the exact name "ſ" (if it exists)
value = getattr(obj, "ſ")

# But this would normalize to "s" and access a different attribute
obj.ſ  # This is interpreted as obj.s, not obj.ſ
```

## [References](#references)

* [Python documentation: `getattr`](https://docs.python.org/3/library/functions.html#getattr)