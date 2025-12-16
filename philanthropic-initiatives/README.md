# Philanthropic Initiatives Advisory Agent Group

**Version**: 1.0.0  
**Status**: Production Ready  
**License**: MIT  
**Requires**: GitHub Copilot CLI  
**Geographic Focus**: Singapore

---

## Overview

A comprehensive AI-powered philanthropic advisory system that evaluates initiatives targeting at-risk communities in Singapore using quantitative impact metrics (SROI, CEA, trajectory uplift), scalability assessment, and portfolio strategy. Six specialized agents work together to analyze funding opportunities, with Devil's Advocate providing critical review for balanced perspective before recommendations.

**Core Focus**: Families in crisis situations and children born into lower-income families, emphasizing quantitative outcomes that lead to upstream systemic changes.

## Quick Start

### Option 1: Comprehensive Initiative Analysis (Recommended) ⭐

Use the **Philanthropic Strategy Advisor** as your starting point:

```bash
@philanthropic-strategy-advisor "I'm considering funding an after-school tutoring program for low-income students. Budget is $200K/year, serves 150 students. Should I fund this?"
```

**What happens**:
1. Advisor conducts discovery (asks clarifying questions about initiative and your priorities)
2. Advisor routes to appropriate specialists (program evaluation, impact metrics, scalability, portfolio fit)
3. Specialists complete analyses and return to advisor
4. Advisor synthesizes into comprehensive recommendation
5. Devil's Advocate reviews for bias and blind spots
6. You receive complete funding guidance with all perspectives (15-20 minutes)

**Best for**: Most users who want thorough analysis before funding decisions

---

### Option 2: Portfolio Strategy Review

Use when you need portfolio-level guidance without specific initiative:

```bash
@philanthropic-strategy-advisor "I've been funding initiatives for 2 years. Help me assess my portfolio and identify gaps."
```

---

### Option 3: Manual Agent-by-Agent (Advanced)

Call specialists directly when you need specific analysis:

```bash
# Calculate impact metrics only
@impact-metrics-analyst "Calculate SROI and CEA for tutoring program: $200K cost, 120 students improve grades"

# Assess scalability only
@scalability-assessor "Evaluate scaling potential for this family crisis hotline serving 500 families annually"

# Portfolio fit only
@portfolio-strategist "Does this financial literacy program align with my focus on families in crisis?"
```

**Best for**: Advanced users who want granular control or partial analysis

---

## What This Agent Group Does

### For Philanthropists
- **Evidence-Based Decisions**: Get rigorous analysis using SROI, CEA, and trajectory uplift metrics
- **Comprehensive Evaluation**: Assess program quality, financial efficiency, scaling potential, and portfolio fit in one place
- **Balanced Perspective**: Devil's Advocate ensures you see skeptical views and alternative scenarios
- **Strategic Portfolio Management**: Understand how initiatives fit within your overall philanthropic vision

### For Family Offices
- **Systematic Process**: Standardize funding decisions with repeatable evaluation framework
- **Risk Management**: Surface implementation risks, ethical concerns, and failure scenarios
- **Documentation**: Maintain audit trail of funding rationale and analysis
- **Portfolio Coherence**: Build intentional philanthropic portfolio, not random collection of grants

---

## The Six Agents

| Agent | Role | Model | When to Use |
|-------|------|-------|-------------|
| **philanthropic-strategy-advisor** ⭐ | Hub coordinator and synthesizer | Claude Sonnet 4.5 | **Recommended entry point** - Discovery, routing, synthesis |
| **initiative-evaluator** | Program design and evidence assessment | Claude Sonnet 4.5 | Evaluate initiative quality and implementation feasibility |
| **impact-metrics-analyst** | SROI, CEA, trajectory uplift calculations | Claude Sonnet 4.5 | Quantify financial efficiency and long-term impact |
| **scalability-assessor** | Growth potential and sustainability evaluation | Claude Sonnet 4.5 | Assess whether initiative can achieve impact at scale |
| **portfolio-strategist** | Thematic fit and portfolio balance analysis | Claude Sonnet 4.5 | Understand how initiative fits within overall portfolio |
| **devils-advocate** | Critical review for bias and blind spots | Claude Sonnet 4.5 | **MANDATORY** - Final quality gate before funding decisions |

---

## Usage Examples

### Example 1: Single Initiative Deep-Dive ⭐ (Most Common)

**Scenario**: You're considering funding an after-school tutoring program for low-income primary students.

```bash
@philanthropic-strategy-advisor "Analyze this tutoring program: $200K/year, 150 low-income students, 2x/week sessions, claims 80% improve grades by 1+ letter. Organization has 5-year track record. Should I fund this?"
```

**Workflow**:
1. **Discovery**: Advisor asks clarifying questions (organization details, your philanthropic priorities, portfolio context)
2. **Initiative Evaluator**: Assesses program design, evidence base, implementation risks
3. **Impact Metrics Analyst**: Calculates SROI ($1 → $3.20), CEA ($1,667/student), trajectory uplift (secondary completion rates)
4. **Scalability Assessor**: Evaluates potential to reach more students, sustainability model
5. **Portfolio Strategist**: Assesses fit with your theme of uplifting lower-income children
6. **Synthesis**: Advisor integrates all analyses into funding recommendation
7. **Devil's Advocate**: Challenges assumptions, develops failure scenarios, surfaces risks
8. **Final Delivery**: Complete recommendation with all perspectives

**Outcome**: You receive comprehensive analysis with funding recommendation, conditions, and monitoring metrics. Decision time: ~20 minutes total.

---

### Example 2: Comparative Analysis

**Scenario**: You're choosing between two initiatives.

```bash
@philanthropic-strategy-advisor "Compare: Family crisis hotline ($150K/year) vs. financial literacy program ($180K/year). Both serve at-risk families. Which aligns better with my goals?"
```

**Workflow**:
- Specialists analyze both initiatives in parallel
- Advisor provides side-by-side comparison
- Devil's Advocate challenges assumptions for both
- You receive clear comparison with recommendation

---

### Example 3: Portfolio Strategy Review

**Scenario**: You want to assess overall portfolio and identify gaps.

```bash
@philanthropic-strategy-advisor "I've funded 5 initiatives over 2 years (education, family support). Total budget $800K annually. Help me assess portfolio and identify gaps."
```

**Workflow**:
- Advisor inventories current portfolio
- Portfolio Strategist analyzes balance, gaps, concentration risk
- Impact Metrics Analyst reviews aggregate impact (if data available)
- Devil's Advocate challenges portfolio assumptions
- You receive strategic guidance on next funding cycle

---

### Example 4: Quick Metrics Calculation

**Scenario**: You just need SROI/CEA, not full evaluation.

```bash
@impact-metrics-analyst "Calculate SROI for job training: $80K cost, 40 single parents complete program, 32 gain employment with $15K income increase. Calculate over 5-year timeframe."
```

**Outcome**: Metrics report with SROI, CEA, sensitivity analysis (5 minutes).

---

## Key Methodologies

### Social Return on Investment (SROI)
**What**: Ratio of social value created to investment  
**Formula**: SROI = (Social Value - Investment) / Investment  
**Example**: $1 invested → $3.50 social value  
**Components**: Outcome valuation, attribution, deadweight, displacement, drop-off

### Cost-Effectiveness Analysis (CEA)
**What**: Cost per outcome unit achieved  
**Formula**: CEA = Total Cost / Number Achieving Outcome  
**Example**: $1,667 per student with grade improvement  
**Use**: Compare initiatives on cost efficiency

### Trajectory Uplift
**What**: Long-term improvement in beneficiary life outcomes vs. baseline  
**Example**: 75% secondary completion (program) vs. 60% baseline = 25% uplift  
**Focus**: User's priority - systemic change through individual trajectory improvement

---

## Geographic and Thematic Focus

**Geography**: Singapore exclusively  
**Target Populations**:
- Families in crisis situations (not of their own making)
- Children born into lower-income families
- Vulnerable populations facing systemic barriers

**Outcomes Prioritized**:
- Quantitative, measurable results
- Upstream systemic changes
- Trajectory uplift (long-term beneficiary improvement)

**Metrics Framework**: SROI, CEA, trajectory analysis aligned with Singapore context

---

## Workflow Architecture

**Hub-and-Spoke with Critical Review Gate**:

```
User Question/Initiative
        ↓
Philanthropic Strategy Advisor (Hub)
    → Discovery & Routing
        ↓
Specialist Consultation (Parallel)
    ├─→ Initiative Evaluator
    ├─→ Impact Metrics Analyst
    ├─→ Scalability Assessor
    └─→ Portfolio Strategist
        ↓
Philanthropic Strategy Advisor
    → Synthesis & Recommendation
        ↓
Devil's Advocate (MANDATORY)
    → Critical Review
        ↓
Final Delivery to User
```

