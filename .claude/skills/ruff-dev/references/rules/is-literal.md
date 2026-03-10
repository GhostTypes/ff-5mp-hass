# [is-literal (F632)](#is-literal-f632)

Added in [v0.0.39](https://github.com/astral-sh/ruff/releases/tag/v0.0.39) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27is-literal%27%20OR%20F632)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Finvalid_literal_comparisons.rs#L53)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `is` and `is not` comparisons against literals, like integers,
strings, or lists.

## [Why is this bad?](#why-is-this-bad)

The `is` and `is not` comparators operate on identity, in that they check
whether two objects are the same object. If the objects are not the same
object, the comparison will always be `False`. Using `is` and `is not` with
constant literals often works "by accident", but are not guaranteed to produce
the expected result.

As of Python 3.8, using `is` and `is not` with constant literals will produce
a `SyntaxWarning`.

This rule will also flag `is` and `is not` comparisons against non-constant
literals, like lists, sets, and dictionaries. While such comparisons will
not raise a `SyntaxWarning`, they are still likely to be incorrect, as they
will compare the identities of the objects instead of their values, which
will always evaluate to `False`.

Instead, use `==` and `!=` to compare literals, which will compare the
values of the objects instead of their identities.

## [Example](#example)

```
x = 200
if x is 200:
    print("It's 200!")
```

Use instead:

```
x = 200
if x == 200:
    print("It's 200!")
```

## [References](#references)

* [Python documentation: Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)
* [Python documentation: Value comparisons](https://docs.python.org/3/reference/expressions.html#value-comparisons)
* [*Why does Python log a SyntaxWarning for ‘is’ with literals?* by Adam Johnson](https://adamj.eu/tech/2020/01/21/why-does-python-3-8-syntaxwarning-for-is-literal/)