# Changelog

All notable changes to the Meta-Agent System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