**Quality Gates**:
1. **Discovery Complete**: Advisor has sufficient context
2. **Specialist Analyses Complete**: All required specialists report back
3. **Synthesis Complete**: Advisor integrates findings
4. **Critical Review Complete**: Devil's Advocate approves (or requests revisions)

---

## Integration Instructions

### Prerequisites
- GitHub Copilot CLI installed
- Access to GitHub Copilot agents

### Installation

1. **Copy to Your Environment**
   ```bash
   # This agent group is already in your repository
   # Located at: /philanthropic-initiatives/
   ```

2. **Start Using**
   ```bash
   # In terminal with Copilot CLI:
   @philanthropic-strategy-advisor "I want to evaluate a philanthropic initiative"
   
   # Or call specialists directly:
   @impact-metrics-analyst "Calculate SROI for [initiative]"
   ```

### Configuration
No configuration required - agents are ready to use immediately.

---

## Decision Trees

### "Which Agent Should I Use?"

```
START: What do you need?

├─ [A] EVALUATE SPECIFIC INITIATIVE
│   → Use @philanthropic-strategy-advisor (comprehensive analysis)
│   → What you get: Program quality, SROI/CEA, scalability, portfolio fit, critical review
│
├─ [B] PORTFOLIO-LEVEL STRATEGY
│   → Use @philanthropic-strategy-advisor (portfolio review mode)
│   → What you get: Portfolio balance analysis, gap identification, strategic guidance
│
├─ [C] QUICK METRICS ONLY (no full evaluation)
│   → Use @impact-metrics-analyst directly
│   → What you get: SROI, CEA, trajectory uplift calculations
│
├─ [D] SCALABILITY ASSESSMENT ONLY
│   → Use @scalability-assessor directly
│   → What you get: Scaling pathways, barriers, resource requirements
│
└─ [E] PORTFOLIO FIT ONLY
    → Use @portfolio-strategist directly
    → What you get: Thematic alignment, portfolio balance, strategic fit

**Recommendation**: For most use cases, start with @philanthropic-strategy-advisor
```

---

### "Should I Fund This Initiative?"

```
After comprehensive analysis from all agents:

Review Final Recommendation from Philanthropic Strategy Advisor

↓

Check Devil's Advocate Critical Review

↓

Are critical concerns raised?
│
├─ YES (High Risk) → Consider carefully
│   - What assumptions are challenged?
│   - What failure scenarios surfaced?
│   - What alternative uses of capital suggested?
│   → Decision: Fund with strong conditions, request revisions, or decline
│
└─ NO (Low Risk) → Proceed with confidence
    - Are SROI/CEA metrics favorable?
    - Is scalability potential sufficient?
    - Does portfolio fit align with themes?
    → Decision: Fund (with monitoring metrics), conditional funding, or decline

**Final Decision**: Yours, informed by all perspectives
```

---

## Troubleshooting

### "Analysis takes too long"
- **Cause**: Comprehensive evaluation requires 15-20 minutes
- **Solution**: Use manual agent-by-agent mode for faster partial analysis

### "I need more detailed metrics"
- **Cause**: Impact Metrics Analyst provides standard calculations
- **Solution**: Ask for sensitivity analysis or specific scenario testing

### "Agents disagree"
- **Expected**: Initiative Evaluator positive, Scalability Assessor skeptical (common pattern)
- **Resolution**: Philanthropic Strategy Advisor synthesizes trade-offs; Devil's Advocate surfaces disagreements

### "Not enough data for SROI"
- **Common**: Many initiatives lack complete outcome data
- **Handling**: Impact Metrics Analyst will flag limitations and provide estimates with caveats

---

## Best Practices

### For Effective Analysis
1. **Provide Complete Information**: More detail = better analysis
2. **State Your Priorities Clearly**: Help agents understand what matters to you
3. **Share Portfolio Context**: Enables better strategic fit assessment
4. **Read Devil's Advocate Review**: Don't skip skeptical perspectives
5. **Use Iteratively**: Start broad, then drill into specific concerns

### For Portfolio Management
1. **Regular Reviews**: Assess portfolio annually or bi-annually
2. **Track Outcomes**: Collect data to validate impact metrics over time
3. **Balance Risk**: Mix proven approaches with innovative pilots
4. **Maintain Theme Focus**: Don't drift from core philanthropic vision
5. **Document Decisions**: Keep record of rationale for future reference

---

## Version History

- **1.0.0** (2025-12-16): Initial release with six specialized agents focused on Singapore at-risk communities

---

## Support and Feedback

For questions, issues, or feedback on this agent group, please open an issue in the repository.

---

## License

MIT License - See repository root for full license text
