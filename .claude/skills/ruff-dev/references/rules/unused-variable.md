# [unused-variable (F841)](#unused-variable-f841)

Added in [v0.0.22](https://github.com/astral-sh/ruff/releases/tag/v0.0.22) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-variable%27%20OR%20F841)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Funused_variable.rs#L55)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the presence of unused variables in function scopes.

## [Why is this bad?](#why-is-this-bad)

A variable that is defined but not used is likely a mistake, and should
be removed to avoid confusion.

If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
[`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) pattern.

## [Example](#example)

```
def foo():
    x = 1
    y = 2
    return x
```

Use instead:

```
def foo():
    x = 1
    return x
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because removing an unused variable assignment may
delete comments that are attached to the assignment.

## [See also](#see-also)

This rule does not apply to bindings in unpacked assignments (e.g. `x, y = 1, 2`). See
[`unused-unpacked-variable`](https://docs.astral.sh/ruff/rules/unused-unpacked-variable/) for this case.

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)