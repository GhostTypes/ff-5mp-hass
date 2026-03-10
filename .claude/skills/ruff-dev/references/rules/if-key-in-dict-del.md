# [if-key-in-dict-del (RUF051)](#if-key-in-dict-del-ruf051)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-key-in-dict-del%27%20OR%20RUF051)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fif_key_in_dict_del.rs#L32)

Fix is always available.

## [What it does](#what-it-does)

Checks for `if key in dictionary: del dictionary[key]`.

## [Why is this bad?](#why-is-this-bad)

To remove a key-value pair from a dictionary, it's more concise to use `.pop(..., None)`.

## [Example](#example)

```
if key in dictionary:
    del dictionary[key]
```

Use instead:

```
dictionary.pop(key, None)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the if statement contains comments.