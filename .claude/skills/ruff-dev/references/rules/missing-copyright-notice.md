# [missing-copyright-notice (CPY001)](#missing-copyright-notice-cpy001)

Preview (since [v0.0.273](https://github.com/astral-sh/ruff/releases/tag/v0.0.273)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-copyright-notice%27%20OR%20CPY001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_copyright%2Frules%2Fmissing_copyright_notice.rs#L22)

Derived from the **[flake8-copyright](../#flake8-copyright-cpy)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for the absence of copyright notices within Python files.

Note that this check only searches within the first 4096 bytes of the file.

## [Why is this bad?](#why-is-this-bad)

In some codebases, it's common to have a license header at the top of every
file. This rule ensures that the license header is present.

## [Options](#options)

* [`lint.flake8-copyright.author`](../../settings/#lint_flake8-copyright_author)
* [`lint.flake8-copyright.min-file-size`](../../settings/#lint_flake8-copyright_min-file-size)
* [`lint.flake8-copyright.notice-rgx`](../../settings/#lint_flake8-copyright_notice-rgx)