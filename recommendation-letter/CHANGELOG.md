# Changelog

All notable changes to the Recommendation Letter Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-13

### Changed
- **Agent Frontmatter**: Updated handoff format to GitHub Copilot object schema across all three recommendation letter agents
  - **Before**: Handoffs were simple string arrays (e.g., `handoffs: [recommendation-writer, recommendation-reviewer]`)
  - **After**: Handoffs are structured objects with `label`, `agent`, `prompt`, and optional `send` fields
  - **Context**: VSCode validation required handoff objects for GitHub Copilot extension compliance. This change resolves validation errors while improving handoff UX with clear labels and contextual prompts.
  - **Migration**: All agents (Recommendation Profiler, Recommendation Writer, Recommendation Reviewer) now use object format. Sequential workflow (Profiler → Writer → Reviewer) with feedback loops remains unchanged.

### Fixed
- **VSCode Validation**: Resolved handoff format validation errors across all three agent files
  - **Issue**: GitHub Copilot extension validation failed on simple string array handoff format
  - **Resolution**: Updated to object format with descriptive labels like "Hand to Writer" and context-rich prompts explaining handoff purpose
  - **Impact**: VSCode validation passes; handoff menu provides clear guidance for users navigating the recommendation letter workflow

### Context
This update ensures Recommendation Letter Agents comply with GitHub Copilot's handoff schema requirements. No changes to the three-phase workflow (profile → draft → review) or feedback loop patterns. Only handoff format updated for validation compliance and improved user experience.

## [1.0.0] - 2024-12-12

### Added
- Recommendation Profiler agent for candidate discovery and profile creation
- Recommendation Writer agent for letter drafting and revision
- Recommendation Reviewer agent for quality assurance and feedback
- Three-phase workflow: profile creation, letter drafting, and quality review
- Feedback loops allowing iteration between Writer and Profiler or Reviewer
- Comprehensive examples for each agent demonstrating the workflow
- Integration points documentation showing agent coordination
- Quality checklists for each phase of recommendation letter creation
- Decision trees for workflow navigation
- Version tracking in agent frontmatter
- Handoff chains defining sequential coordination with feedback loops

### Changed
- N/A (initial release)

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A
