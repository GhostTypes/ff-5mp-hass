# [literal-membership (PLR6201)](#literal-membership-plr6201)

Preview (since [v0.1.1](https://github.com/astral-sh/ruff/releases/tag/v0.1.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27literal-membership%27%20OR%20PLR6201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fliteral_membership.rs#L36)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for membership tests on `list` and `tuple` literals.

## [Why is this bad?](#why-is-this-bad)

When testing for membership in a static sequence, prefer a `set` literal
over a `list` or `tuple`, as Python optimizes `set` membership tests.

## [Example](#example)

```
1 in [1, 2, 3]
```

Use instead:

```
1 in {1, 2, 3}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as the use of a `set` literal will
error at runtime if either the element being tested for membership (the
left-hand side) or any element of the sequence (the right-hand side)
is unhashable (like lists or dictionaries). While Ruff will attempt to
infer the hashability of both sides and skip the fix when it can determine
that either side is unhashable, it may not always be able to do so.

## [References](#references)

* [What’s New In Python 3.2](https://docs.python.org/3/whatsnew/3.2.html#optimizations)