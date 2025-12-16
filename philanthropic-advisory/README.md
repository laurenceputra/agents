# Philanthropic Advisory Agent Group

**Version**: 1.0.0  
**Purpose**: Evidence-based philanthropic decision-making for programs supporting at-risk families and children in Singapore

---

## Quick Start

### Step 1: Request Program Analysis
```
@impact-evaluator

I'd like to analyze this program:
- Target: 50 families facing medical crises in Singapore
- Budget: $100,000 (Year 1)
- Intervention: Emergency financial grants ($2K) + 12-month case management
- Outcomes: Crisis stabilization, housing stability, reduced healthcare costs
- Organization: [Name], 10-year track record, $2M annual budget
```

### Step 2: Get Long-Term Trajectory Assessment
```
@trajectory-analyzer

Based on the impact analysis above, evaluate long-term trajectory uplift potential for these families.
```

### Step 3: Assess Risks
```
@risk-assessor

Assess implementation, financial, external, and reputational risks for this program.
```

### Step 4: Evaluate Portfolio Fit
```
@portfolio-strategist

Here's my current portfolio:
- Program A: After-school tutoring, $50K, 100 children
- Program B: Youth mentorship, $60K, 40 youth
- Program C: Financial literacy, $30K, 30 families

How does this crisis intervention program fit?
```

### Step 5: Get Critical Review (MANDATORY)
```
@devils-advocate

Please critically review all analyses above and identify assumptions, blind spots, and disagreements.
```

### Step 6: Make Informed Decision
Review all analyses, consider trade-offs, make values-explicit decision.

---

## The Five Agents

| Agent | Purpose | Use When |
|-------|---------|----------|
| **impact-evaluator** | SROI and CEA analysis | You need quantitative impact assessment |
| **trajectory-analyzer** | Long-term uplift evaluation | You need to understand sustained behavior change |
| **risk-assessor** | Comprehensive risk analysis | You need to identify and mitigate risks |
| **portfolio-strategist** | Portfolio fit and coherence | You need to see how program fits portfolio |
| **devils-advocate** | Critical review (MANDATORY) | ALWAYS - final gate before decision |

---

## Usage Examples

### Example 1: "Should I fund this crisis intervention program?"

**Request Full Analysis**:
```
@impact-evaluator [provide program details]
 @trajectory-analyzer
 @risk-assessor
 @portfolio-strategist [provide portfolio data]
 @devils-advocate
```

**Result**: Comprehensive analysis with SROI ($3.20), trajectory uplift (moderate-high), risks (medium), portfolio fit (fills critical gap), critical review (challenges 70% attribution assumption).

**Decision**: Fund with conditions (transparent selection criteria, 24-month follow-up evaluation).

---

### Example 2: "Compare two program options"

**Request Comparative Analysis**:
```
@impact-evaluator

Option A: After-school tutoring for 100 kids @ $50K
Option B: Parent financial literacy for 30 families @ $50K

Calculate SROI and CEA for both.
```

**Then**:
```
@portfolio-strategist

Which option better fits my portfolio? [provide portfolio context]
```

**Result**: Option A has lower CEA ($500 per child) but adds to education concentration. Option B has higher SROI ($6.00) and fills family-level gap.

**Decision**: Fund Option B (portfolio needs family programs).

---

### Example 3: "Is my portfolio balanced?"

**Request Portfolio Review**:
```
@portfolio-strategist

Review my portfolio:
1. After-school tutoring A: $50K, 100 children
2. After-school tutoring B: $40K, 80 children
3. Youth mentorship: $60K, 40 youth
4. Financial literacy: $30K, 30 families

Any gaps? Overlaps? Strategic recommendations?
```

**Then**:
```
@devils-advocate

Challenge the portfolio strategy recommendations.
```

**Result**: Portfolio is 71% education-focused (concentration risk), zero crisis intervention (gap), two tutoring programs may overlap.

**Decision**: Maintain separate tutoring programs (different age groups), prioritize crisis intervention in next funding cycle.

---

## Metrics Guide

### SROI (Social Return on Investment)
**What it measures**: Social value created per dollar invested

**Formula**: (Total Social Value - Investment) / Investment

**Example**: $3.20 SROI = $3.20 in social value for every $1 invested

**Interpretation**:
- Below $2.00: Below funding threshold
- $2.00-$3.99: Reasonable return
- $4.00-$6.00: Strong return
- $6.00+: Exceptional return

**Used by**: impact-evaluator

---

### CEA (Cost-Effectiveness Analysis)
**What it measures**: Cost per outcome unit

**Formula**: Total Program Cost / Outcomes Achieved

**Example**: $500 per child completing program

**Interpretation**: Compare to similar programs or portfolio average. Lower is more cost-effective for same outcome.

**Used by**: impact-evaluator

---

### Trajectory Uplift
**What it measures**: Difference between baseline trajectory (without intervention) and projected trajectory (with intervention)

**Types**:
- **Stabilization**: Prevents decline (e.g., family avoids homelessness)
- **Incremental Uplift**: Modest improvement (e.g., child gains 0.3 SD in test scores)
- **Transformational**: Significant change (e.g., family breaks intergenerational poverty)

**Sustainability**: Probability that uplift persists post-program (70% = 70 of 100 families sustain gains)

**Used by**: trajectory-analyzer

---

## Geographic Scope: Singapore

This agent group is specifically designed for philanthropic programs in **Singapore only**, targeting:

