# HACS Publisher Companion

Fast-reference guide for adding or maintaining repositories in HACS, distilled from the official docs at <https://hacs.xyz/docs/publish/>. Use this when creating new FlashForge assets or coaching contributors through the publishing process.

---

## General Requirements
- Only **public GitHub repositories** are eligible.
- Fill in the **repository description**, **topics**, and a practical **README**—all are validated by HACS.
- Maintain an accurate `hacs.json` at the repository root (see field hints below).
- Publish **GitHub releases** when possible; HACS prefers releases over tags and otherwise falls back to the latest commit hash.
- Advertise availability with a `[my.home-assistant.io](https://my.home-assistant.io/create-link/?redirect=hacs_repository)` link in your docs.

### `hacs.json` Field Hints
| Key | Purpose / Notes |
| --- | --- |
| `name` | Display name shown in HACS (required). |
| `content_in_root` | Set `true` if the deliverable lives at repo root instead of a subdirectory. |
| `zip_release` + `filename` | Bundle integration releases as ZIP archives; `filename` names the artifact inside. |
| `hide_default_branch` | Prevent users from installing from the default branch. |
| `country` | ISO 3166-1 alpha-2 codes; accepts string or list. |
| `homeassistant`, `hacs` | Minimum supported versions; append `b0` to allow HA beta releases. |
| `persistent_directory` | Integration-only: path under `custom_components/<domain>/` that survives upgrades. |

Tip: Use the [AwesomeVersion demo](https://awesomeversion.ludeeus.dev/) to verify semantic version strings exactly as HACS will parse them.

---

## Joining the Default Store
**Only repository owners or major contributors** may submit additions, and core overrides/alpha forks are not accepted—keep them as custom repositories instead.

### Prep Checklist *(per [Include default repositories](https://hacs.xyz/docs/publish/include/))*:
- Repository already works as a custom repo and is public on GitHub.
- Enable and pass:
  - [`hacs/action`](https://github.com/hacs/action) (no ignored checks on the submission run).
  - [`hassfest`](https://github.com/home-assistant/actions#hassfest) for integrations.
- Cut a fresh **GitHub release** after validations succeed—tags without releases do not qualify.
- Add the repo alphabetically to the relevant file in [`hacs/default`](https://github.com/hacs/default) (`appdaemon`, `integration`, `plugin`, `python_script`, `template`, `theme`).
- Create the PR from a branch in your fork (not the fork’s default branch or an organization fork).
- Ensure `hacs.json` includes `country` when the project targets limited regions.
- Complete every item in the PR template honestly—misrepresentation or missing info will close the PR.

### Review Pipeline
Once the PR is ready for review, automated checks run in this order. All must pass unless you negotiated exceptions in advance:
- `brands`: integration listed in [`home-assistant/brands`](https://github.com/home-assistant/brands).
- `manifest`: `manifest.json` schema-valid (integrations).
- `hacs-validation`: same validation HACS performs for installs.
- `hacs.json`: file exists and at least defines `name`.
- `archived`: repository must be active.
- `releases`: requires at least one GitHub release.
- `owner`: submitter is owner or major contributor.
- `images`: README contains imagery (plugins/themes).
- `repository`: checks description, issues enabled, and topics set.
- `lint jq` / `lint sorted`: JSON files well-formed and alphabetized.

**After merge** the default list updates on the next scheduled scan—no extra follow-up required.

---

## GitHub Action (`hacs/action`) Essentials
- Supports validating **PRs**, **pushes**, and **scheduled** runs; use all three for early warnings.
- Inputs:
  - `category`: one of `appdaemon`, `integration`, `plugin`, `python_script`, `template`, `theme`.
  - `ignore`: space-separated list of checks to skip (`archived`, `brands`, `description`, `hacsjson`, `images`, `information`, `issues`, `topics`). Ignore sparingly and document why.
- Sample workflow:
  ```yaml
  name: Validate
  on:
    push:
    pull_request:
    schedule: [{cron: "0 0 * * *"}]
    workflow_dispatch:
  permissions: {}
  jobs:
    validate-hacs:
      runs-on: ubuntu-latest
      steps:
        - name: HACS validation
          uses: hacs/action@main  # pin and enable Dependabot for stability
          with:
            category: CHANGE_ME
  ```
- Maintain Dependabot to track upstream action releases.

---

## Repository Type Requirements
Quick structure rules for each supported category.

### Integrations
- Exactly one integration under `custom_components/<domain>/`; all runtime files live inside that folder.
- `manifest.json` must declare `domain`, `documentation`, `issue_tracker`, `codeowners`, `name`, `version`.
- Brand assets must exist in [`home-assistant/brands`](https://github.com/home-assistant/brands).
- Releases strongly recommended; otherwise default branch is used. `content_in_root: true` in `hacs.json` permits root-level layouts.

### Plugin (Dashboard)
- Ship `.js` assets either under `dist/` or repository root; at least one file matches the repository name (strip `lovelace-` prefix when matching).
- Bundle extra assets (CSS, images, translations) alongside the JS file—prefer `dist/`.
- Releases optional but enable version selection; fallback is default branch.

### AppDaemon Apps
- Exactly one app directory under `apps/`; all Python files reside in `apps/<app_name>/`.
- Releases optional; HACS scans the latest release or default branch.
- Reference implementation: [ludeeus/ad-hacs](https://github.com/ludeeus/ad-hacs).

### Python Scripts
- Single script file at `python_scripts/<script_name>.py`.
- Additional files are ignored; keep repo focused on one script.
- Releases optional; same release/default branch behavior applies.

### Custom Templates
- Root must contain `README.md`, `hacs.json`, and a `.jinja` file.
- `hacs.json.filename` must match one of the root `.jinja` files.
- **GitHub releases are mandatory**—HACS only ingests from released artifacts for templates.

### Themes
- Single YAML theme file at `themes/<theme_name>.yaml`.
- Releases optional; default branch used when absent.

---

## Operations & Lifecycle
- **Renames or transfers**: No action needed—HACS automatically updates default records after repository moves.
- **Removal**: HACS staff can delist repositories for abandonment, breakage, credential abuse, or deletion. Maintainers planning removal should open a [“Request for repository removal” issue](https://github.com/hacs/integration/issues/new?assignees=ludeeus&labels=flag&projects=&template=removal.yml).
- **Archiving**: Archived repositories are removed automatically; avoid archiving defaults unless you intend to retire them.

Keep this companion alongside `HOME_ASSISTANT_DOCS_COMPANION.md` to brief new agents quickly and ensure our FlashForge extensions stay compliant with HACS publishing policies.
