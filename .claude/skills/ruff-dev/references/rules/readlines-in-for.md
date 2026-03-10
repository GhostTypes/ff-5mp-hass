# [readlines-in-for (FURB129)](#readlines-in-for-furb129)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27readlines-in-for%27%20OR%20FURB129)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Freadlines_in_for.rs#L50)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `readlines()` when iterating over a file line-by-line.

## [Why is this bad?](#why-is-this-bad)

Rather than iterating over all lines in a file by calling `readlines()`,
it's more convenient and performant to iterate over the file object
directly.

## [Example](#example)

```
with open("file.txt") as fp:
    for line in fp.readlines():
        ...
```

Use instead:

```
with open("file.txt") as fp:
    for line in fp:
        ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there's comments in the
`readlines()` call, as comments may be removed.

For example, the fix would be marked as unsafe in the following case:

```
with open("file.txt") as fp:
    for line in (  # comment
        fp.readlines()  # comment
    ):
        ...
```

## [References](#references)

* [Python documentation: `io.IOBase.readlines`](https://docs.python.org/3/library/io.html#io.IOBase.readlines)