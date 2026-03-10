# [mutable-fromkeys-value (RUF024)](#mutable-fromkeys-value-ruf024)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mutable-fromkeys-value%27%20OR%20RUF024)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fmutable_fromkeys_value.rs#L51)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for mutable objects passed as a value argument to `dict.fromkeys`.

## [Why is this bad?](#why-is-this-bad)

All values in the dictionary created by the `dict.fromkeys` method
refer to the same instance of the provided object. If that object is
modified, all values are modified, which can lead to unexpected behavior.
For example, if the empty list (`[]`) is provided as the default value,
all values in the dictionary will use the same list; as such, appending to
any one entry will append to all entries.

Instead, use a comprehension to generate a dictionary with distinct
instances of the default value.

## [Example](#example)

```
cities = dict.fromkeys(["UK", "Poland"], [])
cities["UK"].append("London")
cities["Poland"].append("Poznan")
print(cities)  # {'UK': ['London', 'Poznan'], 'Poland': ['London', 'Poznan']}
```

Use instead:

```
cities = {country: [] for country in ["UK", "Poland"]}
cities["UK"].append("London")
cities["Poland"].append("Poznan")
print(cities)  # {'UK': ['London'], 'Poland': ['Poznan']}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as the edit will change the behavior of
the program by using a distinct object for every value in the dictionary,
rather than a shared mutable instance. In some cases, programs may rely on
the previous behavior.

## [References](#references)

* [Python documentation: `dict.fromkeys`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys)