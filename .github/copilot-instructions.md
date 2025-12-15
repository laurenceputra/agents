# GitHub Copilot Instructions - Meta-Agent System

## Overview

This is a meta-agent system designed to help you build high-quality, reusable agents for any purpose. The system enforces strict separation of concerns through four specialized agents working in a defined workflow with quality gates.

**This meta-agent group follows the same portable agent structure it enforces for other agent groups.**

## Core Principle

**Strict separation of concerns with enforced workflow gates ensures quality agent implementations.**

Each meta-agent has a single, well-defined responsibility:
- **Agent Architect**: Designs specifications (planning only, no implementation)
- **Agent Implementer**: Implements specifications on feature branches (implementation only, no design decisions)
- **Agent Validator**: Reviews and gates PR submission (quality control only, controls merge process)
- **Devil's Advocate**: Critically reviews agent work, surfaces disagreements, challenges assumptions (pre-PR quality gate)

## The Four Meta-Agents

### Agent Architect (`agents/agent-architect.md`)
**Role**: Design specifications for new agents  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Agent Implementer

**When to use**: 
- You need a new agent but don't have a clear specification
- You have a problem to solve and need to figure out what kind of agent would help
- An existing specification has gaps or ambiguities

**What it does**:
- Analyzes requirements and translates into agent specifications
- Defines scope, boundaries, inputs/outputs, success criteria
- Recommends appropriate model for each agent
- Designs frontmatter schema and handoff chains
- Documents edge cases and integration points

**What it NEVER does**:
- Implement agent definition files (.agent.md)
- Write code or markdown for agents
- Make technical implementation decisions

### Agent Implementer (`agents/agent-implementer.md`)
**Role**: Implement agent definitions from specifications  
**Model**: Claude Haiku 4.5 (copilot)  
**Handoffs to**: Agent Validator

**When to use**:
- You have a complete specification from Agent Architect
- You need to turn a spec into an agent definition file
- You need to update an existing agent based on Validator feedback

**What it does**:
- Creates agent definition markdown files from specifications
- Works in feature branches (never directly on main)
- Follows GitHub Copilot best practices
- Creates comprehensive examples and quality checklists
- Iterates based on Validator feedback

**What it NEVER does**:
- Make design decisions (that's Architect's role)
- Merge PRs or commit to main (that's Validator's role)
- Skip validation review

### Agent Validator (`agents/agent-validator.md`)
**Role**: Review implementations and control PR submission  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Devil's Advocate (for critical review), Agent Implementer (feedback), Agent Architect (spec issues)

**When to use**:
- Agent Implementer has completed an implementation on a feature branch
- You need to ensure an agent meets quality standards
- You're ready to approve and merge an agent to main

**What it does**:
- Reviews agent implementations against specifications and best practices
- Provides structured feedback with severity levels (Critical/Recommendation/Enhancement)
- Iterates with Implementer until approval criteria met
- Hands off to Devil's Advocate for critical review after approval
- **Submits PRs when Devil's Advocate approves** (gatekeeper role)
- Escalates specification issues back to Architect

**What it NEVER does**:
- Implement agents (that's Implementer's role)
- Approve agents with critical issues
- Submit PRs without Devil's Advocate review
- Allow others to submit PRs for agent implementations

### Devil's Advocate (`agents/devils-advocate.md`)
**Role**: Critical review and disagreement facilitation  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Agent Validator (for PR submission), Agent Implementer (for revisions), Agent Architect (for perspective)

**When to use**:
- Agent Validator has approved an implementation
- You need critical review before PR submission
- You want to surface disagreements between agents
- You need to challenge assumptions and identify blind spots

**What it does**:
- Critically reviews work from all agents (Architect, Implementer, Validator)
- Challenges assumptions and identifies blind spots
- Surfaces and documents disagreements between agents
- Captures all perspectives with full reasoning and trade-offs
- Requests orchestrator perspective (Agent Architect) when needed
- Prepares PR writeup with all disagreements marked for human decision
- **Final quality gate before PR submission**

