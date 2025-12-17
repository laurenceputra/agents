# Agent Builder Meta-System

![Version](https://img.shields.io/badge/version-2.0.0-blue)

This directory contains the meta-agent system for designing, implementing, and validating agents for any purpose.

## What is This?

The Agent Builder is a **meta-level system** that helps you create high-quality, reusable agents. Think of it as "agents that build agents" - these are managerial roles that define job scope, requirements, and quality standards for specialized agent development.

## Core Philosophy

**Agents are managerial roles.** They don't execute code; they define what needs to be done, what quality looks like, and how to measure success. This meta-system helps you build agents that fulfill this philosophy effectively.

## How It Works

The system uses five specialized agents in a quality-gated workflow:

### Phase 1: Architecture (Design)
**Agent**: `agent-architect.md`

Start here when you need a new agent. The Agent Architect:
- Analyzes your requirements
- Designs agent specifications
- Defines scope and boundaries
- Establishes success criteria
- Documents integration points

**When to use**: You have a problem to solve and need to figure out what kind of agent would help.

**Example**: "I need something to help review API designs" → Agent Architect produces a detailed specification for an API Design Reviewer agent.

### Phase 2: Implementation (Build)
**Agent**: `agent-implementer.md`

Once you have a specification, the Agent Implementer:
- Translates specifications into agent definition files
- Applies GitHub Copilot best practices
- Creates comprehensive examples
- Designs quality checklists
- Ensures consistency with existing patterns

**When to use**: You have a clear specification and need to create the actual agent definition file.

**Example**: Takes the API Design Reviewer specification → Creates a complete `.md` agent definition file.

### Phase 3: Quality Review
**Agent**: `quality-reviewer.md`

After implementation, the Quality Reviewer:
- Reviews implementations for completeness
- Validates best practices adherence
- Checks examples and quality criteria
- Provides structured feedback
- Approves or requests revisions
- Escalates specification issues to Architect

**When to use**: You have a draft agent definition and need quality review.

**Example**: Reviews the API Design Reviewer implementation → Provides approval or feedback for iteration.

### Phase 4: PR Management
**Agent**: `pr-manager.md`

After quality approval, the PR Manager:
- Creates PR details files
- Coordinates with Devil's Advocate for critical review
- Tracks review status
- Submits PRs when all approvals complete

**When to use**: Quality review is approved and you need to coordinate final steps.

**Example**: Creates PR details, coordinates Devil's Advocate review → Submits PR when approved.

### Phase 5: Critical Review (Pre-PR Gate)
**Agent**: `devils-advocate.md`

Before PR submission, the Devil's Advocate:
- Critically reviews work from all agents
- Challenges assumptions and identifies blind spots
- Surfaces disagreements between agents
- Documents all perspectives for human decision-making
- Final quality gate before PR submission

**When to use**: Quality review approved and need critical review before PR.

**Example**: Reviews the API Design Reviewer implementation → Challenges assumptions, surfaces disagreements, approves for PR.

## Quick Start

### Creating Your First Agent

1. **Describe What You Need**
   ```
   "I need an agent that helps with [specific task/problem]"
   ```

2. **Consult Agent Architect**
   - Provide problem description
   - Receive detailed specification
   - Review and refine scope

3. **Consult Agent Implementer**
   - Provide the specification
   - Receive complete agent definition file
   - Review structure and examples

4. **Consult Quality Reviewer**
   - Provide the implementation
   - Receive validation report
   - Address any issues found

5. **Consult PR Manager**
   - After Quality Reviewer approval
   - PR Manager coordinates Devil's Advocate review
   - Review documented disagreements
   - PR submitted when all approvals complete

6. **Deploy and Iterate**
   - Use your new agent
   - Gather feedback
   - Refine using the same workflow

## Common Agent Use Cases

The meta-system can help you build agents for:

### Development
- Code reviewers (security, quality, style)
- Test designers (unit, integration, e2e)
- Technical writers (docs, API specs)
- Debuggers (systematic troubleshooting)
- Refactoring advisors (code improvement)

### Product
- Product managers (requirements, user stories)
- User researchers (feedback analysis)
- UX designers (interface design)
- Feature prioritizers (roadmap planning)

### Operations
- DevOps engineers (infrastructure, deployment)
- Security auditors (vulnerability scanning)
- Performance optimizers (profiling, tuning)
- Incident responders (troubleshooting, root cause)

### Specialized
- Data analysts (insights, visualization)
- API designers (RESTful, GraphQL)
- Migration planners (legacy system transitions)
- Documentation generators (automated docs)

## Best Practices

### From GitHub Copilot Documentation

1. **Be Specific**: Use concrete examples, explicit instructions
2. **Provide Context**: Explain the "why" behind agent behaviors
3. **Structure Clearly**: Consistent formatting, logical organization
4. **Include Examples**: Show both what to do and what not to do
5. **Define Success**: Measurable outcomes with checklists
6. **Optimize for Iteration**: Modular design, easy updates

### Tips for Effective Agents

- **Single Responsibility**: Each agent should have one clear purpose
- **Composable**: Agents should work well together in workflows
- **Testable**: Include clear success criteria and quality checklists
- **Maintainable**: Document assumptions and limitations
- **Evolvable**: Design for change and improvement

## File Structure

```
.github/
├── copilot-instructions.md          # This meta-system's workflow guide
├── README.md                         # This file
├── CHANGELOG.md                      # Version history
└── agents/
    ├── COMMON-PATTERNS.md            # Shared patterns and schemas
    ├── agent-architect.md            # Designs agent specifications
    ├── agent-implementer.md          # Implements agent definitions
    ├── quality-reviewer.md           # Reviews implementation quality
    ├── pr-manager.md                 # Manages PR submission
    └── devils-advocate.md            # Critical review before PR
```

## Examples

### Example 1: Building a Security Code Reviewer

**Step 1 - Architecture**
```
User: "I need an agent to review code for security vulnerabilities"
↓
Agent Architect produces specification:
- Purpose: Detect OWASP Top 10 in pull requests
- Inputs: PR diff, repo context, dependencies
- Outputs: Security findings report with remediation
- Success criteria: 95%+ detection rate, <5% false positives
```

**Step 2 - Implementation**
```
Agent Implementer creates agent-security-reviewer.md:
- Complete Purpose, Responsibilities, Domain Context sections
- Structured Output Format (findings, severity, remediation)
- Examples: SQL injection detection, XSS prevention, clean PR
- Quality Checklist: 10 measurable criteria
```

**Step 3 - Quality Review**
```
Quality Reviewer reviews implementation:
✅ All sections present and comprehensive
✅ Examples cover happy path and edge cases
✅ Quality checklist is measurable
⚠️ Recommendation: Add example for large PR handling
→ APPROVED WITH RECOMMENDATIONS
```

### Example 2: Building a Test Strategy Designer

**Step 1 - Architecture**
```
User: "I need help designing comprehensive test strategies"
↓
Agent Architect produces specification:
- Purpose: Analyze features and design test strategies
- Inputs: Requirements, architecture, existing coverage
- Outputs: Test scenarios, test cases, coverage plan
- Success criteria: All scenarios covered, edge cases identified
```

**Step 2 - Implementation**
```
Agent Implementer creates agent-test-strategy-designer.md:
- Purpose: Design test strategies for functional and non-functional requirements
- Response Format: 5-step structured approach
- Examples: Login feature, API endpoint, complex workflow
- Quality Checklist: Coverage, edge cases, risk assessment
```

**Step 3 - Quality Review**
```
Quality Reviewer reviews implementation:
✅ Clear purpose and responsibilities
✅ Comprehensive examples with inputs/outputs
✅ Detailed quality checklist
✅ Integration points documented
→ APPROVED
```

## Workflow Tips

### When Creating Agents

**Start Broad, Refine Narrow**
- Initial description can be vague
- Agent Architect will ask clarifying questions
- Iterate on specification before implementation

**Use Existing Agents as Examples**
- Review similar agents in your workspace
- Maintain consistency in structure and style
- Adapt patterns to your specific needs

**Validate Early and Often**
- Don't wait until complete to validate
- Quick validation checks can save rework
- Iterate based on feedback

### When Using the Meta-System

**For Simple Agents**: You might combine phases
- Quick architecture (sketch scope)
- Direct implementation from pattern
- Light validation review

**For Complex Agents**: Follow full workflow
- Detailed specification with stakeholder review
- Implementation with comprehensive examples
- Thorough validation with multiple reviewers

**For Agent Families**: Establish patterns
- First agent: Full workflow with extra care
- Subsequent agents: Reuse patterns, adapt specifics
- Maintain consistency across family

## References

- **GitHub Copilot Best Practices**: [Official Documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
- **Agent Architecture Patterns**: See `agent-architect.md` examples
- **Implementation Guide**: See `agent-implementer.md` best practices
- **Quality Standards**: See `agent-validator.md` checklists

## Support

### Getting Started
1. Read `copilot-instructions.md` for workflow overview
2. Start with Agent Architect to explore possibilities
3. Review existing agent examples for patterns
4. Iterate based on your specific needs

### Troubleshooting

**Issue**: Agent specification seems too broad
- **Solution**: Work with Agent Architect to narrow scope, define clear boundaries

**Issue**: Implementation feels inconsistent
- **Solution**: Review existing agents for patterns, consult Agent Implementer with examples

**Issue**: Not sure if agent is ready
- **Solution**: Run through Agent Validator checklist, request formal validation

**Issue**: Agent isn't working as expected
- **Solution**: Review examples and quality checklist, may need specification revision

## Contributing

When improving the meta-system itself:

1. **Propose Changes**: Describe what you want to improve and why
2. **Update Specifications**: Use Agent Architect to design changes
3. **Implement Updates**: Use Agent Implementer for consistency
4. **Validate Quality**: Use Agent Validator to review
5. **Document Changes**: Update this README and copilot-instructions.md

## Troubleshooting

### "I need a new agent but don't know what to specify"
**Solution**: Consult @agent-architect. Describe your problem and Architect will design a specification.

### "My implementation was rejected by Quality Reviewer"
**Solution**: Review feedback carefully. Address critical issues first, then recommendations. Make changes on the same branch and notify Quality Reviewer for re-review.

### "Quality Reviewer and Devil's Advocate disagree"
**Expected**: Disagreements are captured in the PR for human decision. Both perspectives documented with reasoning.

### "Who submits the PR?"
**Answer**: PR Manager submits PRs after Quality Reviewer and Devil's Advocate approve. No one else merges agent implementations.

### "Can I skip Devil's Advocate review?"
**No**: Devil's Advocate is mandatory. All implementations require critical review before PR submission.

### "Specification has gaps during implementation"
**Solution**: Quality Reviewer escalates to Architect for spec revision. Architect updates spec, then Implementer updates implementation.

### "Too many validation iterations"
**Expected**: Iteration is normal. Quality takes time. Work through feedback systematically.

## Version History

- **2.0.0** - BREAKING CHANGE: Split Validator into Quality Reviewer + PR Manager. Extracted COMMON-PATTERNS.md. Simplified copilot-instructions.md (1542 → 388 lines, 75% reduction). Reduced total agent size by 44% (7039 → 3912 lines). Five-agent system for clearer separation of concerns.
- **1.5.0** - Added Devil's Advocate agent as fourth meta-agent for critical review, disagreement capture, and pre-PR quality gate. Updated workflow to four phases.
- **1.2.0** - Added mandatory CHANGELOG.md and README.md update enforcement with validation checklists, format guidelines, and quality criteria
- **1.1.0** - Added strict workflow enforcement, quality gates, decision trees, PR gatekeeper pattern, and version frontmatter support
- **1.0.0** - Initial meta-agent system with Architect, Implementer, Validator
