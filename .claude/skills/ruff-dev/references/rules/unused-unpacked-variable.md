# [unused-unpacked-variable (RUF059)](#unused-unpacked-variable-ruf059)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-unpacked-variable%27%20OR%20RUF059)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funused_unpacked_variable.rs#L48)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of unused variables in unpacked assignments.

## [Why is this bad?](#why-is-this-bad)

A variable that is defined but never used can confuse readers.

If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
[`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) pattern.

## [Example](#example)

```
def get_pair():
    return 1, 2


def foo():
    x, y = get_pair()
    return x
```

Use instead:

```
def foo():
    x, _ = get_pair()
    return x
```

## [See also](#see-also)

This rule applies only to unpacked assignments. For regular assignments, see
[`unused-variable`](https://docs.astral.sh/ruff/rules/unused-variable/).

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)