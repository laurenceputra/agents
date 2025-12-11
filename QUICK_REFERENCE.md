# Agent Portability Quick Reference

**Status**: ✅ Fully Implemented  
**Scope**: Complete portable agent system for `.github/agents` and all agent groups

## What Changed

### Schema & Standards
- ✅ **Portable frontmatter** added to architect.agent.md (name, description, model, version, handoffs)
- ✅ **Output standards** added to implementer.agent.md (file structure, validation checklist)

### Validation & CI
- ✅ **Validator script** created (`.github/scripts/validate-agents.py`)
- ✅ **GitHub Actions** workflow created (`.github/workflows/validate-agents.yml`)

### Documentation
- ✅ **PORTABILITY.md** — Complete migration and usage guide
- ✅ **README template** — Customizable template for agent groups
- ✅ **IMPLEMENTATION_SUMMARY.md** — Full reference of all changes

### Tools
- ✅ **Migration script** — Automated agent group migration
- ✅ **Validation suite** — Full compliance checking

## Key Features

### 1. Portable Format
```yaml
---
name: legacy-planning-advisor                  # kebab-case, matches filename
description: Guides comprehensive planning    # 50-100 characters
model: Claude Sonnet 4.5 (copilot)           # From architect recommendations
version: 1.0.0                                # Semantic versioning
handoffs:                                     # Optional: agent names
  - trust-structure-designer
  - beneficiary-planning-agent
---
```

### 2. Folder Structure
```
agent-group-name/
├── agents/
│   ├── agent-1.agent.md
│   ├── agent-2.agent.md
│   └── agent-3.agent.md
├── copilot-instructions.md
├── README.md
└── CHANGELOG.md
```

### 3. Validation
```bash
# Validate all agents
python .github/scripts/validate-agents.py

# Validate specific group
python .github/scripts/validate-agents.py agent-group/

# Show schema reference
python .github/scripts/validate-agents.py --schema
```

### 4. Migration
```bash
# Migrate to another repository
./.github/scripts/migrate-agents.sh source-path target-path group-name

# Example
./.github/scripts/migrate-agents.sh ~/src/legacy-planning ~/target/.github/agents
```

## Common Workflows

### Create New Agent Group

1. **Design** with Agent Architect (specification)
2. **Implement** with Agent Implementer (follows portable format)
3. **Validate** — `python .github/scripts/validate-agents.py group-name/`
4. **Commit** — `git add group-name/ && git commit -m "Add group-name agents"`

### Update Existing Agent

1. **Edit** agent file
2. **Bump version** in frontmatter (1.0.0 → 1.1.0)
3. **Validate** — `python .github/scripts/validate-agents.py agents/agent.agent.md`
4. **Commit** — `git commit -m "Update agent-name: description"`

### Migrate to Another Repository

1. **Validate** in source — `python .github/scripts/validate-agents.py group-name/`
2. **Run script** — `./.github/scripts/migrate-agents.sh src target group-name`
3. **Validate** in target — `python .github/scripts/validate-agents.py .github/agents/group-name/`
4. **Integrate** — Update target repo's documentation and handoffs

## Files & Locations

| File | Purpose | Location |
|------|---------|----------|
| validate-agents.py | Validation tool | `.github/scripts/` |
| migrate-agents.sh | Migration tool | `.github/scripts/` |
| validate-agents.yml | CI/CD workflow | `.github/workflows/` |
| PORTABILITY.md | Migration guide | `/` (repo root) |
| README.template.md | Documentation | `.github/templates/` |
| architect.agent.md | Schema definition | `.github/agents/` |
| implementer.agent.md | Output standards | `.github/agents/` |

## Model Options

Approved models for all agents (from architect.agent.md):

| Model | Use Case |
|-------|----------|
| Claude Sonnet 4.5 (copilot) | Analytical, reasoning-heavy tasks |
| Claude Haiku 4.5 (copilot) | Creative, empathetic writing |
| Gemini 3 Pro (Preview) | Log analysis, QA, test design |
| Raptor mini (Preview) | Lightweight, quick interactions |

## Validation Rules

Agent must pass all checks:

- [ ] Frontmatter exists and is valid YAML
- [ ] `name` field matches filename (kebab-case)
- [ ] `description` is 20-150 characters
- [ ] `model` is from approved list
- [ ] `version` format is semantic (X.Y.Z)
- [ ] `handoffs` reference valid agents in group
- [ ] File is in `agents/` subdirectory
- [ ] No hardcoded paths or repo-specific names

## Help & Resources

### Documentation
- **PORTABILITY.md** — Complete guide (650+ lines)
- **IMPLEMENTATION_SUMMARY.md** — All changes (1600+ lines)
- **architect.agent.md** — Schema reference

### Commands
```bash
# Show schema reference
python .github/scripts/validate-agents.py --schema

# Validate with verbose output
python .github/scripts/validate-agents.py agent-group/

# Run all validations and show summary
python .github/scripts/validate-agents.py
```

### Troubleshooting
See **PORTABILITY.md** "Troubleshooting" section for:
- Validation failures
- Migration issues
- Integration problems

## Current Status

### All Agents Valid ✅

- ✅ `.github/agents/architect.agent.md` (1.0.0)
- ✅ `.github/agents/implementer.agent.md` (1.0.0)
- ✅ `.github/agents/validator.agent.md` (1.0.0)
- ✅ `legacy-planning/agents/*` (4 agents, v1.0.0)
- ✅ `product-development-agents/agents/*` (4 agents, v1.0.0)

**Total**: 11/11 agents pass portability validation

### System Ready ✅

- ✅ Validator script tested and working
- ✅ CI/CD workflow configured
- ✅ Migration script tested
- ✅ Documentation complete
- ✅ All agents portable and drop-in ready

## Next Steps

### For Users

1. **Read** PORTABILITY.md for detailed workflow
2. **Use** validator before every commit
3. **Follow** folder structure for new agent groups
4. **Run** CI/CD checks before merge

### For New Agents

1. **Design** specification with Architect
2. **Implement** following portable format
3. **Validate** locally: `python .github/scripts/validate-agents.py`
4. **Commit** when validation passes

### For Migration

1. **Source validate**: Ensure agents pass validation
2. **Run script**: `./.github/scripts/migrate-agents.sh`
3. **Target validate**: Confirm agents work in new repo
4. **Integrate**: Update documentation and handoffs

## Version History

**v1.0.0** (December 11, 2024)
- Initial implementation of complete portability system
- Validator script with full compliance checking
- CI/CD workflow for automated validation
- Comprehensive documentation and migration tools
- All existing agents updated and validated

---

**For detailed information**: See PORTABILITY.md or IMPLEMENTATION_SUMMARY.md  
**For troubleshooting**: See PORTABILITY.md "Troubleshooting" section  
**For schema reference**: Run `python .github/scripts/validate-agents.py --schema`

