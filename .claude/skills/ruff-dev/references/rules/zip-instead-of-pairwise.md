# [zip-instead-of-pairwise (RUF007)](#zip-instead-of-pairwise-ruf007)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27zip-instead-of-pairwise%27%20OR%20RUF007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fzip_instead_of_pairwise.rs#L42)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for use of `zip()` to iterate over successive pairs of elements.

## [Why is this bad?](#why-is-this-bad)

When iterating over successive pairs of elements, prefer
`itertools.pairwise()` over `zip()`.

`itertools.pairwise()` is more readable and conveys the intent of the code
more clearly.

## [Example](#example)

```
letters = "ABCD"
zip(letters, letters[1:])  # ("A", "B"), ("B", "C"), ("C", "D")
```

Use instead:

```
from itertools import pairwise

letters = "ABCD"
pairwise(letters)  # ("A", "B"), ("B", "C"), ("C", "D")
```

## [Fix safety](#fix-safety)

The fix is always marked unsafe because it assumes that slicing an object
(e.g., `obj[1:]`) produces a value with the same type and iteration behavior
as the original object, which is not guaranteed for user-defined types that
override `__getitem__` without properly handling slices. Moreover, the fix
could delete comments.

## [References](#references)

* [Python documentation: `itertools.pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise)