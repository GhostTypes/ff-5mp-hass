# [tab-indentation (W191)](#tab-indentation-w191)

Added in [v0.0.254](https://github.com/astral-sh/ruff/releases/tag/v0.0.254) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27tab-indentation%27%20OR%20W191)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ftab_indentation.rs#L26)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for indentation that uses tabs.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#tabs-or-spaces), spaces are preferred over tabs (unless used to remain
consistent with code that is already indented with tabs).

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter). The
formatter enforces consistent indentation, making the rule redundant.

The rule is also incompatible with the [formatter](https://docs.astral.sh/ruff/formatter) when using
`format.indent-style="tab"`.