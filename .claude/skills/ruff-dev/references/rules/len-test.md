# [len-test (PLC1802)](#len-test-plc1802)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27len-test%27%20OR%20PLC1802)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Flen_test.rs#L61)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `len` calls on sequences in a boolean test context.

## [Why is this bad?](#why-is-this-bad)

Empty sequences are considered false in a boolean context.
You can either remove the call to `len`
or compare the length against a scalar.

## [Example](#example)

```
fruits = ["orange", "apple"]
vegetables = []

if len(fruits):
    print(fruits)

if not len(vegetables):
    print(vegetables)
```

Use instead:

```
fruits = ["orange", "apple"]
vegetables = []

if fruits:
    print(fruits)

if not vegetables:
    print(vegetables)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe when the `len` call includes a comment,
as the comment would be removed.

For example, the fix would be marked as unsafe in the following case:

```
fruits = []
if len(
    fruits  # comment
):
    ...
```

## [References](#references)

[PEP 8: Programming Recommendations](https://peps.python.org/pep-0008/#programming-recommendations)