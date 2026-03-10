# [implicit-string-concatenation-in-collection-literal (ISC004)](#implicit-string-concatenation-in-collection-literal-isc004)

Preview (since [0.14.10](https://github.com/astral-sh/ruff/releases/tag/0.14.10)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-string-concatenation-in-collection-literal%27%20OR%20ISC004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_implicit_str_concat%2Frules%2Fcollection_literal.rs#L53)

Derived from the **[flake8-implicit-str-concat](../#flake8-implicit-str-concat-isc)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for implicitly concatenated strings inside list, tuple, and set literals.

## [Why is this bad?](#why-is-this-bad)

In collection literals, implicit string concatenation is often the result of
a missing comma between elements, which can silently merge items together.

## [Example](#example)

```
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    "Clarinets are made almost entirely out of wood from the mpingo tree."
    "In 1971, astronaut Alan Shepard played golf on the moon.",
)
```

Instead, you likely intended:

```
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    "Clarinets are made almost entirely out of wood from the mpingo tree.",
    "In 1971, astronaut Alan Shepard played golf on the moon.",
)
```

If the concatenation is intentional, wrap it in parentheses to make it
explicit:

```
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    (
        "Clarinets are made almost entirely out of wood from the mpingo tree."
        "In 1971, astronaut Alan Shepard played golf on the moon."
    ),
)
```

## [Fix safety](#fix-safety)

The fix is safe in that it does not change the semantics of your code.
However, the issue is that you may often want to change semantics
by adding a missing comma.