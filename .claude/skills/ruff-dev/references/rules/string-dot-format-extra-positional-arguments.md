# [string-dot-format-extra-positional-arguments (F523)](#string-dot-format-extra-positional-arguments-f523)

Added in [v0.0.139](https://github.com/astral-sh/ruff/releases/tag/v0.0.139) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-dot-format-extra-positional-arguments%27%20OR%20F523)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L468)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `str.format` calls with unused positional arguments.

## [Why is this bad?](#why-is-this-bad)

Unused positional arguments are redundant, and often indicative of a mistake.
They should be removed.

## [Example](#example)

```
"Hello, {0}".format("world", "!")
```

Use instead:

```
"Hello, {0}".format("world")
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if the unused positional argument
contains a function call with potential side effects,
because removing such arguments could change the behavior of the code.

For example, the fix would be marked as unsafe in the following case:

```
"Hello, {0}".format("world", print(1))
```

## [References](#references)

* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)