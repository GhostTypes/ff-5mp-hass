# [bad-open-mode (PLW1501)](#bad-open-mode-plw1501)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-open-mode%27%20OR%20PLW1501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_open_mode.rs#L39)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Check for an invalid `mode` argument in `open` calls.

## [Why is this bad?](#why-is-this-bad)

The `open` function accepts a `mode` argument that specifies how the file
should be opened (e.g., read-only, write-only, append-only, etc.).

Python supports a variety of open modes: `r`, `w`, `a`, and `x`, to control
reading, writing, appending, and creating, respectively, along with
`b` (binary mode), `+` (read and write), and `U` (universal newlines),
the latter of which is only valid alongside `r`. This rule detects both
invalid combinations of modes and invalid characters in the mode string
itself.

## [Example](#example)

```
with open("file", "rwx") as f:
    content = f.read()
```

Use instead:

```
with open("file", "r") as f:
    content = f.read()
```

## [References](#references)

* [Python documentation: `open`](https://docs.python.org/3/library/functions.html#open)