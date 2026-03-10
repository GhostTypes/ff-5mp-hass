# [invalid-index-type (RUF016)](#invalid-index-type-ruf016)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-index-type%27%20OR%20RUF016)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Finvalid_index_type.rs#L28)

## [What it does](#what-it-does)

Checks for indexed access to lists, strings, tuples, bytes, and comprehensions
using a type other than an integer or slice.

## [Why is this bad?](#why-is-this-bad)

Only integers or slices can be used as indices to these types. Using
other types will result in a `TypeError` at runtime and a `SyntaxWarning` at
import time.

## [Example](#example)

```
var = [1, 2, 3]["x"]
```

Use instead:

```
var = [1, 2, 3][0]
```