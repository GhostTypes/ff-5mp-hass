# [enumerate-for-loop (SIM113)](#enumerate-for-loop-sim113)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27enumerate-for-loop%27%20OR%20SIM113)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fenumerate_for_loop.rs#L45)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

## [What it does](#what-it-does)

Checks for `for` loops with explicit loop-index variables that can be replaced
with `enumerate()`.

In [preview](https://docs.astral.sh/ruff/preview/), this rule checks for index variables initialized with any integer rather than only
a literal zero.

## [Why is this bad?](#why-is-this-bad)

When iterating over a sequence, it's often desirable to keep track of the
index of each element alongside the element itself. Prefer the `enumerate`
builtin over manually incrementing a counter variable within the loop, as
`enumerate` is more concise and idiomatic.

## [Example](#example)

```
fruits = ["apple", "banana", "cherry"]
i = 0
for fruit in fruits:
    print(f"{i + 1}. {fruit}")
    i += 1
```

Use instead:

```
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")
```

## [References](#references)

* [Python documentation: `enumerate`](https://docs.python.org/3/library/functions.html#enumerate)