# [compare-to-empty-string (PLC1901)](#compare-to-empty-string-plc1901)

Preview (since [v0.0.255](https://github.com/astral-sh/ruff/releases/tag/v0.0.255)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27compare-to-empty-string%27%20OR%20PLC1901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fcompare_to_empty_string.rs#L43)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for comparisons to empty strings.

## [Why is this bad?](#why-is-this-bad)

An empty string is falsy, so it is unnecessary to compare it to `""`. If
the value can be something else Python considers falsy, such as `None`,
`0`, or another empty container, then the code is not equivalent.

## [Known problems](#known-problems)

High false positive rate, as the check is context-insensitive and does not
consider the type of the variable being compared ([#4282](https://github.com/astral-sh/ruff/issues/4282)).

## [Example](#example)

```
x: str = ...

if x == "":
    print("x is empty")
```

Use instead:

```
x: str = ...

if not x:
    print("x is empty")
```

## [References](#references)

* [Python documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)