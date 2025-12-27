# Philanthropic Advisory Agent Group

## Overview

Comprehensive philanthropic advisory services for Singapore-focused giving, with emphasis on quantitative impact analysis (SROI, CEA, trajectory uplift), strategic portfolio alignment, and risk-opportunity assessment. This agent group helps philanthropists make data-driven funding decisions for initiatives targeting at-risk communities (families in crisis, children from lower-income families) with measurable systemic impact potential.

## Version

**Version 1.2.0** — Added Marketing Content Writer agent for creating marketing writeups aligned with principles

## The Seven Agents

### principles-framework-definer (OPTIONAL - Foundation)
**Role**: Define philanthropic principles and decision framework before evaluating programs  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You want to establish clear giving criteria, values, and decision thresholds before evaluating specific programs  
**Handoffs to**: impact-evaluator (with framework criteria), devils-advocate (framework challenge)

### impact-evaluator
**Role**: Quantitative impact evaluation using SROI, CEA, and trajectory uplift frameworks  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You have a program to evaluate and need quantitative impact analysis  
**Handoffs to**: portfolio-strategist (strategic fit assessment), devils-advocate (methodology review)

### portfolio-strategist
**Role**: Assess program fit with philanthropic strategy and portfolio composition  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need to understand how a program fits your overall giving strategy  
**Handoffs to**: risk-opportunity-analyst (risk assessment), devils-advocate (strategic assumptions review)

### risk-opportunity-analyst
**Role**: Identify risks and opportunities for funding decisions  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You want to understand what could go wrong (or right) with a funding decision  
**Handoffs to**: recommendation-synthesizer (integrated recommendation), devils-advocate (risk assumptions review)

### recommendation-synthesizer
**Role**: Integrate analyses into actionable funding recommendations  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You have completed impact, portfolio, and risk analyses and need a final recommendation  
**Handoffs to**: devils-advocate (MANDATORY critical review before decision)

### devils-advocate
**Role**: Critical review and assumption challenging (MANDATORY final quality gate)  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: ALWAYS — before any funding decision, devils-advocate must review all analyses  
**Handoffs to**: Any agent (for revision) or decision-maker (if approved)

### marketing-content-writer (OPTIONAL - Communication)
**Role**: Create marketing content and writeups for philanthropic programs aligned with principles  
**Model**: Claude Haiku 4.5 (copilot)  
**When to use**: You need marketing content, website copy, or social media posts for programs  
**Handoffs to**: devils-advocate (content review), principles-framework-definer (clarification)

## Workflow

### Option 1: Start with Framework Definition (Recommended for New Philanthropists)

```
Philanthropist Needs Clarity on Giving Principles
    ↓
@principles-framework-definer
(Facilitate 8 foundational question areas: values, beneficiaries, theory of change, criteria)
    ↓
Comprehensive Framework Document Produced
(SROI thresholds, risk tolerance, portfolio strategy, decision criteria)
    ↓
Program Proposal Submitted
    ↓
@impact-evaluator (uses framework criteria)
(Quantitative analysis: SROI, CEA, trajectory uplift against defined thresholds)
    ↓
@portfolio-strategist
(Strategic fit assessed against explicit framework)
    ↓
@risk-opportunity-analyst
(Risk assessment using framework risk tolerance)
    ↓
@recommendation-synthesizer
(Recommendation aligned with framework criteria)
    ↓
@devils-advocate (MANDATORY QUALITY GATE)
(Challenge framework + analysis assumptions, surface disagreements)
    ↓
    ├─ APPROVED → Decision-maker (funding decision)
    ├─ Framework issues → @principles-framework-definer (refine framework)
    ├─ Methodology issues → @impact-evaluator (revise calculations)
    ├─ Strategy issues → @portfolio-strategist (reassess fit)
    ├─ Risk issues → @risk-opportunity-analyst (deeper analysis)
    └─ Synthesis issues → @recommendation-synthesizer (adjust recommendation)
```

### Option 2: Direct Program Evaluation (When Framework Already Clear)

