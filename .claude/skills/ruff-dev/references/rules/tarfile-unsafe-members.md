# [tarfile-unsafe-members (S202)](#tarfile-unsafe-members-s202)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27tarfile-unsafe-members%27%20OR%20S202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Ftarfile_unsafe_members.rs#L40)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of `tarfile.extractall`.

## [Why is this bad?](#why-is-this-bad)

Extracting archives from untrusted sources without prior inspection is
a security risk, as maliciously crafted archives may contain files that
will be written outside of the target directory. For example, the archive
could include files with absolute paths (e.g., `/etc/passwd`), or relative
paths with parent directory references (e.g., `../etc/passwd`).

On Python 3.12 and later, use `filter='data'` to prevent the most dangerous
security issues (see: [PEP 706](https://peps.python.org/pep-0706/#backporting-forward-compatibility)). On earlier versions, set the `members`
argument to a trusted subset of the archive's members.

## [Example](#example)

```
import tarfile
import tempfile

tar = tarfile.open(filename)
tar.extractall(path=tempfile.mkdtemp())
tar.close()
```

## [References](#references)

* [Common Weakness Enumeration: CWE-22](https://cwe.mitre.org/data/definitions/22.html)
* [Python documentation: `TarFile.extractall`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall)
* [Python documentation: Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter)