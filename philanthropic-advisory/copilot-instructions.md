# Philanthropic Advisory Agent Group

## Overview

A comprehensive agent group providing systematic, data-driven analysis of philanthropic initiatives focused on uplifting at-risk communities in Singapore - specifically families facing crises beyond their control and children from lower-income backgrounds.

This group applies established impact frameworks (SROI, CEA), evaluates long-term trajectory uplift, assesses risks, and ensures portfolio coherence to inform evidence-based funding decisions.

## The Five Agents

### 1. impact-evaluator
**Role**: Assess quantitative outcomes and systems change potential  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You have a program proposal and need to understand social return on investment, cost-effectiveness, and systems change potential

**Capabilities**:
- SROI (Social Return on Investment) calculation
- CEA (Cost-Effectiveness Analysis)
- Systems change assessment (upstream vs. downstream)
- Evidence quality rating
- Comparison to benchmarks

**Outputs**: SROI ratio, cost per outcome, systems change rating, evidence assessment

---

### 2. trajectory-analyzer
**Role**: Evaluate long-term beneficiary trajectory uplift  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need to understand whether a program creates sustained upward mobility or temporary stabilization

**Capabilities**:
- Baseline trajectory assessment (without intervention)
- Intervention effect modeling over time horizons
- Trajectory uplift quantification
- Sustainability assessment
- Critical intervention point analysis

**Outputs**: Trajectory uplift rating, sustainability probability, long-term projection

---

### 3. risk-assessor
**Role**: Identify and evaluate program risks  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need comprehensive risk analysis before committing funding

**Capabilities**:
- Implementation risk assessment (organizational capacity, staffing, partnerships)
- Financial sustainability risk evaluation
- External risk identification (policy, economic, community)
- Reputational risk assessment
- Risk prioritization and mitigation strategies

**Outputs**: Risk register, risk ratings, mitigation recommendations

---

### 4. portfolio-strategist
**Role**: Ensure program alignment with mission and portfolio coherence  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need to understand how a program fits within your overall philanthropic portfolio

**Capabilities**:
- Mission alignment assessment
- Portfolio balance analysis (intervention types, populations, timelines)
- Synergy and complementarity identification
- Resource allocation recommendations
- Strategic prioritization

**Outputs**: Portfolio fit assessment, strategic recommendation, funding prioritization

---

### 5. devils-advocate
**Role**: Critical review and disagreement facilitation (MANDATORY FINAL GATE)  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: ALWAYS - after all other analyses complete, before final funding decision

**Capabilities**:
- Challenge optimistic assumptions in all analyses
- Identify blind spots and overlooked risks
- Surface disagreements between agents
- Document all perspectives with full reasoning
- Highlight human decision points

**Outputs**: Critical review report, assumption challenges, human decision framework

---

## Workflow

### Primary Workflow: Comprehensive Program Analysis

```
User Request (Program Analysis)
    ↓
@impact-evaluator
    ↓ (SROI, CEA, systems change)
@trajectory-analyzer
    ↓ (Long-term uplift assessment)
@risk-assessor
    ↓ (Risk evaluation)
@portfolio-strategist
     (Strategic fit and synthesis)
@devils-advocate
    ↓ (Critical review - MANDATORY)
User Decision
```

**When to use**: Complete analysis of a new program proposal before funding decision

---

### Alternative Workflow: Quick Risk Assessment

```
User → @risk-assessor → @devils-advocate → User
```

**When to use**: Existing program has new risk factors, need quick risk review

---

### Alternative Workflow: Portfolio Review Only

```
User → @portfolio-strategist → @devils-advocate → User
```

**When to use**: Review portfolio balance without analyzing specific new program

---

### Alternative Workflow: Comparative Analysis

```
User → @impact-evaluator (multiple programs) → @trajectory-analyzer → @portfolio-strategist → @devils-advocate → User
```

**When to use**: Compare 2-3 program options to determine which to fund

---

## Decision Tree: Which Agent Do I Use?

**START: What do you need?**

### [A] I have a program proposal and need funding recommendation
 **Use PRIMARY WORKFLOW** (all 5 agents in sequence)  
 Start with: @impact-evaluator

### [B] I need to understand social return and cost-effectiveness
 **Use @impact-evaluator** only  
 Then: Optionally continue to @trajectory-analyzer for long-term view

### [C] I need to know if a program creates long-term change
 **Use @trajectory-analyzer**  
 Prerequisite: Have impact analysis completed (or provide outcome data)

### [D] I need to assess risks before funding
 **Use @risk-assessor**  
 Then: ALWAYS consult @devils-advocate for critical review

### [E] I need to know how a program fits my portfolio
 **Use @portfolio-strategist**  
 Prerequisite: Provide current portfolio data  
 Then: ALWAYS consult @devils-advocate for critical review

### [F] I want to compare multiple program options
 **Use COMPARATIVE WORKFLOW**  
 Start with: @impact-evaluator for each program  
 Then: @trajectory-analyzer and @portfolio-strategist to compare  
 End with: @devils-advocate for critical review

### [G] I have analyses and need critical review
 **Use @devils-advocate**  
 Prerequisite: Have completed analyses from other agents  
 Purpose: Challenge assumptions, surface disagreements

---

## Quality Gates

### Gate 1: Impact Analysis Complete (impact-evaluator)
**Pass Criteria**:
- [ ] SROI calculation with clear assumptions
- [ ] CEA with precisely defined outcome unit
- [ ] Systems change level classified (upstream/midstream/downstream)
- [ ] Evidence quality rated (strong/moderate/weak)
- [ ] Benchmarks provided for comparison

### Gate 2: Trajectory Assessment Complete (trajectory-analyzer)
**Pass Criteria**:
- [ ] Baseline trajectory defined with time horizons
- [ ] Intervention effect modeled
- [ ] Trajectory uplift quantified
- [ ] Sustainability assessed with probability estimate
- [ ] Critical intervention point analyzed

### Gate 3: Risk Evaluation Complete (risk-assessor)
**Pass Criteria**:
- [ ] All risk categories covered (implementation, financial, external, reputational, exit)
- [ ] Risks prioritized by likelihood × impact
- [ ] Mitigation strategies provided with feasibility assessment
- [ ] Organizational risk management capacity evaluated
- [ ] Risk monitoring framework recommended

### Gate 4: Portfolio Strategy Complete (portfolio-strategist)
**Pass Criteria**:
- [ ] Mission alignment assessed
- [ ] Portfolio balance analyzed
- [ ] Strategic fit determined (fills gap/complements/overlaps)
- [ ] Resource allocation evaluated
- [ ] Funding recommendation with strategic rationale

### Gate 5: Critical Review Complete (devils-advocate) - MANDATORY
**Pass Criteria**:
- [ ] All agent analyses critiqued
- [ ] Optimistic assumptions challenged
- [ ] Disagreements between agents surfaced
- [ ] Blind spots identified
- [ ] Human decision points documented
- [ ] All perspectives captured with full reasoning

---

## Metrics Frameworks

### SROI (Social Return on Investment)
**Formula**: SROI = (Total Social Value Created - Investment) / Investment

**Methodology**:
1. Map all stakeholder outcomes
2. Assign financial proxies to outcomes
3. Calculate total social value over program lifetime
4. Account for attribution and deadweight
5. Express as ratio (e.g., $4 social value per $1 invested)

**Interpretation**:
- $0-$1.99: Below funding threshold (social value less than investment)
- $2.00-$3.99: Reasonable return (typical for many interventions)
- $4.00-$6.00: Strong return (evidence-based, well-implemented programs)
- $6.00+: Exceptional return (rare, typically prevention or high-leverage interventions)

**Agent Responsible**: impact-evaluator

**Singapore Context**: Use Singapore cost data for financial proxies (healthcare, housing, education costs). High cost of living affects valuations.

---

### CEA (Cost-Effectiveness Analysis)
**Formula**: CEA = Total Program Cost / Number of Outcomes Achieved

**Methodology**:
1. Define outcome unit precisely (e.g., "child completing program with 80%+ attendance and 0.3+ SD gain")
2. Calculate full program cost (direct + indirect + overhead)
3. Project number of outcome units achieved
4. Calculate cost per outcome
5. Compare to similar programs

**Interpretation**: Context-dependent. Compare to:
- Similar programs in Singapore
- Alternative interventions for same population
- Portfolio average cost per beneficiary

**Agent Responsible**: impact-evaluator

---

### Trajectory Uplift Assessment
**Framework**: Baseline Trajectory → Intervention → Projected Trajectory → Uplift Calculation

**Methodology**:
1. Establish baseline trajectory (without intervention)
2. Model intervention effects over time
3. Project outcome trajectory (with intervention)
4. Calculate trajectory uplift (difference between baseline and projected)
5. Assess sustainability (will uplift persist post-intervention?)