```
Program Proposal Submitted
    ↓
@impact-evaluator
(Quantitative analysis: SROI, CEA, trajectory uplift)
    ↓
@portfolio-strategist
(Strategic fit and portfolio alignment)
    ↓
@risk-opportunity-analyst
(Risk/opportunity assessment)
    ↓
@recommendation-synthesizer
(Integrated funding recommendation)
    ↓
@devils-advocate (MANDATORY QUALITY GATE)
(Challenge assumptions, surface disagreements, identify blind spots)
    ↓
    ├─ APPROVED → Decision-maker (funding decision)
    ├─ Methodology issues → @impact-evaluator (revise calculations)
    ├─ Strategy issues → @portfolio-strategist (reassess fit)
    ├─ Risk issues → @risk-opportunity-analyst (deeper analysis)
    └─ Synthesis issues → @recommendation-synthesizer (adjust recommendation)
```

## Send Default Policy

### Overview

This agent group uses a **hybrid auto-send policy** designed for high-stakes philanthropic decisions involving potentially millions of dollars and multi-year commitments.

**Core Principle**: Workflow advances require human confirmation (`send: false`), but critical reviews and feedback loops auto-send (`send: true`) for iterative improvement efficiency.

### Policy Rules

#### Primary Workflow Transitions: `send: false` (Human Confirmation Required)

**Rationale**: Each analytical stage (impact → portfolio → risk → synthesis) represents a critical decision checkpoint where philanthropists should review findings before proceeding.

**Affected Handoffs**:
- `principles-framework-definer → impact-evaluator` (send: false)
- `impact-evaluator → portfolio-strategist` (send: false)
- `portfolio-strategist → risk-opportunity-analyst` (send: false)
- `risk-opportunity-analyst → recommendation-synthesizer` (send: false)

**Why Manual Confirmation**:
- High-stakes decisions: Funding amounts typically $100k-$1M+ per program
- Multi-year commitments: Programs often 3-5 year commitments
- Irreversible impact: Funding decisions affect beneficiaries' lives
- Strategic implications: Portfolio composition affects long-term giving strategy
- Human judgment needed: Quantitative metrics don't capture full context

**User Experience**: After each agent completes analysis, user reviews output and explicitly confirms to proceed to next stage. This creates natural checkpoints for reflection.

#### Critical Reviews: `send: true` (Auto-Send)

**Rationale**: Critical review by devils-advocate is **mandatory**, not optional. Auto-sending ensures quality gate is never skipped while reducing friction in iterative feedback loops.

**Affected Handoffs**:
- `recommendation-synthesizer → devils-advocate` (send: true, mandatory)
- `marketing-content-writer → devils-advocate` (send: true, mandatory)

**Why Auto-Send**:
- **Mandatory gate**: Devils-advocate review is non-negotiable for all funding recommendations and marketing content
- **No decision bypass**: Prevents users from accidentally making decisions without critical review
- **Quality enforcement**: Ensures assumptions challenged, disagreements surfaced, blind spots identified

#### Feedback Loops: `send: true` (Auto-Send)

**Rationale**: When devils-advocate identifies issues requiring revision, the feedback loop should be frictionless to enable rapid iteration.

**Affected Handoffs** (all devils-advocate feedback routes):
- `devils-advocate → impact-evaluator` (send: true)
- `devils-advocate → portfolio-strategist` (send: true)
- `devils-advocate → risk-opportunity-analyst` (send: true)
- `devils-advocate → recommendation-synthesizer` (send: true)
- `devils-advocate → principles-framework-definer` (send: true)
- `devils-advocate → marketing-content-writer` (send: true)

**Why Auto-Send**:
- **Iterative improvement**: Revisions are collaborative, not adversarial
- **Efficiency**: No value in manual confirmation for "fix this and return" loops
- **Clear context**: Devils-advocate provides specific feedback, agent acts on it

#### Optional/Clarification Paths: `send: true` (Auto-Send)

**Rationale**: When agents need clarification or additional information from supporting agents, auto-send reduces friction.

**Affected Handoffs**:
- `principles-framework-definer → devils-advocate` (send: true, framework review)
- `impact-evaluator → devils-advocate` (send: true, methodology review)
- `portfolio-strategist → devils-advocate` (send: true, strategic assumptions review)
- `risk-opportunity-analyst → devils-advocate` (send: true, risk assumptions review)
- `marketing-content-writer → principles-framework-definer` (send: true, clarification)

**Why Auto-Send**:
- **Supporting workflows**: These are auxiliary paths for quality improvement, not primary decision points
- **Low risk**: Clarification requests don't commit resources, just improve analysis
- **User retains control**: Primary workflow still has manual checkpoints

### Policy Rationale Summary

| Transition Type | Send Policy | Rationale |
|---|---|---|
| Workflow advance (impact → portfolio → risk → synthesis) | `send: false` | High-stakes checkpoints, human judgment needed |
| Mandatory critical review (→ devils-advocate) | `send: true` | Quality gate enforcement, prevent bypass |
| Feedback loops (devils-advocate → agents) | `send: true` | Iterative efficiency, clear revision context |
| Clarification/support (auxiliary paths) | `send: true` | Low-risk, supporting workflows |

### Testing and Observability

**How to Test**:
1. Run full workflow: principles → impact → portfolio → risk → synthesis → devils-advocate
2. Verify user is prompted for confirmation at each primary workflow transition
3. Verify auto-send to devils-advocate after recommendation-synthesizer completes
4. Verify feedback loops auto-send without manual confirmation

**Success Metrics**:
- User reports feeling in control of workflow progression (manual checkpoints valued)
- Devils-advocate review never skipped (100% compliance on funding recommendations)
- Feedback iteration cycles complete within 1-2 days (not delayed by manual confirmations)

**Rollback Strategy**:
If policy proves problematic:
- Change all primary workflow handoffs to `send: true` if users want full automation
- Change devils-advocate handoffs to `send: false` if users want manual review trigger
- No code changes needed, only frontmatter `send:` values in agent files

### Migration Notes

**Version 1.2.0**: Policy formalized and documented (policy existed in agent files but was undocumented)

**No Breaking Changes**: Agent behavior unchanged, only documentation added to explain existing pattern.

## Quality Gates

### Gate 1: Impact Evaluation Complete
**Owner**: impact-evaluator  
**Criteria**:
- [ ] SROI calculated with methodology and assumptions documented
- [ ] CEA analyzed with benchmark comparison
- [ ] Trajectory uplift assessed (baseline vs intervention)
- [ ] Systemic impact scored (upstream/midstream/downstream)
- [ ] Data quality rated with measurement gaps identified
- [ ] Red flags surfaced proactively

**Pass**: Impact metrics calculated, data quality assessed → Ready for portfolio fit analysis

---

### Gate 2: Portfolio Fit Assessed
**Owner**: portfolio-strategist  
**Criteria**:
- [ ] Mission alignment scored with rationale
- [ ] Portfolio diversification impact analyzed
- [ ] Strategic gaps identified and prioritized
- [ ] Synergies with existing programs mapped
- [ ] Scalability potential evaluated
- [ ] Concentration risks assessed

**Pass**: Strategic fit evaluated, gaps/synergies identified → Ready for risk assessment

---

### Gate 3: Risk Assessment Complete
**Owner**: risk-opportunity-analyst  
**Criteria**:
- [ ] Risk matrix completed (implementation, financial, impact, external, organizational risks)
- [ ] Mitigation strategies specified for top risks
- [ ] Upside opportunities identified
- [ ] Scenario analysis conducted (pessimistic/realistic/optimistic)
- [ ] Exit/pivot strategies documented

**Pass**: Risks assessed, mitigation strategies proposed → Ready for synthesis

---

### Gate 4: Recommendation Synthesized
**Owner**: recommendation-synthesizer  
**Criteria**:
- [ ] Clear recommendation (fund/decline/modify/pilot) with confidence level
- [ ] Decision rationale integrates impact + portfolio + risk analyses
- [ ] Trade-offs transparently presented
- [ ] Funding terms specified (amount, duration, conditions)
- [ ] Monitoring framework and exit strategy included

**Pass**: Integrated recommendation complete → MANDATORY handoff to devils-advocate

---

### Gate 5: Critical Review Complete (MANDATORY — FINAL QUALITY GATE)
**Owner**: devils-advocate  
**Criteria**:
- [ ] SROI/CEA assumptions challenged
- [ ] Strategic fit claims questioned
- [ ] Risk assessments tested for optimism/pessimism
- [ ] Disagreements between agents surfaced and documented
- [ ] Blind spots identified
- [ ] Alternative interpretations provided
- [ ] Questions for decision-maker prepared
- [ ] Approval status clear (approved/needs revision/needs more data)

**Pass**: All perspectives documented, disagreements captured → Ready for human decision