### At-Risk Families
- Families facing medical crises (serious illness, disability, unexpected costs)
- Job loss or sudden income reduction
- Housing instability
- Caregiving burdens (elderly parents, special needs children)
- Domestic issues

### Children from Lower-Income Backgrounds
- Educational disadvantage (lack of enrichment, tutoring)
- Food insecurity
- Limited extracurricular opportunities
- Intergenerational poverty risk
- Mental health challenges

### Singapore-Specific Context
- High cost of living (affects financial proxy valuations)
- Meritocratic education system (education trajectory heavily influences lifetime outcomes)
- Strong family culture (family-level interventions prioritized)
- Government social services exist but gaps remain (programs should complement, not duplicate)
- Cultural emphasis on self-reliance (programs must avoid creating dependency)

---

## Integration Instructions

### Before Using This Agent Group

**Prepare**:
1. **Program Description**: Detailed intervention model, target population, budget
2. **Expected Outcomes**: Specific, measurable outcomes with baselines and targets
3. **Evidence Base**: Prior program results, research supporting approach
4. **Organizational Context**: Implementing organization's track record and capacity
5. **Portfolio Data**: Existing funded programs (for portfolio-strategist)

---

### After Receiving Analyses

**Next Steps**:
1. **Review All Analyses**: Don't skip to recommendation - understand reasoning
2. **Identify Trade-Offs**: Where do agents disagree? What are decision points?
3. **Apply Your Values**: When analyses point to choices, state which values guide decision
4. **Set Conditions**: If funding, specify conditions for risk mitigation
5. **Monitor Assumptions**: Track key assumptions (attribution, sustainability) during implementation

---

## Troubleshooting

### Q: Analyses take too long. Can I skip agents?
**A**: For major funding decisions, use full 5-agent workflow. For quick decisions, minimum is impact-evaluator + devils-advocate. Risk increases with fewer agents.

### Q: Agents disagree (e.g., impact says high return, risk assessor says high risk). What do I do?
**A**: Request @devils-advocate to synthesize disagreement and clarify trade-offs. Then make values-based decision (is high return worth high risk?).

### Q: SROI seems inflated. How do I validate?
**A**: @devils-advocate will challenge assumptions. Also: Check financial proxies (realistic?), attribution (program actually caused outcomes?), benchmarks (compare to similar programs).

### Q: I only care about cost-effectiveness, not long-term trajectory. Do I still need trajectory-analyzer?
**A**: Trajectory analysis reveals sustainability. If families regress post-program, short-term cost-effectiveness is misleading. Recommend including trajectory-analyzer.

### Q: Can I use this for programs outside Singapore?
**A**: Not without adaptation. Financial proxies, benchmarks, and cultural context are Singapore-specific. For other geographies, adjust cost data and cultural considerations.

### Q: Do I always need devils-advocate?
**A**: YES. Devil's advocate is mandatory final gate. It challenges assumptions, surfaces disagreements, and ensures you have full picture before deciding. Never skip.

---

## Limitations

### What This Agent Group Does NOT Do
- **Does not implement or execute programs** (advisory only)
- **Does not provide fundraising strategy** (focused on funding decisions, not donor cultivation)
- **Does not provide legal or tax advice** (consult professionals for compliance)
- **Does not select individual beneficiaries** (organizational responsibility)
- **Does not provide real-time monitoring dashboards** (pre-funding analysis focus)

### What to Consult Externally
- **Legal compliance**: Charity regulations, PDPA compliance (Singapore)
- **Tax optimization**: Consult tax professionals
- **Beneficiary safeguarding**: Child protection, vulnerable adult protocols
- **Financial management**: Audit, accounting, financial controls
- **Program implementation**: Technical assistance from sector experts

---

## Frequently Asked Questions

### Q: What's the difference between SROI and CEA?
**A**: SROI monetizes social value created per dollar invested (ratio). CEA calculates cost per outcome unit (dollar amount). SROI compares across programs with different outcomes. CEA compares programs with same outcome type.

### Q: What does "systems change potential" mean?
**A**: 
- **Downstream**: Direct services addressing symptoms (e.g., emergency funds for families in crisis)
- **Midstream**: Capacity building addressing immediate causes (e.g., job training)
- **Upstream**: Policy or systems changes addressing root causes (e.g., healthcare affordability advocacy)

### Q: How do I know if 70% sustainability is good?
**A**: Context-dependent. For crisis intervention, 70% is reasonable (some families face repeat crises). For capacity-building programs (education, job training), expect 80%+ sustainability. Compare to similar programs.

### Q: Can I fund programs with Medium or High risk?
**A**: Yes, if strategic value justifies risk. Portfolio balance matters - some high-risk/high-impact programs balanced with lower-risk proven programs. Risk tolerance is funder-specific.

### Q: What if beneficiaries disagree with the analysis?
**A**: Analyses are provider/funder perspective. Include beneficiary voice through participatory design, focus groups, or feedback loops. devils-advocate often flags missing beneficiary perspective.

---

## Contact & Support

This agent group is designed for self-service philanthropic analysis. For best results:

1. Provide detailed program information (the more context, the better the analysis)
2. Use full 5-agent workflow for major decisions ($50K+)
3. Engage critically with analyses (don't just read recommendation, understand trade-offs)
4. Make values-explicit decisions when analyses point to choice points
5. Monitor key assumptions during program implementation

---

## Version History

- **1.0.0** (Initial): Comprehensive philanthropic advisory group with 5 coordinated agents for evidence-based funding decisions supporting at-risk families and children in Singapore

---

**Ready to start?** Consult @impact-evaluator with your first program proposal.