**Trajectory Types**:
- **Stabilization**: Prevents decline, maintains status quo
- **Incremental Uplift**: Modest sustained improvement
- **Transformational**: Significant life path change

**Agent Responsible**: trajectory-analyzer

---

## Target Domain: At-Risk Communities in Singapore

### Families Facing Crises
- Medical emergencies (serious illness, disability)
- Job loss or sudden income reduction
- Housing instability
- Caregiving burdens
- Domestic issues

### Children from Lower-Income Families
- Educational disadvantage
- Food insecurity
- Limited enrichment opportunities
- Intergenerational poverty risk
- Mental health challenges

### Singapore-Specific Context
- High cost of living (housing, healthcare, education)
- Meritocratic system with high educational pressure
- Strong family support culture
- Government social services exist but gaps remain
- Emphasis on self-reliance and prevention of welfare dependency

---

## Examples

### Example 1: New Program Evaluation (Family Crisis Intervention)

**User Request**: "Analyze this program: Emergency funds ($2K) + 12-month case management for 50 families facing medical crises. Budget: $100K."

**Workflow**:

1. **@impact-evaluator**: 
   - SROI: $3.20 per $1 invested
   - CEA: $5,000 per family stabilized
   - Systems change: Low (downstream crisis intervention)
   - Evidence: Moderate (pre-post design, no control group)

2. **@trajectory-analyzer**:
   - Baseline: Declining trajectory (crisis triggering downward spiral)
   - Uplift: Moderate-High (prevents decline, 45pp improvement in stability)
   - Sustainability: 70% (moderate, vulnerable to repeat crises)
   - Critical timing: Yes (crisis moment optimal for intervention)

3. **@risk-assessor**:
   - Overall risk: Medium
   - Critical risks: Beneficiary selection bias, case management quality, dependency
   - Mitigation: Feasible (transparent criteria, training, autonomy focus)
   - Organizational capacity: Strong

4. **@portfolio-strategist**:
   - Mission alignment: Strong (core to at-risk families mission)
   - Portfolio fit: Fills critical gap (zero crisis intervention before this)
   - Strategic priority: High (rebalances education-heavy portfolio)
   - Recommendation: Fund (strategic necessity)

5. **@devils-advocate**:
   - Challenge SROI: 70% attribution may be optimistic, actual SROI likely $2.10-$4.80 range
   - Challenge trajectory: 70% sustainability assumes behavior change persists, may regress if repeat crisis
   - Challenge synergies: Families may choose crisis support OR education programs, not both (time/energy constraints)
   - Overlooked risks: Beneficiary expectations (expecting ongoing grants post-program), community trust if program ends abruptly
   - Disagreements: Impact evaluator assumes sustained outcomes (2 years), trajectory analyst highlights 30% regression risk
   - Human decision: Is 70% sustainability acceptable, or require 80%+?

**User Decision**: Fund with conditions (transparent selection criteria, 24-month follow-up evaluation, synergy tracking with education programs)

---

### Example 2: Portfolio Review

**User Request**: "I've funded 5 programs over the past year. Are they working well together?"

**Workflow**:

