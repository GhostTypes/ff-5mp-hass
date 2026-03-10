# [builtin-argument-shadowing (A002)](#builtin-argument-shadowing-a002)

Added in [v0.0.48](https://github.com/astral-sh/ruff/releases/tag/v0.0.48) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-argument-shadowing%27%20OR%20A002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_builtins%2Frules%2Fbuiltin_argument_shadowing.rs#L56)

Derived from the **[flake8-builtins](../#flake8-builtins-a)** linter.

## [What it does](#what-it-does)

Checks for function arguments that use the same names as builtins.

## [Why is this bad?](#why-is-this-bad)

Reusing a builtin name for the name of an argument increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the argument for the
builtin and vice versa.

Function definitions decorated with [`@override`](https://docs.python.org/3/library/typing.html#typing.override) or
[`@overload`](https://docs.python.org/3/library/typing.html#typing.overload) are exempt from this rule by default.
Builtins can be marked as exceptions to this rule via the
[`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist) configuration option.

## [Example](#example)

```
def remove_duplicates(list, list2):
    result = set()
    for value in list:
        result.add(value)
    for value in list2:
        result.add(value)
    return list(result)  # TypeError: 'list' object is not callable
```

Use instead:

```
def remove_duplicates(list1, list2):
    result = set()
    for value in list1:
        result.add(value)
    for value in list2:
        result.add(value)
    return list(result)
```

## [Options](#options)

* [`lint.flake8-builtins.ignorelist`](../../settings/#lint_flake8-builtins_ignorelist)

## [References](#references)

* [*Is it bad practice to use a built-in function name as an attribute or method identifier?*](https://stackoverflow.com/questions/9109333/is-it-bad-practice-to-use-a-built-in-function-name-as-an-attribute-or-method-ide)
* [*Why is it a bad idea to name a variable `id` in Python?*](https://stackoverflow.com/questions/77552/id-is-a-bad-variable-name-in-python)