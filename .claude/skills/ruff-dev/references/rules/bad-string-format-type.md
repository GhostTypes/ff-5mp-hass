# [bad-string-format-type (PLE1307)](#bad-string-format-type-ple1307)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-string-format-type%27%20OR%20PLE1307)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_string_format_type.rs#L30)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for mismatched argument types in "old-style" format strings.

## [Why is this bad?](#why-is-this-bad)

The format string is not checked at compile time, so it is easy to
introduce bugs by mistyping the format string.

## [Example](#example)

```
print("%d" % "1")
```

Use instead:

```
print("%d" % 1)
```