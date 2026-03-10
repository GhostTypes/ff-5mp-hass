# [bad-str-strip-call (PLE1310)](#bad-str-strip-call-ple1310)

Added in [v0.0.242](https://github.com/astral-sh/ruff/releases/tag/v0.0.242) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-str-strip-call%27%20OR%20PLE1310)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_str_strip_call.rs#L50)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks duplicate characters in `str.strip` calls.

## [Why is this bad?](#why-is-this-bad)

All characters in `str.strip` calls are removed from both the leading and
trailing ends of the string. Including duplicate characters in the call
is redundant and often indicative of a mistake.

In Python 3.9 and later, you can use `str.removeprefix` and
`str.removesuffix` to remove an exact prefix or suffix from a string,
respectively, which should be preferred when possible.

## [Example](#example)

```
# Evaluates to "foo".
"bar foo baz".strip("bar baz ")
```

Use instead:

```
# Evaluates to "foo".
"bar foo baz".strip("abrz ")  # "foo"
```

Or:

```
# Evaluates to "foo".
"bar foo baz".removeprefix("bar ").removesuffix(" baz")
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `str.strip`](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)