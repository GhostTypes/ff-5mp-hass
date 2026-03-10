# [explicit-f-string-type-conversion (RUF010)](#explicit-f-string-type-conversion-ruf010)

Added in [v0.0.267](https://github.com/astral-sh/ruff/releases/tag/v0.0.267) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27explicit-f-string-type-conversion%27%20OR%20RUF010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fexplicit_f_string_type_conversion.rs#L42)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `str()`, `repr()`, and `ascii()` as explicit type
conversions within f-strings.

## [Why is this bad?](#why-is-this-bad)

f-strings support dedicated conversion flags for these types, which are
more succinct and idiomatic.

Note that, in many cases, calling `str()` within an f-string is
unnecessary and can be removed entirely, as the value will be converted
to a string automatically, the notable exception being for classes that
implement a custom `__format__` method.

## [Example](#example)

```
a = "some string"
f"{repr(a)}"
```

Use instead:

```
a = "some string"
f"{a!r}"
```