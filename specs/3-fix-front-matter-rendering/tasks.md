# Tasks: Fix Front-Matter Rendering in Two MDX Files

**Input**: Design documents from `/specs/3-fix-front-matter-rendering/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are explicitly not requested for this task; validation will rely on `npm run build`.

**Organization**: Tasks are grouped by the specific MDX file they target to enable clear, independent processing and validation.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup

**Purpose**: Prepare the environment for front-matter remediation.

- [ ] T001 Update todo list for current task

---

## Phase 2: User Story 1 - Fix Front-Matter in `docs/physical-ai/introduction.mdx` (Priority: P1) 🎯 MVP

**Goal**: Ensure `docs/physical-ai/introduction.mdx` has its front-matter correctly formatted at the top, with no duplicate front-matter text rendered within the page body.

**Independent Test**: Manually inspect `docs/physical-ai/introduction.mdx` for rendered front-matter; `npm run build` should pass.

### Implementation for User Story 1

- [ ] T002 [US1] Read the content of docs/physical-ai/introduction.mdx
- [ ] T003 [US1] Identify and remove rendered front-matter lines from the body of docs/physical-ai/introduction.mdx
- [ ] T004 [US1] Write the corrected content back to docs/physical-ai/introduction.mdx

**Checkpoint**: At this point, `docs/physical-ai/introduction.mdx` should be correctly formatted.

---

## Phase 3: User Story 2 - Fix Front-Matter in `docs/robotics-algorithms/simulation-basics.mdx` (Priority: P2)

**Goal**: Ensure `docs/robotics-algorithms/simulation-basics.mdx` has its front-matter correctly formatted at the top, with no duplicate front-matter text rendered within the page body.

**Independent Test**: Manually inspect `docs/robotics-algorithms/simulation-basics.mdx` for rendered front-matter; `npm run build` should pass.

### Implementation for User Story 2

- [ ] T005 [US2] Read the content of docs/robotics-algorithms/simulation-basics.mdx
- [ ] T006 [US2] Identify and remove rendered front-matter lines from the body of docs/robotics-algorithms/simulation-basics.mdx
- [ ] T007 [US2] Write the corrected content back to docs/robotics-algorithms/simulation-basics.mdx

**Checkpoint**: Both `docs/physical-ai/introduction.mdx` and `docs/robotics-algorithms/simulation-basics.mdx` should now be correctly formatted.

---

## Phase 4: Validation & Cross-Cutting Concerns

**Purpose**: Confirm overall project integrity after modifications.

- [ ] T008 Run `npm run build` to confirm the Docusaurus project builds without errors
- [ ] T009 Create PHR for task generation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **User Story 1 (Phase 2)**: Depends on Setup completion.
- **User Story 2 (Phase 3)**: Depends on Setup completion. Can be worked on in parallel with User Story 1, but sequential execution is also viable.
- **Validation (Phase 4)**: Depends on User Story 1 and User Story 2 completion.

### Within Each User Story

- Reading the file (T002, T005) must precede identifying and removing front-matter (T003, T006).
- Identifying and removing front-matter (T003, T006) must precede writing the corrected content (T004, T007).

### Parallel Opportunities

- Tasks T002-T004 (for `introduction.mdx`) and T005-T007 (for `simulation-basics.mdx`) can conceptually be considered parallelizable if independent agents handle them, as they target different files. However, within a single agent context, they will be executed sequentially per file.

---

## Parallel Example: User Stories 1 and 2 (Conceptual)

```bash
# If processed by multiple agents:
Task: "Read docs/physical-ai/introduction.mdx"
Task: "Read docs/robotics-algorithms/simulation-basics.mdx"
# ... then process and write back in parallel
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: User Story 1 (`docs/physical-ai/introduction.mdx` fix)
3. **STOP and VALIDATE**: Manually inspect `docs/physical-ai/introduction.mdx`. Run `npm run build`.

### Incremental Delivery

1. Complete Setup.
2. Add User Story 1 (`docs/physical-ai/introduction.mdx` fix) → Validate.
3. Add User Story 2 (`docs/robotics-algorithms/simulation-basics.mdx` fix) → Validate.
4. Run final `npm run build` after both files are corrected.

---

## Notes

- The focus is solely on fixing the rendered front-matter and nothing else.
- Each file fix is independently verifiable.
- Verify `npm run build` passes after modifications.
