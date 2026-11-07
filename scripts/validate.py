#!/usr/bin/env python3
"""Validate SKILL.md frontmatter, required files and relative Markdown links."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "references/angle-library.md",
    "references/three-checks.md",
    "references/examples.md",
    "templates/output-template.md",
    "templates/title-feedback-log.md",
]

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LEN = 64
MAX_DESCRIPTION_LEN = 1024
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

errors = []


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        errors.append("SKILL.md: must start with '---' frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append("SKILL.md: frontmatter is not closed with '---'")
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep or line[0].isspace():
            errors.append(f"SKILL.md: unsupported frontmatter line: {line!r}")
            continue
        fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_frontmatter():
    path = ROOT / "SKILL.md"
    if not path.exists():
        return
    fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append("SKILL.md: missing 'name'")
    elif not NAME_RE.match(name) or len(name) > MAX_NAME_LEN:
        errors.append(f"SKILL.md: invalid name {name!r} (lowercase letters, digits, hyphens; <= {MAX_NAME_LEN})")
    if not description:
        errors.append("SKILL.md: missing 'description'")
    elif len(description) > MAX_DESCRIPTION_LEN:
        errors.append(f"SKILL.md: description is {len(description)} chars (> {MAX_DESCRIPTION_LEN})")
    unknown = set(fields) - {"name", "description", "license", "metadata", "allowed-tools", "compatibility"}
    if unknown:
        errors.append(f"SKILL.md: unexpected frontmatter keys: {sorted(unknown)}")


def check_required_files():
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing required file: {rel}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {rel}")


def check_relative_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (md.parent / file_part).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")


def main():
    check_required_files()
    check_frontmatter()
    check_relative_links()
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print(f"OK: frontmatter valid, {len(REQUIRED_FILES)} required files present, relative links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
