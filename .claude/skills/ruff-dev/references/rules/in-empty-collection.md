# [in-empty-collection (RUF060)](#in-empty-collection-ruf060)

Preview (since [0.11.9](https://github.com/astral-sh/ruff/releases/tag/0.11.9)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27in-empty-collection%27%20OR%20RUF060)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fin_empty_collection.rs#L27)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for membership tests on empty collections (such as `list`, `tuple`, `set` or `dict`).

## [Why is this bad?](#why-is-this-bad)

If the collection is always empty, the check is unnecessary, and can be removed.

## [Example](#example)

```
if 1 not in set():
    print("got it!")
```

Use instead:

```
print("got it!")
```