**CRITICAL**: No funding recommendation reaches decision-maker without devils-advocate review. This is non-negotiable quality gate.

## Decision Tree: Which Agent Do I Consult?

### Start Here: What Do You Need?

**[0] I don't have clear giving principles or decision criteria yet**  
 Start with @principles-framework-definer (RECOMMENDED FIRST STEP)  
 Provides: Framework document with values, beneficiaries, theory of change, SROI thresholds, decision criteria  
 Next: Use framework to evaluate programs with @impact-evaluator OR challenge framework with @devils-advocate  
 Duration: ~30-60 minutes for framework definition

**[A] I have a program to evaluate (no analysis yet)**  
 Start with @impact-evaluator  
 Provides: SROI, CEA, trajectory uplift, data quality assessment  
 Next: Automatically hands off to @portfolio-strategist

**[B] I know the impact metrics, need to assess portfolio fit**  
 Consult @portfolio-strategist  
 Provides: Mission alignment, gaps filled, synergies, diversification impact  
 Next: Automatically hands off to @risk-opportunity-analyst

**[C] I understand impact and fit, need to assess risks**  
 Consult @risk-opportunity-analyst  
 Provides: Risk matrix, mitigation strategies, opportunities, scenarios  
 Next: Automatically hands off to @recommendation-synthesizer

**[D] I need an integrated funding recommendation**  
 Consult @recommendation-synthesizer  
 Provides: Fund/decline decision, conditions, monitoring framework  
 Next: MANDATORY handoff to @devils-advocate

**[E] I have a recommendation, ready to decide**  
 **WAIT** — Do NOT decide yet  
 MUST consult @devils-advocate first (mandatory quality gate)  
 Provides: Assumption challenges, disagreements, blind spots, questions for you  
 Next: Make informed decision with full picture

**[F] I want to run full workflow from start to finish (with framework)**  
 1. Start with @principles-framework-definer to establish criteria (30-60 min)  
 2. Submit program to @impact-evaluator with framework criteria  
 3. Workflow runs automatically: impact → portfolio → risk → synthesis → devils-advocate → decision  
 Duration: ~1-2 days for comprehensive analysis after framework established

**[G] I want to run full workflow from start to finish (no framework)**  
 Submit program to @impact-evaluator  
 Workflow runs automatically: impact → portfolio → risk → synthesis → devils-advocate → decision  
 Duration: ~1-2 days for comprehensive analysis

**[H] I need marketing content for a program (website, social media, writeups)**  
 Consult @marketing-content-writer  
 Provides: Marketing copy, social media posts, program descriptions aligned with principles  
 Next: MANDATORY handoff to @devils-advocate for content review  
 Duration: ~2-4 hours for content creation and review

## Singapore Context

### Demographics
- **Population**: 5.7M total, ~50,000 at-risk youth, ~50,000 families needing support
- **At-Risk Children**: 20% of children from lower-income households (<$3,000/month household income)
- **Family Crisis**: 10,000+ families receiving MSF crisis support annually

### Key Policies
- **MSF Programs**: ComCare (financial assistance), KidSTART (early childhood), Family Service Centers
- **MOE Programs**: School-based support, remedial classes, financial aid
- **MOM Programs**: Progressive Wage Model, SkillsFuture (workforce development)

### Existing Landscape
- **Government**: Strong social safety net, but gaps remain (secondary school age, crisis response surge capacity)
- **Nonprofits**: 500+ social service agencies coordinated by NCSS, focus on direct service
- **Philanthropy**: Growing sector, trend toward impact measurement and data-driven giving

## ROI Frameworks

### SROI (Social Return on Investment)
**Formula**: SROI = (Net Present Value of Social Benefits) / Investment

