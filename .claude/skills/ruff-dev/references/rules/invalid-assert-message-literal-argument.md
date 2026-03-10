# [invalid-assert-message-literal-argument (RUF040)](#invalid-assert-message-literal-argument-ruf040)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-assert-message-literal-argument%27%20OR%20RUF040)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Finvalid_assert_message_literal_argument.rs#L28)

## [What it does](#what-it-does)

Checks for invalid use of literals in assert message arguments.

## [Why is this bad?](#why-is-this-bad)

An assert message which is a non-string literal was likely intended
to be used in a comparison assertion, rather than as a message.

## [Example](#example)

```
fruits = ["apples", "plums", "pears"]
fruits.filter(lambda fruit: fruit.startwith("p"))
assert len(fruits), 2  # True unless the list is empty
```

Use instead:

```
fruits = ["apples", "plums", "pears"]
fruits.filter(lambda fruit: fruit.startwith("p"))
assert len(fruits) == 2
```