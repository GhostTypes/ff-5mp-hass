# [percent-format-invalid-format (F501)](#percent-format-invalid-format-f501)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-invalid-format%27%20OR%20F501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L41)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for invalid `printf`-style format strings.

## [Why is this bad?](#why-is-this-bad)

Conversion specifiers are required for `printf`-style format strings. These
specifiers must contain a `%` character followed by a conversion type.

## [Example](#example)

```
"Hello, %" % "world"
```

Use instead:

```
"Hello, %s" % "world"
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)