# [format-literals (UP030)](#format-literals-up030)

Added in [v0.0.218](https://github.com/astral-sh/ruff/releases/tag/v0.0.218) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27format-literals%27%20OR%20UP030)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fformat_literals.rs#L49)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary positional indices in format strings.

## [Why is this bad?](#why-is-this-bad)

In Python 3.1 and later, format strings can use implicit positional
references. For example, `"{0}, {1}".format("Hello", "World")` can be
rewritten as `"{}, {}".format("Hello", "World")`.

If the positional indices appear exactly in-order, they can be omitted
in favor of automatic indices to improve readability.

## [Example](#example)

```
"{0}, {1}".format("Hello", "World")  # "Hello, World"
```

Use instead:

```
"{}, {}".format("Hello", "World")  # "Hello, World"
```

This fix is marked as unsafe because:

* Comments attached to arguments are not moved, which can cause comments to mismatch the actual arguments.
* If arguments have side effects (e.g., print), reordering may change program behavior.

## [References](#references)

* [Python documentation: Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)