# [Settings](#settings)

The Ruff Language Server provides a set of configuration options to customize its behavior
along with the ability to use an existing `pyproject.toml` or `ruff.toml` file to configure the
linter and formatter. This is done by providing these settings while initializing the server.
VS Code provides a UI to configure these settings, while other editors may require manual
configuration. The [setup](../setup/) section provides instructions on where to place these settings
as per the editor.

## [Top-level](#top-level)

### [`configuration`](#configuration)

The `configuration` setting allows you to configure editor-specific Ruff behavior. This can be done
in one of the following ways:

1. **Configuration file path:** Specify the path to a `ruff.toml` or `pyproject.toml` file that
   contains the configuration. User home directory and environment variables will be expanded.
2. **Inline JSON configuration:** Directly provide the configuration as a JSON object.

Added in Ruff `0.9.8`

The **Inline JSON configuration** option was introduced in Ruff `0.9.8`.

The default behavior, if `configuration` is unset, is to load the settings from the project's
configuration (a `ruff.toml` or `pyproject.toml` in the project's directory), consistent with when
running Ruff on the command-line.

The [`configurationPreference`](#configurationpreference) setting controls the precedence if both an
editor-provided configuration (`configuration`) and a project level configuration file are present.

#### [Resolution order](#configuration_resolution_order)

In an editor, Ruff supports three sources of configuration, prioritized as follows (from highest to
lowest):

1. **Specific settings:** Individual settings like [`lineLength`](#linelength) or
   [`lint.select`](#select) defined in the editor
2. [**`ruff.configuration`**](#configuration): Settings provided via the
   [`configuration`](#configuration) field (either a path to a configuration file or an inline
   configuration object)
3. **Configuration file:** Settings defined in a `ruff.toml` or `pyproject.toml` file in the
   project's directory (if present)

For example, if the line length is specified in all three sources, Ruff will use the value from the
[`lineLength`](#linelength) setting.

**Default value**: `null`

**Type**: `string`

**Example usage**:

*Using configuration file path:*

VS CodeNeovimZed

```
{
    "ruff.configuration": "~/path/to/ruff.toml"
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      configuration = "~/path/to/ruff.toml"
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "configuration": "~/path/to/ruff.toml"
        }
      }
    }
  }
}
```

*Using inline configuration:*

VS CodeNeovimZed

```
{
    "ruff.configuration": {
        "lint": {
            "unfixable": ["F401"],
            "extend-select": ["TID251"],
            "flake8-tidy-imports": {
                "banned-api": {
                    "typing.TypedDict": {
                        "msg": "Use `typing_extensions.TypedDict` instead",
                    }
                }
            }
        },
        "format": {
            "quote-style": "single"
        }
    }
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      configuration = {
        lint = {
          unfixable = {"F401"},
          ["extend-select"] = {"TID251"},
          ["flake8-tidy-imports"] = {
            ["banned-api"] = {
              ["typing.TypedDict"] = {
                msg = "Use `typing_extensions.TypedDict` instead"
              }
            }
          }
        },
        format = {
          ["quote-style"] = "single"
        }
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "configuration": {
            "lint": {
              "unfixable": ["F401"],
              "extend-select": ["TID251"],
              "flake8-tidy-imports": {
                "banned-api": {
                  "typing.TypedDict": {
                    "msg": "Use `typing_extensions.TypedDict` instead"
                  }
                }
              }
            },
            "format": {
              "quote-style": "single"
            }
          }
        }
      }
    }
  }
}
```

### [`configurationPreference`](#configurationpreference)

The strategy to use when resolving settings across VS Code and the filesystem. By default, editor
configuration is prioritized over `ruff.toml` and `pyproject.toml` files.

* `"editorFirst"`: Editor settings take priority over configuration files present in the workspace.
* `"filesystemFirst"`: Configuration files present in the workspace takes priority over editor
  settings.
* `"editorOnly"`: Ignore configuration files entirely i.e., only use editor settings.

**Default value**: `"editorFirst"`

**Type**: `"editorFirst" | "filesystemFirst" | "editorOnly"`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.configurationPreference": "filesystemFirst"
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      configurationPreference = "filesystemFirst"
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "configurationPreference": "filesystemFirst"
        }
      }
    }
  }
}
```

### [`exclude`](#exclude)

A list of file patterns to exclude from linting and formatting. See [the
documentation](https://docs.astral.sh/ruff/settings/#exclude) for more details.

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.exclude": ["**/tests/**"]
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      exclude = ["**/tests/**"]
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "exclude": ["**/tests/**"]
        }
      }
    }
  }
}
```

### [`lineLength`](#linelength)

The line length to use for the linter and formatter.

**Default value**: `null`

**Type**: `int`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lineLength": 100
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lineLength = 100
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lineLength": 100
        }
      }
    }
  }
}
```

### [`fixAll`](#fixall)

Whether to register the server as capable of handling `source.fixAll` code actions.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.fixAll": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      fixAll = false
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "fixAll": false
        }
      }
    }
  }
}
```

