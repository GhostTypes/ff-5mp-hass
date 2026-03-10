# [missing-maxsplit-arg (PLC0207)](#missing-maxsplit-arg-plc0207)

Preview (since [0.11.12](https://github.com/astral-sh/ruff/releases/tag/0.11.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-maxsplit-arg%27%20OR%20PLC0207)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fmissing_maxsplit_arg.rs#L43)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for access to the first or last element of `str.split()` or `str.rsplit()` without
`maxsplit=1`

## [Why is this bad?](#why-is-this-bad)

Calling `str.split()` or `str.rsplit()` without passing `maxsplit=1` splits on every delimiter in the
string. When accessing only the first or last element of the result, it
would be more efficient to only split once.

## [Example](#example)

```
url = "www.example.com"
prefix = url.split(".")[0]
```

Use instead:

```
url = "www.example.com"
prefix = url.split(".", maxsplit=1)[0]
```

To access the last element, use `str.rsplit()` instead of `str.split()`:

```
url = "www.example.com"
suffix = url.rsplit(".", maxsplit=1)[-1]
```

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe for `split()`/`rsplit()` calls that contain `*args` or `**kwargs` arguments, as
adding a `maxsplit` argument to such a call may lead to duplicated arguments.