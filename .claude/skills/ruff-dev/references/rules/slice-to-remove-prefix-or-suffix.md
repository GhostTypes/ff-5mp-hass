# [slice-to-remove-prefix-or-suffix (FURB188)](#slice-to-remove-prefix-or-suffix-furb188)

Added in [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27slice-to-remove-prefix-or-suffix%27%20OR%20FURB188)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fslice_to_remove_prefix_or_suffix.rs#L40)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for code that could be written more idiomatically using
[`str.removeprefix()`](https://docs.python.org/3/library/stdtypes.html#str.removeprefix)
or [`str.removesuffix()`](https://docs.python.org/3/library/stdtypes.html#str.removesuffix).

Specifically, the rule flags code that conditionally removes a prefix or suffix
using a slice operation following an `if` test that uses `str.startswith()` or `str.endswith()`.

The rule is only applied if your project targets Python 3.9 or later.

## [Why is this bad?](#why-is-this-bad)

The methods [`str.removeprefix()`](https://docs.python.org/3/library/stdtypes.html#str.removeprefix)
and [`str.removesuffix()`](https://docs.python.org/3/library/stdtypes.html#str.removesuffix),
introduced in Python 3.9, have the same behavior while being more readable and efficient.

## [Example](#example)

```
def example(filename: str, text: str):
    filename = filename[:-4] if filename.endswith(".txt") else filename

    if text.startswith("pre"):
        text = text[3:]
```

Use instead:

```
def example(filename: str, text: str):
    filename = filename.removesuffix(".txt")
    text = text.removeprefix("pre")
```