**Process**:
1. Identify outcomes (e.g., youth retained in school, families stabilized)
2. Value outcomes (e.g., lifetime earnings uplift = $120,000)
3. Adjust for deadweight (would have occurred anyway), attribution (program's contribution), drop-off (benefits fade over time)
4. Calculate NPV and divide by investment

**Example**: $100K investment → $420K social value (NPV) → SROI = 4.2:1

**Interpretation**:
- 3:1 to 5:1 = Typical range for social programs
- 5:1 to 10:1 = Strong return
- >10:1 = Exceptional (rare, scrutinize assumptions)

### CEA (Cost-Effectiveness Analysis)
**Formula**: CEA = Cost / Outcome Unit

**Process**:
1. Define standardized outcome (e.g., "youth retained in school", "family stabilized")
2. Calculate cost per beneficiary
3. Calculate success rate (% achieving outcome)
4. Divide cost by success rate to get cost per outcome

**Example**: $3,000 per youth, 70% success rate → $4,286 per youth retained

**Use**: Compare programs achieving similar outcomes (which is more cost-effective?)

### Trajectory Uplift
**Definition**: Change in beneficiary life trajectory attributable to intervention

**Process**:
1. Baseline trajectory: Projected outcomes without intervention (e.g., 50% graduation)
2. Intervention trajectory: Projected outcomes with intervention (e.g., 85% graduation)
3. Uplift: Difference = 35% improvement

**Time Horizon**: 5-20 years depending on intervention (short-term outcomes vs lifetime impact)

## REFERENCE.md Usage Guide

### Purpose

`REFERENCE.md` contains detailed methodologies (SROI formulas, CEA calculations, trajectory uplift frameworks) to keep agent files concise while maintaining comprehensive guidance.

### Which Agents Should Reference REFERENCE.md?

**Current Usage** (agents with explicit REFERENCE.md links):
- **impact-evaluator**: References for SROI/CEA calculation details, formula steps, benchmark interpretation
- **portfolio-strategist**: References for strategic portfolio frameworks and alignment scoring

**Recommended Additional Usage** (agents that use SROI/CEA concepts but don't link):
- **devils-advocate**: Should reference REFERENCE.md when challenging SROI/CEA methodology assumptions, questioning deadweight/attribution/drop-off estimates
- **recommendation-synthesizer**: Should reference REFERENCE.md when integrating quantitative metrics (SROI, CEA) into funding recommendations
- **risk-opportunity-analyst**: May benefit from referencing systemic impact frameworks (upstream/midstream/downstream)

### Rationale for Expanded References

**Why devils-advocate needs REFERENCE.md**:
- Devils-advocate challenges SROI/CEA assumptions but doesn't link to methodology details
- When questioning "why 20% deadweight?" or "is 70% attribution reasonable?", agent should reference REFERENCE.md for typical ranges (deadweight 10-25%, attribution 50-80%)
- Critical review is stronger when grounded in documented methodology standards

**Why recommendation-synthesizer needs REFERENCE.md**:
- Recommendation-synthesizer integrates SROI/CEA metrics but doesn't link to interpretation benchmarks
- When synthesizing "SROI 4.2:1 is strong but not exceptional", should reference REFERENCE.md benchmarks (3:1-5:1 typical, 5:1-10:1 strong)
- Synthesis credibility improves when citing documented standards

### Implementation Status

**Version 1.2.0**: Documentation issue identified but not yet resolved in agent files.

**Future Enhancement** (targeted for v1.3.0):
- Add REFERENCE.md links to devils-advocate.agent.md (Domain Context section)
- Add REFERENCE.md links to recommendation-synthesizer.agent.md (Domain Context section)
- Consider adding risk-opportunity-analyst link if systemic impact frameworks used

**No Breaking Changes**: Adding reference links is non-breaking enhancement (agents already use concepts, just making documentation explicit).

## Examples

### Example 1: Evaluating Youth Mentorship Program

**User Query**: "I'm considering funding YouthLift, a mentorship program for 100 at-risk youth (ages 13-16) in Jurong West. Should I fund it?"

**Workflow**:
1. **Submit to @impact-evaluator**: Calculate SROI, CEA, trajectory uplift for YouthLift
   - Output: SROI 4.2:1, CEA $8,571 per youth retained, 35% uplift in school retention
   
2. **Automatically hands off to @portfolio-strategist**: Assess fit with philanthropic mission
   - Output: Strong mission alignment (8/10), fills gap in secondary school age, enhances diversification
   
3. **Automatically hands off to @risk-opportunity-analyst**: Identify risks and opportunities
   - Output: Medium risk (mentor recruitment bottleneck), opportunity (volunteer model improves scalability)
   
4. **Automatically hands off to @recommendation-synthesizer**: Integrate into recommendation
   - Output: FUND $150K annually for 3 years with conditions (volunteer pilot, track all participants)
   
5. **MANDATORY handoff to @devils-advocate**: Challenge assumptions, surface disagreements
   - Output: APPROVED (with challenges to SROI precision, scalability rating, confidence level adjusted from 75% to 70%)

**Final Decision**: Philanthropist reviews comprehensive package with all perspectives, makes informed choice to fund/decline.

---

### Example 2: Comparing Two Competing Programs

**User Query**: "I have budget for one program. Should I fund YouthLift (youth mentorship) or FamilyStability Now (family crisis intervention)?"

**Workflow**:
1. **Run both programs through full workflow** (impact → portfolio → risk → synthesis → devils-advocate)

2. **Compare outputs**:
   - **YouthLift**: SROI 4.2:1, Strong mission alignment (8/10), Medium risk, Medium scalability, Prevention focus
   - **FamilyStability**: SROI 3.8:1, Moderate mission alignment (7/10), Medium risk, Low scalability, Crisis response focus

3. **Decision Criteria**:
   - **If prioritize impact metrics**: YouthLift (higher SROI)
   - **If prioritize portfolio balance**: FamilyStability (adds crisis response to prevention-heavy portfolio)
   - **If prioritize scalability**: Neither excellent, but YouthLift slightly better
   - **If prioritize systemic change**: YouthLift (midstream) over FamilyStability (downstream)

4. **Devils-advocate surfaces trade-offs**: Both are fundable, choice depends on values (prevention vs crisis, youth vs families, depth vs breadth)

**Final Decision**: Philanthropist chooses based on values and portfolio strategy (not just highest SROI).

---

### Example 3: Red Flag Investigation

**User Query**: "Impact analysis shows program has amazing SROI (12:1), but I'm skeptical. Can you dig deeper?"

**Workflow**:
1. **@devils-advocate critical review of SROI methodology**:
   - Challenge: SROI 12:1 is unusually high, scrutinize assumptions
   - Investigation: Deadweight assumption (5%) too low? Attribution assumption (90%) too high? Drop-off assumption (10%) too optimistic? Outcome valuation inflated?
   - Finding: Attribution assumption questionable — program claims 90% of outcomes attributable to them, but beneficiaries also receive government support (MOE, MSF). More realistic attribution: 60%, which drops SROI from 12:1 to 8:1.

2. **Recommendation**: Either (a) accept revised SROI 8:1 (still strong) or (b) request program provide comparison group data to validate attribution claim.

**Final Decision**: Philanthropist proceeds with caution, requires stronger evaluation as condition of funding.

## Troubleshooting

### "What if impact data is incomplete?"

**Situation**: Program has limited evaluation data (no SROI, no comparison group)

**Solution**:
1. @impact-evaluator works with available data, rates data quality as "Low"
2. Recommendations include conditions to strengthen evaluation (establish comparison group, extend tracking)
3. Consider pilot funding ($50K for 1 year) to test and gather data, rather than full commitment

**Alternative**: If data too limited for any confidence, @devils-advocate flags "NEEDS MORE DATA" and recommends investigating before decision.

### "What if program doesn't fit portfolio but has high impact?"

**Situation**: SROI is 6:1 (strong) but mission alignment is 4/10 (weak)

**Solution**:
1. @portfolio-strategist flags weak fit, explains why (e.g., serves different beneficiary population than mission focus)
2. @recommendation-synthesizer presents trade-off: high impact but poor strategic fit
3. @devils-advocate surfaces disagreement: Impact Evaluator says "fund" (high SROI), Portfolio Strategist says "decline" (weak fit)
4. Philanthropist decides: Do values prioritize impact metrics or mission alignment?

**Outcome**: No "right" answer — depends on philanthropist's priorities. Devils-advocate ensures both perspectives documented.

### "What if agents disagree?"

**Situation**: Impact Evaluator rates program 8/10, Portfolio Strategist rates 5/10, Risk Analyst rates 7/10

**Solution**:
1. @recommendation-synthesizer acknowledges disagreement, presents range of perspectives
2. @devils-advocate documents all positions with reasoning and trade-offs
3. Philanthropist sees full picture: "Impact is strong (8/10), strategic fit is moderate (5/10), risk is acceptable (7/10). Trade-off: high impact vs strategic fit. Choose based on whether you prioritize impact metrics or portfolio coherence."

**Outcome**: Disagreement is feature, not bug. Devils-advocate ensures no perspective is silenced.

### "Can I skip devils-advocate if I'm in a hurry?"

**Answer**: **NO — Devils-advocate review is MANDATORY.**

**Rationale**: Funding decisions are high-stakes (large sums, multi-year commitments, impact lives). Devils-advocate adds 1-2 hours to process but ensures assumptions challenged, disagreements surfaced, blind spots identified. Skipping risks costly mistakes (funding programs with hidden flaws, missing alternative interpretations, over-anchoring on initial recommendations).

**If urgent**: Request devils-advocate provide expedited review focusing on top 3 challenges (not comprehensive), but still required.

## Agent Size and Complexity Monitoring

### Current Size Distribution (Version 1.2.0)

| Agent | Size (chars) | % of 30k Limit | Status |
|---|---|---|
| principles-framework-definer | 26,716 | 89% | 🔴 Monitor closely |
| portfolio-strategist | 26,071 | 87% | 🔴 Monitor closely |
| impact-evaluator | 23,204 | 77% | 🟡 Acceptable |
| devils-advocate | 21,226 | 71% | ✅ Comfortable |
| marketing-content-writer | 16,265 | 54% | ✅ Comfortable |
| risk-opportunity-analyst | 15,784 | 53% | ✅ Comfortable |
| recommendation-synthesizer | 15,765 | 53% | ✅ Comfortable |

**Hard Limit**: 30,000 characters (GitHub Copilot constraint)
**Yellow Flag Threshold**: 25,000 characters (trigger optimization review)
**Target Range**: 15,000-20,000 characters for new agents

### Size Imbalance Rationale

**Why principles-framework-definer is largest (26,716 chars)**:
- Facilitates 8 comprehensive foundational question areas (values, beneficiaries, problem areas, theory of change, decision criteria, risk tolerance, portfolio strategy, non-negotiables)
- Each question area requires detailed prompts, examples, and Singapore context
- Produces complex framework documents with quantitative thresholds
- Complexity justified: framework definition is foundational to entire decision process

**Why portfolio-strategist is second largest (26,071 chars)**:
- Covers multiple analytical dimensions: mission alignment, portfolio composition, gap analysis, synergy mapping, concentration risk
- Requires extensive Singapore philanthropic landscape context
- Integration point between quantitative impact metrics and strategic decision criteria
- Complexity justified: portfolio strategy bridges multiple stakeholder perspectives

**Size Distribution Justification**:
- Core analytical agents (impact, portfolio) are larger due to technical depth
- Supporting agents (risk, synthesis, marketing) are smaller and more focused
- Size gap (26k vs 15k) reflects differing complexity requirements, not responsibility creep

### Future Size Management Strategy

**If agents approach 30k limit**:
1. **First**: Optimize examples (consolidate, remove redundancy)
2. **Second**: Move detailed methodology to REFERENCE.md (already done for SROI/CEA)
3. **Third**: Consider agent split if fundamental redesign needed
   - Example: Split principles-framework-definer into two agents (values-definer + criteria-builder)
   - Example: Split portfolio-strategist into two agents (alignment-assessor + portfolio-manager)

**Monitoring Plan**:
- Check agent sizes after each minor version release
- Flag any agent exceeding 27,000 characters for review
- Document size changes in CHANGELOG.md

### Quality Checklist Standards

**Current Checklist Size Range**: 8-12 items per agent

**Rationale for Variation**:
- **Complex analytical agents** (impact-evaluator, portfolio-strategist): 10-12 items
  - More methodologies to verify (SROI, CEA, trajectory uplift, portfolio composition)
  - More stakeholder perspectives to consider
- **Focused functional agents** (risk-opportunity-analyst, recommendation-synthesizer): 8-10 items
  - Narrower scope, fewer integration points
  - Clear success criteria (risk matrix complete, recommendation actionable)
- **Critical review agent** (devils-advocate): 10-12 items
  - Must verify multiple agents' work, surface disagreements, identify blind spots

**Consistency Standard**: Similar complexity agents should have similar rigor
- Analytical agents (impact, portfolio, risk): Similar checklist depth ✓
- Synthesis agents (recommendation, devils-advocate): Similar checklist depth ✓
- Supporting agents (principles, marketing): Appropriate checklist depth for scope ✓

**No Action Needed**: Checklist variation justified by agent complexity differences.