### [`organizeImports`](#organizeimports)

Whether to register the server as capable of handling `source.organizeImports` code actions.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.organizeImports": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      organizeImports = false
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "organizeImports": false
        }
      }
    }
  }
}
```

### [`showSyntaxErrors`](#showsyntaxerrors)

*New in Ruff [v0.5.0](https://astral.sh/blog/ruff-v0.5.0#changes-to-e999-and-reporting-of-syntax-errors)*

Whether to show syntax error diagnostics.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.showSyntaxErrors": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      showSyntaxErrors = false
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "showSyntaxErrors": false
        }
      }
    }
  }
}
```

### [`logLevel`](#loglevel)

The log level to use for the server.

**Default value**: `"info"`

**Type**: `"trace" | "debug" | "info" | "warn" | "error"`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.logLevel": "debug"
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      logLevel = "debug"
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "logLevel": "debug"
        }
      }
    }
  }
}
```

### [`logFile`](#logfile)

Path to the log file to use for the server.

If not set, logs will be written to stderr.

**Default value**: `null`

**Type**: `string`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.logFile": "~/path/to/ruff.log"
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      logFile = "~/path/to/ruff.log"
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "logFile": "~/path/to/ruff.log"
        }
      }
    }
  }
}
```

## [`codeAction`](#codeaction)

Enable or disable code actions provided by the server.

### [`disableRuleComment.enable`](#disablerulecommentenable)

Whether to display Quick Fix actions to disable rules via `noqa` suppression comments.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.codeAction.disableRuleComment.enable": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      codeAction = {
        disableRuleComment = {
          enable = false
        }
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "codeAction": {
            "disableRuleComment": {
              "enable": false
            }
          }
        }
      }
    }
  }
}
```

### [`fixViolation.enable`](#fixviolationenable)

Whether to display Quick Fix actions to autofix violations.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.codeAction.fixViolation.enable": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      codeAction = {
        fixViolation = {
          enable = false
        }
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "codeAction": {
            "fixViolation": = {
              "enable": false
            }
          }
        }
      }
    }
  }
}
```

## [`lint`](#lint)

Settings specific to the Ruff linter.

### [`enable`](#lint_enable)

Whether to enable linting. Set to `false` to use Ruff exclusively as a formatter.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lint.enable": false
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lint = {
        enable = false
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lint": {
            "enable": false
          }
        }
      }
    }
  }
}
```

### [`preview`](#lint_preview)

Whether to enable Ruff's preview mode when linting.

**Default value**: `null`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lint.preview": true
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lint = {
        preview = true
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lint": {
            "preview": true
          }
        }
      }
    }
  }
}
```

### [`select`](#select)

Rules to enable by default. See [the documentation](https://docs.astral.sh/ruff/settings/#lint_select).

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lint.select": ["E", "F"]
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lint = {
        select = {"E", "F"}
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lint": {
            "select": ["E", "F"]
          }
        }
      }
    }
  }
}
```

### [`extendSelect`](#extendselect)

Rules to enable in addition to those in [`lint.select`](#select).

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lint.extendSelect": ["W"]
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lint = {
        extendSelect = {"W"}
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lint": {
            "extendSelect": ["W"]
          }
        }
      }
    }
  }
}
```

### [`ignore`](#ignore)

Rules to disable by default. See [the documentation](https://docs.astral.sh/ruff/settings/#lint_ignore).

**Default value**: `null`

**Type**: `string[]`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.lint.ignore": ["E4", "E7"]
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      lint = {
        ignore = {"E4", "E7"}
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "lint": {
            "ignore": ["E4", "E7"]
          }
        }
      }
    }
  }
}
```

## [`format`](#format)

Settings specific to the Ruff formatter.

### [`preview`](#format_preview)

Whether to enable Ruff's preview mode when formatting.

**Default value**: `null`

**Type**: `bool`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.format.preview": true
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      format = {
        preview = true
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "format": {
            "preview": true
          }
        }
      }
    }
  }
}
```

### [`backend`](#format_backend)

The backend to use for formatting files. Following options are available:

* `"internal"`: Use the built-in Ruff formatter
* `"uv"`: Use uv for formatting (requires uv >= 0.8.13)

For `internal`, the formatter version will match the selected Ruff version while for `uv`, the
formatter version may differ.

**Default value**: `"internal"`

**Type**: `"internal" | "uv"`

**Example usage**:

VS CodeNeovimZed

```
{
    "ruff.format.backend": "uv"
}
```

```
require('lspconfig').ruff.setup {
  init_options = {
    settings = {
      format = {
        backend = "uv"
      }
    }
  }
}
```

