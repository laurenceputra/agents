# Agent Portability Guide

This guide explains how to use the portable agent system to create, validate, and migrate agent groups across repositories.

## Overview

Agent groups in this system are designed to be **fully portable** — you can move any agent group folder to another GitHub repository, rename it to `.github/agents`, and it will work without any modifications.

This is achieved through:
- **Standardized folder structure** (`agent-group-name/agents/*.agent.md`)
- **Validated YAML frontmatter schema** (name, description, model, version, handoffs)
- **Relative path references** (no hardcoded repository or organization names)
- **Automated validation** (Python linter + GitHub Actions CI)

## Creating a New Portable Agent Group

### 1. Design the Agent Specification

Use the **Agent Architect** to define your agent(s). The specification should include:
- Problem statement and scope
- Responsibilities and success criteria
- Input/output formats
- Integration points with other agents (if applicable)

Example:
```
I need an agent that reviews pull requests for security vulnerabilities.
```

### 2. Implement the Agent(s)

Use the **Agent Implementer** to create agent definitions. The implementer will:
- Generate standardized YAML frontmatter
- Create example scenarios and quality checklists
- Ensure portable folder structure
- Validate handoff references

### 3. Follow the Portable Format

Your agent group must follow this exact structure:

```
agent-group-name/
├── agents/
│   ├── agent-1.agent.md          # Required: Agent definition with frontmatter
│   ├── agent-2.agent.md
│   └── agent-3.agent.md
├── copilot-instructions.md       # Required: Group setup and integration guide
├── README.md                      # Required: Usage guide
└── CHANGELOG.md                   # Recommended: Version history
```

### 4. Validate Before Committing

Let the `validator` agent validate that theagents are created correctly

## Portable Frontmatter Schema

Every agent **must** include YAML frontmatter at the top of its file:

```yaml
---
name: agent-identifier                         # Required: kebab-case, matches filename
description: Brief one-line summary            # Required: 50-100 characters
model: Claude Sonnet 4.5 (copilot)            # Required: Explicit model from architect
version: 1.0.0                                 # Optional: Semantic versioning (defaults to 1.0.0)
handoffs:                                      # Optional: Agent names for coordination
  - agent-name-1
  - agent-name-2
---
```

### Field Reference

| Field | Required | Format | Notes |
|-------|----------|--------|-------|
| name | Yes | kebab-case string | Must match filename without `.agent.md` |
| description | Yes | String 50-100 chars | One-line summary of purpose |
| model | Yes | Model identifier | Must match architect's recommendations |
| version | No | Semantic (e.g., 1.0.0) | Defaults to 1.0.0 |
| handoffs | No | Array of agent names | Agents this can delegate to |

### Valid Models

These are the approved models for all agents (from `architect.agent.md`):

- `Claude Sonnet 4.5 (copilot)` — Analytical/reasoning-heavy tasks
- `Claude Haiku 4.5 (copilot)` — Creative/empathetic writing
- `Gemini 3 Pro (Preview)` — Log analysis and QA
- `Raptor mini (Preview)` — Lightweight assistants

## Migrating Agent Groups to Other Repositories

### Step 1: Validate in Source Repository

Before moving, ensure the agent group passes all validation checks:

```bash
python .github/scripts/validate-agents.py agent-group-name/
```

Fix any errors or warnings in the agent files.

### Step 2: Export the Agent Group

Copy the entire agent group folder:

```bash
# In source repository
cp -r agent-group-name /tmp/export/
```

### Step 3: Import into Target Repository

Move the folder to the `.github/agents` directory in the target repository:

```bash
# In target repository
mkdir -p .github/agents
cp -r /tmp/export/agent-group-name .github/agents/
```

The folder name can be anything; it will be discovered automatically.

### Step 4: Validate in Target Repository

Run the validator to confirm the agents work in the new location:

```bash
python .github/scripts/validate-agents.py .github/agents/agent-group-name/
```

### Step 5: Integrate with Target Repository

Update the target repository's `copilot-instructions.md` to include the migrated agents:

```markdown
## Available Agent Groups

- **Legacy Planning** (`.github/agents/legacy-planning/`)
  - Comprehensive estate planning and wealth transfer agents
  - Includes trust design, beneficiary planning, and wishes documentation
```

## Example: Migrating Legacy Planning Agents

Here's a complete migration example:

### Source Repository Setup

