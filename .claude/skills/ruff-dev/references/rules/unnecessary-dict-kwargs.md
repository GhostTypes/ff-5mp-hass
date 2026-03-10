# [unnecessary-dict-kwargs (PIE804)](#unnecessary-dict-kwargs-pie804)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-dict-kwargs%27%20OR%20PIE804)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Funnecessary_dict_kwargs.rs#L72)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary `dict` kwargs.

## [Why is this bad?](#why-is-this-bad)

If the `dict` keys are valid identifiers, they can be passed as keyword
arguments directly, without constructing unnecessary dictionary.
This also makes code more type-safe as type checkers often cannot
precisely verify dynamic keyword arguments.

## [Example](#example)

```
def foo(bar):
    return bar + 1


print(foo(**{"bar": 2}))  # prints 3

# No typing errors, but results in an exception at runtime.
print(foo(**{"bar": 2, "baz": 3}))
```

Use instead:

```
def foo(bar):
    return bar + 1


print(foo(bar=2))  # prints 3

# Typing error detected: No parameter named "baz".
print(foo(bar=2, baz=3))
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for dictionaries with comments interleaved between
the items, as comments may be removed.

For example, the fix would be marked as unsafe in the following case:

```
foo(
    **{
        # comment
        "x": 1.0,
        # comment
        "y": 2.0,
    }
)
```

as this is converted to `foo(x=1.0, y=2.0)` without any of the comments.

## [References](#references)

* [Python documentation: Dictionary displays](https://docs.python.org/3/reference/expressions.html#dictionary-displays)
* [Python documentation: Calls](https://docs.python.org/3/reference/expressions.html#calls)