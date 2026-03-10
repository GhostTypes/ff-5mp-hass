# [unused-async (RUF029)](#unused-async-ruf029)

Preview (since [v0.4.0](https://github.com/astral-sh/ruff/releases/tag/v0.4.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-async%27%20OR%20RUF029)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funused_async.rs#L33)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for functions declared `async` that do not await or otherwise use features requiring the
function to be declared `async`.

## [Why is this bad?](#why-is-this-bad)

Declaring a function `async` when it's not is usually a mistake, and will artificially limit the
contexts where that function may be called. In some cases, labeling a function `async` is
semantically meaningful (e.g. with the trio library).

## [Example](#example)

```
async def foo():
    bar()
```

Use instead:

```
def foo():
    bar()
```