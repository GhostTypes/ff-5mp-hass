# [unspecified-encoding (PLW1514)](#unspecified-encoding-plw1514)

Preview (since [v0.1.1](https://github.com/astral-sh/ruff/releases/tag/v0.1.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unspecified-encoding%27%20OR%20PLW1514)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funspecified_encoding.rs#L56)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of `open` and related calls without an explicit `encoding`
argument.

## [Why is this bad?](#why-is-this-bad)

Using `open` in text mode without an explicit encoding can lead to
non-portable code, with differing behavior across platforms. While readers
may assume that UTF-8 is the default encoding, in reality, the default
is locale-specific.

Instead, consider using the `encoding` parameter to enforce a specific
encoding. [PEP 597](https://peps.python.org/pep-0597/) recommends the use of `encoding="utf-8"` as a default,
and suggests that it may become the default in future versions of Python.

If a locale-specific encoding is intended, use `encoding="locale"` on
Python 3.10 and later, or `locale.getpreferredencoding()` on earlier versions,
to make the encoding explicit.

## [Fix safety](#fix-safety)

This fix is always unsafe and may change the program's behavior. It forces
`encoding="utf-8"` as the default, regardless of the platform’s actual default
encoding, which may cause `UnicodeDecodeError` on non-UTF-8 systems.

```
with open("test.txt") as f:
    print(f.read()) # before fix (on UTF-8 systems): 你好，世界！
with open("test.txt", encoding="utf-8") as f:
    print(f.read()) # after fix (on Windows): UnicodeDecodeError
```

## [Example](#example)

```
open("file.txt")
```

Use instead:

```
open("file.txt", encoding="utf-8")
```

## [References](#references)

* [Python documentation: `open`](https://docs.python.org/3/library/functions.html#open)