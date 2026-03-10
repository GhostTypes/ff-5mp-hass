---
name: ruff-dev
description: Professional-grade Python development with Ruff (v0.14.10) - an extremely fast Python linter and formatter. Use when working with Python codebases for (1) linting and fixing code quality issues, (2) formatting Python code, (3) configuring Ruff settings, (4) understanding and resolving specific rule violations, (5) integrating Ruff into projects or editors, (6) migrating from other tools (Black, Flake8, isort, etc.), or (7) any Ruff-related development tasks. Includes complete documentation for 937+ lint rules, formatter settings, configuration options, and editor integrations.
---

# Ruff Professional Development

**Version:** 0.14.10 (Documentation generated December 2025)

## Overview

Ruff is an extremely fast Python linter and formatter written in Rust. It combines the functionality of multiple Python tools (Flake8, isort, Black, pyupgrade, and more) into a single high-performance tool.

This skill provides comprehensive guidance for:
- Configuring and integrating Ruff into Python projects
- Understanding and fixing lint rule violations
- Formatting Python code with Ruff's formatter
- Setting up editor integrations
- Migrating from other Python tooling

## Quick Start

### Installation

See `references/installation.md` for complete installation instructions across all platforms and package managers.

### Basic Usage

**Linting:**
```bash
ruff check .                    # Lint all files
ruff check path/to/file.py      # Lint specific file
ruff check --fix .              # Auto-fix violations
```

**Formatting:**
```bash
ruff format .                   # Format all files
ruff format path/to/file.py     # Format specific file
ruff format --check .           # Check formatting without changes
```

**Configuration:**
```toml
# pyproject.toml or ruff.toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I"]
ignore = ["E501"]
```

See `references/configuration.md` for comprehensive configuration options.

## Core Workflows

### 1. Integrating Ruff into a Project

**Steps:**
1. Install Ruff (see `references/installation.md`)
2. Create initial configuration (see `references/configuration.md`)
3. Run initial check: `ruff check .`
4. Review and configure rules (see `references/settings.md`)
5. Set up pre-commit hooks or CI integration (see `references/integrations.md`)

### 2. Fixing Lint Violations

**Process:**
1. Run `ruff check .` to identify violations
2. For specific rule violations, reference `references/rules/<rule-name>.md`
3. Apply automatic fixes: `ruff check --fix .`
4. Manual fixes for remaining violations using rule documentation

**Finding Rule Documentation:**
- All 937 rules are in `references/rules/`
- Rules are named by their description (e.g., `unused-import.md`, `line-too-long.md`)
- See `references/rules/rules.md` for complete rule index

### 3. Code Formatting

**Workflow:**
1. Review formatter overview: `references/formatter/overview.md`
2. Configure formatter settings in `pyproject.toml`
3. Run formatter: `ruff format .`
4. For Black compatibility: see `references/formatter/black.md`

### 4. Editor Integration

**Setup:**
1. Review `references/editors/overview.md` for editor support
2. Follow setup instructions: `references/editors/setup.md`
3. Configure editor settings: `references/editors/settings.md`
4. Explore editor features: `references/editors/features.md`

### 5. Migrating from Other Tools

**Migration paths:**
- **From Black:** See `references/formatter/black.md`
- **From Flake8/isort/pyupgrade:** See `references/configuration.md` for rule equivalents
- **General migration:** See `references/tutorial.md` for migration guidance

## Documentation Organization

This skill includes comprehensive reference documentation organized for efficient access:

**Navigation Guide:** `references/INDEX.md` - Complete index of all documentation with use-case based navigation

**Core Documentation:**
- `configuration.md` - Complete configuration reference
- `settings.md` - All available settings and options
- `linter.md` - Linter functionality and configuration
- `tutorial.md` - Comprehensive getting started guide

**Formatter:**
- `formatter/overview.md` - Formatter basics
- `formatter/black.md` - Black compatibility

**Rules (937 total):**
- `rules/rules.md` - Rules overview and index
- `rules/<rule-name>.md` - Individual rule documentation

**Editor Integration:**
- `editors/overview.md` - Editor support overview
- `editors/setup.md` - Installation instructions
- `editors/features.md` - Available features
- `editors/settings.md` - Configuration options

**Other Resources:**
- `installation.md` - Installation guide
- `integrations.md` - CI/CD and tool integrations
- `versioning.md` - Versioning and compatibility
- `preview.md` - Preview features
- `faq.md` - Frequently asked questions
- `contributing.md` - Contributing to Ruff

## Finding Specific Information

**For configuration questions:**
1. Start with `references/settings.md` for all available options
2. Review `references/configuration.md` for configuration patterns
3. Check `references/linter.md` or `references/formatter/overview.md` for component-specific settings

**For rule violations:**
1. Note the rule code/name from error message
2. Find corresponding file in `references/rules/`
3. Rules are alphabetically named (e.g., E501 → `line-too-long.md`)

**For editor setup:**
1. Check `references/editors/overview.md` for supported editors
2. Follow `references/editors/setup.md` for your editor
3. Configure with `references/editors/settings.md`

**For tool migration:**
1. Review `references/tutorial.md` for general guidance
2. See `references/formatter/black.md` for Black-specific migration
3. Check `references/configuration.md` for rule mapping from other linters

## Included Scripts

This skill includes Python scripts for updating documentation (located in `scripts/`):

- **scrape_ruff_docs.py** - Scrape a single Ruff documentation page
- **discover_ruff_docs.py** - Discover all Ruff documentation URLs
- **bulk_scrape_ruff.py** - Bulk scrape all Ruff documentation

These scripts use cloudscraper, BeautifulSoup, and markdownify to fetch and convert Ruff documentation.

## Best Practices

**When configuring Ruff:**
- Start with defaults and incrementally add rules
- Use `select` to enable rule categories, `ignore` for exceptions
- Test configuration changes incrementally
- Document reasoning for ignored rules in comments

**When fixing violations:**
- Review auto-fixes before committing
- Understand the rule before ignoring it
- Use inline ignores (`# noqa`) sparingly
- Consider if the rule should be disabled project-wide

**When formatting:**
- Run formatter before linter to avoid conflicts
- Configure line length consistently across tools
- Use `--check` in CI to verify formatting
- Format entire codebase at once when first adopting

**When integrating:**
- Set up editor integration for immediate feedback
- Add pre-commit hooks for team consistency
- Include in CI pipeline with appropriate settings
- Document Ruff configuration in project README

## Advanced Usage

**Performance optimization:**
- Use `--cache-dir` for faster repeated runs
- Configure file exclusions to skip irrelevant paths
- Leverage parallel execution (default behavior)

**Preview features:**
- See `references/preview.md` for experimental features
- Enable with `preview = true` in configuration
- Test preview rules before enabling in production

**Custom rule selection:**
- Combine rule categories: `select = ["E", "F", "I", "N"]`
- Use per-file ignores for specific patterns
- Configure different rules for different directories

## Documentation Coverage

This skill provides complete coverage of Ruff v0.14.10:
- 937 individual rule documentation files
- Full configuration and settings reference
- Complete editor integration guides
- Formatter documentation including Black compatibility
- Installation, integration, and migration guides
- FAQ and troubleshooting resources

All documentation is current as of December 2025 and reflects the latest stable release (0.14.10).
