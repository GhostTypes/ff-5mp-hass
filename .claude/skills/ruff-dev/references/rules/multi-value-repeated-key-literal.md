# [multi-value-repeated-key-literal (F601)](#multi-value-repeated-key-literal-f601)

Added in [v0.0.30](https://github.com/astral-sh/ruff/releases/tag/v0.0.30) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multi-value-repeated-key-literal%27%20OR%20F601)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Frepeated_keys.rs#L51)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for dictionary literals that associate multiple values with the
same key.

## [Why is this bad?](#why-is-this-bad)

Dictionary keys should be unique. If a key is associated with multiple values,
the earlier values will be overwritten. Including multiple values for the
same key in a dictionary literal is likely a mistake.

## [Example](#example)

```
foo = {
    "bar": 1,
    "baz": 2,
    "baz": 3,
}
foo["baz"]  # 3
```

Use instead:

```
foo = {
    "bar": 1,
    "baz": 2,
}
foo["baz"]  # 2
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because removing a repeated dictionary key
may delete comments that are attached to the removed key-value pair. This can also change
the program's behavior if the value expressions have side effects.

## [References](#references)

* [Python documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)