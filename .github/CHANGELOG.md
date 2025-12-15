# Changelog

All notable changes to the Meta-Agent System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.5.0 - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New fourth meta-agent for critical review and disagreement capture
  - **Purpose**: Critically reviews agent work, challenges assumptions, surfaces disagreements between agents
  - **Position in Workflow**: Pre-PR quality gate between Agent Validator approval and PR submission
  - **Key Capabilities**: 
    - Critical review of work from Architect, Implementer, and Validator
    - Assumption challenge and blind spot identification
    - Disagreement facilitation between agents with full perspective capture
    - PR writeup preparation with all disagreements marked for human decision
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for multi-perspective synthesis
  - **Context**: Addresses need to surface and document disagreements between agents (e.g., Staff Engineer vs Code Reviewer) before PR submission, ensuring human decision-makers see full context and trade-offs

- **Quality Gate 4 (Critical Review Complete)**: Added mandatory pre-PR gate after Validator approval
  - **Owner**: Devil's Advocate
  - **Requirements**: Assumptions challenged, blind spots identified, disagreements documented, all perspectives captured
  - **Context**: Ensures all viewpoints are surfaced before PR submission, enabling informed human decisions

### Changed
- **Meta-Agent Count**: System now has four meta-agents (was three)
  - **Before**: Architect, Implementer, Validator
  - **After**: Architect, Implementer, Validator, Devil's Advocate
  - **Migration**: All workflows now include Devil's Advocate review after Validator approval

- **Agent Validator Workflow**: Updated to handoff to Devil's Advocate after approval
  - **Before**: Validator approval → PR submission
  - **After**: Validator approval → Devil's Advocate review → PR submission
  - **Added Handoff**: "Send to Devil's Advocate" for critical review after approval
  - **Context**: Validator still gates PR submission but now works with Devil's Advocate for comprehensive quality assurance
  - **Migration**: No breaking changes—Validator still submits PRs, just with additional review step

