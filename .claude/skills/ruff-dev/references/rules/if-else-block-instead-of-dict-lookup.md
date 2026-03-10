# [if-else-block-instead-of-dict-lookup (SIM116)](#if-else-block-instead-of-dict-lookup-sim116)

Added in [v0.0.250](https://github.com/astral-sh/ruff/releases/tag/v0.0.250) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-else-block-instead-of-dict-lookup%27%20OR%20SIM116)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fif_else_block_instead_of_dict_lookup.rs#L38)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

## [What it does](#what-it-does)

Checks for three or more consecutive if-statements with direct returns

## [Why is this bad?](#why-is-this-bad)

These can be simplified by using a dictionary

## [Example](#example)

```
def find_phrase(x):
    if x == 1:
        return "Hello"
    elif x == 2:
        return "Goodbye"
    elif x == 3:
        return "Good morning"
    else:
        return "Goodnight"
```

Use instead:

```
def find_phrase(x):
    phrases = {1: "Hello", 2: "Goodye", 3: "Good morning"}
    return phrases.get(x, "Goodnight")
```