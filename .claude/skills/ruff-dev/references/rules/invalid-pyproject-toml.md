# [invalid-pyproject-toml (RUF200)](#invalid-pyproject-toml-ruf200)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-pyproject-toml%27%20OR%20RUF200)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Finvalid_pyproject_toml.rs#L33)

## [What it does](#what-it-does)

Checks for any pyproject.toml that does not conform to the schema from the relevant PEPs.

## [Why is this bad?](#why-is-this-bad)

Your project may contain invalid metadata or configuration without you noticing

## [Example](#example)

```
[project]
name = "crab"
version = "1.0.0"
authors = ["Ferris the Crab <[email protected]>"]
```

Use instead:

```
[project]
name = "crab"
version = "1.0.0"
authors = [
  { name = "Ferris the Crab", email = "[email protected]" }
]
```

## [References](#references)

* [Specification of `[project]` in pyproject.toml](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/)
* [Specification of `[build-system]` in pyproject.toml](https://peps.python.org/pep-0518/)
* [Draft but implemented license declaration extensions](https://peps.python.org/pep-0639)