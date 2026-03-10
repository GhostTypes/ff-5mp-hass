# [percent-format-positional-count-mismatch (F507)](#percent-format-positional-count-mismatch-f507)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-positional-count-mismatch%27%20OR%20F507)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L271)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `printf`-style format strings that have a mismatch between the
number of positional placeholders and the number of substitution values.

## [Why is this bad?](#why-is-this-bad)

When a `printf`-style format string is provided with too many or too few
substitution values, it will raise a `TypeError` at runtime.

## [Example](#example)

```
"%s, %s" % ("Hello", "world", "!")
```

Use instead:

```
"%s, %s" % ("Hello", "world")
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)