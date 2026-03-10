# [print-empty-string (FURB105)](#print-empty-string-furb105)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27print-empty-string%27%20OR%20FURB105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fprint_empty_string.rs#L40)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `print` calls with unnecessary empty strings as positional
arguments and unnecessary `sep` keyword arguments.

## [Why is this bad?](#why-is-this-bad)

Prefer calling `print` without any positional arguments, which is
equivalent and more concise.

Similarly, when printing one or fewer items, the `sep` keyword argument,
(used to define the string that separates the `print` arguments) can be
omitted, as it's redundant when there are no items to separate.

## [Example](#example)

```
print("")
```

Use instead:

```
print()
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe if it removes an unused `sep` keyword argument
that may have side effects. Removing such arguments may change the program's
behavior by skipping the execution of those side effects.

## [References](#references)

* [Python documentation: `print`](https://docs.python.org/3/library/functions.html#print)