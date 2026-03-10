# [shebang-leading-whitespace (EXE004)](#shebang-leading-whitespace-exe004)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27shebang-leading-whitespace%27%20OR%20EXE004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_executable%2Frules%2Fshebang_leading_whitespace.rs#L33)

Derived from the **[flake8-executable](../#flake8-executable-exe)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for whitespace before a shebang directive.

## [Why is this bad?](#why-is-this-bad)

In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.

The shebang's `#!` prefix must be the first two characters of a file. The
presence of whitespace before the shebang will cause the shebang to be
ignored, which is likely a mistake.

## [Example](#example)

```
 #!/usr/bin/env python3
```

Use instead:

```
#!/usr/bin/env python3
```

## [References](#references)

* [Python documentation: Executable Python Scripts](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)