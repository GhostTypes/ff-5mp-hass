# [used-dummy-variable (RUF052)](#used-dummy-variable-ruf052)

Preview (since [0.8.2](https://github.com/astral-sh/ruff/releases/tag/0.8.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27used-dummy-variable%27%20OR%20RUF052)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fused_dummy_variable.rs#L70)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for "dummy variables" (variables that are named as if to indicate they are unused)
that are in fact used.

By default, "dummy variables" are any variables with names that start with leading
underscores. However, this is customisable using the [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) setting).

## [Why is this bad?](#why-is-this-bad)

Marking a variable with a leading underscore conveys that it is intentionally unused within the function or method.
When these variables are later referenced in the code, it causes confusion and potential misunderstandings about
the code's intention. If a variable marked as "unused" is subsequently used, it suggests that either the variable
could be given a clearer name, or that the code is accidentally making use of the wrong variable.

Sometimes leading underscores are used to avoid variables shadowing other variables, Python builtins, or Python
keywords. However, [PEP 8](https://peps.python.org/pep-0008/) recommends to use trailing underscores for this rather than leading underscores.

Dunder variables are ignored by this rule, as are variables named `_`.
Only local variables in function scopes are flagged by the rule.

## [Example](#example)

```
def function():
    _variable = 3
    # important: avoid shadowing the builtin `id()` function!
    _id = 4
    return _variable + _id
```

Use instead:

```
def function():
    variable = 3
    # important: avoid shadowing the builtin `id()` function!
    id_ = 4
    return variable + id_
```

## [Fix availability](#fix-availability)

The rule's fix is only available for variables that start with leading underscores.
It will also only be available if the "obvious" new name for the variable
would not shadow any other known variables already accessible from the scope
in which the variable is defined.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe.

For this rule's fix, Ruff renames the variable and fixes up all known references to
it so they point to the renamed variable. However, some renamings also require other
changes such as different arguments to constructor calls or alterations to comments.
Ruff is aware of some of these cases: `_T = TypeVar("_T")` will be fixed to
`T = TypeVar("T")` if the `_T` binding is flagged by this rule. However, in general,
cases like these are hard to detect and hard to automatically fix.

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)