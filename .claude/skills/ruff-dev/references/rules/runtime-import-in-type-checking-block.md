# [runtime-import-in-type-checking-block (TC004)](#runtime-import-in-type-checking-block-tc004)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27runtime-import-in-type-checking-block%27%20OR%20TC004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_type_checking%2Frules%2Fruntime_import_in_type_checking_block.rs#L56)

Derived from the **[flake8-type-checking](../#flake8-type-checking-tc)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for imports that are required at runtime but are only defined in
type-checking blocks.

## [Why is this bad?](#why-is-this-bad)

The type-checking block is not executed at runtime, so if the only definition
of a symbol is in a type-checking block, it will not be available at runtime.

If [`lint.flake8-type-checking.quote-annotations`](../../settings/#lint_flake8-type-checking_quote-annotations) is set to `true`,
annotations will be wrapped in quotes if doing so would enable the
corresponding import to remain in the type-checking block.

## [Example](#example)

```
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import foo


def bar() -> None:
    foo.bar()  # raises NameError: name 'foo' is not defined
```

Use instead:

```
import foo


def bar() -> None:
    foo.bar()
```

## [Options](#options)

* [`lint.flake8-type-checking.quote-annotations`](../../settings/#lint_flake8-type-checking_quote-annotations)

## [References](#references)

* [PEP 563: Runtime annotation resolution and `TYPE_CHECKING`](https://peps.python.org/pep-0563/#runtime-annotation-resolution-and-type-checking)