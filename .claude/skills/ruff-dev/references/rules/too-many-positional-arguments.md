# [too-many-positional-arguments (PLR0917)](#too-many-positional-arguments-plr0917)

Preview (since [v0.1.7](https://github.com/astral-sh/ruff/releases/tag/v0.1.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-positional-arguments%27%20OR%20PLR0917)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_positional_arguments.rs#L56)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for function definitions that include too many positional arguments.

By default, this rule allows up to five arguments, as configured by the
[`lint.pylint.max-positional-args`](../../settings/#lint_pylint_max-positional-args) option.

## [Why is this bad?](#why-is-this-bad)

Functions with many arguments are harder to understand, maintain, and call.
This is especially true for functions with many positional arguments, as
providing arguments positionally is more error-prone and less clear to
readers than providing arguments by name.

Consider refactoring functions with many arguments into smaller functions
with fewer arguments, using objects to group related arguments, or migrating to
[keyword-only arguments](https://docs.python.org/3/tutorial/controlflow.html#special-parameters).

This rule exempts methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override).
Changing the signature of a subclass method may cause type checkers to
complain about a violation of the Liskov Substitution Principle if it
means that the method now incompatibly overrides a method defined on a
superclass. Explicitly decorating an overriding method with `@override`
signals to Ruff that the method is intended to override a superclass
method and that a type checker will enforce that it does so; Ruff
therefore knows that it should not enforce rules about methods having
too many arguments.

## [Example](#example)

```
def plot(x, y, z, color, mark, add_trendline): ...


plot(1, 2, 3, "r", "*", True)
```

Use instead:

```
def plot(x, y, z, *, color, mark, add_trendline): ...


plot(1, 2, 3, color="r", mark="*", add_trendline=True)
```

## [Options](#options)

* [`lint.pylint.max-positional-args`](../../settings/#lint_pylint_max-positional-args)