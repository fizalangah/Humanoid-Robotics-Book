---
id: 0004
title: Generate Tasks for Formatting and Image Replacement
stage: tasks
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 2-image-cleanup-default-chapters
branch: 2-image-cleanup-default-chapters
user: user
command: /sp.tasks
labels: ["task-generation", "formatting-fix", "image-replacement"]
links:
  spec: specs/2-image-cleanup-default-chapters/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/2-image-cleanup-default-chapters/tasks.md
tests:
  -
---

## Prompt

Fix Bad Formatting + Proper Image Replacement

Your job is to repair the MDX files and correctly place generated images.

---

## 1. Front-Matter Rules (IMPORTANT)

When you edit any MDX file:

- Do NOT print front-matter inside the page body.
- Do NOT duplicate the front-matter.
- Keep the front-matter ONLY at the very top of the file, inside a YAML block like:

---
id: chapter-id
title: Chapter Title
description: ...
---

If any file contains front-matter printed as plain text inside the page, REMOVE that text completely.

---

## 2. Image Placeholder Replacement

Find any text blocks that contain:

- "IMAGE PLACEHOLDER"
- "IMAGE/DIAGRAM PLACEHOLDER"
- "DIAGRAM PLACEHOLDER"
- Or anything similar

For each placeholder:

1. Understand the surrounding context.
2. Generate a relevant conceptual illustration.
3. Replace ONLY the placeholder with this MDX component:

```mdx
<div class="ai-generated-image">
  <img src="GENERATED_IMAGE_URL" alt="IMAGE_DESCRIPTION" />
  <p class="image-caption">AI-Generated Image: IMAGE_DESCRIPTION</p>
</div>
```
Do not add extra code, comments, or debug text.

3. Do Not Modify Normal Content
Do NOT rewrite the chapter text.

Do NOT add new headings.

Do NOT insert front-matter again.

Do NOT move or restructure sections.

Only fix formatting errors and replace placeholders.

4. Remove Default Docusaurus Pages
Delete all pages that come from the default installation.
Remove examples like:

/docs/intro.md

/docs/tutorial-basics/*

/docs/tutorial-extras/*

Blog, community, or sample pages

Keep ONLY my textbook pages.

5. Deliverables
After applying all fixes, return:

The corrected MDX content for each changed file.

A list of removed default pages.

Confirmation that front-matter is clean and no longer showing inside pages.

6. Constraints
Maintain valid MDX formatting.

No extra characters, no code fences unless required.

Do not output front-matter anywhere except at the file top.

yaml
Copy code

---

If you want, I can also:

✅ Generate a **validation script** to check the whole project automatically
or
✅ Give you a version specifically for **Claude Code Router (MCP)**

Just tell me.

## Response snapshot

Generated new `tasks.md` with 14 tasks organized into phases for front-matter cleaning, image replacement, content integrity validation, default page removal, and final validation. Identified parallelization opportunities and defined an MVP-first, incremental delivery strategy.

## Outcome

- ✅ Impact: Detailed `tasks.md` generated, providing clear steps for the requested feature, improving workflow clarity.
- 🧪 Tests: No tests performed during task generation.
- 📁 Files: Created `specs/2-image-cleanup-default-chapters/tasks.md`.
- 🔁 Next prompts: Proceed to `/sp.implement` using the newly generated `tasks.md`.
- 🧠 Reflection: Successfully translated complex user instructions into a granular, actionable task list, adhering to strict formatting and organizational rules. The task breakdown ensures a structured approach to fixing formatting and replacing images.

## Evaluation notes (flywheel)

- Failure modes observed: None during task generation.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
