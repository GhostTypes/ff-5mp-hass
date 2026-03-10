# [if-else-block-instead-of-dict-get (SIM401)](#if-else-block-instead-of-dict-get-sim401)

Added in [v0.0.219](https://github.com/astral-sh/ruff/releases/tag/v0.0.219) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-else-block-instead-of-dict-get%27%20OR%20SIM401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fif_else_block_instead_of_dict_get.rs#L55)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` statements that can be replaced with `dict.get` calls.

## [Why is this bad?](#why-is-this-bad)

`dict.get()` calls can be used to replace `if` statements that assign a
value to a variable in both branches, falling back to a default value if
the key is not found. When possible, using `dict.get` is more concise and
more idiomatic.

Under [preview mode](https://docs.astral.sh/ruff/preview), this rule will
also suggest replacing `if`-`else` *expressions* with `dict.get` calls.

## [Example](#example)

```
foo = {}
if "bar" in foo:
    value = foo["bar"]
else:
    value = 0
```

Use instead:

```
foo = {}
value = foo.get("bar", 0)
```

If preview mode is enabled:

```
value = foo["bar"] if "bar" in foo else 0
```

Use instead:

```
value = foo.get("bar", 0)
```

## [References](#references)

* [Python documentation: Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)