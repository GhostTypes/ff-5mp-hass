# [dict-iter-missing-items (PLE1141)](#dict-iter-missing-items-ple1141)

Preview (since [v0.3.0](https://github.com/astral-sh/ruff/releases/tag/v0.3.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27dict-iter-missing-items%27%20OR%20PLE1141)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fdict_iter_missing_items.rs#L53)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for dictionary unpacking in a for loop without calling `.items()`.

## [Why is this bad?](#why-is-this-bad)

When iterating over a dictionary in a for loop, if a dictionary is unpacked
without calling `.items()`, it could lead to a runtime error if the keys are not
a tuple of two elements.

It is likely that you're looking for an iteration over (key, value) pairs which
can only be achieved when calling `.items()`.

## [Example](#example)

```
data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}

for city, population in data:
    print(f"{city} has population {population}.")
```

Use instead:

```
data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}

for city, population in data.items():
    print(f"{city} has population {population}.")
```

## [Known problems](#known-problems)

If the dictionary key is a tuple, e.g.:

```
d = {(1, 2): 3, (3, 4): 5}
for x, y in d:
    print(x, y)
```

The tuple key is unpacked into `x` and `y` instead of the key and values. This means that
the suggested fix of using `d.items()` would result in different runtime behavior. Ruff
cannot consistently infer the type of a dictionary's keys.

## [Fix safety](#fix-safety)

Due to the known problem with tuple keys, this fix is unsafe.