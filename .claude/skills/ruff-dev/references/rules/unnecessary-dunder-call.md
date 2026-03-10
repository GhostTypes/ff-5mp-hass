# [unnecessary-dunder-call (PLC2801)](#unnecessary-dunder-call-plc2801)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-dunder-call%27%20OR%20PLC2801)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funnecessary_dunder_call.rs#L66)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for explicit use of dunder methods, like `__str__` and `__add__`.

## [Why is this bad?](#why-is-this-bad)

Dunder names are not meant to be called explicitly and, in most cases, can
be replaced with builtins or operators.

## [Fix safety](#fix-safety)

This fix is always unsafe. When replacing dunder method calls with operators
or builtins, the behavior can change in the following ways:

1. Types may implement only a subset of related dunder methods. Calling a
   missing dunder method directly returns `NotImplemented`, but using the
   equivalent operator raises a `TypeError`.

   ```
   class C: pass
   c = C()
   c.__gt__(1)  # before fix: NotImplemented
   c > 1        # after fix: raises TypeError
   ```
2. Instance-assigned dunder methods are ignored by operators and builtins.

   ```
   class C: pass
   c = C()
   c.__bool__ = lambda: False
   c.__bool__() # before fix: False
   bool(c)      # after fix: True
   ```
3. Even with built-in types, behavior can differ.

   ```
   (1).__gt__(1.0)  # before fix: NotImplemented
   1 > 1.0          # after fix: False
   ```

## [Example](#example)

```
three = (3.0).__str__()
twelve = "1".__add__("2")


def is_greater_than_two(x: int) -> bool:
    return x.__gt__(2)
```

Use instead:

```
three = str(3.0)
twelve = "1" + "2"


def is_greater_than_two(x: int) -> bool:
    return x > 2
```