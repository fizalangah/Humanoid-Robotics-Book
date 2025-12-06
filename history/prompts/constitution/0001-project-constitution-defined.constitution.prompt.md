---
id: 0001
title: Project Constitution Defined
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: User
command: /sp.constitution
labels: [project-setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - N/A
---

## Prompt

```text
# Project Constitution — AI/Spec-Driven Textbook
# Title: Physical AI & Humanoid Robotics
# Stack: Docusaurus + Claude Code + SpecKit Plus

## Purpose
This Constitution defines all global, immutable rules for the entire textbook.
Every Specification, Plan, Task, Implementation and generated file MUST follow these standards.
No chapter, feature or prompt may override these rules.

## Core Principles
- **AI-Native Production:** All content is generated using SpecKit + Claude Code.
- **Technical Accuracy:** All explanations must be correct for:
  - Physical AI
  - ROS 2
  - Gazebo
  - NVIDIA Isaac
  - Humanoid robotics
  - VLA systems
- **Beginner-Friendly:** Simple explanations, clean English, examples-based teaching.
- **Consistency:** Same tone, structure and formatting across all chapters.
- **Error-Free:** All files must be valid Markdown/MDX and Docusaurus must build without warnings.

## Global Writing Standards
- Clean, simple English (grade 9–12).
- Friendly, clear, educational tone.
- No jargon without explanation.
- Short paragraphs; frequent examples.
- Zero fluff or filler.
- Technical correctness is mandatory.

### Required Chapter Structure
Each chapter MUST include:
1. Learning Objectives
2. Introduction
3. Core Theory
4. Real-World Examples
5. Hands-On Tasks / Practice
6. Summary
7. Glossary (optional)

### Markdown Standards
Front-matter:
---
title: "CHAPTER TITLE"
description: "Short 1–2 sentence summary"
---

Headings:
# Title
## Section
### Subsection

Code blocks must use fenced syntax:
```python
```bash
```xml

## Technical Content Requirements
- ROS 2 examples use correct `rclpy` patterns.
- URDF is valid XML.
- Gazebo and Isaac concepts must match real workflows.
- No hallucinated APIs or commands.
- Diagrams: text descriptions only.

## Required Content Coverage
The textbook must fully cover:
1. Foundations of Physical AI
2. ROS 2
3. Gazebo + Unity Simulation
4. NVIDIA Isaac
5. Humanoid Robotics
6. VLA Systems
7. Capstone Project

## Quality Standards
- **Accuracy:** All explanations must be verifiable.
- **Consistency:** No contradictions across chapters.
- **Exercises:** Minimum one practical task per chapter.
- **Examples:** Must be realistic and technically valid.

## Docusaurus Standards
- All chapters stored under `/docs/...`
- Folder names: lowercase, hyphen-based
- MDX must compile with zero errors/warnings
- Sidebar categories must be valid
- Images stored in `/static/img/...`
- No absolute or local system paths

## File Organization
- Each chapter = one MD/MDX file
- Each major part = its own folder
- No Windows paths (C:\...)
- No manual content writing except metadata fixes

## AI Implementation Rules
- Content must be produced by SpecKit workflows only
- Specs, Plans, Tasks, Implementations must obey this Constitution
- Plans must include formatting + accuracy validation
- Implementations must not break Docusaurus structure

## Success Criteria
The project is considered Constitution-compliant when:
- All chapters share a unified voice & structure
- All content is technically correct
- Local + GitHub Pages builds pass
- All writing was generated via SpecKit + Claude Code

## Immutability
This Constitution must be committed before creating any chapter specifications.
All future work inherits these rules and cannot violate them.
```

## Response snapshot

Confirmed the project constitution. This PHR documents the initial definition of the project's governing principles and standards.

## Outcome

- ✅ Impact: Constitution confirmed.
- 🧪 Tests: Not applicable
- 📁 Files: .specify/memory/constitution.md written.
- 🔁 Next prompts: N/A
- 🧠 Reflection: PHR created for initial constitution.

## Evaluation notes (flywheel)

- Failure modes observed: Not applicable
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable
