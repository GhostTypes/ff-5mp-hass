# [multi-line-implicit-string-concatenation (ISC002)](#multi-line-implicit-string-concatenation-isc002)

Added in [v0.0.201](https://github.com/astral-sh/ruff/releases/tag/v0.0.201) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multi-line-implicit-string-concatenation%27%20OR%20ISC002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_implicit_str_concat%2Frules%2Fimplicit.rs#L94)

Derived from the **[flake8-implicit-str-concat](../#flake8-implicit-str-concat-isc)** linter.

## [What it does](#what-it-does)

Checks for implicitly concatenated strings that span multiple lines.

## [Why is this bad?](#why-is-this-bad)

For string literals that wrap across multiple lines, [PEP 8](https://peps.python.org/pep-0008/#maximum-line-length) recommends
the use of implicit string concatenation within parentheses instead of
using a backslash for line continuation, as the former is more readable
than the latter.

By default, this rule will only trigger if the string literal is
concatenated via a backslash. To disallow implicit string concatenation
altogether, set the [`lint.flake8-implicit-str-concat.allow-multiline`](../../settings/#lint_flake8-implicit-str-concat_allow-multiline) option
to `false`.

## [Example](#example)

```
z = "The quick brown fox jumps over the lazy "\
    "dog."
```

Use instead:

```
z = (
    "The quick brown fox jumps over the lazy "
    "dog."
)
```

## [Options](#options)

* [`lint.flake8-implicit-str-concat.allow-multiline`](../../settings/#lint_flake8-implicit-str-concat_allow-multiline)

## [Formatter compatibility](#formatter-compatibility)

Using this rule with `allow-multiline = false` can be incompatible with the
formatter because the [formatter](https://docs.astral.sh/ruff/formatter/) can introduce new multi-line implicitly
concatenated strings. We recommend to either:

* Enable `ISC001` to disallow all implicit concatenated strings
* Setting `allow-multiline = true`