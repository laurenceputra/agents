# Changelog

All notable changes to the Recommendation Letter Agents group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.1] - 2025-12-22

### Changed
- **Writing Style Guidelines**: Replaced embedded writing style guidelines in all agent files with references to COMMON-PATTERNS.md
  - **Before**: Each agent contained 15-20 lines of embedded style guidelines (~1300 characters)
  - **After**: Agent files reference centralized guidelines in COMMON-PATTERNS.md (3 lines, ~150 characters)
  - **Impact**: Maintenance improvement (single source of truth), ~1150 characters saved per agent, no functional changes

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
- **recommendation-writer**: Consolidated quality checklist from 11 to 10 items for improved focus and clarity
- **devils-advocate**: Version synchronized to 1.3.0 for group consistency (no changes to agent)
- **recommendation-profiler**: Version synchronized to 1.3.0 for group consistency (no changes to agent)
- **recommendation-reviewer**: Version synchronized to 1.3.0 for group consistency (no changes to agent)

### Fixed
- Quality checklist item count inconsistencies across agent groups

## [1.2.0] - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New fourth agent for credibility and authenticity review
  - **Purpose**: Critically reviews recommendation letters for exaggerations, vague praise, and credibility concerns before signature
  - **Position in Workflow**: Final credibility gate after Reviewer approval, before letter signature
  - **Key Capabilities**:
    - Challenges exaggerated or unsubstantiated claims
    - Identifies vague praise lacking specific support
    - Surfaces red flags that might trigger hiring manager skepticism
    - Assesses letter authenticity and believability
    - Reviews from skeptical hiring manager perspective
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for credibility evaluation
  - **Context**: Ensures recommendation letters are believable and won't backfire due to exaggeration or generic praise

### Changed
- **All Agents**: Added handoff to Devil's Advocate for credibility review (Profiler, Writer, Reviewer)
  - **Before**: Letters went from Reviewer approval to signature without credibility check
  - **After**: All letters go through Devil's Advocate credibility gate before finalization
  - **Added Handoff**: "Submit to Devil's Advocate" for credibility and authenticity review
  - **Context**: Prevents credibility issues that might undermine letter effectiveness
  - **Migration**: No breaking changes—workflow extended with credibility gate, existing process preserved

- **Agent Versions**: Synchronized minor version bump for all existing agents
  - **All Agents**: 1.1.0 → 1.2.0 (Profiler, Writer, Reviewer)
  - **Context**: Workflow change affects all agents (handoff to devils-advocate added)

- **Workflow (copilot-instructions.md)**: Updated from three-agent to four-agent workflow with credibility gate
  - **Before**: Profiler → Writer → Reviewer → Signature
  - **After**: Profiler → Writer → Reviewer → Devil's Advocate (credibility review) → Signature
  - **Added Step 4**: Devil's Advocate reviews for exaggerations, vague praise, red flags before signature
  - **Context**: Visualizes mandatory credibility check before letter submission

- **README.md**: Updated agent count and feature list
  - **Before**: Three agents with quality assurance
  - **After**: Four agents including Devil's Advocate credibility review
  - **Added Feature**: Credibility review for authenticity and believability
  - **Context**: Clarifies complete workflow including credibility gate

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after Reviewer approval, before signature
- **No Breaking Changes**: Existing agents and sequential workflow remain valid; workflow extended, not replaced
- **Credibility Focus**: Devil's Advocate specializes in hiring manager skepticism perspective—different from Reviewer's quality focus

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
  - recommendation-profiler: now v1.3.1
  - recommendation-writer: now v1.3.1
  - recommendation-reviewer: now v1.3.1
  - devils-advocate: now v1.3.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

