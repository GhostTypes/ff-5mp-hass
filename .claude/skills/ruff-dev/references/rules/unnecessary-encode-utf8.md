# [unnecessary-encode-utf8 (UP012)](#unnecessary-encode-utf8-up012)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-encode-utf8%27%20OR%20UP012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funnecessary_encode_utf8.rs#L32)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary calls to `encode` as UTF-8.

## [Why is this bad?](#why-is-this-bad)

UTF-8 is the default encoding in Python, so there is no need to call
`encode` when UTF-8 is the desired encoding. Instead, use a bytes literal.

## [Example](#example)

```
"foo".encode("utf-8")
```

Use instead:

```
b"foo"
```

## [References](#references)

* [Python documentation: `str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode)