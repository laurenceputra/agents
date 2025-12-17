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

**Handoffs to**: Agent Implementer (for implementation)

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

**Handoffs to**: PR Manager (when approved), Implementer (for revisions), Architect (for spec issues)

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

**When to use**: Implementation approved by Quality Reviewer and needs critical review before PR

**Responsibilities**:
- Critically reviews agent work before PR submission
- Challenges assumptions and identifies blind spots
- Surfaces disagreements between agents
- Ensures all perspectives are documented for human decision-making
- Final quality gate before PR submission

**Handoffs to**: PR Manager (for PR submission), Implementer (for revisions), Architect (for perspective)

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
│ PR Manager       │ Create PR details, coordinate reviews
└────────┬─────────┘
         │
         ↓
┌──────────────────┐
│ Devil's Advocate │ Critical review, challenge assumptions
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
5. **Handoff**: Specification document → Agent Implementer

#### Phase 2: Implementation (Implementer)
1. Create feature branch: `feature/agent-{name}` or `feature/group-{name}`
2. Implement agent file(s) following specification
3. Follow portable agent group pattern (see COMMON-PATTERNS.md)
4. Self-review against checklist
5. Update CHANGELOG.md and README.md (if applicable)
6. Commit and push to branch
7. **Handoff**: Feature branch → Quality Reviewer

#### Phase 3: Quality Review (Quality Reviewer)
1. Review implementation against specification
2. Check completeness, clarity, examples, best practices
3. **Decision Point**:
   - **Critical Issues**: Provide feedback → Return to Implementer
   - **Spec Issues**: Escalate to Architect for spec revision
   - **Approved**: Handoff to PR Manager

#### Phase 4: PR Coordination (PR Manager)
1. Create PR details file in `.pr_details/{branch-name}.md`
2. Document Quality Reviewer approval
3. **Handoff**: Implementation → Devil's Advocate for critical review

#### Phase 5: Critical Review (Devil's Advocate)
1. Challenge assumptions and identify blind spots
2. Surface disagreements between agents
3. Document all perspectives
4. **Decision Point**:
   - **Revision Needed**: Return to Implementer (Quality Reviewer re-reviews)
   - **Approved**: Hand back to PR Manager with writeup

#### Phase 6: PR Submission (PR Manager)
1. Update PR details file with Devil's Advocate approval
2. Include all disagreements and perspectives in PR description
3. Submit PR with copy-paste ready details
4. Human reviews PR with full context and merges

---

## Quality Gates

### Gate 1: Specification Complete (Architect self-review)
- [ ] Problem statement clear and specific
- [ ] Scope boundaries explicit
- [ ] Model recommendation with rationale
- [ ] Success criteria measurable
- [ ] Frontmatter schema defined (see COMMON-PATTERNS.md)

**Pass**: Specification actionable for Implementer

### Gate 2: Implementation Complete (Implementer self-review)
- [ ] Agent file on feature branch (not main)
- [ ] Frontmatter matches specification
- [ ] All required sections present (see COMMON-PATTERNS.md)
- [ ] Minimum 2 comprehensive examples
- [ ] Quality checklist has 6-10 measurable criteria
- [ ] CHANGELOG.md updated (if version > 1.0.0)

**Pass**: Ready for Quality Reviewer

### Gate 3: Quality Verified (Quality Reviewer)
- [ ] All required sections thorough
- [ ] Instructions clear and actionable
- [ ] Examples comprehensive with input/output
- [ ] Quality checklist measurable
- [ ] Follows GitHub Copilot best practices
- [ ] Aligns with specification
- [ ] No critical issues

**Pass**: Approved, hand to PR Manager

### Gate 4: Critical Review Complete (Devil's Advocate)
- [ ] Assumptions challenged
- [ ] Blind spots identified
- [ ] Disagreements documented
- [ ] All perspectives captured
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
- **Agent File Structure**: 11 required sections in order
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

---

## Best Practices

### From GitHub Copilot Documentation

1. **Be Specific**: Define exact scope, use concrete examples, specify formats
2. **Provide Context**: Explain the "why", define terminology
3. **Structure for Clarity**: Use consistent markdown, clear headings, lists
4. **Include Examples**: Minimum 2 (happy path + edge case), show input/output
5. **Define Success**: Make outcomes measurable, include quality checklists
6. **Optimize for Iteration**: Keep modular, support incremental improvements

Reference: https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results

---

## Tips for Effective Agents

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Composable**: Agents work together through handoffs
3. **Testable**: Include clear success criteria and quality checklists
4. **Maintainable**: Document assumptions and limitations
5. **Evolvable**: Design for change with version history
6. **Portable**: No hardcoded paths, folder-agnostic references

---

## Version History

- **2.0.0** - BREAKING CHANGE: Split Validator into Quality Reviewer + PR Manager. Extracted common patterns to COMMON-PATTERNS.md. Simplified copilot-instructions.md (1542 → 800 lines, 48% reduction). Updated all workflow documentation for five-agent system.
- **1.5.1** - Fixed workflow documentation to clarify PR timing: all reviews complete on branch before PR submission
- **1.5.0** - Added Devil's Advocate agent for critical review and disagreement capture
- **1.4.0** - Updated handoff format to GitHub Copilot object schema
- **1.3.0** - Required specifications in `./.specifications/` directory
- **1.2.0** - Added mandatory CHANGELOG.md and README.md update requirements
- **1.1.0** - Added strict workflow enforcement, quality gates, decision trees
- **1.0.0** - Initial meta-agent system with Architect, Implementer, Validator
