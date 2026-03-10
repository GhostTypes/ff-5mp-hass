# [unnecessary-lambda (PLW0108)](#unnecessary-lambda-plw0108)

Preview (since [v0.1.2](https://github.com/astral-sh/ruff/releases/tag/v0.1.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-lambda%27%20OR%20PLW0108)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funnecessary_lambda.rs#L46)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `lambda` definitions that consist of a single function call
with the same arguments as the `lambda` itself.

## [Why is this bad?](#why-is-this-bad)

When a `lambda` is used to wrap a function call, and merely propagates
the `lambda` arguments to that function, it can typically be replaced with
the function itself, removing a level of indirection.

## [Example](#example)

```
df.apply(lambda x: str(x))
```

Use instead:

```
df.apply(str)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for two primary reasons.

First, the lambda body itself could contain an effect.

For example, replacing `lambda x, y: (func()(x, y))` with `func()` would
lead to a change in behavior, as `func()` would be evaluated eagerly when
defining the lambda, rather than when the lambda is called.

However, even when the lambda body itself is pure, the lambda may
change the argument names, which can lead to a change in behavior when
callers pass arguments by name.

For example, replacing `foo = lambda x, y: func(x, y)` with `foo = func`,
where `func` is defined as `def func(a, b): return a + b`, would be a
breaking change for callers that execute the lambda by passing arguments by
name, as in: `foo(x=1, y=2)`. Since `func` does not define the arguments
`x` and `y`, unlike the lambda, the call would raise a `TypeError`.