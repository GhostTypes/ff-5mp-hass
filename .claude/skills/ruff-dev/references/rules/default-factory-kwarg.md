# [default-factory-kwarg (RUF026)](#default-factory-kwarg-ruf026)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27default-factory-kwarg%27%20OR%20RUF026)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fdefault_factory_kwarg.rs#L53)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for incorrect usages of `default_factory` as a keyword argument when
initializing a `defaultdict`.

## [Why is this bad?](#why-is-this-bad)

The `defaultdict` constructor accepts a callable as its first argument.
For example, it's common to initialize a `defaultdict` with `int` or `list`
via `defaultdict(int)` or `defaultdict(list)`, to create a dictionary that
returns `0` or `[]` respectively when a key is missing.

The default factory *must* be provided as a positional argument, as all
keyword arguments to `defaultdict` are interpreted as initial entries in
the dictionary. For example, `defaultdict(foo=1, bar=2)` will create a
dictionary with `{"foo": 1, "bar": 2}` as its initial entries.

As such, `defaultdict(default_factory=list)` will create a dictionary with
`{"default_factory": list}` as its initial entry, instead of a dictionary
that returns `[]` when a key is missing. Specifying a `default_factory`
keyword argument is almost always a mistake, and one that type checkers
can't reliably detect.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as converting `default_factory` from a
keyword to a positional argument will change the behavior of the code, even
if the keyword argument was used erroneously.

## [Example](#example)

```
defaultdict(default_factory=int)
defaultdict(default_factory=list)
```

Use instead:

```
defaultdict(int)
defaultdict(list)
```