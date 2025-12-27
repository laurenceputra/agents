# Common Patterns for Agent Development

This document contains common patterns, schemas, and guidelines referenced by multiple meta-agents. It's a reference document, not an agent.

⚠️ **CRITICAL**: When changing this file, update the enforcing agents (Quality Reviewer, Architect, Devil's Advocate) to reflect new pattern rules. See copilot-instructions.md for pattern update process.

## Frontmatter Schema

All agents MUST use this standardized YAML frontmatter schema:

```yaml
---
name: agent-identifier                    # Required: kebab-case unique identifier
description: Brief one-line agent purpose # Required: 50-100 characters
model: Claude Sonnet 4.5 (copilot)       # Required: Explicit model name
version: 1.0.0                            # Optional: Semantic versioning (default: 1.0.0)
handoffs:                                 # Optional: List of handoff objects
  - label: "Action description"           # Required: User-facing action (e.g., "Submit to Reviewer")
    agent: "agent-name"                   # Required: Target agent name (kebab-case)
    prompt: "Context for handoff..."      # Required: Instructions for receiving agent
    send: true                            # Optional: Auto-send without confirmation (default: true)
---
```

### Frontmatter Requirements

- **name**: Kebab-case identifier (e.g., `legacy-planning-advisor`). Must match filename (without .agent.md)
- **description**: One-line summary. 50-100 characters recommended
- **model**: Explicit model identifier (e.g., `Claude Sonnet 4.5 (copilot)`)
- **version**: Semantic versioning format (e.g., `1.0.0`). Defaults to `1.0.0`
- **handoffs**: Optional array of handoff objects for agent coordination

## Group Default Handoff Policy

When creating a new **agent group**, the Agent Architect MUST decide and document a **group-level default handoff policy** and include it in the group specification and the group's `copilot-instructions.md` under a `Default Handoff Policy` or `Send Default` section. The policy should state `send_default: true` or `send_default: false` and include a brief rationale.

Suggested assessment criteria (non-exhaustive):
- **Decision criticality**: Final decision points or approvals (e.g., PR submission, funding decisions) should *generally* default to `send: false`.
- **External actions**: Agents that trigger external effects (emails, API calls, PR submission, payments) should default to `send: false` unless strong safeguards are present.
- **Data sensitivity**: High-sensitivity data or privacy-impacting handoffs should favor `send: false`.
- **Observability & rollback**: If robust observability, auditing, and rollback exist, `send: true` may be acceptable for lower-risk flows.
- **User preference & safety**: When in doubt, prefer conservative defaults (`send: false`) and document the decision.

Additional Requirements for `send_default: true` decisions
- **Testing plan**: If the Architect chooses `send_default: true`, include a brief testing plan describing how the behavior will be validated (test cases, staging validation, or pilot rollout).
- **Migration note**: Describe how existing users will be informed and what changes they might expect; include a short rollback/mitigation plan.
- **Observability metrics**: List key metrics or logs to monitor after rollout (e.g., error rate, number of auto-handoffs, user-initiated rollbacks).

Example snippet to add to `copilot-instructions.md` for a new group:

```yaml
# Default Handoff Policy
send_default: false  # Chosen because this group's workflows include final decision points and external actions; requires manual confirmation
```

Architects should justify their choice in the specification (brief rationale and any mitigations such as observability, testing or rollback plans).
## Agent File Structure

All agent files follow this section order:

1. **Purpose**: What the agent does and why
2. **Recommended Model**: Model choice with rationale
3. **Responsibilities**: Specific, actionable duties
4. **Domain Context**: Key concepts and terminology
5. **Input Requirements**: Required inputs with formats
6. **Output Format**: Template or structure for outputs
7. **Response Format**: Step-by-step response structure
8. **Examples**: Minimum 2, ideally 3 comprehensive examples
9. **Quality Checklist**: 6-10 measurable criteria
10. **Integration Points**: Upstream/downstream dependencies

**Version History Prohibition**: Agent files MUST NOT contain version history sections. All version tracking is managed in CHANGELOG.md only.

**Character Limit**: Agent files MUST NOT exceed 30,000 characters (GitHub Copilot hard limit). Target 15,000-20,000 characters. Flag for review if exceeding 25,000 characters.

## Size Management Guidelines

GitHub Copilot enforces a 30,000 character limit on agent files. Follow these guidelines to stay within limits:

### Character Count Targets
- **Target Range**: 15,000-20,000 characters (comfortable headroom)
- **Yellow Flag**: 25,000-30,000 characters (review for optimization)
- **Hard Limit**: 30,000 characters (agent will fail to load)

### Validation Requirements
- Agent Implementer MUST check character count before completion
- Quality Reviewer MUST verify character count during review
- Any agent exceeding 30,000 characters MUST be rejected with critical feedback

### Optimization Strategies

**If approaching 25,000 characters:**
1. **Reduce example verbosity**: Use concise examples, remove redundant scenarios
2. **Consolidate sections**: Merge overlapping content, eliminate repetition
3. **Extract to README**: Move usage guides, tutorials, and extended examples to README.md
4. **Simplify quality checklists**: Keep 6-10 focused criteria, avoid redundancy

**If exceeding 30,000 characters:**
1. **Agent split**: Redesign as multiple coordinated agents with clear handoffs
2. **Reference external docs**: Link to README or external documentation for detailed guidance
3. **Prioritize core functionality**: Keep only essential instructions in agent file

### Version History Prohibition
Agent files MUST NOT contain "Version History" sections. This is the single most impactful size reduction strategy:
- Version history accumulates over time without improving current functionality
- All version tracking belongs in CHANGELOG.md (single source of truth)
- Removing version history can reclaim thousands of characters
- Agents focus on current behavior only

### Checking Character Count
```bash
wc -c path/to/agent.agent.md
```

## Writing Style Guidelines

Agents should produce natural, human-like output following these principles:

1. **Varied sentence structure**: Mix short and long sentences. Don't start every sentence the same way.

2. **Be direct**: Say what you mean. Use "X needs fixing" not "it may potentially be beneficial to consider addressing X."

3. **Skip unnecessary qualifiers**: Avoid "potentially", "might", "could", "possibly" unless there's real uncertainty.

4. **Use active voice**: "I reviewed the code" not "the code was reviewed."

5. **Contractions are fine**: Use "don't", "isn't", "you'll" in appropriate contexts.

6. **Natural transitions**: Not every list needs "First", "Second", "Third". Use "Here's what I found", "Another issue", "Also worth noting".

7. **Mix formats**: Don't make everything a bullet list. Use paragraphs where they flow better.

8. **Sound human**: Write like you're explaining to a colleague, not documenting for compliance.

9. **Avoid AI-typical punctuation**: No em-dashes (use hyphens instead). Limit semicolons and colons (use periods and commas primarily).

## Model Recommendations

When selecting models for new agents:

- **Analytical/Reasoning-heavy agents** (planning, validation, analysis): *Claude Sonnet 4.5 (copilot)*
- **Creative or empathetic writing** (letters, UX copy): *Claude Haiku 4.5 (copilot)*
- **Code generation or technical docs**: *Claude Haiku 4.5 (copilot)*
- **Large-scale log analysis and QA**: *Gemini 3 Pro (Preview)*
- **Lightweight assistants**: *Raptor mini (Preview)*

## Portable Folder Structure

Agent groups use this portable structure:

```
agent-group-name/
├── AGENTGROUPNAME                  # Contains the agent group name (required)
├── agents/
│   ├── agent-1.agent.md
│   ├── agent-2.agent.md
│   └── devils-advocate.agent.md  # MANDATORY for all groups
├── copilot-instructions.md       # Group-level workflow
├── README.md                      # Usage guide
├── CHANGELOG.md                   # Version history (for v1.1.0+)
└── update-from-upstream.sh        # Self-updating script
```

### Portability Requirements

- No hardcoded paths or absolute references
- Agents reference each other by name, not path
- No references to parent folders or repo-specific names
- Folder can be renamed without breaking
- `AGENTGROUPNAME` file must contain the exact agent group name (e.g., "recommendation-letter")

## Versioning Strategy

### Repository-Wide Coordination

Agent groups in this repository follow **coordinated versioning** for major and minor versions:

- **Coordinated releases**: When one group receives a major or minor version bump, other groups may be reviewed and updated together
- **Independent patches**: Individual agents or groups can receive patch versions independently for bug fixes or clarifications
- **Synchronized major versions**: Repository-wide major version bumps (e.g., 1.x.x → 2.x.x) indicate significant breaking changes across multiple groups

### Version Synchronization Within Groups

Per the hybrid versioning strategy:

- **Major.Minor synchronized**: All agents in a group share the same Major.Minor version (e.g., all at 1.3.x)
- **Patch versions can vary**: Individual agents may have different patch versions (e.g., one agent at 1.3.1, another at 1.3.2)
- **Breaking changes**: Require Major bump for entire group
- **New features**: Require Minor bump for entire group
- **Bug fixes/clarifications**: Can be Patch bumps for individual agents

### Version Bump Guidelines

**MAJOR (X.0.0)**: Breaking changes requiring user adaptation
- Workflow redesign, agent splits/merges, removed functionality
- Example: Splitting validator agent into separate agents

**MINOR (1.Y.0)**: New features, backward-compatible changes
- New agents added, new quality gates, workflow enhancements
- Example: Adding devils-advocate to existing group

**PATCH (1.1.Z)**: Bug fixes, clarifications, documentation updates
- Typo fixes, example improvements, minor clarifications
- Example: Fixing calculation error in quality checklist

### When Versions Diverge

If an agent group shows version inconsistency (e.g., some agents at 1.3.0, others at 1.3.1), this typically indicates:

1. **Unintentional drift**: Agents missed during a synchronized update → Fix by syncing versions
2. **Selective patches**: Only some agents needed bug fixes → Document in CHANGELOG why versions differ
3. **Quality issue**: Violation of versioning strategy → Report and correct

## Changelog Format

All version bumps require CHANGELOG.md entry:

```markdown
## X.Y.Z - YYYY-MM-DD

### Added
- New feature or capability

### Changed
- Modified behavior or updated component

### Fixed
- Bug fix or correction

### Deprecated
- Feature marked for removal

### Removed
- Deleted feature or component

### Security
- Security fix or vulnerability resolution
```

**Guidelines**:
- Include specific component names
- Provide context (why changed)
- Add migration guidance for breaking changes
- Be specific, not vague ("updated code-reviewer agent" not "updated agent")

## Version History

- **1.0.0** - Initial common patterns reference document extracted from meta-agent files
