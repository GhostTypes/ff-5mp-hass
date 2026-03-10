# [re-sub-positional-args (B034)](#re-sub-positional-args-b034)

Added in [v0.0.278](https://github.com/astral-sh/ruff/releases/tag/v0.0.278) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27re-sub-positional-args%27%20OR%20B034)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fre_sub_positional_args.rs#L42)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for calls to `re.sub`, `re.subn`, and `re.split` that pass `count`,
`maxsplit`, or `flags` as positional arguments.

## [Why is this bad?](#why-is-this-bad)

Passing `count`, `maxsplit`, or `flags` as positional arguments to
`re.sub`, `re.subn`, or `re.split` can lead to confusion, as most methods in
the `re` module accept `flags` as the third positional argument, while
`re.sub`, `re.subn`, and `re.split` have different signatures.

Instead, pass `count`, `maxsplit`, and `flags` as keyword arguments.

## [Example](#example)

```
import re

re.split("pattern", "replacement", 1)
```

Use instead:

```
import re

re.split("pattern", "replacement", maxsplit=1)
```

## [References](#references)

* [Python documentation: `re.sub`](https://docs.python.org/3/library/re.html#re.sub)
* [Python documentation: `re.subn`](https://docs.python.org/3/library/re.html#re.subn)
* [Python documentation: `re.split`](https://docs.python.org/3/library/re.html#re.split)