1. **@portfolio-strategist**:
   - Portfolio balance: 71% education-focused (4/5 programs), 11% financial literacy, 0% crisis intervention
   - Gap identified: Heavy concentration in children's education, minimal family-level support
   - Overlap: Two tutoring programs (P1-3 and P3-6) may have redundant admin overhead
   - Synergies: Financial literacy complements education (parents manage resources for children's enrichment)
   - Recommendation: Consolidate tutoring programs, prioritize family crisis intervention in next cycle

2. **@devils-advocate**:
   - Challenge concentration: Education focus assumes baseline family stability - if families in crisis, education programs underperform
   - Question overlap claim: Two tutoring programs serve different age groups (P1-3 vs. P3-6), may not be redundant
   - Blind spot: No analysis of beneficiary demographics (racial/ethnic diversity, language access, geography)
   - Alternative view: Education concentration may be intentional (funder's theory of change prioritizes education for intergenerational mobility)
   - Human decision: Is education concentration strategic, or symptom of mission drift?

**User Decision**: Maintain two tutoring programs (serve different needs), prioritize family crisis intervention as Year 2 priority, conduct portfolio equity audit

---

### Example 3: Comparative Analysis (Two Program Options)

**User Request**: "Compare: (A) After-school tutoring for 100 kids @ $50K, (B) Parent financial literacy for 30 families @ $50K. Which should I fund?"

**Workflow**:

1. **@impact-evaluator** (for both):
   - **Option A**: SROI $4.10, CEA $500 per child, systems change Low-Medium
   - **Option B**: SROI $6.00, CEA $1,667 per family, systems change Medium

2. **@trajectory-analyzer** (for both):
   - **Option A**: Moderate uplift for children (education trajectory), limited parent trajectory change
   - **Option B**: High uplift for entire family unit (economic trajectory), systemic change potential

3. **@portfolio-strategist**:
   - **Option A**: Adds to existing education concentration (4th education program)
   - **Option B**: Fills family-level intervention gap, complements children's programs
   - Recommendation: Option B (portfolio needs family-level programs)

4. **@devils-advocate**:
   - Challenge: Option A has stronger evidence base (tutoring well-studied), Option B benefits harder to measure (behavior change)
   - Question portfolio strategy: Is portfolio balance more important than evidence strength?
   - Overlooked: Option A serves 100 beneficiaries vs. 30 for Option B - reach matters
   - Human decision: Portfolio coherence vs. evidence strength vs. beneficiary reach?

**User Decision**: Fund Option B (aligns with portfolio strategy, request robust evaluation plan to address evidence concerns)

---

## Troubleshooting

### Issue: SROI seems too high (e.g., $10 per $1)
**Check**:
- Are financial proxies realistic? (not inflated)
- Is attribution reasonable? (program actually caused outcomes)
- Is deadweight accounted for? (outcomes that would occur anyway)
- Is time horizon too long? (discounting applied correctly)

**Solution**: Request @devils-advocate review of SROI assumptions

---

### Issue: Trajectory analysis conflicts with impact analysis
**Example**: Impact says high SROI, trajectory says low sustainability

**Check**:
- Does SROI assume sustained outcomes that trajectory analyst questions?
- Are time horizons aligned? (SROI over 2 years, trajectory over 5 years)

**Solution**: Request @devils-advocate to resolve disagreement

---

### Issue: Portfolio strategist recommends funding but risk assessor says high risk
**Check**:
- Is strategic priority worth accepting high risk?
- Does funder have risk tolerance for this level?
- Can risks be mitigated to reduce to medium/low?

**Solution**: Request @devils-advocate to clarify risk-benefit trade-off

---

### Issue: Too many agents, analysis takes too long
**Shortcut**:
- For quick decisions: Use @impact-evaluator + @devils-advocate only (skip trajectory, risk, portfolio)
- For low-stakes decisions: Use @impact-evaluator only
- For portfolio review without new program: Use @portfolio-strategist + @devils-advocate

**Caution**: Skipping agents increases decision risk. Use full workflow for major funding decisions.

---

## Integration Instructions

### For Funders (How to Use This Group)

1. **Provide Clear Program Description**: Include target population, budget, intervention model, proposed outcomes
2. **Provide Portfolio Context**: Share existing funded programs for strategic fit assessment
3. **State Risk Tolerance**: Clarify acceptable risk level (low/medium/high)
4. **Specify Decision Timeline**: Urgent decisions may use abbreviated workflow
5. **Engage with Analysis**: Don't just read recommendation, engage with assumptions and trade-offs
6. **Make Values-Explicit Decisions**: When analysis points to decision points, state which values guide choice

### For Program Implementers (How to Prepare Proposals)

To maximize quality of analysis, provide:
- Detailed budget with cost breakdown
- Theory of change (how activities lead to outcomes)
- Evidence base (prior program results, research supporting model)
- Evaluation plan (how you'll measure outcomes)
- Organizational profile (track record, capacity, governance)
- Stakeholder map (beneficiaries, partners, funders, government)

### For Evaluators (How to Strengthen Evidence)

Analyses are only as good as underlying data. Strengthen by:
- Including comparison groups (matched or randomized)
- Extending follow-up periods (12+ months post-program)
- Using validated measurement tools (not just self-report)
- Documenting assumptions explicitly
- Conducting sensitivity analyses
- Tracking attribution factors (what else affects outcomes)

---

## Version History

- **1.0.0** (Initial): Comprehensive philanthropic advisory group with 5 agents (impact-evaluator, trajectory-analyzer, risk-assessor, portfolio-strategist, devils-advocate) for evidence-based funding decisions supporting at-risk families and children in Singapore
