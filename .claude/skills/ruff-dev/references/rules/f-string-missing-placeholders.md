# [f-string-missing-placeholders (F541)](#f-string-missing-placeholders-f541)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27f-string-missing-placeholders%27%20OR%20F541)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Ff_string_missing_placeholders.rs#L56)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for f-strings that do not contain any placeholder expressions.

## [Why is this bad?](#why-is-this-bad)

f-strings are a convenient way to format strings, but they are not
necessary if there are no placeholder expressions to format. In this
case, a regular string should be used instead, as an f-string without
placeholders can be confusing for readers, who may expect such a
placeholder to be present.

An f-string without any placeholders could also indicate that the
author forgot to add a placeholder expression.

## [Example](#example)

```
f"Hello, world!"
```

Use instead:

```
"Hello, world!"
```

**Note:** to maintain compatibility with PyFlakes, this rule only flags
f-strings that are part of an implicit concatenation if *none* of the
f-string segments contain placeholder expressions.

For example:

```
# Will not be flagged.
(
    f"Hello,"
    f" {name}!"
)

# Will be flagged.
(
    f"Hello,"
    f" World!"
)
```

See [#10885](https://github.com/astral-sh/ruff/issues/10885) for more.

## [References](#references)

* [PEP 498 – Literal String Interpolation](https://peps.python.org/pep-0498/)