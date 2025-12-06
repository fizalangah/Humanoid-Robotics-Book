# Tasks: Polish Textbook: Front-Matter, Images, Formatting, Structure

**Branch**: `4-polish-textbook` | **Date**: 2025-12-07 | **Spec**: specs/4-polish-textbook/spec.md
**Input**: Implementation plan from `/specs/4-polish-textbook/plan.md`

---

## Summary

This document outlines the step-by-step tasks for the "Polish Textbook" feature, focusing on fixing front-matter rendering, replacing image placeholders, removing default Docusaurus content, correcting MDX formatting, and standardizing chapter structure. The goal is to deliver a fully polished, error-free, and properly rendered Docusaurus book.

---

## Dependencies

Phases are sequential. Within each phase, tasks are ordered logically, with `[P]` indicating parallelizable tasks.

---

## Implementation Strategy

Tasks will be executed phase-by-phase, ensuring each set of changes is validated before proceeding. This incremental approach minimizes errors and ensures adherence to the specification.

---

## Phase 1: Setup & Pre-checks

- [X] T001 Update todo list for current task

## Phase 2: Fix Front-Matter Rendering

- [X] T002 Find all MDX files in docs/ to check for front-matter issues
- [X] T003 [P] For each file found, read content and correct front-matter for docs/physical-ai/introduction.mdx
- [X] T004 [P] For each file found, read content and correct front-matter for docs/humanoid-robotics/ros2-overview.mdx
- [X] T005 [P] For each file found, read content and correct front-matter for docs/robotics-algorithms/simulation-basics.mdx
- [X] T006 [P] For each file found, read content and correct front-matter for docs/project-applications/humanoid-vla.mdx

## Phase 3: Replace All Image Placeholders with Real Images

- [X] T007 Find all MDX files in docs/ containing image placeholders
- [X] T008 Create image directory if it doesn't exist: static/img/auto/
- [X] T009 [P] For each placeholder in docs/physical-ai/introduction.mdx, generate and insert image placeholder (retry on failure)
- [X] T010 [P] For each placeholder in docs/humanoid-robotics/ros2-overview.mdx, generate and insert image placeholder (retry on failure)
- [X] T011 [P] For each placeholder in docs/robotics-algorithms/simulation-basics.mdx, generate and insert image placeholder (retry on failure)
- [X] T012 [P] For each placeholder in docs/project-applications/humanoid-vla.mdx, generate and insert image placeholder (retry on failure)

## Phase 4: Remove Default Docusaurus Template Chapters

- [X] T013 Delete docs/intro.md (if exists)
- [X] T014 Delete docs/tutorial-basics/ directory (if exists)
- [X] T015 Delete docs/tutorial-extras/ directory (if exists)
- [X] T016 Delete blog/ directory (if exists)
- [X] T017 Inspect docusaurus.config.ts for default references and remove/update if found
- [X] T018 Inspect sidebars.ts for default references and remove/update if found

## Phase 5: Fix All MDX Formatting Issues

- [X] T019 Find all MDX files in docs/ for formatting review
- [X] T020 [P] For each file, review and correct formatting issues in docs/physical-ai/introduction.mdx
- [X] T021 [P] For each file, review and correct formatting issues in docs/humanoid-robotics/ros2-overview.mdx
- [X] T022 [P] For each file, review and correct formatting issues in docs/robotics-algorithms/simulation-basics.mdx
- [X] T023 [P] For each file, review and correct formatting issues in docs/project-applications/humanoid-vla.mdx

## Phase 6: Standardize Chapter Structure

- [X] T024 Verify all MDX chapters in docs/ start with valid front matter
- [X] T025 Verify all MDX chapters in docs/ contain a clear title (from front matter)
- [X] T026 Verify all MDX chapters in docs/ use consistent heading hierarchy
- [X] T027 Verify no junk text or template leftovers in docs/physical-ai/introduction.mdx
- [X] T028 Verify no junk text or template leftovers in docs/humanoid-robotics/ros2-overview.mdx
- [X] T029 Verify no junk text or template leftovers in docs/robotics-algorithms/simulation-basics.mdx
- [X] T030 Verify no junk text or template leftovers in docs/project-applications/humanoid-vla.mdx

## Phase 7: Final Validation & Cleanup

- [X] T031 Run `npm run build` to confirm the Docusaurus project builds without errors
- [ ] T032 Create PHR for task generation
