# [pytest-raises-ambiguous-pattern (RUF043)](#pytest-raises-ambiguous-pattern-ruf043)

Added in [0.13.0](https://github.com/astral-sh/ruff/releases/tag/0.13.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-raises-ambiguous-pattern%27%20OR%20RUF043)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fpytest_raises_ambiguous_pattern.rs#L66)

## [What it does](#what-it-does)

Checks for non-raw literal string arguments passed to the `match` parameter
of `pytest.raises()` where the string contains at least one unescaped
regex metacharacter.

## [Why is this bad?](#why-is-this-bad)

The `match` argument is implicitly converted to a regex under the hood.
It should be made explicit whether the string is meant to be a regex or a "plain" pattern
by prefixing the string with the `r` suffix, escaping the metacharacter(s)
in the string using backslashes, or wrapping the entire string in a call to
`re.escape()`.

## [Example](#example)

```
import pytest


with pytest.raises(Exception, match="A full sentence."):
    do_thing_that_raises()
```

If the pattern is intended to be a regular expression, use a raw string to signal this
intention:

```
import pytest


with pytest.raises(Exception, match=r"A full sentence."):
    do_thing_that_raises()
```

Alternatively, escape any regex metacharacters with `re.escape`:

```
import pytest
import re


with pytest.raises(Exception, match=re.escape("A full sentence.")):
    do_thing_that_raises()
```

or directly with backslashes:

```
import pytest
import re


with pytest.raises(Exception, "A full sentence\\."):
    do_thing_that_raises()
```

## [References](#references)

* [Python documentation: `re.escape`](https://docs.python.org/3/library/re.html#re.escape)
* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)