- **Workflow Diagram (copilot-instructions.md)**: Updated to show four-agent workflow with Devil's Advocate gate
  - **Before**: Three-agent linear workflow (Architect → Implementer → Validator → PR)
  - **After**: Four-agent workflow with decision points (Architect → Implementer → Validator → Devil's Advocate → [Revision/Escalation/Approval] → PR)
  - **Context**: Visualizes new critical review phase and feedback loops

- **Decision Trees (copilot-instructions.md)**: Added section [D] for Devil's Advocate critical review
  - **Before**: [C] Have implementation to review → Validator → PR submission
  - **After**: [C] Validator review → [D] Devil's Advocate critical review → [E] PR submission
  - **Added Decision Points**: Revision needed (to Implementer), Specification issue (to Architect), Approved for PR (to Validator)
  - **Context**: Clarifies when and how to use Devil's Advocate in workflow

- **Workflow Rules (copilot-instructions.md)**: Updated PR submission rule to require Devil's Advocate approval
  - **Before**: Rule 3 - "Only Validator submits PRs" (after Validator approval)
  - **After**: Rule 3 - "Only Validator submits PRs" (after Devil's Advocate approval); Rule 5 - "Devil's Advocate is mandatory"
  - **Context**: Reinforces that critical review is not optional

- **Quick Reference Table (copilot-instructions.md)**: Added Devil's Advocate entry
  - **New Row**: [D] Have approved implementation → @devils-advocate → Critical review, challenge assumptions
  - **Updated Row**: [E] Want to merge → @agent-validator only → Validator submits PR after Devil's Advocate approval

- **README.md Workflow**: Updated from three-phase to four-phase workflow
  - **Added Phase 4**: Critical Review (Pre-PR Gate) with Devil's Advocate
  - **Updated Quick Start**: Added step 5 for Devil's Advocate consultation
  - **Context**: Ensures users understand new workflow step

- **Version Numbers**: Synchronized minor version bump across all meta-agents
  - **All Agents**: 1.4.0 → 1.5.0 (Architect, Implementer, Validator, Devil's Advocate)
  - **Infrastructure**: copilot-instructions.md, README.md version badges updated to 1.5.0
  - **Context**: Synchronized minor bump per meta-agent versioning strategy (workflow change affects all agents)

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after Validator approval, before PR submission
- **No Breaking Changes**: Existing agents and specifications remain valid; workflow extended, not replaced
- **New Agent Groups**: Include Devil's Advocate in agent list with appropriate handoffs from final quality gate agent

## 1.4.0 - 2025-12-13

### Changed
- **Agent Frontmatter**: Updated handoff format to GitHub Copilot object schema across all three meta-agents
  - **Before**: Handoffs were simple string arrays (`handoffs: [agent-implementer, agent-validator]`)
  - **After**: Handoffs are structured objects with `label`, `agent`, `prompt`, and optional `send` fields
  - **Context**: VSCode validation was failing because GitHub Copilot extension expects handoff objects, not strings. This change ensures compliance with the official schema and improves handoff UX with clear labels and context prompts.
  - **Migration**: All meta-agents (Architect, Implementer, Validator) now use object format. No breaking changes to workflow semantics—handoff relationships remain unchanged, only format updated.

- **Agent Architect (Schema Documentation)**: Updated Portable Agent Group Schema section to document new handoff object format
  - **Before**: Schema showed handoffs as simple string array
  - **After**: Schema documents handoff object structure with field requirements (label, agent, prompt, send)
  - **Context**: Ensures future agent specifications follow the correct format from the start
  - **Migration**: New agents designed after v1.4.0 will automatically use object format. Existing agents require manual update.

- **copilot-instructions.md (Schema Documentation)**: Updated Agent Frontmatter Schema section with handoff object format and field requirements
  - **Before**: Example showed string array for handoffs
  - **After**: Example shows object format with inline documentation of field requirements
  - **Context**: Provides clear reference for handoff format across all documentation
  - **Migration**: Documentation change only; no action required for existing agents unless updating them.

### Added
- **Handoff Field Requirements**: Added documentation for all handoff object fields
  - `label`: Short, action-oriented phrase (3-6 words, starts with verb) for user-facing actions
  - `agent`: Target agent name in kebab-case matching target's `name` frontmatter field
  - `prompt`: Context-specific instruction for receiving agent (1-2 sentences describing handoff context and expected action)
  - `send`: Optional boolean for automatic handoffs (default: false, use sparingly)

### Fixed
- **VSCode Validation**: Resolved handoff format validation errors in VSCode GitHub Copilot extension
  - **Issue**: All agent files showed validation warnings about handoff format
  - **Resolution**: Updated all 14 agent files across 4 agent groups to use GitHub Copilot-compliant object format
  - **Impact**: VSCode validation now passes without errors; handoff UI displays clear labels and prompts

### Context
This refactoring addresses VSCode validation failures while maintaining all existing workflow semantics. No handoff relationships were added or removed—only the format changed from simple strings to structured objects. The new format provides better UX (clear labels in handoff menu) and passes GitHub Copilot extension validation.

## 1.3.0 - 2025-12-12

### Changed
- **Agent Architect**: All specification documents now created in `./.specifications/` directory at repository root (previously ad-hoc locations)
  - **Before**: Specifications created without defined location, leading to inconsistent storage
  - **After**: All specifications must be created in `./.specifications/` directory with consistent naming
  - **Migration**: Existing specifications in `.github/specifications/` can remain as historical artifacts; new specifications go to `./.specifications/`
- **Workflow**: Added specification storage convention requiring `.specifications/` directory for all Architect outputs
  - Phase 1 workflows updated for both individual agents and agent groups
  - Architect must create `.specifications/` directory if it doesn't exist before writing specs
- **Version Control**: Added `.specifications/` to `.gitignore` to exclude specifications from repository commits

### Added
- **Documentation**: New "Specification Storage Convention" section in copilot-instructions.md explaining specification directory structure and rationale
  - Documents why specifications are working documents (not final artifacts)
  - Provides clear workflow showing specification lifecycle
  - Includes directory structure diagram for clarity
- **Agent Architect**: Added "Specification Storage Location" subsection documenting directory requirements and naming conventions
  - Path requirement: `./.specifications/` (relative to repository root)
  - Naming convention: `{agent-name}-specification.md` or `{group-name}-group-specification.md`
  - Examples for individual agents, agent groups, and refactorings
  - Exception documented for `.pr_details.md` (remains in root)

### Context
Specifications are working documents created during agent design phase. Storing them in a consistent, gitignored location keeps the repository clean while maintaining local access for reference during implementation and review. This addresses specification storage inconsistency and prevents accidental commits of intermediate artifacts.

## 1.2.0 - 2025-12-12

### Added

#### Documentation Enforcement
- **Mandatory CHANGELOG.md updates**: All version bumps now require CHANGELOG.md entries
  - Implementer must add changelog entry following Keep a Changelog format
  - Entry must include date (YYYY-MM-DD), specific component names, and context
  - Breaking changes require migration guidance (Before/After/Migration sections)
  - Added comprehensive changelog entry format guidelines with examples

- **Mandatory README.md updates**: Significant changes require README.md updates
  - Update when agents added/removed, responsibilities change, workflow changes
  - Update when new user-facing features added or breaking changes made
  - Update version badge for synchronized version bumps
  - Added clear criteria for when README.md updates are required vs optional

- **Documentation validation gate**: Validator now checks documentation completeness
  - CHANGELOG.md validation checklist (format, completeness, specificity, context)
  - README.md validation checklist (consistency, user-facing clarity, version badge)
  - Version consistency validation across all files
  - Added severity levels for documentation issues (Critical vs Recommendation)

- **Documentation requirements section**: Agent Implementer enhanced with documentation guidance
  - Self-review checklist for documentation updates
  - Examples of good vs poor changelog entries
  - Criteria for when to update README.md
  - Format guidelines and quality criteria

### Changed

#### Implementer Workflow (Phase 2)
- **Added Step 2.5 (Individual Agents)**: Update Documentation (MANDATORY)
  - **Before**: Documentation updates were optional or informal
  - **After**: CHANGELOG.md required for all version bumps, README.md required for significant changes
  - **Migration**: Review existing agents and ensure CHANGELOG.md exists for versions > 1.0.0

- **Added Step 2.7 (Agent Groups)**: Update Documentation (MANDATORY)
  - **Before**: Group implementations could skip documentation updates
  - **After**: Same documentation requirements as individual agents apply to groups
  - **Migration**: Ensure all agent groups have CHANGELOG.md if version > 1.0.0

- **Updated exit criteria**: Added documentation update verification to Phase 2 exit gates
  - **Before**: Exit criteria focused on agent file completeness only
  - **After**: Must verify CHANGELOG.md and README.md updates before submission to Validator
  - **Migration**: No breaking changes; new criteria apply to future implementations

#### Validator Workflow (Phase 3)
- **Added Section 3.1.1 (Individual Agents)**: Documentation Validation (MANDATORY)
  - **Before**: Validator focused primarily on agent definition file quality
  - **After**: Validator must check CHANGELOG.md and README.md for every PR
  - **Migration**: No breaking changes; new validation criteria apply to future reviews

- **Enhanced group validation**: Added documentation validation to group-specific criteria
  - **Before**: Group validation focused on structure and handoff integrity
  - **After**: Also validates documentation updates across all agents in group
  - **Migration**: No breaking changes; applies to future agent group submissions

- **Expanded feedback examples**: Added documentation-specific feedback templates
  - Critical issues for missing/vague changelog entries
  - Critical issues for version mismatches
  - Critical issues for missing README updates
  - Recommendation-level feedback for documentation clarity improvements

### Quality Improvements

#### Documentation Standards
- **Changelog format standardized**: All entries follow Added/Changed/Fixed/Deprecated/Removed/Security categories
- **Version consistency enforced**: Version numbers must match across agent frontmatter, CHANGELOG.md, and README.md
- **Context requirement**: All changelog entries must explain why changes were made, not just what changed
- **Migration guidance**: Breaking changes must include Before/After/Migration sections

#### Self-Review Process
- **Enhanced checklist**: Implementer self-review now includes 10 documentation-specific items
- **Quality criteria**: Clear distinction between good vs poor changelog/README updates
- **Examples provided**: Both positive examples and anti-patterns documented

### Migration Guide

#### For Implementers

If implementing agents after v1.2.0:

1. **Always update CHANGELOG.md** with every agent change:
   ```markdown
   ## [Version] - YYYY-MM-DD
   
   ### Added/Changed/Fixed
   - **Component**: Description
     - Context: Why the change was made
     - Migration: How to adapt (if breaking)
   ```

2. **Update README.md when** (use judgment):
   - Agent added/removed
   - Responsibilities change significantly
   - Workflow changes
   - New user-facing features
   - Breaking changes
   - Synchronized version bumps (always update version badge)

3. **Verify version consistency** before submitting to Validator:
   - Agent frontmatter matches CHANGELOG.md
   - README.md badge matches (if synchronized bump)
   - Date is current (YYYY-MM-DD)

4. **Use self-review checklist** in agent-implementer.md before submission

#### For Validators

If validating agents after v1.2.0:

1. **Always check CHANGELOG.md**:
   - Entry exists for current version
   - Follows standard format
   - Includes specific component names
   - Provides context (why changed)
   - Includes migration guidance for breaking changes

2. **Check README.md if applicable**:
   - Updated when responsibilities/workflow/agents change
   - Version badge updated for synchronized bumps
   - No outdated information

3. **Verify version consistency**:
   - Frontmatter matches CHANGELOG.md
   - README.md badge matches (if synchronized)
   - Date is current

4. **Use severity levels appropriately**:
   - Critical: Missing changelog, vague entries, version mismatches
   - Recommendation: Could be clearer, more specific

#### For Existing Agents (No Breaking Changes)

No migration required for existing agents. New requirements apply only to:
- New implementations after v1.2.0
- Updates to existing agents after v1.2.0
- PRs submitted after v1.2.0

Existing agents with versions > 1.0.0 should have CHANGELOG.md, but retroactive updates are not required.

## 1.1.0 - 2025-12-12

### Added

#### Workflow Enforcement
- **Feature branch workflow**: All agent implementations must be created on feature branches (`feature/agent-{name}` or `feature/group-{name}`)
- **Quality gates**: Three mandatory gates (Architect specification approval, Implementer completion, Validator approval)
- **Decision trees**: Added comprehensive decision trees for users to navigate the meta-agent system ("Should I build an individual agent or group?", "I need a new agent", etc.)
- **Agent group workflow**: Complete workflow for building coordinated agent groups with infrastructure files

#### Validator Enhancements
- **PR gatekeeper pattern**: Agent Validator now exclusively submits PRs after approval
- **Iteration workflow**: Structured feedback loops between Validator and Implementer with severity levels (Critical/Recommendation/Enhancement)
- **Specification escalation**: Validator can escalate specification issues back to Architect
- **Validation report structure**: Standardized feedback format with approval criteria status

#### Agent Coordination
- **Handoff chains**: Added `handoffs` field to agent frontmatter for defining agent coordination
- **Integration points**: Required documentation of how agents coordinate within groups
- **Handoff integrity validation**: Validator checks for broken handoff references and validates graph structure

#### Frontmatter Schema
- **Version field**: Added optional `version` field to agent frontmatter (semantic versioning)
- **Handoffs field**: Added optional `handoffs` array for agent coordination
- **Model field**: Made model recommendation mandatory in agent specifications

#### Portability Features
- **Portable agent group pattern**: Enforced folder-agnostic structure (`group-name/agents/`, `copilot-instructions.md`, `README.md`)
- **Infrastructure file requirements**: Defined copilot-instructions.md and README.md standards for agent groups
- **Cross-agent references**: Guidelines for relative references (no hardcoded paths)

### Changed

#### Role Boundaries
- **Architect**: Explicitly prohibited from implementing agents (planning only)
- **Implementer**: Must work on feature branches and submit to Validator (cannot merge directly)
- **Validator**: Now responsible for PR submission and merge approval (gatekeeper role)

#### Workflow Process
- **Mandatory validation**: All agent implementations must pass through Validator before merge
- **Branch-based development**: Replaced direct-to-main commits with feature branch workflow
- **Approval criteria**: Expanded validation criteria for individual agents and agent groups

#### Documentation Standards
- **Quality checklist**: Increased from 5-10 items to 6-10 items (individual) and 8-15 items (groups)
- **Examples**: Minimum 2 examples required (ideally 3)
- **Integration points**: Now required section for documenting agent coordination

### Breaking Changes

⚠️ **These changes fundamentally alter the meta-agent workflow and require process updates:**

1. **Architect cannot implement agents**
   - **Before**: Architect could create agent definition files
   - **After**: Architect only creates specifications; Implementer creates files
   - **Migration**: If working on agent implementation, handoff to Implementer

2. **Implementer cannot merge to main**
   - **Before**: Implementer could create PR and merge directly
   - **After**: Implementer submits to Validator; only Validator creates PR
   - **Migration**: All feature branches must be submitted to Validator for review

3. **Validator is mandatory PR gatekeeper**
   - **Before**: PRs could be submitted by anyone after self-review
   - **After**: Only Validator submits PRs after approval
   - **Migration**: Wait for Validator approval before any agent goes live

4. **Feature branches are mandatory**
   - **Before**: Could commit directly to main branch
   - **After**: All work on `feature/agent-{name}` or `feature/group-{name}` branches
   - **Migration**: Create feature branch for any new agent work

5. **Handoff chains required for agent groups**
   - **Before**: Agent coordination was informal
   - **After**: Must define `handoffs` in frontmatter and validate graph integrity
   - **Migration**: Add handoffs field to existing agent groups

### Migration Guide

#### For In-Progress Agent Work

If you have agent work in progress before v1.1.0:

1. **Create feature branch** (if not already on one):
   ```bash
   git checkout -b feature/agent-{your-agent-name}
   ```

2. **Add frontmatter fields** to your agent file:
   ```yaml
   ---
   name: your-agent-name
   description: Brief description
   model: Claude Sonnet 4.5 (copilot)
   version: 1.0.0
   handoffs:  # Optional, if agent coordinates with others
     - other-agent-name
   ---
   ```

3. **Submit to Validator** (do not create PR yourself):
   - Commit and push your feature branch
   - Notify Agent Validator that implementation is ready
   - Wait for Validator review and feedback

4. **Iterate based on feedback**:
   - Make changes on same feature branch
   - Push updates and notify Validator
   - Repeat until approved

5. **Validator submits PR**:
   - When approved, Validator will create and submit PR
   - PR will be merged to main

#### For Existing Agent Groups

If you have existing agent groups without v1.1.0 features:

1. **Add CHANGELOG.md** (if version > 1.0.0)
2. **Add handoffs to frontmatter** for all agents
3. **Document integration points** showing agent coordination
4. **Validate handoff chains** (no broken references)
5. **Submit to Validator** for compliance review

#### For New Agent Work

Follow the new workflow from the start:
1. Consult Architect for specification
2. Implementer creates on feature branch
3. Submit to Validator (do not merge)
4. Iterate until approved
5. Validator submits PR

## 1.0.0 - 2024-12-01

### Added

#### Core Meta-Agent System
- **Three-agent pattern**: Architect (design), Implementer (implement), Validator (review)
- **Separation of concerns**: Strict role boundaries for each agent
- **Agent definition structure**: Standard markdown format with frontmatter

#### Agent Architect
- **Specification design**: Translates user needs into actionable agent specifications
- **Scope definition**: Defines boundaries, responsibilities, inputs/outputs
- **Success criteria**: Establishes measurable quality metrics
- **Model recommendations**: Suggests appropriate AI models for agents

#### Agent Implementer
- **Agent file creation**: Generates agent definition markdown files from specifications
- **Template structure**: Applies consistent sections (Purpose, Responsibilities, Domain Context, etc.)
- **Example generation**: Creates comprehensive examples for agent behavior
- **Quality checklists**: Designs measurable validation criteria

#### Agent Validator
- **Quality review**: Validates agent implementations against specifications
- **Best practices compliance**: Checks adherence to GitHub Copilot guidelines
- **Feedback provision**: Provides actionable improvement suggestions
- **Approval decision**: Determines if agent meets quality standards

#### Documentation
- **copilot-instructions.md**: Meta-agent system workflow and integration guide
- **README.md**: Getting started guide and agent overview
- **Agent templates**: Standard structure for agent definitions

#### Best Practices
- **GitHub Copilot guidelines**: Integrated official best practices
- **Clarity standards**: Instructions for clear, actionable agent definitions
- **Example requirements**: Minimum 2 examples per agent
- **Quality criteria**: 5-10 measurable checklist items per agent

### Workflow (v1.0.0)
1. User describes need → Architect designs specification
2. Architect hands specification → Implementer creates agent file
3. Implementer hands agent → Validator reviews quality
4. Validator provides feedback or approval

---

## Version Comparison

| Feature | v1.0.0 | v1.1.0 |
|---------|--------|--------|
| Feature branches | Optional | **Mandatory** |
| PR submission | Anyone | **Validator only** |
| Handoff chains | Informal | **Formalized in frontmatter** |
| Validation | Optional | **Mandatory gate** |
| Architect role | Could implement | **Specification only** |
| Implementer role | Could merge | **Submit to Validator** |
| Validator role | Review only | **PR gatekeeper** |
| Agent groups | Basic support | **Full infrastructure** |
| Quality gates | 1 (Validator) | **3 (Architect, Implementer, Validator)** |

---

## Links

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [GitHub Copilot Best Practices](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
