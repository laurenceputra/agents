# GitHub Copilot Instructions - Meta-Agent System

## Overview

This is a meta-agent system for building high-quality, reusable agents. The system enforces strict separation of concerns through five specialized agents working in a defined workflow with quality gates.

**This meta-agent group follows the same portable agent structure it enforces for other agent groups.**

## Core Principle

**Strict separation of concerns with enforced workflow gates ensures quality agent implementations.**

Each meta-agent has a single, well-defined responsibility:
- **Agent Architect**: Designs specifications (planning only, no implementation)
- **Agent Implementer**: Implements specifications on feature branches (implementation only, no design decisions)
- **Quality Reviewer**: Reviews implementations for quality and completeness (review only, no PR management)
- **PR Manager**: Manages PR submission process (PR logistics only, no quality review)
- **Devil's Advocate**: Critically reviews all work, surfaces disagreements, challenges assumptions (pre-PR quality gate)

## Default Handoff Policy

**send_default: true**

All handoffs in the meta-agent group default to `send: true` (auto-send without user confirmation).

### Rationale

The meta-agent workflow includes multiple quality gates (Devil's Advocate critical review, PR approval) that provide sufficient oversight without requiring manual confirmation at each handoff:
- Workflow iterations are frequent and require rapid feedback loops for agent development
- Devil's Advocate serves as a critical quality gate before PR submission, catching issues missed in earlier reviews
- PR approval provides final human oversight with full context of all agent reviews
- All agents operate within version-controlled branches with full audit trails
- Manual handoff confirmation at each transition would create checkpoint fatigue without adding meaningful safety

This approach allows velocity while maintaining quality standards through concentrated oversight at critical decision points.

## The Five Meta-Agents

### Agent Architect (`agents/architect.agent.md`)
**Role**: Design specifications for new agents  
**Model**: Claude Sonnet 4.5 (copilot)

**When to use**: Need a new agent but don't have a clear specification

**Responsibilities**:
- Analyzes requirements and translates into agent specifications
- Defines scope, boundaries, inputs/outputs, success criteria
- Recommends appropriate model for each agent
- Designs frontmatter schema and handoff chains
- Documents edge cases and integration points
- Submits specifications to Devil's Advocate for Phase 1.5 review
- Handles Devil's Advocate approval and manually invokes Implementer

**Handoffs to**: Devil's Advocate (for specification review), Agent Implementer (after DA approval)

---

### Agent Implementer (`agents/implementer.agent.md`)
**Role**: Implement agent definitions from specifications  
**Model**: Claude Haiku 4.5 (copilot)

**When to use**: Have a complete specification and need to create the agent definition file

**Responsibilities**:
- Creates agent definition markdown files from specifications
- Works in feature branches (never directly on main)
- Follows GitHub Copilot best practices
- Creates comprehensive examples and quality checklists
- Iterates based on Quality Reviewer feedback

**Handoffs to**: Quality Reviewer (for review)

---

### Quality Reviewer (`agents/quality-reviewer.agent.md`)
**Role**: Review implementations for quality and completeness  
**Model**: Claude Sonnet 4.5 (copilot)

**When to use**: Have an implementation that needs quality review

**Responsibilities**:
- Reviews agent implementations against specifications and best practices
- Provides structured feedback with severity levels (Critical/Recommendation/Enhancement)
- Iterates with Implementer until approval criteria met
- Escalates specification issues back to Architect
- Approves implementations when quality standards are met

**Handoffs to**: Devil's Advocate (when approved), Implementer (for revisions), Architect (for spec issues)

---

### PR Manager (`agents/pr-manager.agent.md`)
**Role**: Manage PR submission process  
**Model**: Claude Haiku 4.5 (copilot)

**When to use**: Quality review is approved and need to coordinate final steps for PR

**Responsibilities**:
- Creates and maintains PR details files in `.pr_details/` directory
- Tracks review status through the workflow
- Coordinates with Devil's Advocate for critical review
- Updates PR details files with review history
- Submits PRs when all approvals (Quality Reviewer + Devil's Advocate) are complete

**Handoffs to**: Devil's Advocate (for critical review), Quality Reviewer (if more review needed)

---

### Devil's Advocate (`agents/devils-advocate.agent.md`)
**Role**: Critical review and disagreement facilitation  
**Model**: Claude Sonnet 4.5 (copilot)

**When to use**: 
- Phase 1.5: After Architect creates specification (pre-implementation review)
- Phase 3.5: After Quality Reviewer approves implementation (pre-PR review)

**Responsibilities**:
- Critically reviews specifications (Phase 1.5) and implementations (Phase 3.5)
- Challenges assumptions and identifies blind spots
- Surfaces disagreements between agents
- Ensures all perspectives are documented for human decision-making
- Quality gates at both specification and implementation stages

**Handoffs to**: Architect (with approval status or revision feedback), PR Manager (for PR submission), Implementer (for revisions)

---

## Workflow

### Quick Reference Decision Tree

| Your Situation | Agent to Consult | What They'll Do |
|---|---|---|
| **Need agent, no spec** | @agent-architect | Design specification |
| **Have spec to implement** | @agent-implementer | Create agent on branch |
| **Have implementation to review** | @quality-reviewer | Review and provide feedback or approve |
| **Have approved implementation** | @pr-manager | Coordinate with Devil's Advocate and PR submission |
| **Need critical review** | @devils-advocate | Challenge assumptions, document disagreements |

### Complete Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                        AGENT DEVELOPMENT WORKFLOW                     │
└──────────────────────────────────────────────────────────────────────┘

User Need
   ↓
┌──────────────────┐
│ Agent Architect  │ Design specification
└────────┬─────────┘
         │ Specification (.specifications/ directory)
         ↓
┌──────────────────┐
│ Devil's Advocate │ Critical review of specification (Phase 1.5)
└────┬────┬────────┘
     │    │
     │    └─→ Issues found? Return to Architect (iterate)
     │
     │ Approved - Return to Architect
     ↓
┌──────────────────┐
│ Agent Architect  │ Hand to Implementer (using designated handoff)
└────────┬─────────┘
         │
         ↓
┌──────────────────┐
│ Agent Implementer│ Create agent on feature branch
└────────┬─────────┘
         │ Implementation on branch
         ↓
┌──────────────────┐
│ Quality Reviewer │ Review quality & completeness
└────┬────┬────────┘
     │    │
     │    └─→ Issues found? Return to Implementer (iterate)
     │
     │ Approved
     ↓
┌──────────────────┐
│ Devil's Advocate │ Critical review of work package (Phase 3.5)
└────┬────┬────────┘
     │    │
     │    └─→ Issues found? Return to Implementer (Quality Reviewer re-reviews)
     │
     │ Approved
     ↓
┌──────────────────┐
│ PR Manager       │ Submit PR with all approvals documented
└────────┬─────────┘
         │
         ↓
    Main Branch
```

### Workflow Steps

#### Phase 1: Specification (Architect)
1. User describes need for new agent
2. Architect asks clarifying questions
3. Architect creates specification in `.specifications/` directory
4. Specification includes: scope, responsibilities, model recommendation, success criteria
5. **Handoff**: Specification document → Devil's Advocate for critical review

#### Phase 1.5: Specification Critical Review (Devil's Advocate)
1. Challenge specification assumptions and design decisions
2. Identify blind spots in scope, requirements, or agent boundaries
3. Question model recommendations and success criteria
4. Surface potential issues before implementation begins
5. **Decision Point**:
   - **Critical Issues**: Provide feedback → Return to Architect
   - **Approved**: Return to Architect with approval signal, Architect uses designated handoff to Implementer

#### Phase 2: Implementation (Implementer)
1. Create feature branch: `feature/agent-{name}` or `feature/group-{name}`
2. Implement agent file(s) following specification
3. Follow portable agent group pattern (see COMMON-PATTERNS.md)
4. Self-review against checklist
5. Update CHANGELOG.md and README.md (if applicable)
6. Commit and push to branch
7. **Handoff**: Feature branch → Quality Reviewer for review

#### Phase 3: Quality Review (Quality Reviewer)
1. Review implementation against specification
2. Check completeness, clarity, examples, best practices
3. **Decision Point**:
   - **Critical Issues**: Provide feedback → Return to Implementer
   - **Spec Issues**: Escalate to Architect for spec revision
   - **Approved**: Handoff to Devil's Advocate with complete work package

#### Phase 3.5: Work Package Critical Review (Devil's Advocate)
1. Review complete work package: implementation + quality review assessment
2. Challenge assumptions from both Implementer and Quality Reviewer
3. Identify blind spots not caught by either agent
4. Surface disagreements between agents' perspectives
5. Document all perspectives and trade-offs
6. **Decision Point**:
   - **Revision Needed**: Return to Implementer (Quality Reviewer re-reviews)
   - **Approved**: Hand to PR Manager with comprehensive writeup

#### Phase 4: PR Submission (PR Manager)
1. Create PR details file in `.pr_details/{branch-name}.md`
2. Document all approvals (Quality Reviewer + Devil's Advocate)
3. Include Devil's Advocate writeup with disagreements documented
4. Submit PR with all context for human review
5. Human reviews PR with full context and merges

---

## Quality Gates

### Gate 1: Specification Complete (Architect self-review)
- [ ] Problem statement clear and specific
- [ ] Scope boundaries explicit
- [ ] Model recommendation with rationale
- [ ] Success criteria measurable
- [ ] Frontmatter schema defined (see COMMON-PATTERNS.md)
- [ ] Specification is concise (target 15,000-20,000 characters for resulting agent)
- [ ] No version history section in agent file structure template
- [ ] If complex, multi-agent split or extraction strategy noted

**Pass**: Specification actionable for Implementer and targets appropriate size

### Gate 1.5: Specification Critical Review (Devil's Advocate)
- [ ] Specification assumptions challenged
- [ ] Scope boundaries questioned for completeness
- [ ] Model recommendation rationale verified
- [ ] Success criteria evaluated for measurability
- [ ] Blind spots in requirements identified
- [ ] Design decisions questioned for appropriateness
- [ ] Edge cases and integration points validated
- [ ] All perspectives documented

**Pass**: Specification ready for implementation with critical review complete

### Gate 2: Implementation Complete (Implementer self-review)
- [ ] Agent file on feature branch (not main)
- [ ] Frontmatter matches specification
- [ ] All required sections present (10 sections, NOT including Version History)
- [ ] Minimum 2 comprehensive examples
- [ ] Quality checklist has 6-10 measurable criteria
- [ ] CHANGELOG.md updated (if version > 1.0.0)
- [ ] Agent file does NOT contain "Version History" section
- [ ] Character count under 30,000 (ideally under 25,000)
- [ ] Character count reported to Quality Reviewer
- [ ] If over 25,000 characters, optimization attempted or justification provided

**Pass**: Ready for Quality Reviewer with size compliance

### Gate 3: Quality Verified (Quality Reviewer)
- [ ] All required sections thorough
- [ ] Instructions clear and actionable
- [ ] Examples comprehensive with input/output
- [ ] Quality checklist measurable
- [ ] Follows GitHub Copilot best practices
- [ ] Aligns with specification
- [ ] No critical issues
- [ ] Agent file does NOT contain "Version History" section (CRITICAL)
- [ ] Character count under 30,000 characters (CRITICAL)
- [ ] If 25,000-30,000 characters, optimization recommendations provided
- [ ] Character count validation documented in review

**Pass**: Approved, hand to Devil's Advocate for critical review

**Critical Failures**:
- Version history section present → Return to Implementer
- Character count exceeds 30,000 → Return to Implementer (may require Architect for redesign)

### Gate 3.5: Work Package Critical Review Complete (Devil's Advocate)
- [ ] Assumptions challenged across both Implementer and Quality Reviewer work
- [ ] Blind spots identified in implementation and quality assessment
- [ ] Disagreements documented with full reasoning
- [ ] All perspectives captured from Implementer and Quality Reviewer
- [ ] Trade-offs clearly articulated
- [ ] Ready for human decision

**Pass**: Approved for PR submission

---

## Portable Agent Group Pattern

See `COMMON-PATTERNS.md` for complete details.

### Required Structure
```
agent-group-name/
├── agents/
│   ├── agent-1.agent.md
│   ├── agent-2.agent.md
│   └── devils-advocate.agent.md  # MANDATORY for all groups
├── copilot-instructions.md
├── README.md
└── CHANGELOG.md
```

### Key Requirements
- All agents in `agents/` subdirectory
- Frontmatter follows standard schema (see COMMON-PATTERNS.md)
- No hardcoded paths (portable, folder-agnostic)
- Valid handoff chains (no broken references)
- Devil's Advocate included in all agent groups

---

## Common Patterns Reference

For detailed information on these topics, see `agents/COMMON-PATTERNS.md`:

- **Frontmatter Schema**: YAML schema all agents must use
- **Agent File Structure**: 10 required sections in order
- **Writing Style Guidelines**: 9 principles for natural, human-like output
- **Model Recommendations**: Which model for which task type
- **Portable Folder Structure**: Standard directory layout
- **Changelog Format**: Versioning and change documentation

---

## Workflow Rules (Critical)

1. **All implementations on feature branches** - Never commit directly to main
2. **Branch naming**:
   - Individual agent: `feature/agent-{name}`
   - Agent group: `feature/group-{name}`
   - Refactoring: `feature/refactor-{description}`
3. **Only PR Manager submits PRs** - After all approvals complete
4. **Iterate until approved** - Expect feedback loops; quality takes time
5. **Devil's Advocate is mandatory** - All implementations require critical review
6. **Reviews happen on branch** - All reviews complete before PR submission
7. **Quality Reviewer does not manage PRs** - Separate responsibilities

---

## Size and Versioning Constraints

### Character Limit Enforcement

GitHub Copilot has a hard 30,000 character limit for agent files. The meta-agent system enforces this:

**During Specification (Architect)**:
- Design concise specifications (target 15,000-20,000 characters)
- Flag specifications approaching 25,000 characters for review
- Recommend agent splits for overly complex specifications

**During Implementation (Implementer)**:
- Validate character count before marking complete
- Alert if agent exceeds 25,000 characters (yellow flag)
- Critical alert if agent exceeds 30,000 characters (red flag)
- Provide optimization recommendations

**During Review (Quality Reviewer)**:
- Verify character count is under 30,000 (critical requirement)
- Flag for optimization if exceeding 25,000 characters
- Reject with critical feedback if over 30,000 characters

**Checking Character Count**:
```bash
wc -c path/to/agent.agent.md
```

### No Version History in Agent Files

**Rule**: Agent files MUST NOT contain "Version History" sections.

**Rationale**:
- Version history accumulates over time, bloating file size
- Duplicates information already in CHANGELOG.md
- Makes agents harder to read and maintain
- Contributes to approaching the 30k character limit

**Enforcement**:
- Architect: Do not include version history sections in specifications
- Implementer: Do not create version history sections in agent files
- Quality Reviewer: Reject implementations with version history sections

**Version Tracking**: All version history is managed in CHANGELOG.md only. This provides:
- Single source of truth for changes
- Proper semantic versioning
- Migration guidance for breaking changes
- Historical context separate from current functionality

**Exception**: COMMON-PATTERNS.md is a reference document (not an agent) and may contain a version history section for tracking the patterns themselves.

---

## Troubleshooting

### "I need a new agent but don't know what to specify"
**Solution**: Consult @agent-architect. Describe your problem, and Architect will design a specification.

### "My implementation was rejected by Quality Reviewer"
**Solution**: Review the feedback report carefully. Address critical issues first, then recommendations. Make changes on the same branch, commit, and notify Quality Reviewer for re-review.

### "Quality Reviewer and Devil's Advocate disagree"
**Expected**: Disagreements are captured in the PR for human decision. Both perspectives are documented with reasoning.

### "Who submits the PR?"
**Answer**: PR Manager submits PRs after both Quality Reviewer and Devil's Advocate approve. No one else merges agent implementations.

### "Can I skip Devil's Advocate review?"
**No**: Devil's Advocate is a mandatory quality gate. All implementations require critical review before PR submission.

### "Specification has gaps during implementation"
**Solution**: Quality Reviewer escalates to Architect for specification revision. Architect updates spec, then Implementer updates implementation.

---

## Versioning Strategy

**Hybrid Approach: Synchronized Major/Minor, Independent Patches**

- **Major.Minor versions synchronized** across all agents in the group
  - Breaking changes or significant features trigger group-wide bumps
  - Example: Workflow changes affect all agents → bump 1.0.0 → 1.1.0 for all

- **Patch versions can be independent** for individual agents
  - Bug fixes, documentation updates, minor clarifications
  - Example: architect.agent.md can be 1.1.1 while others remain 1.1.0

### Version Bumping
- **MAJOR (2.0.0)**: Breaking changes (validator split, workflow redesign)
- **MINOR (1.1.0)**: New features, new quality gates, infrastructure updates
- **PATCH (1.1.1)**: Bug fixes, typos, documentation clarifications

See `COMMON-PATTERNS.md` for changelog format requirements.


