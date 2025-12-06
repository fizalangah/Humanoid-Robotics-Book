Project Name: AI/Spec-Driven Textbook — Physical AI & Humanoid Robotics
Feature: Fix Front-Matter Rendering in Two MDX Files
Short Name: fix-front-matter-rendering
Documentation Framework: Docusaurus (https://docusaurus.io/)

---

## Task Goal
Fix front-matter rendering issues in `docs/physical-ai/introduction.mdx` and `docs/robotics-algorithms/simulation-basics.mdx`.

### 1. Remove Rendered Front-Matter
Inside these two files, delete any accidental text such as:
- `id: '...'`
- `slug: ...`
- `title: ...`
- `description: ...`
- `version: ...`
- `author: ...`
Front-matter must NOT appear inside the visible page body.

### 2. Preserve Front-Matter Block
Keep ONLY the YAML front-matter at the very top of each file, formatted as:

```yaml
---
id: chapter-id
title: Chapter Title
description: ...
version: '1.0'
author: Fiza
---
```
Do NOT modify this block unless absolutely required for MDX validity.

### 3. Do Not Change Anything Else
- Do NOT rewrite chapter content.
- Do NOT rewrite headings.
- Do NOT rewrite text.
- Do NOT add or remove sections.
- Do NOT generate new images.
- Do NOT replace existing placeholders.
- Do NOT modify any other chapters.

The task is ONLY to:
- Remove duplicated/rendered front-matter lines that appear inside the visible content.
- Keep the layout and existing text untouched.

---

## Deliverables
After completing the task, provide:
- The corrected MDX content for `docs/physical-ai/introduction.mdx`.
- The corrected MDX content for `docs/robotics-algorithms/simulation-basics.mdx`.
- Confirmation that the Docusaurus project builds without errors.

---

## Constraints
- Maintain valid MDX formatting.
- No extra characters or code fences unless required.
- Do not output front-matter anywhere except at the file top.
- The solution must be compatible with the current Docusaurus setup.
