# [six-py3 (YTT202)](#six-py3-ytt202)

Added in [v0.0.113](https://github.com/astral-sh/ruff/releases/tag/v0.0.113) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27six-py3%27%20OR%20YTT202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_2020%2Frules%2Fname_or_attribute.rs#L38)

Derived from the **[flake8-2020](../#flake8-2020-ytt)** linter.

## [What it does](#what-it-does)

Checks for uses of `six.PY3`.

## [Why is this bad?](#why-is-this-bad)

`six.PY3` will evaluate to `False` on Python 4 and greater. This is likely
unintended, and may cause code intended to run on Python 2 to run on Python 4
too.

Instead, use `not six.PY2` to validate that the current Python major version is
*not* equal to 2, to future-proof the code.

## [Example](#example)

```
import six

six.PY3  # `False` on Python 4.
```

Use instead:

```
import six

not six.PY2  # `True` on Python 4.
```

## [References](#references)

* [PyPI: `six`](https://pypi.org/project/six/)
* [Six documentation: `six.PY2`](https://six.readthedocs.io/#six.PY2)
* [Six documentation: `six.PY3`](https://six.readthedocs.io/#six.PY3)