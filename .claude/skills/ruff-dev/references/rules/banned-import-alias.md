# [banned-import-alias (ICN002)](#banned-import-alias-icn002)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27banned-import-alias%27%20OR%20ICN002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_import_conventions%2Frules%2Fbanned_import_alias.rs#L36)

Derived from the **[flake8-import-conventions](../#flake8-import-conventions-icn)** linter.

## [What it does](#what-it-does)

Checks for imports that use non-standard naming conventions, like
`import tensorflow.keras.backend as K`.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Avoid using a non-standard naming convention for
imports, and, in particular, choosing import aliases that violate PEP 8.

For example, aliasing via `import tensorflow.keras.backend as K` violates
the guidance of PEP 8, and is thus avoided in some projects.

## [Example](#example)

```
import tensorflow.keras.backend as K
```

Use instead:

```
import tensorflow as tf

tf.keras.backend
```

## [Options](#options)

* [`lint.flake8-import-conventions.banned-aliases`](../../settings/#lint_flake8-import-conventions_banned-aliases)