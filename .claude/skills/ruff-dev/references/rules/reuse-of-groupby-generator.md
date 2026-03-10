# [reuse-of-groupby-generator (B031)](#reuse-of-groupby-generator-b031)

Added in [v0.0.260](https://github.com/astral-sh/ruff/releases/tag/v0.0.260) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27reuse-of-groupby-generator%27%20OR%20B031)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Freuse_of_groupby_generator.rs#L36)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for multiple usage of the generator returned from
`itertools.groupby()`.

## [Why is this bad?](#why-is-this-bad)

Using the generator more than once will do nothing on the second usage.
If that data is needed later, it should be stored as a list.

## [Example:](#example)

```
import itertools

for name, group in itertools.groupby(data):
    for _ in range(5):
        do_something_with_the_group(group)
```

Use instead:

```
import itertools

for name, group in itertools.groupby(data):
    values = list(group)
    for _ in range(5):
        do_something_with_the_group(values)
```