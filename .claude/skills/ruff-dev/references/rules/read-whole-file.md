# [read-whole-file (FURB101)](#read-whole-file-furb101)

Preview (since [v0.1.2](https://github.com/astral-sh/ruff/releases/tag/v0.1.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27read-whole-file%27%20OR%20FURB101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fread_whole_file.rs#L43)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of `open` and `read` that can be replaced by `pathlib`
methods, like `Path.read_text` and `Path.read_bytes`.

## [Why is this bad?](#why-is-this-bad)

When reading the entire contents of a file into a variable, it's simpler
and more concise to use `pathlib` methods like `Path.read_text` and
`Path.read_bytes` instead of `open` and `read` calls via `with` statements.

## [Example](#example)

```
with open(filename) as f:
    contents = f.read()
```

Use instead:

```
from pathlib import Path

contents = Path(filename).read_text()
```

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.

## [References](#references)

* [Python documentation: `Path.read_bytes`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes)
* [Python documentation: `Path.read_text`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text)