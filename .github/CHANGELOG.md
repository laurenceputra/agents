# Changelog

All notable changes to the Meta-Agent System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
