# [p-print (T203)](#p-print-t203)

Added in [v0.0.57](https://github.com/astral-sh/ruff/releases/tag/v0.0.57) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27p-print%27%20OR%20T203)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_print%2Frules%2Fprint_call.rs#L100)

Derived from the **[flake8-print](../#flake8-print-t20)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `pprint` statements.

## [Why is this bad?](#why-is-this-bad)

Like `print` statements, `pprint` statements used for debugging should
be omitted from production code. They can lead the accidental inclusion
of sensitive information in logs, and are not configurable by clients,
unlike `logging` statements.

`pprint` statements used to produce output as a part of a command-line
interface program are not typically a problem.

## [Example](#example)

```
import pprint


def merge_dicts(dict_a, dict_b):
    dict_c = {**dict_a, **dict_b}
    pprint.pprint(dict_c)
    return dict_c
```

Use instead:

```
def merge_dicts(dict_a, dict_b):
    dict_c = {**dict_a, **dict_b}
    return dict_c
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it will remove `pprint` statements
that are used beyond debugging purposes.