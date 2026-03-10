# [unicode-kind-prefix (UP025)](#unicode-kind-prefix-up025)

Added in [v0.0.201](https://github.com/astral-sh/ruff/releases/tag/v0.0.201) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unicode-kind-prefix%27%20OR%20UP025)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funicode_kind_prefix.rs#L27)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of the Unicode kind prefix (`u`) in strings.

## [Why is this bad?](#why-is-this-bad)

In Python 3, all strings are Unicode by default. The Unicode kind prefix is
unnecessary and should be removed to avoid confusion.

## [Example](#example)

```
u"foo"
```

Use instead:

```
"foo"
```

## [References](#references)

* [Python documentation: Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)