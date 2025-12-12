# Legacy Planning Agents

A comprehensive legacy planning guidance system for GitHub Copilot with four specialized agents that help individuals and families navigate trust setup, beneficiary planning, and documenting their wishes.

## Overview

This system provides empathetic, structured guidance through complex legacy planning decisions. It's designed to help users think through estate planning considerations while recognizing when professional legal advice is needed.

### The Four Agents

1. **Legacy Planning Advisor** - Primary coordinator for discovery and structured guidance
2. **Beneficiary Planning Agent** - Analyzes beneficiary circumstances and distribution design
3. **Trust Structure Designer** - Explains trust types and recommends appropriate structures
4. **Letter of Wishes Composer** - Guides writing of personal letters documenting values and guidance

### Key Features

- ✅ **Hub-and-Spoke Coordination**: Central advisor routes to specialists as needed
- ✅ **Empathetic Guidance**: Sensitive tone for complex family and financial discussions
- ✅ **Structured Discovery**: Thoughtful questions to surface important considerations
- ✅ **Educational Focus**: Explains concepts clearly while noting when legal advice is needed
- ✅ **Comprehensive Examples**: Each agent includes detailed scenario examples
- ✅ **Flexible Workflow**: Specialists engaged based on user needs, not fixed sequence

## Quick Start

### Installation

1. **Copy to Your Project**
   ```bash
   # From your project root
   cp -r /path/to/this-agent-group .github/legacy-planning
   ```

2. **Start Using**
   
   In GitHub Copilot Chat, reference agents with `@`:
   ```
   @legacy-planning-advisor I want to start planning my estate
   ```

### Basic Usage

#### Scenario 1: Starting Legacy Planning

```
Step 1: Initial Discovery
You: "@legacy-planning-advisor I'm 55, married with two adult children. I want to start thinking about estate planning but don't know where to begin."

Legacy Planning Advisor will:
- Ask structured discovery questions about your situation
- Explore family structure, assets, and goals
- Help identify planning priorities
- Recommend which specialist agents to consult

Step 2: Beneficiary Analysis (if recommended)
You: "@beneficiary-planning-agent Here's my situation: [context from advisor]. Help me think through fair distributions."

Beneficiary Planning Agent will:
- Analyze each beneficiary's circumstances
- Discuss fairness vs. equality considerations
- Help design distribution strategies
- Surface potential conflict areas

Step 3: Trust Structure Design (if appropriate)
You: "@trust-structure-designer Based on my situation, which trust structures should I consider?"

Trust Structure Designer will:
- Explain relevant trust types
- Analyze pros/cons for your situation
- Recommend appropriate structures
- Identify when to consult estate attorney

Step 4: Letter of Wishes (if desired)
You: "@letter-of-wishes-composer Help me write a letter explaining my decisions to my family."

Letter of Wishes Composer will:
- Help structure your letter
- Guide you through what to include
- Draft sections based on your input
- Create meaningful personal messages
```

#### Scenario 2: Specific Planning Question

```
You: "@beneficiary-planning-agent I have two children - one is financially stable, the other struggles with money management. How do I divide my estate fairly?"

Beneficiary Planning Agent will directly:
- Analyze the different circumstances
- Discuss fairness vs. equal split
- Explore options (trusts, staggered distributions)
- Help you align distributions with your values
```

## Workflow

### The Hub-and-Spoke Pattern

```
User with Legacy Planning Need
    ↓
Legacy Planning Advisor (Discovery & Coordination)
    │
    ├─ Asks structured questions
    ├─ Identifies family structure, assets, goals
    ├─ Determines which specialists are needed
    └─ Routes to appropriate specialist(s) with context
    
    ↓ (Can hand to any specialist based on needs)
    
    ├─→ Beneficiary Planning Agent
    │   (Analyzes beneficiary needs, designs distributions)
    │   └─→ Returns analysis to advisor
    │
    ├─→ Trust Structure Designer
    │   (Recommends trust types and structures)
    │   └─→ Returns recommendations to advisor
    │
    └─→ Letter of Wishes Composer
        (Writes letter documenting values & guidance)
        └─→ Returns draft to advisor

    ↓
Legacy Planning Advisor (Synthesizes specialist outputs)
    │
    └─ Provides comprehensive guidance to user
```

### Key Characteristics

- **Flexible Order**: Specialists engaged based on user needs, not fixed sequence
- **Central Coordination**: Advisor synthesizes outputs from multiple specialists
- **Parallel Work**: Multiple specialists can be consulted for same planning effort
- **Context Preservation**: Advisor maintains context across specialist consultations

See `copilot-instructions.md` for detailed workflow documentation including:
- Agent coordination patterns
- Decision trees for which agent to consult
- Handoff protocols between agents
- Complete planning journey examples

## Agent Capabilities

### Legacy Planning Advisor

**Purpose**: Guide users through comprehensive legacy planning with structured discovery

**Key Capabilities**:
- Ask thoughtful discovery questions about situation and goals
- Identify all relevant beneficiaries and circumstances
- Surface values and priorities for decision-making
- Recommend appropriate specialist consultations
- Synthesize specialist outputs into cohesive plan
- Recognize when to recommend professional legal advice

