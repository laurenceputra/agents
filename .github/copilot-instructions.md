# GitHub Copilot Instructions - Agent Builder System

## Overview

This is a meta-agent system designed to help you build high-quality, reusable agents for any purpose. The system follows GitHub Copilot best practices for agent development.

## Core Principle

**Agents are managerial roles that define job scope, requirements, and quality standards for specialized tasks.**

## Workflow: Building New Agents

When creating a new agent, follow this structured workflow:

### Phase 1: Agent Architecture (Define the Need)
**Consult**: `.github/agents/agent-architect.md`

The Agent Architect analyzes your requirements and designs the agent specification including:
- Agent purpose and scope
- Key responsibilities
- Required inputs and expected outputs
- Success criteria
- Integration points with other agents (if applicable)

### Phase 2: Agent Implementation (Build the Agent)
**Consult**: `.github/agents/agent-implementer.md`

The Agent Implementer creates the agent definition file following best practices:
- Clear, actionable instructions
- Structured response formats
- Example scenarios
- Quality checklists
- GitHub Copilot optimization

### Phase 3: Agent Validation (Quality Assurance)
**Consult**: `.github/agents/agent-validator.md`

The Agent Validator reviews the agent implementation for:
- Clarity and completeness
- Adherence to best practices
- Testability and measurability
- Documentation quality
- Usability

## Best Practices (from GitHub Copilot Documentation)

### 1. Be Specific and Clear
- Define exact scope and boundaries
- Use concrete examples
- Specify output formats explicitly
- Include edge cases and constraints

### 2. Provide Context
- Explain the "why" behind the agent's purpose
- Reference relevant domain knowledge
- Define terminology and abbreviations
- Link to related agents or documentation

### 3. Structure for Clarity
- Use consistent markdown formatting
- Organize with clear headings
- Include bullet points and numbered lists
- Separate instructions from examples

### 4. Include Examples
- Provide concrete input/output examples
- Show both simple and complex scenarios
- Demonstrate edge case handling
- Include counterexamples (what NOT to do)

### 5. Define Success Criteria
- Make outcomes measurable
- Include quality checklists
- Specify acceptance criteria
- Define what "done" looks like

### 6. Optimize for Iteration
- Keep instructions modular
- Support incremental improvements
- Enable easy updates
- Document versioning and changes

## Agent Template Structure

Every agent should follow this structure:

```markdown
---
name: agent-name
description: Brief one-line description
version: 1.0.0
---

# Agent Name

## Purpose
Clear statement of what this agent does and why it exists.

## Responsibilities
- List of key responsibilities
- Each should be actionable and specific

## Domain Context
- Relevant background information
- Key concepts and terminology
- Constraints and requirements

## Input Requirements
What information this agent needs to operate effectively.

## Output Format
Exact structure of what this agent produces.

## Response Format
1. Section 1
2. Section 2
3. Section 3

## Examples

### Example 1: [Scenario Name]
**Input:**
[description]

**Output:**
[expected result]

### Example 2: [Edge Case]
**Input:**
[description]

**Output:**
[expected result]

## Quality Checklist
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Integration Points
How this agent connects with other agents or systems.

## Version History
Track changes and improvements over time.
```

## Creating Your First Agent

1. **Start with the Agent Architect**: Describe what you need
2. **Use the Agent Implementer**: Turn the spec into a working agent file
3. **Validate with the Agent Validator**: Ensure quality and best practices
4. **Iterate**: Refine based on feedback and real-world usage

## Common Agent Categories

Consider building agents for these common needs:

### Development Agents
- **Code Reviewer**: Reviews code for quality, security, and best practices
- **Technical Writer**: Creates documentation, API specs, and guides
- **Test Designer**: Designs comprehensive test strategies
- **Debugger**: Diagnoses and fixes issues systematically

### Product Agents
- **Product Manager**: Defines requirements and acceptance criteria
- **User Researcher**: Analyzes user needs and feedback
- **UX Designer**: Designs user experiences and interfaces

### Operations Agents
- **DevOps Engineer**: Handles deployment, infrastructure, monitoring
- **Security Auditor**: Reviews for security vulnerabilities
- **Performance Optimizer**: Analyzes and improves performance

### Specialized Agents
- **Data Analyst**: Analyzes data and generates insights
- **API Designer**: Designs clean, consistent APIs
- **Migration Planner**: Plans and executes system migrations

## Tips for Effective Agents

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Composable**: Agents should work well together
3. **Testable**: Include clear success criteria
4. **Maintainable**: Document assumptions and limitations
5. **Evolvable**: Design for change and improvement

## Agent File Naming Convention

- Use kebab-case: `agent-name.md`
- Place in: `.github/agents/`
- Version in front matter

## Getting Help

- Review existing agents as examples
- Start with simple use cases
- Iterate based on real usage
- Document what works and what doesn't

## References

- [GitHub Copilot Best Practices](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
- Agent files in `.github/agents/`
