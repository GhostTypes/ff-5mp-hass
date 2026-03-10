# [hardcoded-string-charset (FURB156)](#hardcoded-string-charset-furb156)

Preview (since [0.7.0](https://github.com/astral-sh/ruff/releases/tag/0.7.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-string-charset%27%20OR%20FURB156)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fhardcoded_string_charset.rs#L31)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of hardcoded charsets, which are defined in Python string module.

## [Why is this bad?](#why-is-this-bad)

Usage of named charsets from the standard library is more readable and less error-prone.

## [Example](#example)

```
x = "0123456789"
y in "abcdefghijklmnopqrstuvwxyz"
```

Use instead

```
import string

x = string.digits
y in string.ascii_lowercase
```

## [References](#references)

* [Python documentation: String constants](https://docs.python.org/3/library/string.html#string-constants)