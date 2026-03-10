# [unnecessary-iterable-allocation-for-first-element (RUF015)](#unnecessary-iterable-allocation-for-first-element-ruf015)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-iterable-allocation-for-first-element%27%20OR%20RUF015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_iterable_allocation_for_first_element.rs#L56)

Fix is always available.

## [What it does](#what-it-does)

Checks the following constructs, all of which can be replaced by
`next(iter(...))`:

* `list(...)[0]`
* `tuple(...)[0]`
* `list(i for i in ...)[0]`
* `[i for i in ...][0]`
* `list(...).pop(0)`

## [Why is this bad?](#why-is-this-bad)

Calling e.g. `list(...)` will create a new list of the entire collection,
which can be very expensive for large collections. If you only need the
first element of the collection, you can use `next(...)` or
`next(iter(...)` to lazily fetch the first element. The same is true for
the other constructs.

## [Example](#example)

```
head = list(x)[0]
head = [x * x for x in range(10)][0]
```

Use instead:

```
head = next(iter(x))
head = next(x * x for x in range(10))
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as migrating from (e.g.) `list(...)[0]`
to `next(iter(...))` can change the behavior of your program in two ways:

1. First, all above-mentioned constructs will eagerly evaluate the entire
   collection, while `next(iter(...))` will only evaluate the first
   element. As such, any side effects that occur during iteration will be
   delayed.
2. Second, accessing members of a collection via square bracket notation
   `[0]` or the `pop()` function will raise `IndexError` if the collection
   is empty, while `next(iter(...))` will raise `StopIteration`.

## [References](#references)

* [Iterators and Iterables in Python: Run Efficient Iterations](https://realpython.com/python-iterators-iterables/#when-to-use-an-iterator-in-python)