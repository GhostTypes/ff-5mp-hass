# [if-expr-with-true-false (SIM210)](#if-expr-with-true-false-sim210)

Added in [v0.0.214](https://github.com/astral-sh/ruff/releases/tag/v0.0.214) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-expr-with-true-false%27%20OR%20SIM210)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_ifexp.rs#L39)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` expressions that can be replaced with `bool()` calls.

## [Why is this bad?](#why-is-this-bad)

`if` expressions that evaluate to `True` for a truthy condition an `False`
for a falsey condition can be replaced with `bool()` calls, which are more
concise and readable.

## [Example](#example)

```
True if a else False
```

Use instead:

```
bool(a)
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe because it may change the program’s behavior if the condition does not
return a proper Boolean. While the fix will try to wrap non-boolean values in a call to bool,
custom implementations of comparison functions like `__eq__` can avoid the bool call and still
lead to altered behavior. Moreover, the fix may remove comments.

## [References](#references)

* [Python documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)