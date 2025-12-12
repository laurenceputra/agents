# GitHub Copilot Instructions - Meta-Agent System

## Overview

This is a meta-agent system designed to help you build high-quality, reusable agents for any purpose. The system enforces strict separation of concerns through three specialized agents working in a defined workflow with quality gates.

**This meta-agent group follows the same portable agent structure it enforces for other agent groups.**

## Core Principle

**Strict separation of concerns with enforced workflow gates ensures quality agent implementations.**

Each meta-agent has a single, well-defined responsibility:
- **Agent Architect**: Designs specifications (planning only, no implementation)
- **Agent Implementer**: Implements specifications on feature branches (implementation only, no design decisions)
- **Agent Validator**: Reviews and gates PR submission (quality control only, controls merge process)

## The Three Meta-Agents

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
**Handoffs to**: Agent Implementer (feedback), Agent Architect (spec issues)

**When to use**:
- Agent Implementer has completed an implementation on a feature branch
- You need to ensure an agent meets quality standards
- You're ready to approve and merge an agent to main

**What it does**:
- Reviews agent implementations against specifications and best practices
- Provides structured feedback with severity levels (Critical/Recommendation/Enhancement)
- Iterates with Implementer until approval criteria met
- **Submits PRs when approved** (gatekeeper role)
- Escalates specification issues back to Architect

**What it NEVER does**:
- Implement agents (that's Implementer's role)
- Approve agents with critical issues
- Allow others to submit PRs for agent implementations

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
                         │   • Gate PR submission       │
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
             │ Feedback            │ Escalate                   │ PR Created
             │ Report              │ to Architect               │ by Validator
             ▼                     ▼                            ▼
    ┌─────────────────┐   ┌─────────────────┐         ┌─────────────────┐
    │  IMPLEMENTER    │   │   ARCHITECT     │         │   MAIN BRANCH   │
    │  (Fix & Push)   │   │  (Revise Spec)  │         │  (Agent Live)   │
    └────────┬────────┘   └────────┬────────┘         └─────────────────┘
             │                     │
             │ Re-submit           │ Updated Spec
             │ to Validator        │ to Implementer
             │                     │
             └─────────┐     ┌─────┘
                       │     │
                       ▼     ▼
                  [Iteration Loop]

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
│ GATE 3: QUALITY VERIFIED (MANDATORY PR GATE)                            │
│ ───────────────────────────────────────────────────────────────────     │
│ ✓ All quality standards met                  Owner: Validator           │
│ ✓ No critical issues remaining               Pass: PR Submitted         │
│ ✓ Aligns with specification                                             │
│ ✓ Best practices followed                    ⚠️  Only Validator         │
│                                                  submits PRs!            │
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

## Workflow: Building Individual Agents

### Phase 1: Specification Design (Architect)

**Entry Point**: User describes need for new agent

**Architect Responsibilities**:
1. Ask clarifying questions if requirements are unclear
2. Design comprehensive specification including:
   - Problem statement and scope boundaries
   - Key responsibilities and required inputs/outputs
   - Success criteria and quality metrics
   - Recommended model for the agent (REQUIRED)
   - Frontmatter schema (name, description, model, version, handoffs)
   - Integration points and edge cases
   - Implementation sequence and next steps

**Exit Criteria**:
- [ ] Specification is complete and actionable
- [ ] All required sections present
- [ ] Model recommendation provided with rationale
- [ ] Success criteria are measurable
- [ ] Edge cases documented

**Handoff**: Specification document → Agent Implementer

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

#### 2.5: Submit to Validator
- Notify Agent Validator that implementation is ready
- Provide branch name and link to original specification
- **DO NOT create PR** - Validator does that after approval

**Exit Criteria**:
- [ ] Agent file created on feature branch
- [ ] Follows specification completely
- [ ] Self-review checklist passed
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

### Phase 1: Group Specification Design (Architect)

**Entry Point**: User describes need for multiple coordinated agents

**Architect Responsibilities**:
1. Ask clarifying questions about scope, coordination, and handoff patterns
2. Design group specification including:
   - Group purpose and scope boundaries
   - List of agents in group with individual responsibilities
   - Handoff chain design (which agents coordinate)
   - Model recommendations for each agent
   - Frontmatter schema for all agents
   - Infrastructure file requirements (copilot-instructions.md, README.md)
   - Integration points and workflow diagrams
   - Quality gates for group cohesion

**Exit Criteria**:
- [ ] Group purpose clear and actionable
- [ ] All agents defined with responsibilities
- [ ] Handoff chains documented (which agent hands to which)
- [ ] Model recommendations for each agent
- [ ] Infrastructure file structure defined
- [ ] Group-level quality criteria established
- [ ] Portable structure requirements specified

**Handoff**: Group specification document → Agent Implementer

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

#### 2.7: Submit to Validator
- Notify Agent Validator that group implementation is ready
- Provide branch name and specification reference
- **DO NOT create PR** - Validator does that after approval

**Exit Criteria**:
- [ ] Agent group created on feature branch (not main)
- [ ] All agents implemented with valid frontmatter
- [ ] Infrastructure files complete
- [ ] Handoff chains validated
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
| **[D] Want to merge** | @agent-validator only | Validator submits PR after approval |

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
  │             └─> Validator submits PR
  │                 ↓
  │                 PR merged to main
  │                 ↓
  │                 DONE! Agent goes live
  │
  │
  └─ [D] I WANT TO MERGE MY IMPLEMENTATION
      │
      ⚠️  STOP - Only @agent-validator submits PRs
      │
      Has Agent Validator approved it?
        │
        ├─ NO → Return to [C]
        │       Submit to Validator for review
        │
        └─ YES → Wait for Validator to submit PR
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
3. **Only Validator submits PRs** - Implementer and Architect never merge
4. **Iterate until approved** - Expect feedback loops; quality takes time
5. **Feature branch workflow**: Create branch → Implement → Submit to Validator → Iterate → Validator approves and submits PR

---

### Quick Navigation

- **Need specification?** → Start at [A], consult @agent-architect
- **Have specification?** → Start at [B], consult @agent-implementer  
- **Have implementation?** → Start at [C], consult @agent-validator
- **Want to merge?** → Start at [D], but remember: only Validator submits PRs
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
│   └── agent-3.agent.md
├── copilot-instructions.md       # Group-level workflow and setup (THIS FILE)
├── README.md                      # Usage guide and agent overview
└── CHANGELOG.md                   # Version history (optional, for v1.1.0+)
```

### Agent Frontmatter Schema (Required)
```yaml
---
name: agent-identifier              # Required: kebab-case, matches filename
description: One-line agent purpose # Required: 50-100 characters
model: Claude Sonnet 4.5 (copilot) # Required: From Architect recommendations
version: 1.0.0                      # Optional: Semantic versioning (default 1.0.0)
handoffs:                           # Optional: Agents this one hands off to
  - agent-name-1
  - agent-name-2
---
```

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

- **1.1.0** - Added strict workflow enforcement, quality gates, decision trees, and PR gatekeeper pattern
- **1.0.0** - Initial meta-agent system with Architect, Implementer, Validator
