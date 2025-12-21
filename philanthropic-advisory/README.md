# Philanthropic Advisory Agent Group

Comprehensive philanthropic advisory services for Singapore-focused giving with quantitative impact analysis, strategic portfolio alignment, and risk-opportunity assessment.

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](./CHANGELOG.md)
[![Model](https://img.shields.io/badge/model-Claude%20Sonnet%204.5-purple.svg)](https://www.anthropic.com/claude)

## Overview

This agent group helps philanthropists make data-driven funding decisions for initiatives targeting at-risk communities in Singapore (families in crisis, children from lower-income families). Six coordinated agents provide comprehensive analysis from framework definition through impact evaluation to strategic recommendation with mandatory critical review.

## Quick Start

**I need to define my giving principles first:**
1. Start with `@principles-framework-definer`
2. Answer 8 foundational questions about values, beneficiaries, theory of change, decision criteria
3. Receive comprehensive framework document with explicit criteria
4. Then evaluate specific programs against your framework

**I have a program to evaluate (with existing framework):**
1. Submit program details to `@impact-evaluator`
2. Workflow runs automatically through evaluation agents
3. Receive comprehensive recommendation with all perspectives

**I have a program to evaluate (no framework yet):**
1. Start with `@principles-framework-definer` to establish criteria first
2. Then submit program to `@impact-evaluator` (uses your framework criteria)
3. Receive recommendation aligned with your explicit values and thresholds

## The Six Agents

### 0. Principles & Framework Definer (OPTIONAL - Run First)
**Define giving principles and decision framework before evaluating programs**
- Guides through 8 foundational question areas (values, beneficiaries, theory of change, criteria)
- Produces framework document with quantitative thresholds (SROI, mission alignment)
- Operates standalone or integrates with evaluation workflow
- Ensures consistent, values-aligned decisions
- Can operate independently or hand off to impact evaluation

### 1. Impact Evaluator
**Quantitative impact analysis using SROI, CEA, and trajectory uplift**
- Calculates Social Return on Investment (SROI ratio)
- Performs Cost-Effectiveness Analysis (cost per outcome)
- Evaluates trajectory uplift for beneficiaries
- Assesses systemic impact potential
- Rates data quality and identifies measurement gaps

### 2. Portfolio Strategist
**Strategic fit and portfolio composition analysis**
- Assesses mission alignment (scoring 1-10)
- Evaluates portfolio diversification impact
- Identifies strategic gaps and synergies
- Maps concentration risks
- Recommends portfolio rebalancing

### 3. Risk-Opportunity Analyst
**Risk assessment and opportunity identification**
- Identifies implementation, financial, impact, external, and organizational risks
- Rates likelihood and impact for each risk
- Proposes mitigation strategies
- Identifies upside opportunities (scaling, partnerships, innovation)
- Provides scenario analysis (pessimistic/realistic/optimistic)

### 4. Recommendation Synthesizer
**Integrated funding recommendations**
- Synthesizes impact + portfolio + risk analyses
- Generates clear recommendation (fund/decline/modify/pilot)
- Specifies funding terms (amount, duration, conditions)
- Proposes monitoring framework and exit strategy
- Prepares executive summary for decision-makers

### 5. Devil's Advocate (MANDATORY)
**Critical review and assumption challenging**
- Challenges SROI/CEA assumptions
- Questions strategic fit claims
- Tests risk assessments for optimism/pessimism
- Surfaces disagreements between agents
- Identifies blind spots and alternative interpretations
- **Final quality gate before decision**

## Workflow

```
Program → @impact-evaluator → @portfolio-strategist → @risk-opportunity-analyst 
  → @recommendation-synthesizer → @devils-advocate (MANDATORY) → Decision
```

All agents use **Claude Sonnet 4.5 (copilot)** for high-quality analytical reasoning.

## Features

### Quantitative Rigor
- SROI and CEA calculations with transparent assumptions
- Trajectory uplift analysis (5-20 year projections)
- Benchmarking against comparable Singapore programs
- Data quality ratings (high/medium/low)

### Strategic Alignment
- Mission alignment scoring (1-10 scale)
- Portfolio gap analysis and diversification assessment
- Synergy mapping across funded programs
- Concentration risk evaluation

### Risk Management
- Comprehensive risk matrix (likelihood × impact)
- Mitigation strategies with specific actions
- Upside opportunity identification
- Scenario planning (pessimistic/realistic/optimistic)
- Exit and pivot strategies

### Critical Review
- Assumption challenging across all analyses
- Disagreement facilitation and documentation
- Blind spot identification
- Alternative perspective presentation
- **Mandatory quality gate before decisions**

## Singapore Focus

### Context
- **Demographics**: 5.7M population, ~50,000 at-risk youth, ~50,000 families needing support
- **Key Policies**: MSF ComCare, KidSTART, MOE school support, SkillsFuture
- **Landscape**: 500+ nonprofits via NCSS, strong government safety net with remaining gaps

### Beneficiary Focus
- **Families in crisis**: Domestic violence, job loss, eviction risk
- **Children from lower-income families**: <$3,000/month household income, ~20% of children

### Intervention Types
- **Crisis response**: Rapid stabilization for families in acute distress
- **Prevention**: Early intervention before crises occur
- **Systemic change**: Addressing root causes (policy, education systems, economic structures)

## Integration

### Prerequisites
- Access to GitHub Copilot with agent functionality
- Understanding of philanthropic decision-making
- Singapore context knowledge (helpful but not required)

### Usage Patterns

**Pattern 1: Full Workflow (Recommended)**
```
User: "I'm considering funding YouthLift, a mentorship program for 100 at-risk youth. 
       Budget: $150K annually. Should I fund it?"
       
@impact-evaluator (Workflow starts automatically)
```

**Pattern 2: Partial Workflow (Quick Analysis)**
```
User: "I already know SROI is 4.2:1. How does this program fit my portfolio?"

@portfolio-strategist (Provide SROI data, assess fit)
```

**Pattern 3: Critical Review Only (Second Opinion)**
```
User: "I have a recommendation to fund Program X. Challenge the assumptions."

@devils-advocate (Review existing recommendation)
```

### Output Formats
- **Executive Summaries**: 1-page decision briefs
- **Detailed Reports**: 10-20 page comprehensive analyses
- **Comparative Tables**: Side-by-side program comparisons
- **Risk Matrices**: Visual likelihood × impact grids

## Examples

### Example 1: Youth Mentorship Program
**Input**: YouthLift serves 100 at-risk youth (13-16) in Jurong West, $150K annually  
**Output**: SROI 4.2:1, Strong mission alignment (8/10), Medium risk (mitigable)  
**Recommendation**: FUND with conditions (volunteer pilot, comprehensive tracking)  
**Decision**: Philanthropist funds $150K annually for 3 years

### Example 2: Family Crisis Intervention
**Input**: FamilyStability Now serves 150 families in crisis, $500K annually  
**Output**: SROI 3.8:1, Moderate mission alignment (7/10), Fills crisis response gap  
**Recommendation**: FUND with portfolio balance consideration  
**Decision**: Philanthropist funds to diversify from prevention-only portfolio

## Troubleshooting

**Q: What if data is incomplete?**  
A: Impact Evaluator works with available data, rates quality as "Low", recommends pilot funding to gather data.

**Q: What if agents disagree?**  
A: Devil's Advocate documents all positions with trade-offs, presents to decision-maker for values-based choice.

**Q: Can I skip Devil's Advocate?**  
A: No — Critical review is MANDATORY final quality gate. Adds 1-2 hours but prevents costly mistakes.

**Q: How long does full workflow take?**  
A: 1-2 days for comprehensive analysis (can expedite to same-day if urgent).

## Resources

### Singapore Data Sources
- [Singapore Department of Statistics](https://www.singstat.gov.sg/) — Demographics
- [Ministry of Social and Family Development](https://www.msf.gov.sg/) — Policies and programs
- [National Council of Social Service](https://www.ncss.gov.sg/) — Nonprofit landscape

### Impact Measurement
- [Singapore Centre for Social Enterprise (raiSE)](https://www.raise.sg/) — Impact measurement standards
- [Charity Council](https://www.charities.gov.sg/) — Transparency requirements

## Contributing

This is a reference implementation. To adapt for your context:
1. Modify Singapore-specific references in agent files
2. Update demographic data and policy landscape
3. Adjust SROI/CEA benchmarks for your region
4. Preserve five-agent structure and workflow

## License

These agents follow GitHub Copilot agent patterns and are provided as-is for philanthropic decision support.

## Version History

- **1.0.0** (2024-12-16): Initial release with five agents (impact-evaluator, portfolio-strategist, risk-opportunity-analyst, recommendation-synthesizer, devils-advocate)

## Updating This Agent Group

This agent group can be updated from the upstream repository to get the latest improvements, bug fixes, and new features.

**To update:**

```bash
cd philanthropic-advisory  # or wherever you installed this agent group
./update-from-upstream.sh
```

The script will:
- Fetch the latest changes from the upstream repository
- Update agents and documentation files
- Preserve the update script itself
- Show a summary of changes

After running the update:
```bash
git status              # Review what changed
git diff                # See detailed changes
git add .              # Stage the updates
git commit -m "Update philanthropic-advisory agents from upstream"
```

**Note:** If you've made local customizations to agent files, the update will overwrite them. Consider keeping local modifications in a separate branch or using different file names.

---

**For detailed workflow and decision trees, see [copilot-instructions.md](./copilot-instructions.md)**
