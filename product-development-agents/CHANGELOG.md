# Changelog

All notable changes to the Product Development Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-13

### Changed
- **Agent Frontmatter**: Updated handoff format to GitHub Copilot object schema across all four product development agents
  - **Before**: Handoffs were simple string arrays (e.g., `handoffs: [staff-engineer, qa]`)
  - **After**: Handoffs are structured objects with `label`, `agent`, `prompt`, and optional `send` fields
  - **Context**: VSCode validation required handoff objects for GitHub Copilot extension compliance. This change resolves validation errors while improving handoff UX with clear labels and context.
  - **Migration**: All agents (Product Manager, Staff Engineer, Code Reviewer, QA) now use object format. No changes to workflow—handoff relationships remain identical.

### Fixed
- **VSCode Validation**: Resolved handoff format validation errors across all four agent files
  - **Issue**: GitHub Copilot extension validation failed on simple string array handoff format
  - **Resolution**: Updated to object format with user-facing labels and context prompts
  - **Impact**: VSCode validation passes; handoff menu displays clear action labels

### Context
This update ensures Product Development Agents comply with GitHub Copilot's handoff schema requirements. No workflow logic changed—only the handoff format. All agent coordination patterns (PM → Engineer → Code Review → QA) remain unchanged.

## [1.0.0] - 2024-12-12

### Added
- Product Manager agent for requirements definition and PRD creation
- Staff Engineer agent for technical design and implementation
- Code Reviewer agent for quality assurance and security validation
- QA agent for comprehensive testing and bug reporting
- Complete workflow documentation with quality gates and feedback loops
- Comprehensive examples for each agent (2-3 examples per agent)
- Integration points documentation showing agent coordination
- Quality checklists for each agent role
- Decision trees for workflow navigation
- Version tracking in agent frontmatter
- Handoff chains defining agent coordination

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
