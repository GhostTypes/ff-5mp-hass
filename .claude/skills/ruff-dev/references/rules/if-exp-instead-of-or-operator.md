# [if-exp-instead-of-or-operator (FURB110)](#if-exp-instead-of-or-operator-furb110)

Preview (since [v0.3.6](https://github.com/astral-sh/ruff/releases/tag/v0.3.6)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-exp-instead-of-or-operator%27%20OR%20FURB110)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fif_exp_instead_of_or_operator.rs#L40)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for ternary `if` expressions that can be replaced with the `or`
operator.

## [Why is this bad?](#why-is-this-bad)

Ternary `if` expressions are more verbose than `or` expressions while
providing the same functionality.

## [Example](#example)

```
z = x if x else y
```

Use instead:

```
z = x or y
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe in the event that the body of the
`if` expression contains side effects.

For example, `foo` will be called twice in `foo() if foo() else bar()`
(assuming `foo()` returns a truthy value), but only once in
`foo() or bar()`.