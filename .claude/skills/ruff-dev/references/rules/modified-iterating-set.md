# [modified-iterating-set (PLE4703)](#modified-iterating-set-ple4703)

Preview (since [v0.3.5](https://github.com/astral-sh/ruff/releases/tag/v0.3.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27modified-iterating-set%27%20OR%20PLE4703)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fmodified_iterating_set.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for loops in which a `set` is modified during iteration.

## [Why is this bad?](#why-is-this-bad)

If a `set` is modified during iteration, it will cause a `RuntimeError`.

If you need to modify a `set` within a loop, consider iterating over a copy
of the `set` instead.

## [Known problems](#known-problems)

This rule favors false negatives over false positives. Specifically, it
will only detect variables that can be inferred to be a `set` type based on
local type inference, and will only detect modifications that are made
directly on the variable itself (e.g., `set.add()`), as opposed to
modifications within other function calls (e.g., `some_function(set)`).

## [Example](#example)

```
nums = {1, 2, 3}
for num in nums:
    nums.add(num + 5)
```

Use instead:

```
nums = {1, 2, 3}
for num in nums.copy():
    nums.add(num + 5)
```

## [Fix safety](#fix-safety)

This fix is always unsafe because it changes the program’s behavior. Replacing the
original set with a copy during iteration allows code that would previously raise a
`RuntimeError` to run without error.

## [References](#references)

* [Python documentation: `set`](https://docs.python.org/3/library/stdtypes.html#set)