```
{
  "lsp": {
    "ruff": {
      "initialization_options": {
        "settings": {
          "format": {
            "backend": "uv"
          }
        }
      }
    }
  }
}
```

## [VS Code specific](#vs-code-specific)

Additionally, the Ruff extension provides the following settings specific to VS Code. These settings
are not used by the language server and are only relevant to the extension.

### [`enable`](#enable)

Whether to enable the Ruff extension. Modifying this setting requires restarting VS Code to take effect.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

```
{
    "ruff.enable": false
}
```

### [`format.args`](#formatargs)

Deprecated

This setting is only used by [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) which is
deprecated in favor of the native language server. Refer to the [migration
guide](../migration/) for more information.

***This setting is not used by the native language server.***

Additional arguments to pass to the Ruff formatter.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```
{
    "ruff.format.args": ["--line-length", "100"]
}
```

### [`ignoreStandardLibrary`](#ignorestandardlibrary)

Deprecated

This setting is only used by [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) which is
deprecated in favor of the native language server. Refer to the [migration
guide](../migration/) for more information.

***This setting is not used by the native language server.***

Whether to ignore files that are inferred to be part of the Python standard library.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

```
{
    "ruff.ignoreStandardLibrary": false
}
```

### [`importStrategy`](#importstrategy)

Strategy for loading the `ruff` executable.

* `fromEnvironment` finds Ruff in the environment, falling back to the bundled version
* `useBundled` uses the version bundled with the extension

**Default value**: `"fromEnvironment"`

**Type**: `"fromEnvironment" | "useBundled"`

**Example usage**:

```
{
    "ruff.importStrategy": "useBundled"
}
```

### [`interpreter`](#interpreter)

A list of paths to Python interpreters. Even though this is a list, only the first interpreter is
used.

This setting depends on the [`ruff.nativeServer`](#nativeserver) setting:

* If using the native server, the interpreter is used to find the `ruff` executable when
  [`ruff.importStrategy`](#importstrategy) is set to `fromEnvironment`.
* Otherwise, the interpreter is used to run the `ruff-lsp` server.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```
{
    "ruff.interpreter": ["/home/user/.local/bin/python"]
}
```

### [`lint.args`](#lintargs)

Deprecated

This setting is only used by [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) which is
deprecated in favor of the native language server. Refer to the [migration
guide](../migration/) for more information.

***This setting is not used by the native language server.***

Additional arguments to pass to the Ruff linter.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```
{
    "ruff.lint.args": ["--config", "/path/to/pyproject.toml"]
}
```

### [`lint.run`](#lintrun)

Deprecated

This setting is only used by [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) which is
deprecated in favor of the native language server. Refer to the [migration
guide](../migration/) for more information.

***This setting is not used by the native language server.***

Run Ruff on every keystroke (`onType`) or on save (`onSave`).

**Default value**: `"onType"`

**Type**: `"onType" | "onSave"`

**Example usage**:

```
{
    "ruff.lint.run": "onSave"
}
```

### [`nativeServer`](#nativeserver)

Whether to use the native language server, [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) or
automatically decide between the two based on the Ruff version and extension settings.

* `"on"`: Use the native language server. A warning will be displayed if deprecated settings are
  detected.
* `"off"`: Use [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp). A warning will be displayed if
  settings specific to the native server are detected.
* `"auto"`: Automatically select between the native language server and
  [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) based on the following conditions:
  1. If the Ruff version is >= `0.5.3`, use the native language server unless any deprecated
     settings are detected. In that case, show a warning and use
     [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) instead.
  2. If the Ruff version is < `0.5.3`, use [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp). A
     warning will be displayed if settings specific to the native server are detected.
* `true`: Same as `on`
* `false`: Same as `off`

**Default value**: `"auto"`

**Type**: `"on" | "off" | "auto" | true | false`

**Example usage**:

```
{
    "ruff.nativeServer": "on"
}
```

### [`path`](#path)

A list of path to `ruff` executables.

The first executable in the list which is exists is used. This setting takes precedence over the
[`ruff.importStrategy`](#importstrategy) setting.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```
{
    "ruff.path": ["/home/user/.local/bin/ruff"]
}
```

### [`showNotifications`](#shownotifications)

Deprecated

This setting is only used by [`ruff-lsp`](https://github.com/astral-sh/ruff-lsp) which is
deprecated in favor of the native language server. Refer to the [migration
guide](../migration/) for more information.

Setting to control when a notification is shown.

**Default value**: `"off"`

**Type**: `"off" | "onError" | "onWarning" | "always"`

**Example usage**:

```
{
    "ruff.showNotifications": "onWarning"
}
```

### [`trace.server`](#traceserver)

The trace level for the language server. Refer to the [LSP
specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#traceValue)
for more information.

**Default value**: `"off"`

**Type**: `"off" | "messages" | "verbose"`

**Example usage**:

```
{
    "ruff.trace.server": "messages"
}
```