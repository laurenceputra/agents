# Changelog

All notable changes to the Legacy Planning Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-13

### Changed
- **Agent Frontmatter**: Updated handoff format to GitHub Copilot object schema across all four legacy planning agents
  - **Before**: Handoffs were simple string arrays (e.g., `handoffs: [legacy-planning-advisor]`)
  - **After**: Handoffs are structured objects with `label`, `agent`, `prompt`, and optional `send` fields
  - **Context**: VSCode validation required handoff objects for GitHub Copilot extension compliance. This change resolves validation errors while improving handoff clarity with descriptive labels and context.
  - **Migration**: All agents (Legacy Planning Advisor, Beneficiary Planning Agent, Trust Structure Designer, Letter of Wishes Composer) now use object format. Hub-and-spoke coordination pattern unchanged.

### Fixed
- **VSCode Validation**: Resolved handoff format validation errors across all four agent files
  - **Issue**: GitHub Copilot extension validation failed on simple string array handoff format
  - **Resolution**: Updated to object format with clear labels like "Hand to Beneficiary Planner" and context-rich prompts
  - **Impact**: VSCode validation passes; handoff menu provides better user guidance with descriptive action labels

### Context
This update ensures Legacy Planning Agents comply with GitHub Copilot's handoff schema requirements. No changes to the hub-and-spoke coordination model—the advisor still coordinates with three specialist agents. Only handoff format updated for validation compliance and improved UX.

## [1.0.0] - 2024-12-12

### Added
- Legacy Planning Advisor for discovery, coordination, and synthesis
- Beneficiary Planning Agent for distribution analysis and conflict prevention
- Trust Structure Designer for trust education and recommendations
- Letter of Wishes Composer for personal documentation and family guidance
- Hub-and-spoke coordination model for flexible specialist consultation
- Comprehensive workflow documentation with decision trees
- Complete infrastructure files (copilot-instructions.md, README.md)
- Version tracking in agent frontmatter
- Handoff chains defining hub-and-spoke coordination pattern
- Empathetic, accessible guidance for sensitive legacy planning topics

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
