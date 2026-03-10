# [needless-bool (SIM103)](#needless-bool-sim103)

Added in [v0.0.214](https://github.com/astral-sh/ruff/releases/tag/v0.0.214) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27needless-bool%27%20OR%20SIM103)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fneedless_bool.rs#L58)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `if` statements that can be replaced with `bool`.

## [Why is this bad?](#why-is-this-bad)

`if` statements that return `True` for a truthy condition and `False` for
a falsy condition can be replaced with boolean casts.

## [Example](#example)

Given:

```
def foo(x: int) -> bool:
    if x > 0:
        return True
    else:
        return False
```

Use instead:

```
def foo(x: int) -> bool:
    return x > 0
```

Or, given:

```
def foo(x: int) -> bool:
    if x > 0:
        return True
    return False
```

Use instead:

```
def foo(x: int) -> bool:
    return x > 0
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe because it may change the program’s behavior if the condition does not
return a proper Boolean. While the fix will try to wrap non-boolean values in a call to bool,
custom implementations of comparison functions like `__eq__` can avoid the bool call and still
lead to altered behavior.

## [References](#references)

* [Python documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)