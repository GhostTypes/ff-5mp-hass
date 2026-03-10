# [multiple-starts-ends-with (PIE810)](#multiple-starts-ends-with-pie810)

Added in [v0.0.243](https://github.com/astral-sh/ruff/releases/tag/v0.0.243) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-starts-ends-with%27%20OR%20PIE810)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Fmultiple_starts_ends_with.rs#L51)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `startswith` or `endswith` calls on the same value with
different prefixes or suffixes.

## [Why is this bad?](#why-is-this-bad)

The `startswith` and `endswith` methods accept tuples of prefixes or
suffixes respectively. Passing a tuple of prefixes or suffixes is more
efficient and readable than calling the method multiple times.

## [Example](#example)

```
msg = "Hello, world!"
if msg.startswith("Hello") or msg.startswith("Hi"):
    print("Greetings!")
```

Use instead:

```
msg = "Hello, world!"
if msg.startswith(("Hello", "Hi")):
    print("Greetings!")
```

## [Fix safety](#fix-safety)

This rule's fix is unsafe, as in some cases, it will be unable to determine
whether the argument to an existing `.startswith` or `.endswith` call is a
tuple. For example, given `msg.startswith(x) or msg.startswith(y)`, if `x`
or `y` is a tuple, and the semantic model is unable to detect it as such,
the rule will suggest `msg.startswith((x, y))`, which will error at
runtime.

## [References](#references)

* [Python documentation: `str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)
* [Python documentation: `str.endswith`](https://docs.python.org/3/library/stdtypes.html#str.endswith)