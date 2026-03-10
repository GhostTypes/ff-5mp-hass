# [yield-in-for-loop (UP028)](#yield-in-for-loop-up028)

Added in [v0.0.210](https://github.com/astral-sh/ruff/releases/tag/v0.0.210) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27yield-in-for-loop%27%20OR%20UP028)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fyield_in_for_loop.rs#L53)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `for` loops that can be replaced with `yield from` expressions.

## [Why is this bad?](#why-is-this-bad)

If a `for` loop only contains a `yield` statement, it can be replaced with a
`yield from` expression, which is more concise and idiomatic.

## [Example](#example)

```
def bar():
    for x in foo:
        yield x

    global y
    for y in foo:
        yield y
```

Use instead:

```
def bar():
    yield from foo

    for _element in foo:
        y = _element
        yield y
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as converting a `for` loop to a `yield from` expression can change the behavior of the program in rare cases.
For example, if a generator is being sent values via `send`, then rewriting
to a `yield from` could lead to an attribute error if the underlying
generator does not implement the `send` method.

Additionally, if at least one target is `global` or `nonlocal`,
no fix will be offered.

In most cases, however, the fix is safe, and such a modification should have
no effect on the behavior of the program.

## [References](#references)

* [Python documentation: The `yield` statement](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
* [PEP 380 – Syntax for Delegating to a Subgenerator](https://peps.python.org/pep-0380/)