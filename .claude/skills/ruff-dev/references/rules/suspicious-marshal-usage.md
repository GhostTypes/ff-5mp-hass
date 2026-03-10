# [suspicious-marshal-usage (S302)](#suspicious-marshal-usage-s302)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-marshal-usage%27%20OR%20S302)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L108)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for calls to `marshal` functions.

## [Why is this bad?](#why-is-this-bad)

Deserializing untrusted data with `marshal` is insecure, as it can allow for
the creation of arbitrary objects, which can then be used to achieve
arbitrary code execution and otherwise unexpected behavior.

Avoid deserializing untrusted data with `marshal`. Instead, consider safer
formats, such as JSON.

If you must deserialize untrusted data with `marshal`, consider signing the
data with a secret key and verifying the signature before deserializing the
payload. This will prevent an attacker from injecting arbitrary objects
into the serialized data.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to `marshal` functions.

## [Example](#example)

```
import marshal

with open("foo.marshal", "rb") as file:
    foo = marshal.load(file)
```

Use instead:

```
import json

with open("foo.json", "rb") as file:
    foo = json.load(file)
```

## [References](#references)

* [Python documentation: `marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
* [Common Weakness Enumeration: CWE-502](https://cwe.mitre.org/data/definitions/502.html)