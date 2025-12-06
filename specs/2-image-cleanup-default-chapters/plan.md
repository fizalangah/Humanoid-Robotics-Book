Project: AI/Spec-Driven Textbook — Physical AI & Humanoid Robotics
Feature: Auto-Insert Images & Remove Default Chapters
Author: Fiza
Version: 1.0
Status: Draft

---

## 1. Scope and Dependencies:

### In Scope:
- Detecting and replacing image/diagram placeholders in existing MDX/Markdown files with AI-generated image URLs and descriptions.
- Deleting default Docusaurus template chapters (e.g., `intro.md`, tutorial directories).
- Ensuring only custom textbook chapters remain.
- Updating `sidebars.ts` to reflect the removal of default chapters.
- Validating that the Docusaurus project builds without errors after changes.
- Providing a list of affected files and removed chapters as deliverables.

### Out of Scope:
- Generating new textbook chapters.
- Modifying existing textbook chapter content beyond placeholder replacement.
- Implementing image hosting or AI image generation tools; it is assumed Claude Code has this capability.
- Altering non-placeholder content in any files.
- Adding new image placeholders.

### External Dependencies:
- **Claude Code's Image Generation Capability**: Required for generating context-relevant images and providing URLs.
- **Docusaurus Project Structure**: Reliance on the existing Docusaurus setup for identifying default chapters and building the site.

---

## 2. Key Decisions and Rationale:

### Options Considered:
- **Manual Image Insertion**: User manually finds placeholders and provides image URLs.
- **Automated Image Insertion (Chosen)**: Claude Code automatically detects placeholders, generates images, and inserts them.

### Trade-offs:
- **Manual**: High user effort, potential for inconsistencies, slower. **Automated**: Low user effort, consistent, faster, but relies on Claude's image generation capabilities.

### Rationale:
- Automated approach aligns with the AI-Native Production principle from the Project Constitution and significantly reduces manual effort, promoting efficiency and consistency.

---

## 3. Interfaces and API Contracts:

### Internal API Interactions (Claude Code):
- **File System Access**: `Glob` to find MDX/Markdown files; `Read` to get file content; `Edit`/`Write` to replace placeholders and delete files.
- **Image Generation**: Assumed internal Claude Code capability to generate images and provide URLs/descriptions.

---

## 4. Non-Functional Requirements (NFRs) and Budgets:

### Performance:
- The process should be efficient enough to complete within typical interactive session limits for a small to medium-sized Docusaurus project.

### Reliability:
- The process must be robust; if image generation fails for a placeholder, it should be logged or handled gracefully without crashing the entire operation.
- File operations must be atomic where possible to prevent data loss or corruption.

### Security:
- No sensitive data should be exposed or modified during the image generation or file cleanup process.
- Only authorized files and directories should be accessed/modified.

---

## 5. Data Management and Migration:

### Source of Truth:
- Existing MDX/Markdown files are the source of truth for content.
- The generated image URLs become part of the content and should be stable.

### Schema Evolution:
- No significant schema changes are anticipated, only content modification within existing MDX structure.

### Migration and Rollback:
- Git branching provides a natural rollback mechanism (revert the feature branch).
- Intermediate commits will be made to allow for easy rollback of specific changes.

---

## 6. Operational Readiness:

### Observability:
- Logs will be provided for:
    - Files scanned and placeholders found.
    - Images generated (URL and description).
    - Files modified and default chapters removed.
    - Docusaurus build status.

### Alerting:
- Alerts for Docusaurus build failures after the process.

### Deployment and Rollback strategies:
- Deployment is local Docusaurus build. Rollback via Git revert.

---

## 7. Risk Analysis and Mitigation:

### Top 3 Risks:
1.  **Incorrect Placeholder Detection**: The regex or search pattern might miss some placeholders or incorrectly identify non-placeholders.
    *   **Mitigation**: Rigorous testing of detection patterns and user review of changes.
2.  **Irrelevant/Low-Quality AI-Generated Images**: Generated images might not be contextually relevant or of poor visual quality.
    *   **Mitigation**: Post-generation review and potential manual override or regeneration if quality is critical.
3.  **Accidental Deletion of Custom Content**: Default chapter removal logic might inadvertently delete user's custom chapters.
    *   **Mitigation**: Explicit whitelisting of custom textbook chapter paths and careful validation of deletion targets.

---

## 8. Evaluation and Validation:

### Definition of Done:
- All image placeholders are replaced with valid image MDX blocks.
- All default Docusaurus chapters are removed.
- Only custom textbook chapters remain.
- Docusaurus project builds successfully without errors or warnings.
- Deliverables (lists of changed/removed files, build confirmation) are provided.

### Output Validation:
- Validate image URLs are correctly inserted and accessible.
- Validate MDX syntax after modifications.
- Validate `sidebars.ts` correctly reflects remaining chapters.

---

## 9. Architectural Decision Record (ADR):
- 📋 Architectural decision detected: Automated Image Insertion and Default Chapter Removal Strategy — Document reasoning and tradeoffs? Run `/sp.adr Automated Image Insertion`