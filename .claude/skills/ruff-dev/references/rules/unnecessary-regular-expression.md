# [unnecessary-regular-expression (RUF055)](#unnecessary-regular-expression-ruf055)

Preview (since [0.8.1](https://github.com/astral-sh/ruff/releases/tag/0.8.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-regular-expression%27%20OR%20RUF055)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_regular_expression.rs#L57)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of the `re` module that can be replaced with builtin `str` methods.

## [Why is this bad?](#why-is-this-bad)

Performing checks on strings directly can make the code simpler, may require
less escaping, and will often be faster.

## [Example](#example)

```
re.sub("abc", "", s)
```

Use instead:

```
s.replace("abc", "")
```

## [Details](#details)

The rule reports the following calls when the first argument to the call is
a plain string literal, and no additional flags are passed:

* `re.sub`
* `re.match`
* `re.search`
* `re.fullmatch`
* `re.split`

For `re.sub`, the `repl` (replacement) argument must also be a string literal,
not a function. For `re.match`, `re.search`, and `re.fullmatch`, the return
value must also be used only for its truth value.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if the affected expression contains comments. Otherwise,
the fix can be applied safely.

## [References](#references)

* [Python Regular Expression HOWTO: Common Problems - Use String Methods](https://docs.python.org/3/howto/regex.html#use-string-methods)