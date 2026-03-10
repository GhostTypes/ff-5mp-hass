# [percent-format-expected-sequence (F503)](#percent-format-expected-sequence-f503)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-expected-sequence%27%20OR%20F503)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L118)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for uses of mapping-type values in `printf`-style format strings
without named placeholders.

## [Why is this bad?](#why-is-this-bad)

When using mapping-type values (such as `dict`) in `printf`-style format
strings, the keys must be named. Otherwise, the expression will raise a
`TypeError`.

## [Example](#example)

```
"%s, %s" % {"greeting": "Hello", "name": "World"}
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