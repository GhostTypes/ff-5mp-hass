# [property-without-return (RUF066)](#property-without-return-ruf066)

Preview (since [0.14.7](https://github.com/astral-sh/ruff/releases/tag/0.14.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27property-without-return%27%20OR%20RUF066)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fproperty_without_return.rs#L34)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Detects class `@property` methods that does not have a `return` statement.

## [Why is this bad?](#why-is-this-bad)

Property methods are expected to return a computed value, a missing return in a property usually indicates an implementation mistake.

## [Example](#example)

```
class User:
    @property
    def full_name(self):
        f"{self.first_name} {self.last_name}"
```

Use instead:

```
class User:
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

## [References](#references)

* [Python documentation: The property class](https://docs.python.org/3/library/functions.html#property)