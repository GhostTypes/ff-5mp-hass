# [bad-string-format-character (PLE1300)](#bad-string-format-character-ple1300)

Added in [v0.0.283](https://github.com/astral-sh/ruff/releases/tag/v0.0.283) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-string-format-character%27%20OR%20PLE1300)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_string_format_character.rs#L29)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for unsupported format types in format strings.

## [Why is this bad?](#why-is-this-bad)

An invalid format string character will result in an error at runtime.

## [Example](#example)

```
# `z` is not a valid format type.
print("%z" % "1")

print("{:z}".format("1"))
```