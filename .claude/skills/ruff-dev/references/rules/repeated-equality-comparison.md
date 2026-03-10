# [repeated-equality-comparison (PLR1714)](#repeated-equality-comparison-plr1714)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27repeated-equality-comparison%27%20OR%20PLR1714)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Frepeated_equality_comparison.rs#L55)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for repeated equality comparisons that can be rewritten as a membership
test.

This rule will try to determine if the values are hashable
and the fix will use a `set` if they are. If unable to determine, the fix
will use a `tuple` and suggest the use of a `set`.

## [Why is this bad?](#why-is-this-bad)

To check if a variable is equal to one of many values, it is common to
write a series of equality comparisons (e.g.,
`foo == "bar" or foo == "baz"`).

Instead, prefer to combine the values into a collection and use the `in`
operator to check for membership, which is more performant and succinct.
If the items are hashable, use a `set` for efficiency; otherwise, use a
`tuple`.

## [Fix safety](#fix-safety)

This rule is always unsafe since literal sets and tuples
evaluate their members eagerly whereas `or` comparisons
are short-circuited. It is therefore possible that a fix
will change behavior in the presence of side-effects.

## [Example](#example)

```
foo == "bar" or foo == "baz" or foo == "qux"
```

Use instead:

```
foo in {"bar", "baz", "qux"}
```

## [References](#references)

* [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
* [Python documentation: Membership test operations](https://docs.python.org/3/reference/expressions.html#membership-test-operations)
* [Python documentation: `set`](https://docs.python.org/3/library/stdtypes.html#set)