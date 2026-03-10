# [falsy-dict-get-fallback (RUF056)](#falsy-dict-get-fallback-ruf056)

Preview (since [0.8.5](https://github.com/astral-sh/ruff/releases/tag/0.8.5)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27falsy-dict-get-fallback%27%20OR%20RUF056)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Ffalsy_dict_get_fallback.rs#L42)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `dict.get(key, falsy_value)` calls in boolean test positions.

## [Why is this bad?](#why-is-this-bad)

The default fallback `None` is already falsy.

## [Example](#example)

```
if dict.get(key, False):
    ...
```

Use instead:

```
if dict.get(key):
    ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as safe, unless the `dict.get()` call contains comments between
arguments that will be deleted.

## [Fix availability](#fix-availability)

This rule's fix is unavailable in cases where invalid arguments are provided to `dict.get`. As
shown in the [documentation](https://docs.python.org/3.13/library/stdtypes.html#dict.get), `dict.get` takes two positional-only arguments, so invalid cases
are identified by the presence of more than two arguments or any keyword arguments.