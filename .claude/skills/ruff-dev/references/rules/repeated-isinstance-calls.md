# [repeated-isinstance-calls (PLR1701)](#repeated-isinstance-calls-plr1701)

Removed (since [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27repeated-isinstance-calls%27%20OR%20PLR1701)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Frepeated_isinstance_calls.rs#L51)

Derived from the **[Pylint](../#pylint-pl)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

Fix is always available.

## [Removed](#removed)

This rule is identical to [SIM101](https://docs.astral.sh/ruff/rules/duplicate-isinstance-call/) which should be used instead.

## [What it does](#what-it-does)

Checks for repeated `isinstance` calls on the same object.

## [Why is this bad?](#why-is-this-bad)

Repeated `isinstance` calls on the same object can be merged into a
single call.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe on Python 3.10 and later, as combining
multiple `isinstance` calls with a binary operator (`|`) will fail at
runtime if any of the operands are themselves tuples.

For example, given `TYPES = (dict, list)`, then
`isinstance(None, TYPES | set | float)` will raise a `TypeError` at runtime,
while `isinstance(None, set | float)` will not.

## [Example](#example)

```
def is_number(x):
    return isinstance(x, int) or isinstance(x, float) or isinstance(x, complex)
```

Use instead:

```
def is_number(x):
    return isinstance(x, (int, float, complex))
```

Or, for Python 3.10 and later:

```
def is_number(x):
    return isinstance(x, int | float | complex)
```

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)