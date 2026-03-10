# [string-dot-format-extra-named-arguments (F522)](#string-dot-format-extra-named-arguments-f522)

Added in [v0.0.139](https://github.com/astral-sh/ruff/releases/tag/v0.0.139) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-dot-format-extra-named-arguments%27%20OR%20F522)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L416)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `str.format` calls with unused keyword arguments.

## [Why is this bad?](#why-is-this-bad)

Unused keyword arguments are redundant, and often indicative of a mistake.
They should be removed.

## [Example](#example)

```
"Hello, {name}".format(greeting="Hello", name="World")
```

Use instead:

```
"Hello, {name}".format(name="World")
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if the unused keyword argument
contains a function call with potential side effects,
because removing such arguments could change the behavior of the code.

For example, the fix would be marked as unsafe in the following case:

```
"Hello, {name}".format(greeting=print(1), name="World")
```

## [References](#references)

* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)