**What it NEVER does**:
- Override agent decisions (documents and surfaces issues, doesn't block)
- Resolve disagreements (humans make final decisions)
- Submit PRs directly (hands back to Validator with approval)
- Skip critical review even when agents agree

---

## Meta-Agent Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        META-AGENT SYSTEM WORKFLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

                                   ┌──────────┐
                                   │   USER   │
                                   │  (Need)  │
                                   └────┬─────┘
                                        │
                                        ▼
                         ┌──────────────────────────────┐
                         │   AGENT ARCHITECT            │
                         │   Model: Claude Sonnet 4.5   │
                         │   ─────────────────────      │
                         │   • Design specification     │
                         │   • Define scope/boundaries  │
                         │   • Recommend models         │
                         │   • Document handoffs        │
                         └──────────┬───────────────────┘
                                    │
                                    │ Specification
                                    ▼
                         ┌──────────────────────────────┐
                         │   AGENT IMPLEMENTER          │
                         │   Model: Claude Haiku 4.5    │
                         │   ─────────────────────      │
                         │   • Create feature branch    │
                         │   • Implement agent file(s)  │
                         │   • Self-review checklist    │
                         │   • Commit & push to branch  │
                         └──────────┬───────────────────┘
                                    │
                                    │ Feature Branch
                                    ▼
                         ┌──────────────────────────────┐
                         │   AGENT VALIDATOR            │
                         │   Model: Claude Sonnet 4.5   │
                         │   ─────────────────────      │
                         │   • Review implementation    │
                         │   • Check quality standards  │
                         │   • Validate handoffs        │
                         │   • Handoff to Devil's Adv.  │
                         └──┬───────┬───────────────┬───┘
                            │       │               │
              ┌─────────────┘       │               └─────────────┐
              │                     │                             │
              ▼                     ▼                             ▼
    ┌─────────────────┐   ┌─────────────────┐         ┌─────────────────┐
    │  Code Issues    │   │  Spec Issues    │         │    APPROVED     │
    │  (Minor/Major)  │   │  (Gaps/Unclear) │         │                 │
    └────────┬────────┘   └────────┬────────┘         └────────┬────────┘
             │                     │                            │
             │ Feedback            │ Escalate                   │ To Devil's
             │ Report              │ to Architect               │ Advocate
             ▼                     ▼                            ▼
    ┌─────────────────┐   ┌─────────────────┐         ┌─────────────────┐
    │  IMPLEMENTER    │   │   ARCHITECT     │         │ DEVIL'S ADVOCATE│
    │  (Fix & Push)   │   │  (Revise Spec)  │         │ Claude Sonnet   │
    └────────┬────────┘   └────────┬────────┘         │ • Critical Rev. │
             │                     │                   │ • Challenge     │
             │ Re-submit           │ Updated Spec      │ • Surface Disag.│
             │ to Validator        │ to Implementer    └──┬──────┬───┬───┘
             │                     │                      │      │   │
             └─────────┐     ┌─────┘            ┌─────────┘      │   └────────┐
                       │     │                  │                │            │
                       ▼     ▼                  ▼                ▼            ▼
                  [Iteration Loop]    ┌─────────────┐  ┌─────────────┐  ┌─────────┐
                                      │  Revision   │  │  Request    │  │APPROVED │
                                      │  Needed     │  │ Architect   │  │ for PR  │
                                      │ (to Impl.)  │  │ Perspective │  │         │
                                      └──────┬──────┘  └──────┬──────┘  └────┬────┘
                                             │                │              │
                                             │                │              │ PR Created
                                             │                │              │ by Validator
                                             ▼                ▼              ▼
                                      [Return Loop]    [Architect]  ┌───────────────┐
                                                       [Reviews]     │  MAIN BRANCH  │
                                                                     │  (Agent Live) │
                                                                     └───────────────┘

═════════════════════════════════════════════════════════════════════════════

QUALITY GATES (Checkpoints):

┌─────────────────────────────────────────────────────────────────────────┐
│ GATE 1: SPECIFICATION COMPLETE                                          │
│ ───────────────────────────────────────────────────────────────────     │
│ ✓ Problem statement clear                    Owner: Architect           │
│ ✓ Scope boundaries defined                   Pass: Ready for Impl.      │
│ ✓ Model recommendations provided                                        │
│ ✓ Success criteria measurable                                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ GATE 2: IMPLEMENTATION COMPLETE                                         │
│ ───────────────────────────────────────────────────────────────────     │
│ ✓ Agent file on feature branch (NOT main)   Owner: Implementer         │
│ ✓ Frontmatter matches spec                   Pass: Ready for Review     │
│ ✓ All sections present & complete                                       │
│ ✓ Examples comprehensive (2+ required)                                  │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ GATE 3: QUALITY VERIFIED                                                │
│ ───────────────────────────────────────────────────────────────────     │
│ ✓ All quality standards met                  Owner: Validator           │
│ ✓ No critical issues remaining               Pass: To Devil's Advocate  │
│ ✓ Aligns with specification                                             │
│ ✓ Best practices followed                                               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ GATE 4: CRITICAL REVIEW COMPLETE (MANDATORY PR GATE)                    │
│ ───────────────────────────────────────────────────────────────────     │
│ ✓ Assumptions challenged                     Owner: Devil's Advocate    │
│ ✓ Blind spots identified                     Pass: PR Submitted         │
│ ✓ Disagreements documented                                              │
│ ✓ All perspectives captured                  ⚠️  Only Validator         │
│ ✓ Ready for human decision                      submits PRs!            │
└─────────────────────────────────────────────────────────────────────────┘

═════════════════════════════════════════════════════════════════════════════

LEGEND:

  ┌─────┐
  │ Box │     = Agent or stage in workflow
  └─────┘

     │        = Primary workflow path (sequential)
     ▼

     ↓        = Feedback/iteration loop (returns to earlier stage)

  ═══════     = Section separator

  ✓           = Checkpoint/requirement

  ⚠️          = Critical enforcement point

═════════════════════════════════════════════════════════════════════════════

BRANCH WORKFLOW:

  feature/agent-{name}  or  feature/group-{name}
        ↓
  [Development & Testing]
        ↓
  [Validation Review]
        ↓
  [PR Submission by Validator]
        ↓
  main branch (production)

```

---

## Workflows

The meta-agent system supports two parallel workflows:
1. **Individual Agent Workflow**: Build a single agent with one .agent.md file
2. **Agent Group Workflow**: Build multiple coordinated agents with infrastructure files

### Choosing Between Individual vs Group Workflow

**Use Individual Agent Workflow when:**
- Building a single, standalone agent
- Agent doesn't require coordination with other agents
- Adding one agent to an existing group
- Simple use case with one clear responsibility

**Use Agent Group Workflow when:**
- Building 2+ agents that coordinate via handoffs
- Need infrastructure files (copilot-instructions.md, README.md)
- Creating a portable, drop-in agent system
- Agents share domain context and work together on complex workflows

---

### Specification Storage Convention

**All specifications created by Agent Architect are stored in `./.specifications/` directory at the repository root.**

**Rationale:**
- Consistent location for all specification documents
- Excluded from version control (specifications are working documents, not final artifacts)
- Easy to find and reference during implementation
- Separates specifications from final agent implementations
- Keeps repository clean (only committed code, not working documents)

**Directory Structure:**
```
/
├── .specifications/           # Agent Architect creates specs here (gitignored)
│   ├── agent-name-specification.md
│   ├── group-name-group-specification.md
│   └── refactoring-specification.md
├── .pr_details.md            # Created in root (gitignored, used by Validator)
├── .github/                   # Final agent implementations (committed)
│   ├── agents/
│   └── copilot-instructions.md
└── .gitignore                 # Excludes .specifications/ and .pr_details.md
```

**Workflow:**
1. Agent Architect creates specification in `./.specifications/{name}-specification.md`
2. Agent Implementer reads specification from `./.specifications/`
3. Agent Implementer creates implementation on feature branch
4. Agent Validator reviews implementation (may reference specification)
5. After PR merge, specification remains in `.specifications/` as historical reference (local only)

---

## Workflow: Building Individual Agents

### Phase 1: Specification Design (Architect)

**Entry Point**: User describes need for new agent

**Architect Responsibilities**:
1. Ask clarifying questions if requirements are unclear
2. Create `.specifications/` directory at repository root if it doesn't exist
3. Design comprehensive specification including:
   - Problem statement and scope boundaries
   - Key responsibilities and required inputs/outputs
   - Success criteria and quality metrics
   - Recommended model for the agent (REQUIRED)
   - Frontmatter schema (name, description, model, version, handoffs)
   - Integration points and edge cases
   - Implementation sequence and next steps

**Exit Criteria**:
- [ ] Specification is complete and actionable
- [ ] Specification saved in `./.specifications/` directory
- [ ] All required sections present
- [ ] Model recommendation provided with rationale
- [ ] Success criteria are measurable
- [ ] Edge cases documented

**Handoff**: Specification document (from `./.specifications/` directory) → Agent Implementer

---

### Phase 2: Implementation (Implementer)

**Entry Point**: Receive specification from Agent Architect

**Implementer Responsibilities**:

#### 2.1: Create Feature Branch
```bash
git checkout -b feature/agent-{agent-name}
# or for refactoring:
git checkout -b feature/refactor-{description}
```

**Branch Naming Convention**:
- Individual agent: `feature/agent-{agent-name}`
- Agent group: `feature/group-{group-name}`
- Refactoring: `feature/refactor-{description}`

**Examples**:
- `feature/agent-security-reviewer` (single agent)
- `feature/group-api-design` (multiple agents)
- `feature/refactor-meta-agents-workflow`

#### 2.2: Implement Agent Definition
Create agent file following specification:
- **Location**: `./agent-group-name/agents/{agent-name}.agent.md`
- **Frontmatter**: Include name, description, model, version, handoffs (from spec)
- **Sections**: Purpose, Responsibilities, Domain Context, Input Requirements, Output Format, Response Format, Examples (2+), Quality Checklist, Integration Points, Version History
- **Examples**: Minimum 2 (happy path + edge case), ideally 3
- **Quality Checklist**: 6-10 measurable criteria

#### 2.3: Self-Review
Before submitting to Validator, check:
- [ ] Frontmatter matches specification exactly
- [ ] Filename matches `name` field (kebab-case)
- [ ] All required sections present and complete
- [ ] At least 2 comprehensive examples with input/output
- [ ] Quality checklist has 6-10 measurable items
- [ ] No hardcoded paths or repo-specific references

#### 2.4: Commit and Push
```bash
git add .
git commit -m "Implement {agent-name} agent following specification"
git push origin feature/agent-{agent-name}
```

#### 2.5: Update Documentation (MANDATORY)

Every implementation MUST update documentation files:

**CHANGELOG.md** (Always Required):
- Add entry for current version bump
- Use standard format: Added/Changed/Fixed/Deprecated/Removed/Security
- Include date (YYYY-MM-DD), specific component names, context
- Provide migration guidance for breaking changes
- See "Changelog Entry Format Guidelines" section for examples

**README.md** (Required When):
- Agent added/removed
- Agent responsibilities change significantly
- Workflow changes
- New features affect user interaction
- Breaking changes
- Synchronized version bumps (update version badge)

**Version Number Consistency**:
- Ensure version matches across:
  - Agent frontmatter (`version: X.Y.Z`)
  - CHANGELOG.md (`## X.Y.Z - YYYY-MM-DD`)
  - README.md version badge (if synchronized bump)

**Self-Review Checklist**:
- [ ] CHANGELOG.md entry added with all changes documented
- [ ] Changelog follows standard format (Added/Changed/Fixed/etc.)
- [ ] Changelog includes context (why changed) and migration guidance (if breaking)
- [ ] README.md updated if responsibilities/workflow/features changed
- [ ] Version numbers consistent across all files
- [ ] Date in changelog is current (YYYY-MM-DD format)

#### 2.6: Submit to Validator
- Notify Agent Validator that implementation is ready
- Provide branch name and link to original specification
- **DO NOT create PR** - Validator does that after approval

**Exit Criteria**:
- [ ] Agent file created on feature branch
- [ ] Follows specification completely
- [ ] Self-review checklist passed
- [ ] Documentation updated (CHANGELOG.md and README.md if applicable)
- [ ] Submitted to Validator (not merged)

**Handoff**: Feature branch with implementation → Agent Validator

---

### Phase 3: Validation (Validator)

**Entry Point**: Receive implementation from Agent Implementer on feature branch

**Validator Responsibilities**:

#### 3.1: Review Implementation
Check against specification and best practices:
- Completeness (all required sections present)
- Quality (depth and clarity of each section)
- Best practices (GitHub Copilot guidelines)
- Examples (sufficient coverage, clear input/output)
- Quality checklist (measurable criteria)
- Frontmatter (matches spec, valid handoffs)

#### 3.1.1: Documentation Validation (MANDATORY)

Validator MUST check documentation updates:

**CHANGELOG.md Validation**:
- [ ] Entry exists for current version
- [ ] Entry uses standard format (Added/Changed/Fixed/Deprecated/Removed/Security)
- [ ] Entry includes date in YYYY-MM-DD format
- [ ] All changes from PR are documented in changelog
- [ ] Descriptions are specific (not vague like "updated agent")
- [ ] Context provided for why changes were made
- [ ] Breaking changes include migration guidance
- [ ] Version number matches agent frontmatter

**README.md Validation**:
- [ ] Updated if agent added/removed
- [ ] Updated if agent responsibilities changed
- [ ] Updated if workflow changed
- [ ] Updated if new user-facing features added
- [ ] Version badge updated (if synchronized bump)
- [ ] Consistent with changes described in CHANGELOG.md
- [ ] No outdated information remains

**Version Consistency Check**:
- [ ] Agent frontmatter version matches CHANGELOG.md
- [ ] README.md version badge matches (if synchronized bump)
- [ ] Date in changelog is current

**Feedback Examples**:

*Critical Issue - Missing Changelog*:
"CRITICAL: CHANGELOG.md not updated. Every version bump requires a changelog entry following the standard format (Added/Changed/Fixed/etc.). Document the changes made in this PR with context and migration guidance."

*Critical Issue - Incomplete Changelog*:
"CRITICAL: Changelog entry is too vague. 'Updated agent' doesn't describe what changed or why. Provide specific component names, describe the change, and explain the context. See examples in copilot-instructions.md."

*Critical Issue - Version Mismatch*:
"CRITICAL: Version mismatch detected. Agent frontmatter shows 1.2.0, but CHANGELOG.md has 1.1.1. Ensure version numbers are consistent across all files."

*Recommendation - README Could Be Clearer*:
"RECOMMENDATION: README.md was updated but could be clearer. Consider adding an example in the 'Quick Start' section showing the new workflow step."

#### 3.2: Decision Tree

**Path A: Critical Issues Found → Feedback Loop**
```
Validator reviews → Issues found → Detailed feedback report
   ↓
Validator categorizes: Critical / Recommendations / Enhancements
   ↓
Validator sends back to Implementer with specific, actionable feedback
   ↓
Implementer fixes on same branch → Commits → Pushes → Notifies Validator
   ↓
Validator re-reviews (return to 3.1)
   ↓
Repeat until all critical issues resolved
```

**Feedback Report Structure**:
- Overall Assessment (status, confidence, summary)
- Completeness Review (all sections present and thorough)
- Best Practices Compliance (GitHub Copilot guidelines)
- Quality Assessment (strengths + issues by severity)
- Testability Assessment
- Integration Review
- Approval Criteria Status
- **PR Submission Decision** (Approved / Needs Revision / Spec Issue)
- Next Steps (prioritized actions)

**Path B: Specification Issues Found → Escalation**
```
Validator identifies specification gaps/ambiguities
   ↓
Validator escalates to Agent Architect with specific concerns
   ↓
Architect revises specification
   ↓
Architect hands revised spec back to Implementer
   ↓
Implementer updates implementation on same branch
   ↓
Return to Path A (validation loop)
```

**Path C: Approved → PR Submission**
```
Validator confirms all approval criteria met
   ↓
Validator marks as APPROVED in validation report
   ↓
Validator creates pull request from feature branch to main
   ↓
Validator includes validation summary in PR description
   ↓
Validator submits PR
   ↓
PR merged to main (agent goes live)
```

**Exit Criteria for Approval**:
- [ ] All required sections present and complete
- [ ] Instructions clear and actionable
- [ ] At least 2 comprehensive examples
- [ ] Quality checklist with measurable criteria (6-10 items)
- [ ] Integration points documented
- [ ] Follows markdown conventions
- [ ] Aligns with specification
- [ ] No critical issues remaining

**Handoff Options**:
- If needs revision → Agent Implementer (with feedback)
- If spec issue → Agent Architect (for spec revision)
- If approved → Repository (via PR submission)

---

## Workflow: Building Agent Groups

Agent groups are collections of coordinated agents with infrastructure files (copilot-instructions.md, README.md). They are portable and can be dropped into any repository.

**CRITICAL REQUIREMENT**: Every agent group MUST include Devil's Advocate agent for critical review and disagreement capture. This is non-negotiable and applies to all agent groups without exception.

### Phase 1: Group Specification Design (Architect)

**Entry Point**: User describes need for multiple coordinated agents

**Architect Responsibilities**:
1. Ask clarifying questions about scope, coordination, and handoff patterns
2. Create `.specifications/` directory at repository root if it doesn't exist
3. Design group specification including:
   - Group purpose and scope boundaries
   - List of agents in group with individual responsibilities
   - **MANDATORY: Include Devil's Advocate agent for critical review (REQUIRED for all groups)**
   - Handoff chain design (which agents coordinate, including handoffs to devils-advocate)
   - Model recommendations for each agent
   - Frontmatter schema for all agents (all must have handoff to devils-advocate)
   - Infrastructure file requirements (copilot-instructions.md, README.md)
   - Integration points and workflow diagrams
   - Quality gates for group cohesion (including critical review gate)

**Exit Criteria**:
- [ ] Group purpose clear and actionable
- [ ] Specification saved in `./.specifications/` directory
- [ ] All agents defined with responsibilities
- [ ] **Devil's Advocate agent included in specification (MANDATORY)**
- [ ] Handoff chains documented (which agent hands to which, including devils-advocate as final gate)
- [ ] Model recommendations for each agent
- [ ] Infrastructure file structure defined
- [ ] Group-level quality criteria established
- [ ] Portable structure requirements specified
- [ ] All agents have handoff to devils-advocate defined

**Handoff**: Group specification document (from `./.specifications/` directory) → Agent Implementer

---

### Phase 2: Group Implementation (Implementer)

**Entry Point**: Receive group specification from Agent Architect

**Implementer Responsibilities**:

#### 2.1: Create Feature Branch
```bash
git checkout -b feature/group-{group-name}
```

**Branch Naming Examples**:
- `feature/group-api-design`
- `feature/group-security-review`
- `feature/group-testing-strategy`

#### 2.2: Implement Agent Group Structure
Create folder structure following portable agent group pattern:
```
group-name/
├── agents/
│   ├── agent-1.agent.md
│   ├── agent-2.agent.md
│   └── agent-3.agent.md
├── copilot-instructions.md
├── README.md
└── CHANGELOG.md (optional for v1.0.0, required for v1.1.0+)
```

#### 2.3: Implement Infrastructure Files

**copilot-instructions.md**:
- Group overview and purpose
- Agent descriptions (name, role, model, handoffs)
- Workflow documentation (how agents coordinate)
- Decision trees for users
- Quality gates
- Examples
- Version history

**README.md**:
- Getting started guide
- Agent list with descriptions
- Usage examples
- Integration instructions
- Troubleshooting

**CHANGELOG.md** (for versions > 1.0.0):
- Version history
- Breaking changes
- Migration guides

#### 2.4: Implement Individual Agent Files
For each agent in the group:
- Create agent definition in `agents/` folder
- Follow individual agent implementation standards
- Ensure handoff references are valid (point to agents in group)
- Include integration points section showing coordination
- Use portable references (no hardcoded paths)

#### 2.5: Validate Group Cohesion (Self-Review)
Before submitting to Validator, check:
- [ ] Folder structure matches portable pattern
- [ ] All infrastructure files present and complete
- [ ] All agent files present with valid frontmatter
- [ ] Handoff chains form valid graph (no broken references)
- [ ] Models match Architect recommendations
- [ ] No hardcoded paths or repo-specific names
- [ ] Filenames match agent `name` fields (kebab-case)
- [ ] copilot-instructions.md includes workflow and examples
- [ ] README.md provides usage guidance

#### 2.6: Commit and Push
```bash
git add .
git commit -m "Implement {group-name} agent group following specification"
git push origin feature/group-{group-name}
```

#### 2.7: Update Documentation (MANDATORY)

Every agent group implementation MUST update documentation files (same requirements as individual agents):

**CHANGELOG.md** (Always Required):
- Add entry for current version bump
- Use standard format: Added/Changed/Fixed/Deprecated/Removed/Security
- Document changes to all agents in the group
- Include context and migration guidance
- See "Changelog Entry Format Guidelines" section for examples

**README.md** (Required When):
- Agent group structure changes
- Agent added/removed from group
- Workflow changes
- New features affect user interaction
- Breaking changes
- Synchronized version bumps (update version badge)

**Version Number Consistency**:
- Ensure version matches across:
  - All agent frontmatter fields (`version: X.Y.Z`)
  - CHANGELOG.md (`## X.Y.Z - YYYY-MM-DD`)
  - README.md version badge (if synchronized bump)

**Self-Review Checklist**:
- [ ] CHANGELOG.md entry added documenting all changes
- [ ] Changelog follows standard format with specific component names
- [ ] Changelog includes context and migration guidance
- [ ] README.md updated if group structure/workflow changed
- [ ] Version numbers consistent across all agent files
- [ ] Date in changelog is current (YYYY-MM-DD format)

#### 2.8: Submit to Validator
- Notify Agent Validator that group implementation is ready
- Provide branch name and specification reference
- **DO NOT create PR** - Validator does that after approval

**Exit Criteria**:
- [ ] Agent group created on feature branch (not main)
- [ ] All agents implemented with valid frontmatter
- [ ] Infrastructure files complete
- [ ] Handoff chains validated
- [ ] Documentation updated (CHANGELOG.md and README.md if applicable)
- [ ] Self-review checklist passed
- [ ] Submitted to Validator (not merged)

**Handoff**: Feature branch with agent group → Agent Validator

---

### Phase 3: Group Validation (Validator)

**Entry Point**: Receive agent group implementation from Implementer on feature branch

**Validator Responsibilities**:

#### 3.1: Review Group Implementation
Check against group specification and best practices:
- **Completeness**: All agents and infrastructure files present
- **Consistency**: Agents follow same patterns and quality standards
- **Handoff Integrity**: All handoff references valid, no broken chains
- **Infrastructure Quality**: copilot-instructions.md and README.md comprehensive
- **Portability**: No hardcoded paths, folder-agnostic references
- **Frontmatter Validity**: All agents have valid YAML frontmatter matching spec
- **Model Alignment**: All agent models match Architect recommendations

#### 3.2: Group-Specific Validation Criteria

**Structural Validation**:
- [ ] Folder structure: `group-name/agents/`, `copilot-instructions.md`, `README.md`
- [ ] All agents in `agents/` subdirectory
- [ ] Filenames match `name` fields exactly (kebab-case)
- [ ] No agents outside `agents/` folder

**Handoff Chain Validation**:
- [ ] All handoff references point to agents in group
- [ ] No broken handoff chains (dangling references)
- [ ] Handoff chains form valid graph (can trace workflows)
- [ ] Circular handoffs documented if intentional

**Infrastructure Completeness**:
- [ ] copilot-instructions.md includes: overview, agents, workflows, decision trees, examples
- [ ] README.md includes: getting started, agent list, usage examples
- [ ] CHANGELOG.md present if version > 1.0.0

**Cross-Agent Consistency**:
- [ ] All agents follow same section structure
- [ ] Quality checklists comparable depth (6-10 items each)
- [ ] Integration points documented for coordinating agents
- [ ] Examples demonstrate handoff patterns

**Portability Validation**:
- [ ] No absolute paths
- [ ] No references to parent folders or repo-specific names
- [ ] Folder can be renamed without breaking references
- [ ] Agents reference each other by name, not path

**Documentation Validation** (Same as Individual Agent):
- [ ] CHANGELOG.md entry exists for current version
- [ ] Changelog uses standard format and includes all changes
- [ ] Changelog provides context and migration guidance
- [ ] README.md updated if group structure/workflow changed
- [ ] Version numbers consistent across all agent files
- [ ] Date in changelog is current

#### 3.3: Decision Tree (Same as Individual Agent)

**Path A: Critical Issues → Feedback Loop**  
**Path B: Specification Issues → Escalate to Architect**  
**Path C: Approved → PR Submission**

**Exit Criteria for Group Approval**:
- [ ] All structural validation passed
- [ ] All handoff chains valid
- [ ] Infrastructure files complete and comprehensive
- [ ] Cross-agent consistency verified
- [ ] Portability validated
- [ ] All agents meet individual quality standards
- [ ] No critical issues remaining

**Handoff Options**:
- If needs revision → Agent Implementer (with feedback)
- If spec issue → Agent Architect (for spec revision)
- If approved → Repository (via PR submission)

---

## Decision Trees

### Quick Reference

| Your Situation | Agent to Consult | What They'll Do |
|---|---|---|
| **[A] Need agent, no spec** | @agent-architect | Design specification |
| **[B] Have spec to implement** | @agent-implementer | Create agent on branch |
| **[C] Have implementation to review** | @agent-validator | Review and provide feedback or approve |
| **[D] Have approved implementation** | @devils-advocate | Critical review, challenge assumptions |
| **[E] Want to merge** | @agent-validator only | Validator submits PR after Devil's Advocate approval |

---

### Master Decision Tree

```
START: Where are you in the agent lifecycle?
  │
  ├─ [A] I NEED AN AGENT (but no specification yet)
  │   │
  │   Is there a clear specification?
  │     │
  │     ├─ NO → Consult @agent-architect
  │     │        │
  │     │        Architect asks: Single agent or group?
  │     │          │
  │     │          ├─ SINGLE AGENT
  │     │          │   - Architect designs specification
  │     │          │   - Defines scope, model, inputs/outputs
  │     │          │   - Provides spec document
  │     │          │   └─> Proceed to [B]
  │     │          │
  │     │          └─ AGENT GROUP (multiple coordinating agents)
  │     │              - Architect designs group specification
  │     │              - Defines all agents, handoff chains, models
  │     │              - Provides group spec document
  │     │              └─> Proceed to [B]
  │     │
  │     └─ YES → Skip to [B]
  │
  │
  ├─ [B] I HAVE A SPECIFICATION TO IMPLEMENT
  │   │
  │   Consult @agent-implementer
  │     │
  │     Implementer asks: Individual agent or group?
  │       │
  │       ├─ INDIVIDUAL AGENT
  │       │   1. Create branch: feature/agent-{name}
  │       │   2. Create {name}.agent.md with frontmatter
  │       │   3. Implement all sections from spec
  │       │   4. Self-review checklist
  │       │   5. Commit and push to branch
  │       │   └─> Proceed to [C]
  │       │
  │       └─ AGENT GROUP
  │           1. Create branch: feature/group-{name}
  │           2. Create folder: {group-name}/agents/
  │           3. Implement all agent files with frontmatter
  │           4. Create copilot-instructions.md (workflow, decision trees)
  │           5. Create README.md (usage guide)
  │           6. Validate handoff chains (no broken references)
  │           7. Self-review group cohesion
  │           8. Commit and push to branch
  │           └─> Proceed to [C]
  │
  │
  ├─ [C] I HAVE AN IMPLEMENTATION TO REVIEW
  │   │
  │   Submit to @agent-validator (DO NOT merge yourself)
  │     │
  │     Validator reviews implementation
  │       │
  │       Decision point:
  │         │
  │         ├─ CRITICAL ISSUES FOUND
  │         │   └─> Validator provides detailed feedback
  │         │       ↓
  │         │       @agent-implementer fixes on same branch
  │         │       ↓
  │         │       Commit and push fixes
  │         │       ↓
  │         │       Notify Validator
  │         │       ↓
  │         │       Return to [C] (re-review)
  │         │
  │         ├─ SPECIFICATION ISSUES FOUND
  │         │   └─> Validator escalates to @agent-architect
  │         │       ↓
  │         │       Architect revises specification
  │         │       ↓
  │         │       @agent-implementer updates implementation
  │         │       ↓
  │         │       Commit and push updates
  │         │       ↓
  │         │       Return to [C] (re-review)
  │         │
  │         └─ APPROVED ✓
         └─ APPROVED ✓
             └─> Hand off to @devils-advocate
                 ↓
                 Devil's Advocate reviews
                 ↓
                 Proceed to [D]
  │
  │
  ├─ [D] APPROVED IMPLEMENTATION UNDER CRITICAL REVIEW
  │   │
  │   Submit to @devils-advocate (after Validator approval)
  │     │
  │     Devil's Advocate performs critical review
  │       │
       Decision point:  
  │         │
  │         ├─ REVISION NEEDED
  │         │   └─> Critical issues found
  │         │       ↓
  │         │       Devil's Advocate sends back to @agent-implementer
  │         │       ↓
  │         │       Implementer fixes on same branch
  │         │       ↓
  │         │       Return to [C] (re-review by Validator)
  │         │
  │         ├─ SPECIFICATION ISSUE
  │         │   └─> Requests @agent-architect perspective
  │         │       ↓
  │         │       Architect reviews and weighs in
  │         │       ↓
  │         │       If spec revision needed: Return to [B]
  │         │       If just perspective: Continue to approval
  │         │
  │         └─ APPROVED FOR PR ✓
  │             └─> Hand back to @agent-validator
  │                 ↓
  │                 Validator submits PR with Devil's Advocate writeup
  │                 ↓
  │                 PR merged to main
  │                 ↓
  │                 DONE! Agent goes live
  │
  │
  └─ [E] I WANT TO MERGE MY IMPLEMENTATION
  │
  └─ [E] I WANT TO MERGE MY IMPLEMENTATION
      │
      ⚠️  STOP - Only @agent-validator submits PRs (after Devil's Advocate approval)
      │
      Has Agent Validator AND Devil's Advocate approved it?
        │
        ├─ NO VALIDATOR APPROVAL → Return to [C]
        │                          Submit to Validator for review
        │
        ├─ NO DEVIL'S ADVOCATE APPROVAL → Return to [D]
        │                                  Wait for critical review
        │
        └─ BOTH APPROVED → Wait for Validator to submit PR
                           (Validator handles merge process)
                           You do NOT create the PR yourself
```

---

### Workflow Rules (Critical)

1. **All implementations on feature branches** - Never commit directly to main
2. **Branch naming**:
   - Individual agent: `feature/agent-{name}`
   - Agent group: `feature/group-{name}`
   - Refactoring: `feature/refactor-{description}`
3. **Only Validator submits PRs** - Implementer, Architect, and Devil's Advocate never merge
4. **Iterate until approved** - Expect feedback loops; quality takes time
5. **Devil's Advocate is mandatory** - All implementations require critical review before PR
6. **Feature branch workflow**: Create branch → Implement → Submit to Validator → Submit to Devil's Advocate → Iterate → Validator submits PR

---

### Quick Navigation

- **Need specification?** → Start at [A], consult @agent-architect
- **Have specification?** → Start at [B], consult @agent-implementer  
- **Have implementation?** → Start at [C], consult @agent-validator
- **Have approved implementation?** → Start at [D], consult @devils-advocate
- **Want to merge?** → Start at [E], but remember: only Validator submits PRs after Devil's Advocate approval
- **Not sure which agent to use?** → See Quick Reference table above

## Quality Gates

### Gate 1: Architect Approval (Specification Complete)
**Checked by**: Agent Architect (self-review)

Must have:
- [ ] Problem statement clear and specific
- [ ] Scope boundaries explicit (in-scope and out-of-scope)
- [ ] Responsibilities actionable and measurable
- [ ] Required inputs and expected outputs documented
- [ ] Success criteria measurable
- [ ] Recommended model specified with rationale
- [ ] Frontmatter schema defined
- [ ] Edge cases and constraints documented
- [ ] Integration points designed
- [ ] Implementation sequence provided
- [ ] **For Agent Groups: Devil's Advocate agent included in specification (MANDATORY)**
- [ ] **For Agent Groups: All agents have handoff to devils-advocate defined**

**Pass criteria**: Specification is actionable and complete enough for Implementer to proceed without guessing.

---

### Gate 2: Implementer Completion (Agent Implemented on Branch)
**Checked by**: Agent Implementer (self-review)

Must have:
- [ ] Agent file created on feature branch (not main)
- [ ] Branch named correctly: `feature/agent-{name}` or `feature/refactor-{description}`
- [ ] Frontmatter matches specification (name, description, model, version, handoffs)
- [ ] Filename matches `name` field exactly (kebab-case)
- [ ] All required sections present and complete
- [ ] At least 2 comprehensive examples (ideally 3)
- [ ] Quality checklist has 6-10 measurable criteria
- [ ] Integration points documented
- [ ] Version history started
- [ ] No hardcoded paths or repo-specific names

**Pass criteria**: Agent definition is complete and ready for quality review. Implementer has submitted to Validator (not merged).

---

### Gate 3: Validator Approval (Quality Verified, PR Submitted) - MANDATORY
**Checked by**: Agent Validator

Must have:
- [ ] All required sections present and thorough
- [ ] Instructions clear, specific, and actionable
- [ ] At least 2 comprehensive examples with input/output
- [ ] Quality checklist measurable (not subjective)
- [ ] Integration points clear
- [ ] Follows GitHub Copilot best practices
- [ ] Follows markdown conventions
- [ ] Aligns with original specification
- [ ] No critical issues remaining
- [ ] Frontmatter valid and handoffs correct

**Pass criteria**: Agent meets all quality standards. Validator approves and submits PR to main.

**Only after Gate 3**: Agent is merged and goes live.

---

## Portable Agent Group Pattern

This meta-agent system enforces and exemplifies the portable agent group structure:

### Required Structure
```
agent-group-name/
├── agents/
│   ├── agent-1.agent.md          # Individual agent definition
│   ├── agent-2.agent.md
│   ├── agent-3.agent.md
│   └── devils-advocate.agent.md  # MANDATORY: Critical review agent (REQUIRED for all groups)
├── copilot-instructions.md       # Group-level workflow and setup (THIS FILE)
├── README.md                      # Usage guide and agent overview
└── CHANGELOG.md                   # Version history (optional, for v1.1.0+)
```

**CRITICAL**: Every agent group MUST include `devils-advocate.agent.md` for critical review and disagreement capture. This is non-negotiable.

### Agent Frontmatter Schema (Required)
```yaml
---
name: agent-identifier              # Required: kebab-case, matches filename
description: One-line agent purpose # Required: 50-100 characters
model: Claude Sonnet 4.5 (copilot) # Required: From Architect recommendations
version: 1.0.0                      # Optional: Semantic versioning (default 1.0.0)
handoffs:                           # Optional: Handoff objects for agent coordination
  - label: "Action description"     # Required: User-facing handoff action
    agent: "agent-name"             # Required: Target agent name (kebab-case)
    prompt: "Context for handoff"   # Required: Instructions for receiving agent
    send: false                     # Optional: Auto-send (default: false)
---
```

**Handoff Field Requirements**:
- **label**: Short, action-oriented phrase (3-6 words, starts with verb)
- **agent**: Target agent's `name` field value (kebab-case)
- **prompt**: Context-specific instruction for receiving agent (1-2 sentences)
- **send**: Optional boolean for automatic handoffs (use sparingly)

### Portability Features
- **No hardcoded paths**: Agents use relative references
- **Folder-agnostic**: Can be renamed from `product-development-agents` to `.github` without modification
- **Self-contained**: All agents and workflow documentation in one folder
- **Documented handoffs**: Frontmatter defines agent coordination
- **Consistent structure**: Same pattern across all agent groups

**This meta-agent system (`/.github/`) follows this exact pattern**, serving as the reference implementation.

---

## Best Practices (from GitHub Copilot Documentation)

### 1. Be Specific and Clear
- Define exact scope and boundaries
- Use concrete examples
- Specify output formats explicitly
- Include edge cases and constraints

### 2. Provide Context
- Explain the "why" behind the agent's purpose
- Reference relevant domain knowledge
- Define terminology and abbreviations
- Link to related agents or documentation

### 3. Structure for Clarity
- Use consistent markdown formatting
- Organize with clear headings
- Include bullet points and numbered lists
- Separate instructions from examples

### 4. Include Examples
- Provide concrete input/output examples
- Show both simple and complex scenarios
- Demonstrate edge case handling
- Include counterexamples (what NOT to do)

### 5. Define Success Criteria
- Make outcomes measurable
- Include quality checklists
- Specify acceptance criteria
- Define what "done" looks like

### 6. Optimize for Iteration
- Keep instructions modular
- Support incremental improvements
- Enable easy updates
- Document versioning and changes

---

## Troubleshooting Common Issues

### "Architect is implementing agents"
**Problem**: Architect created agent definition file directly  
**Violation**: Architect only designs specifications, never implements  
**Solution**: 
1. Architect provides specification ONLY
2. Implementer creates agent file from spec
3. Validator reviews implementation

---

### "Implementer merged directly to main"
**Problem**: Implementer created PR and merged without Validator review  
**Violation**: Only Validator submits PRs  
**Solution**:
1. Implementer always works on feature branches
2. Implementer submits to Validator (does not create PR)
3. Validator reviews and submits PR when approved

---

### "Validator approved but someone else merged"
**Problem**: Validator said "approved" but didn't submit PR  
**Violation**: Validator must submit the PR themselves  
**Solution**:
1. Validator approval includes PR submission
2. Validator creates the PR after approval
3. Validator is responsible for merge (can delegate click but owns process)

---

### "Implementation doesn't match specification"
**Problem**: Implementer made design decisions not in spec  
**Violation**: Implementer should only implement what's specified  
**Solution**:
1. If spec is ambiguous: Implementer asks Architect for clarification
2. Implementer does not guess or make design decisions
3. Architect updates spec, then Implementer proceeds

---

### "Validator found specification issues during review"
**Problem**: Specification had gaps that became apparent during implementation review  
**Not a violation**: This is expected and part of workflow  
**Solution**:
1. Validator documents specification issues clearly
2. Validator escalates to Architect (handoff)
3. Architect revises specification
4. Implementer updates implementation based on revised spec
5. Validator re-reviews

---

### "Too many validation iterations"
**Problem**: Implementer and Validator going back and forth 5+ times  
**Not necessarily a violation**: Iteration is expected  
**Solutions**:
- If repeated rejections for same issue type: Architect and Validator should clarify standards
- If specification keeps changing: Architect should stabilize spec before implementation
- If quality bar unclear: Validator should provide examples of "good" in feedback
- Patience: Quality takes time; iteration is normal

---

### "Emergency hotfix needed for agent"
**Problem**: Critical bug in agent blocking users  
**Acceptable exception**: Abbreviated workflow for emergencies  
**Process**:
1. Implementer fixes on emergency branch
2. Validator does rapid review (same day)
3. Validator fast-tracks approval if fix is clear
4. Document why emergency process used
5. Full retrospective review after fix deployed

---

## Common Agent Categories

The meta-system can help you build agents for:

### Development Agents
- **Code Reviewers**: Reviews code for quality, security, and best practices
- **Test Designers**: Designs comprehensive test strategies
- **Technical Writers**: Creates documentation, API specs, and guides
- **Debuggers**: Diagnoses and fixes issues systematically
- **Refactoring Advisors**: Plans code improvements and migrations

### Product Agents
- **Product Managers**: Defines requirements and acceptance criteria
- **User Researchers**: Analyzes user needs and feedback
- **UX Designers**: Designs user experiences and interfaces
- **Feature Prioritizers**: Evaluates and ranks features by impact

### Operations Agents
- **DevOps Engineers**: Handles deployment, infrastructure, monitoring
- **Security Auditors**: Reviews for security vulnerabilities
- **Performance Optimizers**: Analyzes and improves performance
- **Incident Responders**: Troubleshoots production issues

### Specialized Agents
- **Data Analysts**: Analyzes data and generates insights
- **API Designers**: Designs clean, consistent APIs
- **Migration Planners**: Plans and executes system migrations
- **Documentation Generators**: Automates documentation creation

### Universal Agent (MANDATORY for all Agent Groups)
- **Devil's Advocate**: Critical review and disagreement facilitation - MUST be included in every agent group for quality assurance and assumption challenging

---

## Tips for Effective Agents

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Composable**: Agents should work well together through handoffs
3. **Testable**: Include clear success criteria and quality checklists
4. **Maintainable**: Document assumptions and limitations
5. **Evolvable**: Design for change with version history
6. **Portable**: No hardcoded paths, folder-agnostic references

---

## Versioning Strategy

This meta-agent system uses **hybrid versioning** to balance group cohesion with individual agent evolution:

### Versioning Model

**Hybrid Approach: Synchronized Major/Minor, Independent Patches**

- **Major.Minor versions synchronized** across all agents in the group
  - Breaking changes or significant feature additions trigger group-wide minor version bumps
  - Example: When workflow changes affect all agents, bump 1.0.0 → 1.1.0 for all
  
- **Patch versions can be independent** for individual agents
  - Bug fixes, documentation updates, or minor clarifications can increment patch independently
  - Example: architect.agent.md can be 1.1.1 while others remain 1.1.0

### Version Format

```yaml
version: MAJOR.MINOR.PATCH
```

- **MAJOR**: Breaking changes to agent behavior or workflow (synchronized)
- **MINOR**: New features or workflow enhancements (synchronized)
- **PATCH**: Bug fixes, clarifications, documentation updates (can be independent)

### When to Bump Versions

#### Synchronized (All Agents Updated)

**Minor Version Bump (1.0.0 → 1.1.0)**:
- Workflow changes affecting multiple agents
- New handoff patterns introduced
- Quality gates added or modified
- Infrastructure file updates (copilot-instructions.md, README.md)
- Breaking changes to agent coordination

**Major Version Bump (1.0.0 → 2.0.0)**:
- Complete workflow redesign
- Incompatible changes to agent interfaces
- Removal of agents from group
- Breaking changes to frontmatter schema

#### Independent (Single Agent Updated)

**Patch Version Bump (1.1.0 → 1.1.1)**:
- Bug fixes in individual agent instructions
- Clarifications to examples or quality checklists
- Typo corrections
- Documentation improvements
- Small refinements not affecting workflow

### Decision Tree: Which Version to Bump?

```
START: Change proposed to meta-agent system
  ↓
Does it affect the workflow or coordination between agents?
  │
  ├─ YES → Does it break existing behavior?
  │         │
  │         ├─ YES → MAJOR version bump (synchronized)
  │         │        Example: 1.1.0 → 2.0.0 all agents
  │         │        Update: All agents, copilot-instructions.md, README.md
  │         │
  │         └─ NO → MINOR version bump (synchronized)
  │                 Example: 1.0.0 → 1.1.0 all agents
  │                 Update: All agents, copilot-instructions.md, README.md
  │
  └─ NO → Is it a single agent change?
           │
           ├─ YES → PATCH version bump (independent)
           │        Example: architect.agent.md 1.1.0 → 1.1.1
           │        Update: Only the affected agent file
           │
           └─ NO → Evaluate scope and choose appropriate version
```

### Examples

**Scenario 1: Bug Fix in Agent Architect**
- **Change**: Fixed typo in example output
- **Decision**: Patch bump (independent)
- **Action**: architect.agent.md 1.1.0 → 1.1.1
- **Files Updated**: `agents/architect.agent.md` only

**Scenario 2: New Quality Gate Added**
- **Change**: Added portability validation checklist affecting all agents
- **Decision**: Minor bump (synchronized)
- **Action**: All agents 1.0.0 → 1.1.0
- **Files Updated**: All agents, `copilot-instructions.md`, `README.md`

**Scenario 3: Workflow Redesign**
- **Change**: Replaced three-phase workflow with two-phase workflow
- **Decision**: Major bump (synchronized)
- **Action**: All agents 1.1.0 → 2.0.0
- **Files Updated**: All agents, `copilot-instructions.md`, `README.md`, migration guide

**Scenario 4: Documentation Clarification**
- **Change**: Added example to Agent Implementer's Response Format section
- **Decision**: Patch bump (independent)
- **Action**: implementer.agent.md 1.1.0 → 1.1.1
- **Files Updated**: `agents/implementer.agent.md` only

### Version History Requirements

All agent files and infrastructure files MUST include a Version History section:

**Agent Files (agents/*.agent.md)**:
```markdown
## Version History

- **1.1.1**: Fixed typo in example output
- **1.1.0**: Added strict workflow enforcement, quality gates, decision trees
- **1.0.0** (Initial): Core agent architecture design capabilities
```

**Infrastructure Files (copilot-instructions.md, README.md)**:
```markdown
## Version History

- **1.1.0** - Added strict workflow enforcement, quality gates, decision trees
- **1.0.0** - Initial meta-agent system with Architect, Implementer, Validator
```

### Validation Checklist

When updating versions, verify:
- [ ] Version numbers follow semantic versioning (MAJOR.MINOR.PATCH)
- [ ] Synchronized changes update all agents + infrastructure files
- [ ] Independent changes update only affected agent
- [ ] Version history updated with clear, concise change description
- [ ] Frontmatter `version` field matches version history
- [ ] CHANGELOG.md created if version > 1.0.0 (optional for 1.1.0, required for 1.2.0+)

---

## References

- **GitHub Copilot Best Practices**: [Official Documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
- **Agent Files**: See `agents/` directory for the three meta-agents
- **Example Agent Groups**: See `../product-development-agents/` and `../legacy-planning/` for working examples

---

## Version History

- **1.5.0** - Added Devil's Advocate agent for critical review and disagreement capture before PR submission. Updated workflow to include mandatory critical review gate, updated decision trees, and added fourth quality gate.
- **1.4.0** - Updated handoff format to GitHub Copilot object schema (label, agent, prompt, send) across all meta-agents and updated Agent Frontmatter Schema documentation
- **1.3.0** - Required all specifications be created in `./.specifications/` directory at repository root, added specification storage convention section, updated workflows
- **1.2.0** - Added mandatory CHANGELOG.md and README.md update requirements with format guidelines
- **1.1.0** - Added strict workflow enforcement, quality gates, decision trees, and PR gatekeeper pattern
- **1.0.0** - Initial meta-agent system with Architect, Implementer, Validator
