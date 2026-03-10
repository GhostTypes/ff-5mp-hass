# [percent-format-mixed-positional-and-named (F506)](#percent-format-mixed-positional-and-named-f506)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-mixed-positional-and-named%27%20OR%20F506)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L240)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `printf`-style format strings that have mixed positional and
named placeholders.

## [Why is this bad?](#why-is-this-bad)

Python does not support mixing positional and named placeholders in
`printf`-style format strings. The use of mixed placeholders will raise a
`TypeError` at runtime.

## [Example](#example)

```
"%s, %(name)s" % ("Hello", {"name": "World"})
```

Use instead:

```
"%s, %s" % ("Hello", "World")
```

Or:

```
"%(greeting)s, %(name)s" % {"greeting": "Hello", "name": "World"}
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)