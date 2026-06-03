# Contributing

Thank you for helping improve this Codex skill.

## Project Scope

This repository should stay focused on reusable public guidance for Apple-inspired Liquid Glass web UI design. Good contributions improve:

- The skill trigger description or workflow.
- Accessibility, responsive design, motion, or contrast guidance.
- Web implementation patterns for CSS, React, Tailwind, or similar frontend stacks.
- Example prompts that make the skill easier to test.
- Security, privacy, licensing, or validation automation.

Please do not add proprietary assets, Apple logos, SF Symbols, private screenshots, customer data, API keys, or business-specific code.

## Local Validation

Run this before submitting changes:

```powershell
python .\scripts\validate_skill.py .\apple-liquid-glass-ui
```

The validator checks the skill frontmatter, metadata, required references, placeholder text, and non-English text in repository documentation.

## Pull Request Checklist

- Keep the skill concise and practical.
- Put detailed implementation notes in `references/` instead of overloading `SKILL.md`.
- Include examples when changing behavior.
- Keep all public documentation in English.
- Run the validation script and fix any reported issue.

## Style

Use plain, direct English. Prefer guidance that an AI coding agent can execute over broad design theory.
