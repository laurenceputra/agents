# Common Patterns for Agent Development

This document contains common patterns, schemas, and guidelines referenced by multiple meta-agents. It's a reference document, not an agent.

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
11. **Version History**: Chronological change log

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
├── agents/
│   ├── agent-1.agent.md
│   ├── agent-2.agent.md
│   └── devils-advocate.agent.md  # MANDATORY for all groups
├── copilot-instructions.md       # Group-level workflow
├── README.md                      # Usage guide
└── CHANGELOG.md                   # Version history (for v1.1.0+)
```

### Portability Requirements

- No hardcoded paths or absolute references
- Agents reference each other by name, not path
- No references to parent folders or repo-specific names
- Folder can be renamed without breaking

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
