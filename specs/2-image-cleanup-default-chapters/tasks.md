Feature: Fix Bad Formatting + Proper Image Replacement

## Task List

### Phase 1: Front-Matter Cleaning
- [ ] T001 Find all MDX files in `docs/` that contain duplicate front-matter or front-matter printed as plain text inside the page body.
- [ ] T002 For each identified file, remove any duplicate or plain text front-matter from the page body, ensuring front-matter exists only once at the very top of the file in YAML format. (e.g., `docs/physical-ai/introduction.mdx`)

### Phase 2: Image Placeholder Replacement
- [ ] T003 Identify all MDX/Markdown files in `docs/` that contain image placeholders (e.g., "IMAGE PLACEHOLDER", "IMAGE/DIAGRAM PLACEHOLDER", "DIAGRAM PLACEHOLDER").
- [ ] T004 For each detected placeholder in each file, understand the surrounding context and generate a relevant conceptual illustration (simulated image generation).
- [ ] T005 For each placeholder, replace ONLY the placeholder text with the specified MDX image component, including the simulated `GENERATED_IMAGE_URL` and `IMAGE_DESCRIPTION`. (e.g., `docs/physical-ai/introduction.mdx`)

### Phase 3: Content Integrity Validation
- [ ] T006 Verify that no chapter text was rewritten or new headings added during the previous steps. (Manual review/diff)
- [ ] T007 Confirm that no front-matter was accidentally re-inserted into the page body. (Manual review/diff)
- [ ] T008 Ensure no sections were moved or restructured beyond what was necessary for placeholder replacement. (Manual review/diff)

### Phase 4: Remove Default Docusaurus Pages
- [ ] T009 Identify all default Docusaurus installation pages and directories to be removed (e.g., `/docs/intro.md`, `/docs/tutorial-basics/*`, `/docs/tutorial-extras/*`, `blog/`).
- [ ] T010 Delete all identified default Docusaurus pages and directories, ensuring only custom textbook pages remain. (e.g., `rm -rf docs/intro.md docs/tutorial-basics blog`)

### Phase 5: Deliverables & Final Validation
- [ ] T011 Compile a list of all MDX files where formatting was fixed and/or image placeholders were replaced.
- [ ] T012 Compile a list of all removed default Docusaurus pages and directories.
- [ ] T013 Confirm that front-matter is clean and no longer showing inside any pages across the entire project. (Implicitly verified by T001/T002)
- [ ] T014 Run a Docusaurus build (`npm run build`) to confirm the entire project builds successfully without errors or warnings.

## Dependencies
- T001 -> T002
- T003 -> T004 -> T005
- T002 & T005 -> T006, T007, T008
- T008 -> T009 -> T010
- T010 -> T011, T012
- T012 -> T013
- All tasks must be completed before T014

## Parallel Execution Examples
- Tasks T002 and T005 can be executed in parallel across different MDX files.
- Tasks T006, T007, T008 can be performed concurrently with T009 and T010, provided the file deletions don't interfere with the content validation of existing textbook chapters.

## Implementation Strategy
- **MVP First**: Focus initially on completing all front-matter fixes and image placeholder replacements for the existing textbook chapters.
- **Incremental Delivery**: Tackle default page removal as a separate, subsequent step once content integrity is assured.
- **Validation-Driven**: Each phase concludes with explicit validation steps to minimize rework.
