# Specification: Update Agent Send Field to True

**Date**: 2025-12-20  
**Author**: Agent Architect  
**Status**: Approved for Implementation

## Problem Statement

All agent files currently have `send: false` in their handoff frontmatter, requiring manual confirmation for each agent handoff. This creates unnecessary friction in the workflow. The system should default to automatic handoffs (`send: true`) while preserving the ability to explicitly set `send: false` when manual confirmation is needed.

## Objectives

1. Update all agent files to use `send: true` in handoff configurations
2. Update documentation (COMMON-PATTERNS.md) to reflect `send: true` as the new default
3. Ensure consistency across all agent groups including the meta-agent system in `.github/agents/`

## Scope

### In Scope
- Update `send: false` to `send: true` in all `.agent.md` files across all directories
- Update `.github/agents/COMMON-PATTERNS.md` to document `send: true` as default
- Update any other documentation referencing the `send` field default value

### Out of Scope
- Changes to agent logic or functionality
- Changes to handoff structure beyond the `send` field
- Creating new agents or modifying agent responsibilities

## Success Criteria

1. All agent files have `send: true` in their handoff configurations (71 total instances found)
2. COMMON-PATTERNS.md reflects `send: true` as the default value
3. No `send: false` instances remain in any agent file
4. All changes pass Quality Reviewer validation
5. Changes approved by Devil's Advocate critical review

## Affected Files

### Agent Files (71 total `send: false` instances)
Based on grep search results, the following directories contain agent files with `send: false`:
- `.github/agents/` - Meta-agent system (3 agent files with send: false)
- `corporate-team-building/agents/` - 4 instances
- `holiday-itinerary-planning/agents/` - (to be verified)
- `legacy-planning/agents/` - 6 instances
- `philanthropic-advisory/agents/` - 10 instances
- `portfolio-analysis/agents/` - 5 instances
- `product-development-agents/agents/` - 4 instances
- `recommendation-letter/agents/` - 5 instances
- `social-media-team/agents/` - 16 instances
- `stock-investment-analysis/agents/` - 11 instances

### Documentation Files
- `.github/agents/COMMON-PATTERNS.md` - Line 20: Update default from `false` to `true`

## Implementation Approach

### Step 1: Find and Replace
Use multi-file replace to change all instances:
- Old: `send: false`
- New: `send: true`

### Step 2: Update Documentation
Update COMMON-PATTERNS.md frontmatter schema example:
```yaml
send: true  # Optional: Auto-send without confirmation (default: true)
```

### Step 3: Verification
- Run grep search to confirm no `send: false` remains
- Validate YAML frontmatter still parses correctly
- Confirm all handoff chains still valid

## Edge Cases and Considerations

### Edge Case 1: Multi-line handoff blocks
Some agents may have multiple handoffs in a single block. Each `send: false` must be updated.

### Edge Case 2: Comments in YAML
The COMMON-PATTERNS.md documentation includes inline comments. Update the comment to reflect the new default.

### Edge Case 3: Indentation
Maintain exact indentation when replacing to preserve YAML validity.

## Model Recommendation

**Agent Implementer**: Claude Haiku 4.5 (copilot)
- **Rationale**: This is a straightforward find-and-replace task with clear boundaries. No complex reasoning required, just systematic file updates.

**Quality Reviewer**: Claude Sonnet 4.5 (copilot)
- **Rationale**: Verification requires careful checking of multiple files and validation of YAML syntax.

**Devil's Advocate**: Claude Sonnet 4.5 (copilot)
- **Rationale**: Critical review of the decision to default to auto-send requires reasoning about workflow implications.

## Risks and Mitigations

**Risk**: Breaking YAML syntax during replacement  
**Mitigation**: Use multi-replace tool with exact string matching including indentation

**Risk**: Missing instances of `send: false`  
**Mitigation**: Run comprehensive grep search before and after to verify all instances updated

**Risk**: Changing default behavior unexpectedly affects existing workflows  
**Mitigation**: This is an intentional change to improve workflow efficiency. Document in PR.

## Validation Checklist

- [ ] All 71+ instances of `send: false` updated to `send: true`
- [ ] COMMON-PATTERNS.md documentation updated
- [ ] No `send: false` remains in any agent file
- [ ] All YAML frontmatter still valid
- [ ] Grep search confirms completion
- [ ] Quality Reviewer approval obtained
- [ ] Devil's Advocate critical review passed

## Dependencies

- None. This is a self-contained change.

## Timeline

Estimated completion: Single implementation session (all changes in one batch).

---

**Handoff to Implementer**: This specification is complete and ready for implementation. Create a feature branch and implement all file changes using the multi-replace tool.
