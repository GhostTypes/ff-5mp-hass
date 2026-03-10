# [blanket-noqa (PGH004)](#blanket-noqa-pgh004)

Added in [v0.0.200](https://github.com/astral-sh/ruff/releases/tag/v0.0.200) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blanket-noqa%27%20OR%20PGH004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpygrep_hooks%2Frules%2Fblanket_noqa.rs#L41)

Derived from the **[pygrep-hooks](../#pygrep-hooks-pgh)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Check for `noqa` annotations that suppress all diagnostics, as opposed to
targeting specific diagnostics.

## [Why is this bad?](#why-is-this-bad)

Suppressing all diagnostics can hide issues in the code.

Blanket `noqa` annotations are also more difficult to interpret and
maintain, as the annotation does not clarify which diagnostics are intended
to be suppressed.

## [Example](#example)

```
from .base import *  # noqa
```

Use instead:

```
from .base import *  # noqa: F403
```

## [Fix safety](#fix-safety)

This rule will attempt to fix blanket `noqa` annotations that appear to
be unintentional. For example, given `# noqa F401`, the rule will suggest
inserting a colon, as in `# noqa: F401`.

While modifying `noqa` comments is generally safe, doing so may introduce
additional diagnostics.

## [References](#references)

* [Ruff documentation](https://docs.astral.sh/ruff/configuration/#error-suppression)