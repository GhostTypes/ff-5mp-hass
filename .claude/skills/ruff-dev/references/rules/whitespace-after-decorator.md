# [whitespace-after-decorator (E204)](#whitespace-after-decorator-e204)

Preview (since [0.5.1](https://github.com/astral-sh/ruff/releases/tag/0.5.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27whitespace-after-decorator%27%20OR%20E204)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fwhitespace_after_decorator.rs#L32)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for trailing whitespace after a decorator's opening `@`.

## [Why is this bad?](#why-is-this-bad)

Including whitespace after the `@` symbol is not compliant with
[PEP 8](https://peps.python.org/pep-0008/#maximum-line-length).

## [Example](#example)

```
@ decorator
def func():
   pass
```

Use instead:

```
@decorator
def func():
  pass
```