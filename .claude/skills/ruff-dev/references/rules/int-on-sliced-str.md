# [int-on-sliced-str (FURB166)](#int-on-sliced-str-furb166)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27int-on-sliced-str%27%20OR%20FURB166)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fint_on_sliced_str.rs#L50)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `int` with an explicit base in which a string expression
is stripped of its leading prefix (i.e., `0b`, `0o`, or `0x`).

## [Why is this bad?](#why-is-this-bad)

Given an integer string with a prefix (e.g., `0xABC`), Python can automatically
determine the base of the integer by the prefix without needing to specify
it explicitly.

Instead of `int(num[2:], 16)`, use `int(num, 0)`, which will automatically
deduce the base based on the prefix.

## [Example](#example)

```
num = "0xABC"

if num.startswith("0b"):
    i = int(num[2:], 2)
elif num.startswith("0o"):
    i = int(num[2:], 8)
elif num.startswith("0x"):
    i = int(num[2:], 16)

print(i)
```

Use instead:

```
num = "0xABC"

i = int(num, 0)

print(i)
```

## [Fix safety](#fix-safety)

The rule's fix is marked as unsafe, as Ruff cannot guarantee that the
argument to `int` will remain valid when its base is included in the
function call.

## [References](#references)

* [Python documentation: `int`](https://docs.python.org/3/library/functions.html#int)