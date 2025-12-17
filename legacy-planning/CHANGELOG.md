# Changelog

All notable changes to the Legacy Planning Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-12-15

### Added
- **Feature Enhancement**: Improved quality checklist usability across all agents

### Changed
- **beneficiary-planning-agent**: Consolidated quality checklist from 12 to 10 items for improved focus and clarity
- **devils-advocate**: Consolidated quality checklist from 16 to 10 items for improved focus and clarity
- **legacy-planning-advisor**: Consolidated quality checklist from 14 to 10 items for improved focus and clarity
- **letter-of-wishes-composer**: Version synchronized to 1.3.0 for group consistency (no changes to agent)
- **trust-structure-designer**: Version synchronized to 1.3.0 for group consistency (no changes to agent)
- Standardized agent file references in copilot-instructions.md to use `.agent.md` extension consistently

### Fixed
- Quality checklist item count inconsistencies across agent groups

## [1.2.0] - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New fifth agent for critical review and ethical consideration surfacing
  - **Purpose**: Critically reviews legacy planning guidance for assumptions, ethical dilemmas, and family dynamics before client delivery
  - **Position in Workflow**: Final quality gate after specialist guidance, before client delivery
  - **Key Capabilities**:
    - Challenges assumptions about beneficiary fairness and distribution equity
    - Surfaces potential family conflicts and ethical dilemmas
    - Reviews trust structure complexity trade-offs
    - Questions letter of wishes clarity and trustee guidance
    - Documents all perspectives including uncomfortable family dynamics
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for multi-perspective ethical analysis
  - **Context**: Ensures clients have full context for important family decisions by surfacing issues that specialists may not challenge

### Changed
- **All Agents**: Added handoff to Devil's Advocate for critical review (Legacy Planning Advisor, Beneficiary Planning Agent, Trust Structure Designer, Letter of Wishes Composer)
  - **Before**: Agents returned directly to advisor or client without critical review
  - **After**: All guidance goes through Devil's Advocate quality gate before finalization
  - **Added Handoff**: "Submit to Devil's Advocate" for critical review before client delivery
  - **Context**: Ensures ethical considerations and family dynamics are explicitly addressed
  - **Migration**: No breaking changes—workflow extended with quality gate, existing handoff patterns preserved

- **Agent Versions**: Synchronized minor version bump for all existing agents
  - **All Agents**: 1.1.0 → 1.2.0 (Legacy Planning Advisor, Beneficiary Planning Agent, Trust Structure Designer, Letter of Wishes Composer)
  - **Context**: Workflow change affects all agents (handoff to devils-advocate added)

- **Workflow (copilot-instructions.md)**: Updated from four-agent to five-agent workflow with critical review gate
  - **Before**: Advisor → Specialists → Synthesis → Client delivery
  - **After**: Advisor → Specialists → Synthesis → Devil's Advocate (critical review) → Client delivery
  - **Added Step 4**: Devil's Advocate reviews all guidance, surfaces ethical dilemmas, marks critical decisions
  - **Context**: Visualizes mandatory critical review phase before client-facing guidance

- **README.md**: Updated agent count and workflow description
  - **Before**: Four agents in hub-and-spoke model
  - **After**: Five agents including Devil's Advocate as final quality gate
  - **Context**: Clarifies complete workflow including critical review

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after specialist guidance synthesis, before client delivery
- **No Breaking Changes**: Existing agents and hub-and-spoke coordination remain valid; workflow extended, not replaced
- **Handoff Integration**: All specialists can now handoff directly to Devil's Advocate or route through Legacy Planning Advisor

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

## 1.3.1 - 2025-12-17

### Added
- **Writing Style Guidelines**: All agents now include comprehensive writing style guidelines to ensure natural, human-like output
  - Added 9 core principles for natural writing (varied sentence structures, direct language, active voice, natural transitions, etc.)
  - Principle 9 specifically addresses AI-typical punctuation (avoid em-dashes, limit semicolons/colons)
  - Guidelines positioned after Domain Context section in all agent files
  - Ensures all agent outputs avoid robotic, AI-detectable patterns
  - **Context**: Aligns all agent groups with meta-agent system v1.6.1/1.7.1 standards for human-like communication
  - **Migration**: No breaking changes. Existing usage patterns remain valid. Agents will now produce more natural-sounding output.

### Changed
- **Version Numbers**: All agents bumped to next patch version
  - legacy-planning-advisor: now v1.3.1
  - beneficiary-planning-agent: now v1.3.1
  - trust-structure-designer: now v1.3.1
  - letter-of-wishes-composer: now v1.3.1
  - devils-advocate: now v1.3.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

