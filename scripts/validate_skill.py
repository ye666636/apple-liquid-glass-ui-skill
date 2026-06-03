#!/usr/bin/env python3
"""Validate the Codex skill package without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]+$")
NON_ASCII_RE = re.compile(r"[^\x00-\x7f]")
TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".txt", ".gitignore"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path} is not valid UTF-8: {exc}")


def parse_frontmatter(skill_md: Path) -> tuple[dict[str, str], str]:
    content = read_text(skill_md)
    if not content.startswith("---\n"):
        fail(f"{skill_md} must start with YAML frontmatter")
    end = content.find("\n---\n", 4)
    if end == -1:
        fail(f"{skill_md} must close YAML frontmatter with ---")

    raw = content[4:end]
    body = content[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line in {skill_md}: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data, body


def validate_skill(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"Missing {skill_md}")

    frontmatter, body = parse_frontmatter(skill_md)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        fail("SKILL.md frontmatter is missing name")
    if not NAME_RE.match(name):
        fail(f"Skill name must use lowercase letters, digits, and hyphens: {name}")
    if skill_dir.name != name:
        fail(f"Skill folder name must match frontmatter name: {skill_dir.name} != {name}")
    if len(description) < 80:
        fail("Skill description should explain what it does and when to use it")
    if "TODO" in body or "TODO" in description:
        fail("SKILL.md still contains TODO text")

    required_refs = [
        skill_dir / "references" / "apple-principles.md",
        skill_dir / "references" / "web-patterns.md",
    ]
    for ref in required_refs:
        if not ref.exists():
            fail(f"Missing required reference: {ref}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        fail(f"Missing {openai_yaml}")
    metadata = read_text(openai_yaml)
    for key in ["display_name", "short_description", "default_prompt"]:
        if key not in metadata:
            fail(f"{openai_yaml} is missing interface.{key}")
    if f"${name}" not in metadata:
        fail(f"{openai_yaml} default_prompt should mention ${name}")


def validate_public_text(repo_root: Path) -> None:
    for path in repo_root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix not in TEXT_EXTENSIONS and path.name != ".gitignore":
            continue
        content = read_text(path)
        match = NON_ASCII_RE.search(content)
        if match:
            fail(f"Non-ASCII text found in {path}: {match.group(0)!r}")


def main(argv: list[str]) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    skill_dir = Path(argv[1]).resolve() if len(argv) > 1 else repo_root / "apple-liquid-glass-ui"
    validate_skill(skill_dir)
    validate_public_text(repo_root)
    print("Skill package validation passed.")


if __name__ == "__main__":
    main(sys.argv)
