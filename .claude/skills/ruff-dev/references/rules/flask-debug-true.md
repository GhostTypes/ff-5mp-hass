# [flask-debug-true (S201)](#flask-debug-true-s201)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27flask-debug-true%27%20OR%20S201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fflask_debug_true.rs#L41)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of `debug=True` in Flask.

## [Why is this bad?](#why-is-this-bad)

Enabling debug mode shows an interactive debugger in the browser if an
error occurs, and allows running arbitrary Python code from the browser.
This could leak sensitive information, or allow an attacker to run
arbitrary code.

## [Example](#example)

```
from flask import Flask

app = Flask()

app.run(debug=True)
```

Use instead:

```
import os

from flask import Flask

app = Flask()

app.run(debug=os.environ["ENV"] == "dev")
```

## [References](#references)

* [Flask documentation: Debug Mode](https://flask.palletsprojects.com/en/latest/quickstart/#debug-mode)