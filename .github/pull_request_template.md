# Agent Implementation PR

<!-- This template is used by the PR Manager when submitting agent implementations to main. -->
<!-- Fill in all applicable sections. For agent groups, include group-specific sections. -->

## Type
<!-- Check one -->
- [ ] Individual Agent Implementation
- [ ] Agent Group Implementation
- [ ] Agent Refactor/Update

## Validation Status
<!-- PR Manager confirms all approval criteria met -->
- [ ] ✅ **APPROVED** by Quality Reviewer
- [ ] All critical issues resolved
- [ ] Quality standards met
- [ ] Ready for merge

## Agent Information

### Individual Agent
<!-- Complete this section for individual agent PRs -->
**Agent Name**: `agent-name`  
**Description**: Brief one-line description  
**Model**: Claude Sonnet 4.5 (copilot) / Claude Haiku 4.5 (copilot) / Gemini 3 Pro (copilot)  
**Version**: 1.0.0  
**Location**: `path/to/agent-name.agent.md`

### Agent Group
<!-- Complete this section for agent group PRs -->
**Group Name**: `group-name`  
**Purpose**: Brief description of agent group  
**Agents in Group**:
- `agent-1` - Description (Model)
- `agent-2` - Description (Model)
- `agent-3` - Description (Model)

**Location**: `path/to/group-name/`

## Files Changed
<!-- List all files added, modified, or deleted -->

### Added
- `path/to/file1.md`
- `path/to/file2.md`

### Modified
- `path/to/file3.md`

### Deleted
- `path/to/file4.md` (if applicable)

## Validation Summary

### Completeness Review
<!-- Agent Validator confirms all required sections present -->
- [ ] All required sections present and thorough
- [ ] Instructions clear and actionable
- [ ] Examples comprehensive (minimum 2, ideally 3)
- [ ] Quality checklist measurable (6-10 items for individuals, 8-15 for groups)
- [ ] Integration points documented

### Best Practices Compliance
<!-- Follows GitHub Copilot guidelines -->
- [ ] Clear purpose statement
- [ ] Specific and actionable responsibilities
- [ ] Concrete examples with input/output
- [ ] Structured formatting (headings, bullets, code blocks)
- [ ] Consistent markdown conventions

### Agent-Specific Validation
**For Individual Agents:**
- [ ] Frontmatter valid (name, description, model, version, handoffs)
- [ ] Filename matches `name` field (kebab-case)
- [ ] No hardcoded paths or repo-specific references

**For Agent Groups:**
- [ ] Folder structure matches portable pattern (`group-name/agents/`, `copilot-instructions.md`, `README.md`)
- [ ] All agents have valid frontmatter
- [ ] Handoff chains form valid graph (no broken references)
- [ ] Models match Architect recommendations
- [ ] Infrastructure files complete (copilot-instructions.md, README.md)
- [ ] Workflow documented with decision trees
- [ ] Cross-agent consistency verified
- [ ] Portability validated (folder-agnostic)

### Quality Assessment
**Strengths**:
- List key strengths of the implementation

**Issues Addressed**:
- Summary of feedback loop iterations and resolutions

## Approval Criteria Met
<!-- All items must be checked for approval -->
- [ ] Specification requirements fulfilled
- [ ] All required sections complete
- [ ] Examples demonstrate key scenarios
- [ ] Quality checklist actionable
- [ ] No critical issues remaining
- [ ] Aligns with GitHub Copilot best practices
- [ ] Follows portable agent pattern (if applicable)

## Related Issues
<!-- Link to specification, discussions, or related issues -->
- Specification: #issue-number or link
- Related: #issue-number (if applicable)

## Next Steps
<!-- Actions after merge -->
- [ ] Agent available for use via `@agent-name`
- [ ] Documentation updated (if needed)
- [ ] Announce to team (if applicable)

---

## Quality Reviewer Sign-Off
**Reviewed by**: @quality-reviewer  
**Approval Date**: YYYY-MM-DD  
**Validation Report**: [Link to detailed validation report if applicable]

**Confidence Level**: High / Medium  
**Recommendation**: Approve and merge

<!-- 
QUALITY REVIEWER CHECKLIST (Internal):
- Verified feature branch origin: feature/agent-{name} or feature/group-{name}
- Confirmed no direct commits to main
- Validated against original specification
- Reviewed all feedback loop iterations
- Confirmed all critical issues resolved
- Tested agent invocation (if applicable)
-->
