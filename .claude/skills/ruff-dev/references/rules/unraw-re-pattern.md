# [unraw-re-pattern (RUF039)](#unraw-re-pattern-ruf039)

Preview (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unraw-re-pattern%27%20OR%20RUF039)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funraw_re_pattern.rs#L61)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Reports the following `re` and `regex` calls when
their first arguments are not raw strings:

* For `regex` and `re`: `compile`, `findall`, `finditer`,
  `fullmatch`, `match`, `search`, `split`, `sub`, `subn`.
* `regex`-specific: `splititer`, `subf`, `subfn`, `template`.

## [Why is this bad?](#why-is-this-bad)

Regular expressions should be written
using raw strings to avoid double escaping.

## [Fix safety](#fix-safety)

The fix is unsafe if the string/bytes literal contains an escape sequence because the fix alters
the runtime value of the literal while retaining the regex semantics.

For example

```
# Literal is `1\n2`.
re.compile("1\n2")

# Literal is `1\\n2`, but the regex library will interpret `\\n` and will still match a newline
# character as before.
re.compile(r"1\n2")
```

## [Fix availability](#fix-availability)

A fix is not available if either

* the argument is a string with a (no-op) `u` prefix (e.g., `u"foo"`) as the prefix is
  incompatible with the raw prefix `r`
* the argument is a string or bytes literal with an escape sequence that has a different
  meaning in the context of a regular expression such as `\b`, which is word boundary or
  backspace in a regex, depending on the context, but always a backspace in string and bytes
  literals.

## [Example](#example)

```
re.compile("foo\\bar")
```

Use instead:

```
re.compile(r"foo\bar")
```