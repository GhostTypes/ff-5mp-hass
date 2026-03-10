# [blanket-type-ignore (PGH003)](#blanket-type-ignore-pgh003)

Added in [v0.0.187](https://github.com/astral-sh/ruff/releases/tag/v0.0.187) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blanket-type-ignore%27%20OR%20PGH003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpygrep_hooks%2Frules%2Fblanket_type_ignore.rs#L44)

Derived from the **[pygrep-hooks](../#pygrep-hooks-pgh)** linter.

## [What it does](#what-it-does)

Check for `type: ignore` annotations that suppress all type warnings, as
opposed to targeting specific type warnings.

## [Why is this bad?](#why-is-this-bad)

Suppressing all warnings can hide issues in the code.

Blanket `type: ignore` annotations are also more difficult to interpret and
maintain, as the annotation does not clarify which warnings are intended
to be suppressed.

## [Example](#example)

```
from foo import secrets  # type: ignore
```

Use instead:

```
from foo import secrets  # type: ignore[attr-defined]
```

## [References](#references)

Mypy supports a [built-in setting](https://mypy.readthedocs.io/en/stable/error_code_list2.html#check-that-type-ignore-include-an-error-code-ignore-without-code)
to enforce that all `type: ignore` annotations include an error code, akin
to enabling this rule:

```
[tool.mypy]
enable_error_code = ["ignore-without-code"]
```