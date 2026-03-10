# [ssh-no-host-key-verification (S507)](#ssh-no-host-key-verification-s507)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ssh-no-host-key-verification%27%20OR%20S507)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fssh_no_host_key_verification.rs#L36)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of policies disabling SSH verification in Paramiko.

## [Why is this bad?](#why-is-this-bad)

By default, Paramiko checks the identity of the remote host when establishing
an SSH connection. Disabling the verification might lead to the client
connecting to a malicious host, without the client knowing.

## [Example](#example)

```
from paramiko import client

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
```

Use instead:

```
from paramiko import client

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.RejectPolicy)
```

## [References](#references)

* [Paramiko documentation: set\_missing\_host\_key\_policy](https://docs.paramiko.org/en/latest/api/client.html#paramiko.client.SSHClient.set_missing_host_key_policy)