# [percent-format-expected-mapping (F502)](#percent-format-expected-mapping-f502)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-expected-mapping%27%20OR%20F502)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L81)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for named placeholders in `printf`-style format strings without
mapping-type values.

## [Why is this bad?](#why-is-this-bad)

When using named placeholders in `printf`-style format strings, the values
must be a map type (such as a dictionary). Otherwise, the expression will
raise a `TypeError`.

## [Example](#example)

```
"%(greeting)s, %(name)s" % ("Hello", "World")
```

Use instead:

```
"%(greeting)s, %(name)s" % {"greeting": "Hello", "name": "World"}
```

Or:

```
"%s, %s" % ("Hello", "World")
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)