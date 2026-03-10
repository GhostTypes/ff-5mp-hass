# [unnecessary-generator-set (C401)](#unnecessary-generator-set-c401)

Added in [v0.0.61](https://github.com/astral-sh/ruff/releases/tag/v0.0.61) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-generator-set%27%20OR%20C401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_generator_set.rs#L45)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary generators that can be rewritten as set
comprehensions (or with `set()` directly).

## [Why is this bad?](#why-is-this-bad)

It is unnecessary to use `set` around a generator expression, since
there are equivalent comprehensions for these types. Using a
comprehension is clearer and more idiomatic.

Further, if the comprehension can be removed entirely, as in the case of
`set(x for x in foo)`, it's better to use `set(foo)` directly, since it's
even more direct.

## [Example](#example)

```
set(f(x) for x in foo)
set(x for x in foo)
set((x for x in foo))
```

Use instead:

```
{f(x) for x in foo}
set(foo)
set(foo)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.