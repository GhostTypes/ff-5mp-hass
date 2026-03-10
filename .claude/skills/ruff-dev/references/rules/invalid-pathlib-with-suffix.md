# [invalid-pathlib-with-suffix (PTH210)](#invalid-pathlib-with-suffix-pth210)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-pathlib-with-suffix%27%20OR%20PTH210)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Finvalid_pathlib_with_suffix.rs#L59)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `pathlib.Path.with_suffix()` calls where
the given suffix does not have a leading dot
or the given suffix is a single dot `"."` and the
Python version is less than 3.14.

## [Why is this bad?](#why-is-this-bad)

`Path.with_suffix()` will raise an error at runtime
if the given suffix is not prefixed with a dot
or, in versions prior to Python 3.14, if it is a single dot `"."`.

## [Example](#example)

```
from pathlib import Path

path = Path()

path.with_suffix("py")
```

Use instead:

```
from pathlib import Path

path = Path()

path.with_suffix(".py")
```

## [Known problems](#known-problems)

This rule is likely to have false negatives, as Ruff can only emit the
lint if it can say for sure that a binding refers to a `Path` object at
runtime. Due to type inference limitations, Ruff is currently only
confident about this if it can see that the binding originates from a
function parameter annotated with `Path` or from a direct assignment to a
`Path()` constructor call.

## [Fix safety](#fix-safety)

The fix for this rule adds a leading period to the string passed
to the `with_suffix()` call. This fix is marked as unsafe, as it
changes runtime behaviour: the call would previously always have
raised an exception, but no longer will.

Moreover, it's impossible to determine if this is the correct fix
for a given situation (it's possible that the string was correct
but was being passed to the wrong method entirely, for example).

No fix is offered if the suffix `"."` is given, since the intent is unclear.