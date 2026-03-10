# [hardcoded-temp-file (S108)](#hardcoded-temp-file-s108)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-temp-file%27%20OR%20S108)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fhardcoded_tmp_directory.rs#L42)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for the use of hardcoded temporary file or directory paths.

## [Why is this bad?](#why-is-this-bad)

The use of hardcoded paths for temporary files can be insecure. If an
attacker discovers the location of a hardcoded path, they can replace the
contents of the file or directory with a malicious payload.

Other programs may also read or write contents to these hardcoded paths,
causing unexpected behavior.

## [Example](#example)

```
with open("/tmp/foo.txt", "w") as file:
    ...
```

Use instead:

```
import tempfile

with tempfile.NamedTemporaryFile() as file:
    ...
```

## [Options](#options)

* [`lint.flake8-bandit.hardcoded-tmp-directory`](../../settings/#lint_flake8-bandit_hardcoded-tmp-directory)
* [`lint.flake8-bandit.hardcoded-tmp-directory-extend`](../../settings/#lint_flake8-bandit_hardcoded-tmp-directory-extend)

## [References](#references)

* [Common Weakness Enumeration: CWE-377](https://cwe.mitre.org/data/definitions/377.html)
* [Common Weakness Enumeration: CWE-379](https://cwe.mitre.org/data/definitions/379.html)
* [Python documentation: `tempfile`](https://docs.python.org/3/library/tempfile.html)