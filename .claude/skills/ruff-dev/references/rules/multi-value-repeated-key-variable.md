# [multi-value-repeated-key-variable (F602)](#multi-value-repeated-key-variable-f602)

Added in [v0.0.30](https://github.com/astral-sh/ruff/releases/tag/v0.0.30) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multi-value-repeated-key-variable%27%20OR%20F602)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Frepeated_keys.rs#L124)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for dictionary keys that are repeated with different values.

## [Why is this bad?](#why-is-this-bad)

Dictionary keys should be unique. If a key is repeated with a different
value, the first values will be overwritten and the key will correspond to
the last value. This is likely a mistake.

## [Example](#example)

```
foo = {
    bar: 1,
    baz: 2,
    baz: 3,
}
foo[baz]  # 3
```

Use instead:

```
foo = {
    bar: 1,
    baz: 2,
}
foo[baz]  # 2
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because removing a repeated dictionary key
may delete comments that are attached to the removed key-value pair. This can also change
the program's behavior if the value expressions have side effects.

## [References](#references)

* [Python documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)