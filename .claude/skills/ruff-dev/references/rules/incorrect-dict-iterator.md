# [incorrect-dict-iterator (PERF102)](#incorrect-dict-iterator-perf102)

Added in [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27incorrect-dict-iterator%27%20OR%20PERF102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fperflint%2Frules%2Fincorrect_dict_iterator.rs#L46)

Derived from the **[Perflint](../#perflint-perf)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `dict.items()` that discard either the key or the value
when iterating over the dictionary.

## [Why is this bad?](#why-is-this-bad)

If you only need the keys or values of a dictionary, you should use
`dict.keys()` or `dict.values()` respectively, instead of `dict.items()`.
These specialized methods are more efficient than `dict.items()`, as they
avoid allocating tuples for every item in the dictionary. They also
communicate the intent of the code more clearly.

Note that, as with all `perflint` rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.

## [Example](#example)

```
obj = {"a": 1, "b": 2}
for key, value in obj.items():
    print(value)
```

Use instead:

```
obj = {"a": 1, "b": 2}
for value in obj.values():
    print(value)
```

## [Fix safety](#fix-safety)

The fix does not perform any type analysis and, as such, may suggest an
incorrect fix if the object in question does not duck-type as a mapping
(e.g., if it is missing a `.keys()` or `.values()` method, or if those
methods behave differently than they do on standard mapping types).