**When to Use**:
- Starting legacy planning journey
- Unclear what to plan for or where to begin
- Need to coordinate multiple planning areas
- Want comprehensive review of planning needs
- Synthesizing specialist recommendations

### Beneficiary Planning Agent

**Purpose**: Analyze beneficiary circumstances and design fair distributions

**Key Capabilities**:
- Inventory all potential beneficiaries
- Assess each beneficiary's needs and circumstances
- Balance fairness vs. equality considerations
- Design distribution strategies aligned with values
- Address complex family dynamics
- Prevent potential conflicts through thoughtful planning

**When to Use**:
- Determining how to divide estate among beneficiaries
- Dealing with different beneficiary circumstances
- Balancing competing needs and fairness
- Complex family situations (blended families, special needs)
- Want to prevent inheritance conflicts

### Trust Structure Designer

**Purpose**: Explain trust types and design appropriate structures

**Key Capabilities**:
- Educate on trust types (revocable, irrevocable, special needs, charitable, etc.)
- Assess whether trusts are appropriate for situation
- Recommend trust structures aligned with goals
- Explain trade-offs between trust options
- Identify when professional legal counsel is required
- Design multi-trust strategies for complex estates

**When to Use**:
- Learning about trust options
- Deciding if trusts are appropriate for your situation
- Choosing between trust types
- Designing trust structure for specific needs
- Complex estate requiring multiple trusts

### Letter of Wishes Composer

**Purpose**: Guide writing of comprehensive letter documenting values and wishes

**Key Capabilities**:
- Plan letter content based on specific situation
- Structure letter logically with clear sections
- Draft content that balances warmth and clarity
- Include personal messages to beneficiaries
- Explain distribution reasoning
- Provide guidance to trustees
- Create meaningful, non-legal documentation

**When to Use**:
- Want to explain estate plan decisions
- Need to provide guidance to trustees
- Want to leave personal messages to beneficiaries
- Documenting values and priorities
- Creating warmth alongside legal documents

## Customization Guide

### Project-Specific Configuration

Each agent has a **"Domain Context (Project-Specific)"** section to customize. For legacy planning agents, you might add:

#### Region-Specific Considerations
```markdown
### Domain Context (Project-Specific)

- **Jurisdiction**: [State/Country] estate laws
- **Tax Thresholds**: Estate tax exemption amounts
- **Common Trust Types**: Most common in your jurisdiction
- **Legal Resources**: Where to find estate attorneys
```

## Troubleshooting

### Common Questions

**Q: Is this agent system a replacement for legal advice?**
A: No. These agents provide educational guidance to help you think through planning considerations. Always consult a qualified estate attorney for legal advice and document preparation.

**Q: Which agent should I start with?**
A: Start with `@legacy-planning-advisor` if you're beginning your planning journey or unsure what you need. If you have a specific question (e.g., about trust types), you can go directly to the specialist agent.

**Q: Can I use multiple specialists for the same planning effort?**
A: Yes! The hub-and-spoke pattern is designed for this. The Legacy Planning Advisor can coordinate consultations with multiple specialists and help synthesize their guidance.

**Q: What if my situation is complex (blended family, special needs, international assets)?**
A: The agents can help you think through complexity and surface considerations, but complex situations require professional legal and tax advice. The agents will note when your situation requires professional consultation.

## Best Practices

### For Effective Legacy Planning

- ✅ **Be Thorough**: Share complete context about family, assets, and goals
- ✅ **Think Long-Term**: Consider not just current circumstances but future changes
- ✅ **Surface Conflicts**: Be honest about family dynamics and potential conflict areas
- ✅ **Involve Family**: Have conversations with spouse, adult children, trustees
- ✅ **Document Values**: Use Letter of Wishes to explain your reasoning
- ✅ **Seek Professional Advice**: Consult estate attorney for legal documents

### For Complex Situations

- ✅ **Break It Down**: Work through one area at a time with specialists
- ✅ **Coordinate Through Advisor**: Let Legacy Planning Advisor synthesize complex guidance
- ✅ **Document Decisions**: Keep notes on what you decide and why
- ✅ **Review Regularly**: Revisit plan when circumstances change

## Examples

### Example 1: Couple Planning Estate (Ages 60 and 62)
A comprehensive walkthrough of a couple starting estate planning with two adult children. See Legacy Planning Advisor agent for full example.

### Example 2: Blended Family with Special Needs Child
Complex scenario balancing needs of biological children, stepchildren, and special needs child. See Beneficiary Planning Agent for full example.

### Example 3: Choosing Trust Structure
Deciding between revocable living trust and irrevocable trust for estate planning. See Trust Structure Designer for full example.

## Additional Resources

- **copilot-instructions.md** - Detailed workflow documentation with coordination patterns
- **agents/legacy-planning-advisor.agent.md** - Primary coordinator agent definition
- **agents/beneficiary-planning-agent.agent.md** - Distribution planning specialist
- **agents/trust-structure-designer.agent.md** - Trust recommendation specialist
- **agents/letter-of-wishes-composer.agent.md** - Letter writing specialist

## Version

**Version**: 1.0.0

**Last Updated**: 2024-12-12

Built with care for thoughtful legacy planning 💙