```
/home/laurence/code/agents/
├── legacy-planning/
│   ├── agents/
│   │   ├── legacy-planning-advisor.agent.md
│   │   ├── trust-structure-designer.agent.md
│   │   ├── beneficiary-planning-agent.agent.md
│   │   └── letter-of-wishes-composer.agent.md
│   ├── copilot-instructions.md
│   └── README.md
```

### Migration Commands

```bash
# 1. Validate in source
cd /home/laurence/code/agents
python .github/scripts/validate-agents.py legacy-planning/

# 2. Export
cp -r legacy-planning /tmp/export/

# 3. Clone target repository
cd ~/my-new-project
git clone https://github.com/myorg/myproject.git
cd myproject

# 4. Import agents
mkdir -p .github/agents
cp -r /tmp/export/legacy-planning .github/agents/

# 5. Validate in target
python .github/scripts/validate-agents.py .github/agents/legacy-planning/

# 6. Commit and push
git add .github/agents/legacy-planning/
git commit -m "Add legacy planning agents from upstream"
git push origin main
```

### Target Repository Structure After Migration

```
~/my-new-project/
├── .github/
│   ├── agents/
│   │   └── legacy-planning/
│   │       ├── agents/
│   │       │   ├── legacy-planning-advisor.agent.md
│   │       │   ├── trust-structure-designer.agent.md
│   │       │   ├── beneficiary-planning-agent.agent.md
│   │       │   └── letter-of-wishes-composer.agent.md
│   │       ├── copilot-instructions.md
│   │       └── README.md
│   └── scripts/
│       └── validate-agents.py
├── src/
└── README.md
```

## Updating Agent Groups

### Pulling Updates from Upstream Repository

Each agent group includes a self-updating script (`update-from-upstream.sh`) that downloads the latest updates from the upstream repository (`https://github.com/laurenceputra/agents`).

**To update an agent group:**

```bash
cd path/to/agent-group-name
./update-from-upstream.sh
```

The script will:
1. Read the agent group name from the `AGENTGROUPNAME` file
2. Download the file list from the upstream repository using GitHub API
3. Download and compare each file from upstream
4. Selectively update files for this agent group only (including the update script itself)
5. Show a summary of new, updated, and unchanged files

**After running the script:**
- Review the changes with your version control system (if using git: `git status` and `git diff`)
- If satisfied, commit the updates: `git add . && git commit -m "Update agent-group-name from upstream"`

**Requirements:**
- `curl` must be installed
- Internet access to GitHub

**Note:** The script downloads files directly from GitHub without requiring git operations or adding remotes. This makes it suitable for projects that have copied agent groups to any location, whether or not they use version control.

### Adding a New Agent to a Group

1. **Design** the new agent using Agent Architect
2. **Implement** it using Agent Implementer
3. **Add handoff references** to existing agents (if applicable)
4. **Update CHANGELOG.md** with version bump and change notes
5. **Validate** all agents in the group
6. **Commit** with message: "Add {agent-name} to {group-name}"

### Updating an Existing Agent

1. **Modify** the agent definition (agents/agent-name.agent.md)
2. **Update** the `version` field in frontmatter (e.g., 1.0.0 → 1.1.0)
3. **Update CHANGELOG.md** with change summary
4. **Validate** the agent: `python .github/scripts/validate-agents.py agents/agent-name.agent.md`
5. **Commit** with message: "Update {agent-name}: {change description}"

### Breaking Changes (Major Version Bump)

If you make breaking changes to an agent's input/output format or behavior:

1. **Update** the `version` to next major (e.g., 1.0.0 → 2.0.0)
2. **Document** the breaking changes in CHANGELOG.md
3. **Add migration notes** for users upgrading from previous versions
4. **Notify** downstream repositories using this agent group

Example CHANGELOG entry:

```markdown
## [2.0.0] - 2024-12-11

### BREAKING CHANGES
- Changed `output_format` from "structured" to "markdown_only"
  - Migration: Update consuming agents to parse markdown instead of JSON

### Added
- New `verbosity` input parameter (high, medium, low)
- Better error messages with actionable remediation

### Fixed
- Handoff to `beneficiary-planning-agent` now includes all context
```

## Validation CI/CD Integration

The repository includes a GitHub Actions workflow (`.github/workflows/validate-agents.yml`) that:

- ✓ Runs on every push to `main` (agent files only)
- ✓ Runs on pull requests to `main` (agent files only)
- ✓ Validates all agents in the repository
- ✓ Checks specific changed files in PRs
- ✓ Displays portable schema reference

