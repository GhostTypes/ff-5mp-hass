#!/usr/bin/env python3
"""
Unpack a .skill file to a directory.

A .skill file is a zip archive. This script extracts it to a directory
with the same name (without .skill extension) and removes the original file.

Run: python unpack_skill.py <source.skill> [destination-dir]

If destination-dir is not specified, extracts to the same directory as the .skill file.
"""

import sys
import os
import zipfile
import shutil
from pathlib import Path


def unpack_skill(skill_file, dest_dir=None):
    """Unpack a .skill file to a directory."""
    skill_path = Path(skill_file)

    if not skill_path.exists():
        print(f"[ERROR] File not found: {skill_file}")
        return False

    if skill_path.suffix != ".skill":
        print(f"[ERROR] File must have .skill extension: {skill_file}")
        return False

    # Determine destination
    if dest_dir:
        dest_path = Path(dest_dir)
    else:
        dest_path = skill_path.parent / skill_path.stem

    # Check if destination already exists
    if dest_path.exists():
        print(f"[WARN] Destination exists, removing: {dest_path}")
        shutil.rmtree(dest_path)

    try:
        # Extract the zip
        with zipfile.ZipFile(skill_path, 'r') as zf:
            zf.extractall(dest_path)

        # Remove the original .skill file
        skill_path.unlink()

        # Verify SKILL.md exists
        skill_md = dest_path / "SKILL.md"
        if skill_md.exists():
            print(f"[OK] Unpacked: {skill_path.name} -> {dest_path.name}/")
            return True
        else:
            print(f"[WARN] Unpacked but no SKILL.md found in {dest_path.name}/")
            return True

    except zipfile.BadZipFile:
        print(f"[ERROR] Invalid zip file: {skill_file}")
        return False
    except Exception as e:
        print(f"[ERROR] Failed to unpack: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python unpack_skill.py <source.skill> [destination-dir]")
        print("\nUnpacks a .skill file (zip archive) to a directory.")
        sys.exit(1)

    skill_file = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else None

    success = unpack_skill(skill_file, dest_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
