# [invalid-rule-code (RUF102)](#invalid-rule-code-ruf102)

Preview (since [0.11.4](https://github.com/astral-sh/ruff/releases/tag/0.11.4)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-rule-code%27%20OR%20RUF102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Finvalid_rule_code.rs#L35)

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `noqa` codes that are invalid.

## [Why is this bad?](#why-is-this-bad)

Invalid rule codes serve no purpose and may indicate outdated code suppressions.

## [Example](#example)

```
import os  # noqa: XYZ999
```

Use instead:

```
import os
```

Or if there are still valid codes needed:

```
import os  # noqa: E402
```

## [Options](#options)

* [`lint.external`](../../settings/#lint_external)