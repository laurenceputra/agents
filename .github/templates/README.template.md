# Agent Group README Template

Use this template as a starting point for your agent group's README.md file.

---

# [Agent Group Name]

[One-line description of what this agent group does]

## Overview

[Detailed explanation of the agent group's purpose, scope, and value]

### Example

> I need to [problem statement]. This agent group helps by [how the agents solve it].

## Quick Start

### Prerequisites

- GitHub Copilot in VS Code (or integrated into your development environment)
- Python 3.7+ (for validation)
- PyYAML library: `pip install pyyaml`

### Installation

1. **Clone or import** this agent group into your `.github/agents/` directory:
   ```bash
   # Copy the entire folder
   cp -r [agent-group-name] /path/to/repo/.github/agents/
   ```

2. **Validate** the agents are portable:
   ```bash
   python .github/scripts/validate-agents.py .github/agents/[agent-group-name]/
   ```

3. **Integrate** with your workflow (see examples below)

## Agents in This Group

### 1. [Agent Name 1]

**Purpose**: [One-line summary]

**Responsibilities**:
- [Responsibility 1]
- [Responsibility 2]

**Inputs**: [Description of required context/information]

**Outputs**: [Description of what this agent produces]

**Handoffs**: Can delegate to [other agents in group]

[See agents/[agent-name-1].agent.md for full specification]

### 2. [Agent Name 2]

[Same structure as Agent 1]

### 3. [Agent Name 3] (if applicable)

[Same structure]

## Usage Examples

### Workflow 1: [Scenario Name]

**Goal**: [What you're trying to accomplish]

**Steps**:
1. Start with [Agent Name 1]
   - Provide: [Required inputs]
   - Expect: [What the agent returns]

2. Hand off to [Agent Name 2]
   - Agent 1's output feeds into Agent 2
   - Expect: [Refined output]

3. Complete with [Agent Name 3]
   - Finalize: [Final deliverable]

**Example Interaction**:
```
User: "I want to [problem]. Can you help?"

Agent 1 Response:
[Agent 1 provides initial analysis/recommendations]

Agent 2 Response:
[Agent 2 builds on Agent 1's output]

Agent 3 Response:
[Agent 3 provides final output/documentation]
```

### Workflow 2: [Another Scenario]

[Describe another common usage pattern]

## Integration Points

### With Other Agent Groups

This agent group can integrate with:
- **[Other Group Name]**: [How they work together]
- **[Another Group]**: [Specific integration points]

### With External Tools

- **[Tool 1]**: [How this group uses Tool 1]
- **[Tool 2]**: [How this group uses Tool 2]

### With Your Development Workflow

Example integration in VS Code:
1. Open a new file requiring [task type]
2. Invoke [Agent Name 1] via Copilot Chat
3. Provide the required context (from copilot-instructions.md)
4. Let the agent complete the task with integrated [Agent Name 2] if needed

## Agent Coordination

Agents in this group coordinate through **handoff patterns**:

```
[Agent 1] ──context──> [Agent 2] ──refined output──> [Agent 3]
```

**Handoff Protocol**:
- Each agent documents its outputs in a format the next agent can understand
- Context is accumulated and passed downstream
- Errors or constraints discovered by downstream agents feed back upstream

See COORDINATION_PATTERN.txt (if applicable) for detailed handoff specifications.

## Configuration

### Environment Variables

No environment variables required. Agents use the frontmatter model specifications defined in each file.

### Customization

To customize this agent group:

1. **Update agent descriptions** in `copilot-instructions.md`
2. **Adjust model selection** by editing `model:` field in frontmatter (must be approved model)
3. **Add new agents** following the portable format and run `validate-agents.py`
4. **Update CHANGELOG.md** with version and changes

## Validation & Quality

### Running Validation

```bash
# Validate entire group
python .github/scripts/validate-agents.py [agent-group-name]/

# Validate specific agent
python .github/scripts/validate-agents.py agents/[agent-name].agent.md

# Show portable schema reference
python .github/scripts/validate-agents.py --schema
```

### What Gets Validated

✓ Frontmatter compliance (required fields, valid models)
✓ Filename matching (must match `name:` field)
✓ Folder structure (agents/ subdirectory)
✓ Handoff references (no broken chains)
✓ Model identifiers (must be from architect recommendations)

### CI/CD

GitHub Actions workflow (`.github/workflows/validate-agents.yml`) automatically:
- Validates on every push to main
- Validates on pull requests
- Blocks merge if validation fails
- Reports specific errors and warnings

## Updating This Agent Group

### Adding a New Agent

1. **Design** with Agent Architect
2. **Implement** with Agent Implementer
3. **Add to handoffs** of related agents (if applicable)
4. **Run validation**: `python .github/scripts/validate-agents.py [group-name]/`
5. **Update CHANGELOG.md**: Document new agent and increment version
6. **Commit**: `git commit -m "Add [agent-name] to [group-name]"`

### Updating an Existing Agent

1. **Edit** the agent file
2. **Bump version** in frontmatter (e.g., 1.0.0 → 1.1.0)
3. **Update CHANGELOG.md** with changes
4. **Validate**: `python .github/scripts/validate-agents.py agents/[agent-name].agent.md`
5. **Commit**: `git commit -m "Update [agent-name]: [description]"`

### Breaking Changes

For major version updates (1.0.0 → 2.0.0):
1. **Increment major version** in all affected agents
2. **Document in CHANGELOG.md**: "BREAKING CHANGES" section
3. **Provide migration guide**: How to update integrations
4. **Notify users** of the breaking change

Example:
```markdown
## [2.0.0] - 2024-12-11

### BREAKING CHANGES
- Changed input format from CSV to JSON
  - Migration: Update your input preparation scripts
  
### Migration Guide
See MIGRATION_GUIDE.md for step-by-step upgrade instructions.
```

## Performance & Limitations

### Model Assignment

- **[Agent Name 1]**: Claude Sonnet 4.5
  - Strong reasoning for complex analysis
  - ~2-3 second response time
  
- **[Agent Name 2]**: Claude Haiku 4.5
  - Fast, conversational responses
  - ~1 second response time

- **[Agent Name 3]**: [Model]
  - [Reason for model choice]
  - [Typical response time]

### Known Limitations

- [Limitation 1]: [Workaround or mitigation]
- [Limitation 2]: [Context or reasoning]
- [Limitation 3]: [Expected resolution timeline]

### Scaling

For large batches of work:
1. Run agents in sequence (recommended)
2. Provide complete context to minimize back-and-forth
3. Use [Agent Name 1] for initial analysis, then [Agent Name 2] for refinement

## Troubleshooting

### Agent Not Responding

- Check that you're providing all required inputs
- Verify model is available and not rate-limited
- Try reducing context size or breaking into smaller tasks

### Integration Issues

- Run validation: `python .github/scripts/validate-agents.py`
- Check handoff naming in frontmatter
- Verify agents are in correct directory structure

### Unexpected Results

- Provide more specific context/examples to agents
- Check which model is assigned (some are better for specific tasks)
- Review agent's "Examples" section for usage patterns

## Contributing

To contribute improvements:

1. **Test changes** locally with validation script
2. **Update CHANGELOG.md** with your improvements
3. **Submit pull request** with clear description
4. **Include examples** demonstrating the improvement
5. **Verify CI passes** all validation checks

See CONTRIBUTING.md for detailed guidelines.

## License

[Specify license for this agent group, e.g., MIT, Apache 2.0, etc.]

## Support

- **Questions**: See copilot-instructions.md for integration examples
- **Bug Reports**: Open an issue with validation output and error details
- **Feature Requests**: Describe the agent capability you need and use case
- **Maintenance**: Check CHANGELOG.md for version history and updates

---

## Files in This Group

```
[agent-group-name]/
├── agents/
│   ├── [agent-1].agent.md         # Agent definition with examples
│   ├── [agent-2].agent.md
│   └── [agent-3].agent.md
├── copilot-instructions.md        # Setup and integration guidance
├── README.md                       # This file
├── CHANGELOG.md                    # Version history and migration notes
└── [optional: COORDINATION_PATTERN.txt, MIGRATION_GUIDE.md, etc.]
```

### Next Steps

1. **Read** `copilot-instructions.md` for agent group integration guidance
2. **Review** `agents/[agent-name].agent.md` for detailed agent specifications
3. **Check** `CHANGELOG.md` for version history and breaking changes
4. **Run** agents following examples in this README

---

*Last Updated: [Date]*  
*Version: [Version number matching CHANGELOG.md]*
