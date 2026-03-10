# [unsorted-imports (I001)](#unsorted-imports-i001)

Added in [v0.0.110](https://github.com/astral-sh/ruff/releases/tag/v0.0.110) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unsorted-imports%27%20OR%20I001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fisort%2Frules%2Forganize_imports.rs#L41)

Derived from the **[isort](../#isort-i)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

De-duplicates, groups, and sorts imports based on the provided `isort` settings.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.

## [Example](#example)

```
import pandas
import numpy as np
```

Use instead:

```
import numpy as np
import pandas
```