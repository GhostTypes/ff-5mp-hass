# [invalid-escape-sequence (W605)](#invalid-escape-sequence-w605)

Added in [v0.0.85](https://github.com/astral-sh/ruff/releases/tag/v0.0.85) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-escape-sequence%27%20OR%20W605)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Finvalid_escape_sequence.rs#L43)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for invalid escape sequences.

## [Why is this bad?](#why-is-this-bad)

Invalid escape sequences are deprecated in Python 3.6.

## [Example](#example)

```
regex = "\.png$"
```

Use instead:

```
regex = r"\.png$"
```

Or, if the string already contains a valid escape sequence:

```
value = "new line\nand invalid escape \_ here"
```

Use instead:

```
value = "new line\nand invalid escape \\_ here"
```

## [References](#references)

* [Python documentation: String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)