# [percent-format-star-requires-sequence (F508)](#percent-format-star-requires-sequence-f508)

Added in [v0.0.142](https://github.com/astral-sh/ruff/releases/tag/v0.0.142) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27percent-format-star-requires-sequence%27%20OR%20F508)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L310)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `printf`-style format strings that use the `*` specifier with
non-tuple values.

## [Why is this bad?](#why-is-this-bad)

The use of the `*` specifier with non-tuple values will raise a
`TypeError` at runtime.

## [Example](#example)

```
from math import pi

"%(n).*f" % {"n": (2, pi)}
```

Use instead:

```
from math import pi

"%.*f" % (2, pi)  # 3.14
```

## [References](#references)

* [Python documentation: `printf`-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)