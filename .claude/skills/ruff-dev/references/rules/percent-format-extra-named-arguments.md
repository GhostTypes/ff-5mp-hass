# [percent-format-extra-named-arguments (F504)](#percent-format-extra-named-arguments-f504)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-extra-named-arguments%27%20OR%20F504)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L158)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unused mapping keys in `printf`-style format strings.

## [Why is this bad?](#why-is-this-bad)

Unused named placeholders in `printf`-style format strings are unnecessary,
and likely indicative of a mistake. They should be removed.

## [Example](#example)

```
"Hello, %(name)s" % {"greeting": "Hello", "name": "World"}
```

Use instead:

```
"Hello, %(name)s" % {"name": "World"}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for mapping key
containing function calls with potential side effects,
because removing such arguments could change the behavior of the code.

For example, the fix would be marked as unsafe in the following case:

```
"Hello, %(name)s" % {"greeting": print(1), "name": "World"}
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)