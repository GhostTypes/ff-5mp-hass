# [implicit-cwd (FURB177)](#implicit-cwd-furb177)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-cwd%27%20OR%20FURB177)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fimplicit_cwd.rs#L31)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for current-directory lookups using `Path().resolve()`.

## [Why is this bad?](#why-is-this-bad)

When looking up the current directory, prefer `Path.cwd()` over
`Path().resolve()`, as `Path.cwd()` is more explicit in its intent.

## [Example](#example)

```
from pathlib import Path

cwd = Path().resolve()
```

Use instead:

```
from pathlib import Path

cwd = Path.cwd()
```

## [References](#references)

* [Python documentation: `Path.cwd`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd)