# [typing-text-str-alias (UP019)](#typing-text-str-alias-up019)

Added in [v0.0.195](https://github.com/astral-sh/ruff/releases/tag/v0.0.195) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27typing-text-str-alias%27%20OR%20UP019)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Ftyping_text_str_alias.rs#L36)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `typing.Text`.

In preview mode, also checks for `typing_extensions.Text`.

## [Why is this bad?](#why-is-this-bad)

`typing.Text` is an alias for `str`, and only exists for Python 2
compatibility. As of Python 3.11, `typing.Text` is deprecated. Use `str`
instead.

## [Example](#example)

```
from typing import Text

foo: Text = "bar"
```

Use instead:

```
foo: str = "bar"
```

## [References](#references)

* [Python documentation: `typing.Text`](https://docs.python.org/3/library/typing.html#typing.Text)