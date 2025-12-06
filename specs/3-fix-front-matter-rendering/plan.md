# Implementation Plan: Fix Front-Matter Rendering in Two MDX Files

**Branch**: `3-fix-front-matter-rendering` | **Date**: 2025-12-06 | **Spec**: specs/3-fix-front-matter-rendering/spec.md
**Input**: Feature specification from `/specs/3-fix-front-matter-rendering/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The primary requirement is to fix front-matter rendering issues in `docs/physical-ai/introduction.mdx` and `docs/robotics-algorithms/simulation-basics.mdx`. This involves carefully identifying and removing any accidental front-matter text that has been rendered *inside the visible page body* of these files, while strictly preserving the correct YAML front-matter block at the very top of each file. The technical approach will involve reading the specified MDX files, performing precise string manipulation to remove the duplicated front-matter lines, and then writing the corrected content back to the files. A crucial validation step will be to confirm that the Docusaurus project builds successfully without any errors after the modifications.

## Technical Context

**Language/Version**: Markdown/MDX, TypeScript (for Docusaurus config)
**Primary Dependencies**: Docusaurus
**Storage**: files
**Testing**: npm run build
**Target Platform**: Web (Docusaurus static site)
**Project Type**: web
**Performance Goals**: N/A (static content, formatting fix)
**Constraints**: Maintain valid MDX formatting; no extra characters or code fences unless required; strictly preserve all existing content, headings, and images; do not modify any other chapters.
**Scale/Scope**: Limited to two specific MDX files (`docs/physical-ai/introduction.mdx` and `docs/robotics-algorithms/simulation-basics.mdx`).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The plan adheres to the project Constitution:
- **AI-Native Production:** Content will be fixed using SpecKit + Claude Code workflows.
- **Technical Accuracy:** Fixes will ensure correct MDX parsing and Docusaurus rendering.
- **Beginner-Friendly, Consistency, Error-Free:** The core goal is to eliminate rendering errors and maintain a clean, consistent format.
- **Markdown Standards:** Specifically targets correct front-matter placement and syntax.
- **Docusaurus Standards:** Ensures MDX compiles without errors/warnings and maintains file organization.
- **AI Implementation Rules:** Adheres to SpecKit workflows and avoids breaking Docusaurus structure.
- **Success Criteria:** Aims for error-free builds and correct content display.

No violations are detected as this task focuses on corrective formatting within the existing structure.

## Project Structure

### Documentation (this feature)

```text
specs/3-fix-front-matter-rendering/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
docs/
├── physical-ai/
│   └── introduction.mdx # Target file for modification
└── robotics-algorithms/
    └── simulation-basics.mdx # Target file for modification

src/
└── pages/
    └── index.tsx # No modification expected, but relevant for Docusaurus context

docusaurus.config.ts # No modification expected, but relevant for Docusaurus context
```

**Structure Decision**: The modifications are localized to the two specified MDX files within the existing `docs/` structure. No new source code files or directories are expected to be created for this feature. The Docusaurus configuration files (`docusaurus.config.ts`, `src/pages/index.tsx`) are part of the broader project context but are not expected to be modified by this specific fix.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - No constitution violations have been identified.
