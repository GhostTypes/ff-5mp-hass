# [redefined-argument-from-local (PLR1704)](#redefined-argument-from-local-plr1704)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redefined-argument-from-local%27%20OR%20PLR1704)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fredefined_argument_from_local.rs#L35)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for variables defined in `for`, `try`, `with` statements
that redefine function parameters.

## [Why is this bad?](#why-is-this-bad)

Redefined variables can cause unexpected behavior because of overridden function parameters.
If nested functions are declared, an inner function's body can override an outer function's parameters.

## [Example](#example)

```
def show(host_id=10.11):
    for host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, host)
```

Use instead:

```
def show(host_id=10.11):
    for inner_host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, inner_host_id, host)
```

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)

## [References](#references)

* [Pylint documentation](https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/redefined-argument-from-local.html)