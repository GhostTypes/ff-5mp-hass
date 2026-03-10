# [strip-with-multi-characters (B005)](#strip-with-multi-characters-b005)

Added in [v0.0.106](https://github.com/astral-sh/ruff/releases/tag/v0.0.106) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27strip-with-multi-characters%27%20OR%20B005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fstrip_with_multi_characters.rs#L47)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for uses of multi-character strings in `.strip()`, `.lstrip()`, and
`.rstrip()` calls.

## [Why is this bad?](#why-is-this-bad)

All characters in the call to `.strip()`, `.lstrip()`, or `.rstrip()` are
removed from the leading and trailing ends of the string. If the string
contains multiple characters, the reader may be misled into thinking that
a prefix or suffix is being removed, rather than a set of characters.

In Python 3.9 and later, you can use `str.removeprefix` and
`str.removesuffix` to remove an exact prefix or suffix from a string,
respectively, which should be preferred when possible.

## [Known problems](#known-problems)

As a heuristic, this rule only flags multi-character strings that contain
duplicate characters. This allows usages like `.strip("xyz")`, which
removes all occurrences of the characters `x`, `y`, and `z` from the
leading and trailing ends of the string, but not `.strip("foo")`.

The use of unique, multi-character strings may be intentional and
consistent with the intent of `.strip()`, `.lstrip()`, or `.rstrip()`,
while the use of duplicate-character strings is very likely to be a
mistake.

## [Example](#example)

```
"text.txt".strip(".txt")  # "e"
```

Use instead:

```
"text.txt".removesuffix(".txt")  # "text"
```

## [References](#references)

* [Python documentation: `str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip)