# [starmap-zip (RUF058)](#starmap-zip-ruf058)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27starmap-zip%27%20OR%20RUF058)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fstarmap_zip.rs#L43)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `itertools.starmap` calls where the second argument is a `zip` call.

## [Why is this bad?](#why-is-this-bad)

`zip`-ping iterables only to unpack them later from within `starmap` is unnecessary.
For such cases, `map()` should be used instead.

## [Example](#example)

```
from itertools import starmap


starmap(func, zip(a, b))
starmap(func, zip(a, b, strict=True))
```

Use instead:

```
map(func, a, b)
map(func, a, b, strict=True)  # 3.14+
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if the `starmap` or `zip` expressions contain comments that
would be deleted by applying the fix. Otherwise, the fix can be applied safely.

## [Fix availability](#fix-availability)

This rule will emit a diagnostic but not suggest a fix if `map` has been shadowed from its
builtin binding.