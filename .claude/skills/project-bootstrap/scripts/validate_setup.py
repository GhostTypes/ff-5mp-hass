#!/usr/bin/env python3
"""
Validate a project's .claude setup.

Checks:
- All skills have valid SKILL.md files
- All agents have valid YAML frontmatter
- No orphaned .skill files (should be unpacked)

Run: python validate_setup.py [project-dir]
"""

import sys
import os
import zipfile
import re
from pathlib import Path


def validate_skill_md(skill_dir):
    """Validate a skill directory has proper SKILL.md."""
    errors = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        errors.append(f"Missing SKILL.md in {skill_dir.name}")
        return errors

    try:
        content = skill_md.read_text(encoding="utf-8")

        # Check frontmatter
        if not content.startswith("---"):
            errors.append(f"{skill_dir.name}/SKILL.md: Missing YAML frontmatter")
            return errors

        # Find closing frontmatter
        end_idx = content.find("\n---", 4)
        if end_idx == -1:
            errors.append(f"{skill_dir.name}/SKILL.md: Unclosed frontmatter")
            return errors

        frontmatter = content[4:end_idx]

        # Check required fields
        if "name:" not in frontmatter:
            errors.append(f"{skill_dir.name}/SKILL.md: Missing 'name' in frontmatter")
        if "description:" not in frontmatter:
            errors.append(f"{skill_dir.name}/SKILL.md: Missing 'description' in frontmatter")

    except Exception as e:
        errors.append(f"{skill_dir.name}/SKILL.md: Error reading file: {e}")

    return errors


def validate_agent_md(agent_file):
    """Validate an agent markdown file."""
    errors = []

    try:
        content = agent_file.read_text(encoding="utf-8")

        # Check frontmatter
        if not content.startswith("---"):
            errors.append(f"{agent_file.name}: Missing YAML frontmatter")
            return errors

        end_idx = content.find("\n---", 4)
        if end_idx == -1:
            errors.append(f"{agent_file.name}: Unclosed frontmatter")
            return errors

        frontmatter_text = content[4:end_idx]

        # Parse frontmatter
        frontmatter = {}
        for line in frontmatter_text.strip().split("\n"):
            if ":" in line and not line.strip().startswith("#"):
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()

        # Check required fields
        if "name" not in frontmatter:
            errors.append(f"{agent_file.name}: Missing 'name' in frontmatter")
        if "description" not in frontmatter:
            errors.append(f"{agent_file.name}: Missing 'description' in frontmatter")

        # Check name format
        if "name" in frontmatter:
            name = frontmatter["name"]
            if not re.match(r'^[a-z0-9-]+$', name):
                errors.append(f"{agent_file.name}: Invalid name '{name}' (lowercase, numbers, hyphens only)")

        # Check description is single line
        if "description" in frontmatter:
            desc = frontmatter["description"]
            if "\n" in desc:
                errors.append(f"{agent_file.name}: Description must be single line")

        # Check model if present
        valid_models = {"sonnet", "opus", "haiku", "inherit"}
        if "model" in frontmatter:
            model = frontmatter["model"].lower()
            if model not in valid_models:
                errors.append(f"{agent_file.name}: Invalid model '{model}'")

    except Exception as e:
        errors.append(f"{agent_file.name}: Error reading file: {e}")

    return errors


def check_orphaned_skill_files(skills_dir):
    """Check for .skill files that should be unpacked."""
    orphans = []

    if not skills_dir.exists():
        return orphans

    for item in skills_dir.iterdir():
        if item.suffix == ".skill":
            orphans.append(item.name)

    return orphans


def validate_project(project_dir):
    """Validate the entire .claude setup."""
    project_path = Path(project_dir)
    claude_dir = project_path / ".claude"

    errors = []
    warnings = []
    skills_found = []
    agents_found = []

    if not claude_dir.exists():
        print(f"[INFO] No .claude directory found at {project_dir}")
        return errors, warnings, skills_found, agents_found

    # Validate skills
    skills_dir = claude_dir / "skills"
    if skills_dir.exists():
        for item in skills_dir.iterdir():
            if item.is_dir():
                skill_errors = validate_skill_md(item)
                errors.extend(skill_errors)
                if not skill_errors:
                    skills_found.append(item.name)
            elif item.suffix == ".skill":
                warnings.append(f"Unpacked skill file: {item.name} (should be unpacked)")

        # Check for orphaned .skill files
        orphans = check_orphaned_skill_files(skills_dir)
        for orphan in orphans:
            warnings.append(f"Orphaned .skill file: {orphan} (unpack it)")

    # Validate agents
    agents_dir = claude_dir / "agents"
    if agents_dir.exists():
        for item in agents_dir.iterdir():
            if item.is_file() and item.suffix == ".md":
                agent_errors = validate_agent_md(item)
                errors.extend(agent_errors)
                if not agent_errors:
                    agents_found.append(item.stem)

    return errors, warnings, skills_found, agents_found


def main():
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = os.getcwd()

    print(f"Validating .claude setup in: {project_dir}")
    print("-" * 50)

    errors, warnings, skills_found, agents_found = validate_project(project_dir)

    # Report skills
    if skills_found:
        print(f"\n[SKILLS] {len(skills_found)} valid skill(s):")
        for skill in sorted(skills_found):
            print(f"  - {skill}")
    else:
        print("\n[SKILLS] No skills found")

    # Report agents
    if agents_found:
        print(f"\n[AGENTS] {len(agents_found)} valid agent(s):")
        for agent in sorted(agents_found):
            print(f"  - {agent}")
    else:
        print("\n[AGENTS] No agents found")

    # Report warnings
    if warnings:
        print(f"\n[WARNINGS] {len(warnings)}:")
        for warning in warnings:
            print(f"  - {warning}")

    # Report errors
    if errors:
        print(f"\n[ERRORS] {len(errors)}:")
        for error in errors:
            print(f"  - {error}")
        print("\n[FAIL] Validation failed")
        sys.exit(1)
    else:
        print("\n[PASS] Validation passed")
        sys.exit(0)


if __name__ == "__main__":
    main()
