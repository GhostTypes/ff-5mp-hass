# [banned-module-level-imports (TID253)](#banned-module-level-imports-tid253)

Added in [v0.0.285](https://github.com/astral-sh/ruff/releases/tag/v0.0.285) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27banned-module-level-imports%27%20OR%20TID253)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_tidy_imports%2Frules%2Fbanned_module_level_imports.rs#L45)

Derived from the **[flake8-tidy-imports](../#flake8-tidy-imports-tid)** linter.

## [What it does](#what-it-does)

Checks for module-level imports that should instead be imported lazily
(e.g., within a function definition, or an `if TYPE_CHECKING:` block, or
some other nested context).

## [Why is this bad?](#why-is-this-bad)

Some modules are expensive to import. For example, importing `torch` or
`tensorflow` can introduce a noticeable delay in the startup time of a
Python program.

In such cases, you may want to enforce that the module is imported lazily
as needed, rather than at the top of the file. This could involve inlining
the import into the function that uses it, rather than importing it
unconditionally, to ensure that the module is only imported when necessary.

## [Example](#example)

```
import tensorflow as tf


def show_version():
    print(tf.__version__)
```

Use instead:

```
def show_version():
    import tensorflow as tf

    print(tf.__version__)
```

## [Options](#options)

* [`lint.flake8-tidy-imports.banned-module-level-imports`](../../settings/#lint_flake8-tidy-imports_banned-module-level-imports)