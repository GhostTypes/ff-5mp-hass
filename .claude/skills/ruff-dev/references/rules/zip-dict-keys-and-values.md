# [zip-dict-keys-and-values (SIM911)](#zip-dict-keys-and-values-sim911)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27zip-dict-keys-and-values%27%20OR%20SIM911)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fzip_dict_keys_and_values.rs#L35)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for use of `zip()` to iterate over keys and values of a dictionary at once.

## [Why is this bad?](#why-is-this-bad)

The `dict` type provides an `.items()` method which is faster and more readable.

## [Example](#example)

```
flag_stars = {"USA": 50, "Slovenia": 3, "Panama": 2, "Australia": 6}

for country, stars in zip(flag_stars.keys(), flag_stars.values()):
    print(f"{country}'s flag has {stars} stars.")
```

Use instead:

```
flag_stars = {"USA": 50, "Slovenia": 3, "Panama": 2, "Australia": 6}

for country, stars in flag_stars.items():
    print(f"{country}'s flag has {stars} stars.")
```

## [References](#references)

* [Python documentation: `dict.items`](https://docs.python.org/3/library/stdtypes.html#dict.items)