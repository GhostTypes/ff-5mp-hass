# [split-static-string (SIM905)](#split-static-string-sim905)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27split-static-string%27%20OR%20SIM905)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fsplit_static_string.rs#L49)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for static `str.split` calls that can be replaced with list literals.

## [Why is this bad?](#why-is-this-bad)

List literals are more readable and do not require the overhead of calling `str.split`.

## [Example](#example)

```
"a,b,c,d".split(",")
```

Use instead:

```
["a", "b", "c", "d"]
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for implicit string concatenations with comments interleaved
between segments, as comments may be removed.

For example, the fix would be marked as unsafe in the following case:

```
(
    "a"  # comment
    ","  # comment
    "b"  # comment
).split(",")
```

as this is converted to `["a", "b"]` without any of the comments.

## [References](#references)

* [Python documentation: `str.split`](https://docs.python.org/3/library/stdtypes.html#str.split)