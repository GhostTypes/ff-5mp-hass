# [relative-imports (TID252)](#relative-imports-tid252)

Added in [v0.0.169](https://github.com/astral-sh/ruff/releases/tag/v0.0.169) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27relative-imports%27%20OR%20TID252)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_tidy_imports%2Frules%2Frelative_imports.rs#L48)

Derived from the **[flake8-tidy-imports](../#flake8-tidy-imports-tid)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for relative imports.

## [Why is this bad?](#why-is-this-bad)

Absolute imports, or relative imports from siblings, are recommended by [PEP 8](https://peps.python.org/pep-0008/#imports):

> Absolute imports are recommended, as they are usually more readable and tend to be better behaved...
>
> ```
> import mypkg.sibling
> from mypkg import sibling
> from mypkg.sibling import example
> ```
>
> However, explicit relative imports are an acceptable alternative to absolute imports,
> especially when dealing with complex package layouts where using absolute imports would be
> unnecessarily verbose:
>
> ```
> from . import sibling
> from .sibling import example
> ```

## [Example](#example)

```
from .. import foo
```

Use instead:

```
from mypkg import foo
```

## [Options](#options)

* [`lint.flake8-tidy-imports.ban-relative-imports`](../../settings/#lint_flake8-tidy-imports_ban-relative-imports)