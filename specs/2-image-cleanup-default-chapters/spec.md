Auto-Insert Images & Remove Default Chapters

**Task Goal**
Scan the entire Docusaurus project and:
1. Automatically replace every “IMAGE/DIAGRAM PLACEHOLDER” block with a newly generated, context-relevant image.
2. Remove all default/template chapters that come with a fresh Docusaurus installation.
3. Keep only the chapters that belong to my textbook.

---

## 1. Image Insertion Requirements

**Detection**
- Search all MDX/Markdown files for any text containing:
  - "IMAGE/DIAGRAM PLACEHOLDER"
  - "IMAGE PLACEHOLDER"
  - "DIAGRAM PLACEHOLDER"
  - or any similar variant.

**Image Generation**
For each placeholder:
- Read the surrounding content.
- Generate a relevant conceptual illustration (not a real photo).
- Produce a clean PNG or JPG image.
- Upload or host it (according to Claude’s capabilities) and provide a usable link.
- **Error Handling**: If image generation fails, insert a generic "Image Generation Failed" placeholder with a broken image link (`/img/image-generation-failed.png`) and log a warning.

**Insertion Format**
Replace the placeholder with this MDX block:

```mdx
<div class="ai-generated-image">
  <img src="GENERATED_IMAGE_URL" alt="IMAGE_DESCRIPTION" />
  <p class="image-caption">AI-Generated Image: IMAGE_DESCRIPTION</p>
</div>
```
Rules

Remove the placeholder text entirely.

Do not change or delete any other content.

Ensure final MDX is valid for Docusaurus.

## 2. Remove Default Docusaurus Chapters
Action
Identify and delete any chapters, pages, or sidebar entries that come from the default Docusaurus template, including but not limited to:

Introduction pages that are not part of my textbook

Tutorial examples

Blog, Community, or redundant template sections

Placeholder docs from /docs/intro.md, /docs/tutorial-basics, /docs/tutorial-extras, etc.

Rules

Only keep the chapters that belong to my textbook.

Ensure the final sidebar reflects only the correct book structure.

Preserve all custom pages I created.

## 3. Deliverables
After completing the task, provide:

A list of all files where placeholders were replaced.

A list of all removed default/template chapters.

The updated MDX content for each changed file.

Confirmation that the Docusaurus project builds without errors.

## 4. Constraints
Do not alter non-placeholder content.

Do not add new chapters unless instructed.

Keep folder structure clean and consistent.

If you want, I can also create:

✅ A version specifically for **Claude Code Router (MCP)**
or
✅ A version specifically for **Claude Prompt Library (Reusable Template)**

Just tell me!