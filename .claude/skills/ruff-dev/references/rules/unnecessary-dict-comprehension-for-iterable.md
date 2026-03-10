# [unnecessary-dict-comprehension-for-iterable (C420)](#unnecessary-dict-comprehension-for-iterable-c420)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-dict-comprehension-for-iterable%27%20OR%20C420)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_dict_comprehension_for_iterable.rs#L51)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary dict comprehension when creating a dictionary from
an iterable.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a dict comprehension to build a dictionary from
an iterable when the value is static.

Prefer `dict.fromkeys(iterable)` over `{value: None for value in iterable}`,
as `dict.fromkeys` is more readable and efficient.

## [Example](#example)

```
{a: None for a in iterable}
{a: 1 for a in iterable}
```

Use instead:

```
dict.fromkeys(iterable)
dict.fromkeys(iterable, 1)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there's comments inside the dict comprehension,
as comments may be removed.

For example, the fix would be marked as unsafe in the following case:

```
{  # comment 1
    a:  # comment 2
    None  # comment 3
    for a in iterable  # comment 4
}
```

## [References](#references)

* [Python documentation: `dict.fromkeys`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys)