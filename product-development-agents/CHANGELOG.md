# Changelog

## [1.4.2] - 2025-12-22

### Changed
- **Writing Style Guidelines**: Replaced embedded writing style guidelines in all agent files with references to COMMON-PATTERNS.md
  - **Before**: Each agent contained 15-20 lines of embedded style guidelines (~1300 characters)
  - **After**: Agent files reference centralized guidelines in COMMON-PATTERNS.md (3 lines, ~150 characters)
  - **Impact**: Maintenance improvement (single source of truth), ~1150 characters saved per agent, no functional changes

## [1.4.1] - 2025-12-22

### Changed
- **Examples Restoration**: Restored comprehensive examples (minimum 2 per agent with full input/output)
  - **Before**: Many agents had only 1 truncated example after size optimization (commit ee14332)
  - **After**: All agents now have 2+ complete examples demonstrating full workflow
  - **Impact**: Significantly improved agent clarity and usability while maintaining <30k character limit


All notable changes to the Product Development Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2025-12-21

### Added
- Self-update capability via `update-from-upstream.sh` script
- `UPDATING.md` documentation with complete guide for using the self-update feature
- Support for direct downloads from GitHub repository using HTTP endpoints
- GitHub token support for higher API rate limits (5000 req/hr vs 60 req/hr)
- Automatic file discovery via GitHub API with intelligent fallback to common agent names
- Portable design allowing agent group to be copied to other projects via `cp -r` and updating itself
- Smart file handling: updates changed files, adds new files, preserves unchanged files
- Intentional preservation of local script modifications (update-from-upstream.sh)

### Changed
- Added `AGENTGROUPNAME` file containing the group name for script auto-detection
- Enhanced error handling and logging in update process

## [1.3.0] - 2025-12-15

### Added
- **Feature Enhancement**: Improved quality checklist usability across all agents

### Changed
- **code-reviewer**: Consolidated quality checklist from 14 to 10 items for improved focus and clarity
- **devils-advocate**: Consolidated quality checklist from 15 to 10 items for improved focus and clarity
- **product-manager**: Consolidated quality checklist from 12 to 10 items for improved focus and clarity
- **qa**: Consolidated quality checklist from 13 to 10 items for improved focus and clarity
- **staff-engineer**: Consolidated quality checklist from 13 to 10 items for improved focus and clarity
- Standardized agent file references in copilot-instructions.md to use `.agent.md` extension consistently

### Fixed
- Quality checklist item count inconsistencies across agent groups

## [1.2.0] - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New fifth agent for critical review and disagreement capture
  - **Purpose**: Critically reviews product development work, challenges assumptions from all agents, surfaces disagreements
  - **Position in Workflow**: Pre-PR quality gate between QA approval and PR submission
  - **Key Capabilities**:
    - Critical review of work from Product Manager, Staff Engineer, Code Reviewer, and QA
    - Assumption challenge across product, technical, and quality dimensions
    - Disagreement facilitation between agents (e.g., Staff Engineer vs Code Reviewer on technical trade-offs)
    - Product Manager perspective integration on technical disagreements
    - PR writeup preparation with all disagreements marked for human decision
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for multi-perspective synthesis
  - **Context**: Addresses need to surface product-technical trade-offs and technical disagreements (e.g., custom caching vs framework caching) before PR submission, ensuring human decision-makers see full context

- **QA Handoff to Devil's Advocate**: Added "Send to Devil's Advocate" handoff after QA approval
  - **Context**: QA is no longer final gate; now hands off to Devil's Advocate for critical review

- **Product Manager Disagreement Participation**: Added "Weigh in on disagreement" handoff
  - **Purpose**: Product Manager can provide business context on technical disagreements when requested by Devil's Advocate
  - **Context**: Enables product perspective on technical trade-offs (e.g., performance vs maintainability when revenue-critical)

### Changed
- **Agent Count**: System now has five agents (was four)
  - **Before**: Product Manager, Staff Engineer, Code Reviewer, QA
  - **After**: Product Manager, Staff Engineer, Code Reviewer, QA, Devil's Advocate
  - **Migration**: Workflows now include Devil's Advocate review after QA approval

- **Workflow (copilot-instructions.md)**: Updated to include Devil's Advocate gate
  - **Before**: PM → Engineer → Code Review → QA → Deployment
  - **After**: PM → Engineer → Code Review → QA → Devil's Advocate → PR/Deployment
  - **Added Decision Points**: Revision needed (to Engineer), Product issue (to PM), Approved (to PR)
  - **Context**: Devil's Advocate can send work back to Staff Engineer if critical issues found, or escalate to Product Manager if requirements unclear

- **Critical Rules (copilot-instructions.md)**: Added Devil's Advocate mandatory rule
  - **Rule 4**: "Devil's Advocate is Mandatory" - all features require critical review after QA
  - **Rule 5**: Updated from "Iterative Loops" to include Devil's Advocate cycles
  - **Context**: Reinforces that critical review is not optional

- **Decision Trees (copilot-instructions.md)**: Added Devil's Advocate decision points
  - **New**: "I have QA-approved code ready for PR" → Consult Devil's Advocate
  - **New**: "I received critical concerns from Devil's Advocate" → Work with Staff Engineer
  - **New**: "Devil's Advocate found a product issue" → Work with Product Manager
  - **New**: "I want to skip Devil's Advocate" → Not allowed ❌
  - **Context**: Clarifies when and how to use Devil's Advocate in workflow

- **README.md**: Updated from four-agent to five-agent system
  - **Agent List**: Added Devil's Advocate as fifth agent
  - **Installation**: Updated agent file list to include devils-advocate.md
  - **Context**: Ensures users understand new workflow step

- **Version Numbers**: Synchronized minor version bump across all agents
  - **All Agents**: 1.1.0 → 1.2.0 (Product Manager, Staff Engineer, Code Reviewer, QA, Devil's Advocate)
  - **Context**: Synchronized minor bump per versioning strategy (workflow change affects all agents)

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after QA approval, before PR submission
- **No Breaking Changes**: Existing workflow patterns remain valid; workflow extended with new quality gate
- **Product Manager Role**: Product Manager can now weigh in on technical disagreements when requested by Devil's Advocate (optional but valuable for business context)

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
  - product-manager: now v1.3.1
  - staff-engineer: now v1.3.1
  - code-reviewer: now v1.3.1
  - qa: now v1.3.1
  - devils-advocate: now v1.3.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

