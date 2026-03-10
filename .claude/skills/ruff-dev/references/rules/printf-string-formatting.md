# [printf-string-formatting (UP031)](#printf-string-formatting-up031)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27printf-string-formatting%27%20OR%20UP031)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fprintf_string_formatting.rs#L77)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `printf`-style string formatting, and offers to replace it with
`str.format` calls.

## [Why is this bad?](#why-is-this-bad)

`printf`-style string formatting has a number of quirks, and leads to less
readable code than using `str.format` calls or f-strings. In general, prefer
the newer `str.format` and f-strings constructs over `printf`-style string
formatting.

## [Example](#example)

```
"%s, %s" % ("Hello", "World")  # "Hello, World"
```

Use instead:

```
"{}, {}".format("Hello", "World")  # "Hello, World"
```

```
f"{'Hello'}, {'World'}"  # "Hello, World"
```

## [Fix safety](#fix-safety)

In cases where the format string contains a single generic format specifier
(e.g. `%s`), and the right-hand side is an ambiguous expression,
we cannot offer a safe fix.

For example, given:

```
"%s" % val
```

`val` could be a single-element tuple, *or* a single value (not
contained in a tuple). Both of these would resolve to the same
formatted string when using `printf`-style formatting, but
resolve differently when using f-strings:

```
val = 1
print("%s" % val)  # "1"
print("{}".format(val))  # "1"

val = (1,)
print("%s" % val)  # "1"
print("{}".format(val))  # "(1,)"
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)