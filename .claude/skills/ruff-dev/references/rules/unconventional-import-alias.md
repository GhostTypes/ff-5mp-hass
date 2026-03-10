# [unconventional-import-alias (ICN001)](#unconventional-import-alias-icn001)

Added in [v0.0.166](https://github.com/astral-sh/ruff/releases/tag/v0.0.166) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unconventional-import-alias%27%20OR%20ICN001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_import_conventions%2Frules%2Funconventional_import_alias.rs#L37)

Derived from the **[flake8-import-conventions](../#flake8-import-conventions-icn)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for imports that are typically imported using a common convention,
like `import pandas as pd`, and enforces that convention.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.

For example, `import pandas as pd` is a common
convention for importing the `pandas` library, and users typically expect
Pandas to be aliased as `pd`.

## [Example](#example)

```
import pandas
```

Use instead:

```
import pandas as pd
```

## [Options](#options)

* [`lint.flake8-import-conventions.aliases`](../../settings/#lint_flake8-import-conventions_aliases)
* [`lint.flake8-import-conventions.extend-aliases`](../../settings/#lint_flake8-import-conventions_extend-aliases)