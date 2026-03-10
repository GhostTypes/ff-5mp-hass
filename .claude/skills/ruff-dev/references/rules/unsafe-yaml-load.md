# [unsafe-yaml-load (S506)](#unsafe-yaml-load-s506)

Added in [v0.0.212](https://github.com/astral-sh/ruff/releases/tag/v0.0.212) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unsafe-yaml-load%27%20OR%20S506)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Funsafe_yaml_load.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the `yaml.load` function.

## [Why is this bad?](#why-is-this-bad)

Running the `yaml.load` function over untrusted YAML files is insecure, as
`yaml.load` allows for the creation of arbitrary Python objects, which can
then be used to execute arbitrary code.

Instead, consider using `yaml.safe_load`, which allows for the creation of
simple Python objects like integers and lists, but prohibits the creation of
more complex objects like functions and classes.

## [Example](#example)

```
import yaml

yaml.load(untrusted_yaml)
```

Use instead:

```
import yaml

yaml.safe_load(untrusted_yaml)
```

## [References](#references)

* [PyYAML documentation: Loading YAML](https://pyyaml.org/wiki/PyYAMLDocumentation)
* [Common Weakness Enumeration: CWE-20](https://cwe.mitre.org/data/definitions/20.html)