# [needless-else (RUF047)](#needless-else-ruf047)

Preview (since [0.9.3](https://github.com/astral-sh/ruff/releases/tag/0.9.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27needless-else%27%20OR%20RUF047)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fneedless_else.rs#L33)

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `else` clauses that only contains `pass` and `...` statements.

## [Why is this bad?](#why-is-this-bad)

Such an else clause does nothing and can be removed.

## [Example](#example)

```
if foo:
    bar()
else:
    pass
```

Use instead:

```
if foo:
    bar()
```