
## How to set up bash completion

When using bash as your shell, `pytest` can use argcomplete
(https://kislyuk.github.io/argcomplete/) for auto-completion.
For this `argcomplete` needs to be installed **and** enabled.

Install argcomplete using:

```bash

    sudo pip install 'argcomplete>=0.5.7'

```

For global activation of all argcomplete enabled python applications run:

```bash

    sudo activate-global-python-argcomplete

```

For permanent (but not global) `pytest` activation, use:

```bash

    register-python-argcomplete pytest >> ~/.bashrc

```

For one-time activation of argcomplete for `pytest` only, use:

```bash

    eval "$(register-python-argcomplete pytest)"

```