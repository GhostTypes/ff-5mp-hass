# [ambiguous-unicode-character-string (RUF001)](#ambiguous-unicode-character-string-ruf001)

Added in [v0.0.102](https://github.com/astral-sh/ruff/releases/tag/v0.0.102) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ambiguous-unicode-character-string%27%20OR%20RUF001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fambiguous_unicode_character.rs#L48)

## [What it does](#what-it-does)

Checks for ambiguous Unicode characters in strings.

## [Why is this bad?](#why-is-this-bad)

Some Unicode characters are visually similar to ASCII characters, but have
different code points. For example, `GREEK CAPITAL LETTER ALPHA` (`U+0391`)
is visually similar, but not identical, to the ASCII character `A`.

The use of ambiguous Unicode characters can confuse readers, cause subtle
bugs, and even make malicious code look harmless.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag Unicode characters that are
confusable with other, non-preferred Unicode characters. For example, the
spec recommends `GREEK CAPITAL LETTER OMEGA` over `OHM SIGN`.

You can omit characters from being flagged as ambiguous via the
[`lint.allowed-confusables`](../../settings/#lint_allowed-confusables) setting.

## [Example](#example)

```
print("Ηello, world!")  # "Η" is the Greek eta (`U+0397`).
```

Use instead:

```
print("Hello, world!")  # "H" is the Latin capital H (`U+0048`).
```

## [Options](#options)

* [`lint.allowed-confusables`](../../settings/#lint_allowed-confusables)