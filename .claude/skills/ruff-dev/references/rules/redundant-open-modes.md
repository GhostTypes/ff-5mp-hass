# [redundant-open-modes (UP015)](#redundant-open-modes-up015)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-open-modes%27%20OR%20UP015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fredundant_open_modes.rs#L32)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for redundant `open` mode arguments.

## [Why is this bad?](#why-is-this-bad)

Redundant `open` mode arguments are unnecessary and should be removed to
avoid confusion.

## [Example](#example)

```
with open("foo.txt", "r") as f:
    ...
```

Use instead:

```
with open("foo.txt") as f:
    ...
```

## [References](#references)

* [Python documentation: `open`](https://docs.python.org/3/library/functions.html#open)