### Workflow Output

The validation workflow will:
1. Install Python 3.10 and PyYAML dependency
2. Run the validator script against all agents
3. Report errors (blocking), warnings (informational), and successes
4. Display portable schema reference
5. Pass (all agents valid) or fail (fixable errors found)

Example GitHub Actions output:

```
Validating 4 agent group(s)...

Group: legacy-planning
  ✓ legacy-planning-advisor.agent.md
  ✓ trust-structure-designer.agent.md
  ✓ beneficiary-planning-agent.agent.md
  ✓ letter-of-wishes-composer.agent.md

============================================================
Validation Summary
============================================================
Agent Groups:  1
Agents Checked: 4
Agents Valid:   4
Errors:        0
Warnings:      0
============================================================

PASSED: All agents are portable and valid
```

## Troubleshooting

### Validation Failures

**Error: "Missing required field: name"**
- Add `name: agent-identifier` to the frontmatter (must be kebab-case)

**Error: "Name 'my-agent' does not match filename 'my_agent'**
- Rename the file to match the name field, or update the name field
- Both must be kebab-case and identical

**Error: "Invalid model 'GPT-4'**
- Use one of the approved models: Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 3 Pro, Raptor mini
- See `python .github/scripts/validate-agents.py --schema` for full list

**Error: "Agent file must be in 'agents/' subdirectory"**
- Move the agent file to `agent-group-name/agents/{name}.agent.md`
- Ensure folder structure matches portable format

**Error: "Invalid handoff 'unknown-agent': agent not found in group"**
- Check the handoff name matches an existing agent in the group
- Verify the referenced agent file exists

### Migration Issues

**"Agents work in source but not in target repository"**
1. Run `python .github/scripts/validate-agents.py` in target repo
2. Check for path-dependent references (hardcoded repo names, etc.)
3. Verify all handoff references are valid in target environment

**"Different agents available after migration"**
- Ensure the entire agent group folder was copied (agents/, copilot-instructions.md, README.md)
- Verify no files were accidentally deleted during migration

## Best Practices

1. **Always validate** before committing agent changes
   ```bash
   python .github/scripts/validate-agents.py agent-group-name/
   ```

2. **Keep agents in groups** — even single agents should be in a folder
   ```
   my-agent/
   ├── agents/
   │   └── my-agent.agent.md
   ├── copilot-instructions.md
   └── README.md
   ```

3. **Document handoffs** — clearly indicate which agents can coordinate
   ```yaml
   handoffs:
     - trust-structure-designer
     - beneficiary-planning-agent
   ```

4. **Use semantic versioning** — help users track updates
   - 1.0.0 = Initial release
   - 1.1.0 = Bug fixes or minor enhancements
   - 2.0.0 = Breaking changes

5. **Maintain CHANGELOG.md** — document what changed and how to upgrade
   ```markdown
   ## [1.1.0] - 2024-12-11
   ### Fixed
   - Improved handoff context sharing with beneficiary agent
   ### Added
   - New validation for trust document references
   ```

6. **Test migrations** — before sharing agent groups, verify they work in a fresh repo
   ```bash
   # Create temp repo for testing
   mkdir /tmp/test-migration
   cd /tmp/test-migration
   git clone https://github.com/test-org/test-repo.git
   # Copy agents and validate
   ```

7. **Version lock models** — don't change model assignments without major version bump
   - If you must switch models, increment major version and document in CHANGELOG

## Contributing New Agents

To contribute a new agent group to this repository:

1. **Design**: Create specification with Agent Architect
2. **Implement**: Use Agent Implementer with portable format
3. **Validate**: Ensure zero errors: `python .github/scripts/validate-agents.py`
4. **Document**: Include copilot-instructions.md, README.md, CHANGELOG.md
5. **Test**: Run agents with sample inputs to verify behavior
6. **PR**: Submit pull request with clear commit message and description

Pull request checklist:
- [ ] All agents pass validation
- [ ] At least 2-3 examples per agent (with realistic scenarios)
- [ ] Clear integration points documented
- [ ] README explains agent group purpose and usage
- [ ] CHANGELOG documents version and changes
- [ ] No hardcoded repo/org names or absolute paths

## Further Reading

- **Architecture Guide**: `.github/agents/architect.agent.md`
- **Implementation Guide**: `.github/agents/implementer.agent.md`
- **Validation Guide**: `.github/agents/validator.agent.md`
- **Copilot Instructions**: `.github/agents/copilot-instructions.md`

