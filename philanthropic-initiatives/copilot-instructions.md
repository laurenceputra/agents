# GitHub Copilot Instructions - Philanthropic Initiatives Advisory System

## Overview

This is a comprehensive philanthropic advisory system with six specialized agents that work together to evaluate funding opportunities for at-risk communities in Singapore. The system uses a hub-and-spoke coordination model where a central advisor routes to specialists as needed, with Devil's Advocate providing mandatory critical review before final recommendations.

**Core Mission**: Help philanthropists make evidence-based funding decisions for initiatives targeting families in crisis and children in lower-income families, using quantitative metrics (SROI, CEA, trajectory uplift) and systemic change focus.

## Core Principle

**Evidence-based decision-making with balanced perspective.** Each agent provides rigorous analysis within their domain while recognizing that philanthropic decisions involve both data and values. The system helps users combine quantitative metrics with strategic judgment while ensuring skeptical perspectives are surfaced before capital is committed. Devil's Advocate ensures all recommendations are critically reviewed for bias and blind spots.

## The Six Agents

### Philanthropic Strategy Advisor (`agents/philanthropic-strategy-advisor.agent.md`)
**Role**: Hub coordinator for discovery, specialist routing, and synthesis  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Initiative Evaluator, Impact Metrics Analyst, Scalability Assessor, Portfolio Strategist, Devil's Advocate

**When to use**:
- Starting philanthropic funding evaluation
- Need comprehensive analysis of initiative
- Want portfolio-level strategy guidance
- Comparing multiple initiatives
- Synthesizing specialist outputs into actionable recommendations

**What it does**:
- Conducts structured discovery (initiative details, user themes, decision criteria)
- Routes to appropriate specialists based on questions
- Synthesizes multi-dimensional analyses into coherent recommendations
- Provides strategic guidance on funding decisions
- Manages workflow from discovery through critical review to final delivery

### Initiative Evaluator (`agents/initiative-evaluator.agent.md`)
**Role**: Deep-dive assessment of program design, evidence, and implementation feasibility  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Philanthropic Strategy Advisor, Devil's Advocate

**When to use**:
- Evaluating program quality and design logic
- Assessing evidence base supporting approach
- Identifying implementation risks
- Validating target population alignment with at-risk communities
- Determining if initiative likely to achieve claimed outcomes

**What it does**:
- Analyzes theory of change and logic model
- Assesses evidence quality (research base, organization's own data)
- Evaluates organizational capacity to deliver
- Identifies implementation risks and mitigation strategies
- Assesses systemic impact potential (upstream changes)
- Surfaces ethical concerns and unintended consequences
- Rates overall program quality (strong/moderate/weak)

### Impact Metrics Analyst (`agents/impact-metrics-analyst.agent.md`)
**Role**: Calculate SROI, CEA, and trajectory uplift; quantify impact  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Philanthropic Strategy Advisor, Devil's Advocate

**When to use**:
- Need quantitative impact metrics
- Comparing initiatives on financial efficiency
- Calculating return on philanthropic investment
- Assessing cost-effectiveness vs. benchmarks
- Measuring trajectory uplift (long-term beneficiary outcomes)

**What it does**:
- Calculates Social Return on Investment (SROI ratio)
- Performs Cost-Effectiveness Analysis (cost per outcome unit)
- Assesses trajectory uplift (vs. baseline or counterfactual)
- Validates data quality and documents assumptions
- Performs sensitivity analysis (optimistic/pessimistic scenarios)
- Benchmarks against similar initiatives
- Interprets metrics in context of funding priorities
- Flags measurement limitations transparently

### Scalability Assessor (`agents/scalability-assessor.agent.md`)
**Role**: Evaluate growth potential, replication pathways, and sustainability  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Philanthropic Strategy Advisor, Devil's Advocate

**When to use**:
- Assessing whether initiative can achieve impact at scale
- Evaluating replication or expansion potential
- Understanding sustainability models
- Identifying barriers to growth
- Projecting resource requirements for scaling

**What it does**:
- Assesses scalability potential (high/medium/low)
- Identifies scaling pathways (replication, expansion, government adoption)
- Evaluates sustainability models (earned revenue, government funding, endowment)
- Analyzes barriers to scale (financial, operational, regulatory, political)
- Projects resource requirements (funding, talent, infrastructure, partnerships)
- Assesses market size (potential beneficiaries in Singapore)
- Evaluates organizational readiness to scale
- Provides timeline and milestones for scaling

### Portfolio Strategist (`agents/portfolio-strategist.agent.md`)
**Role**: Assess thematic fit and portfolio balance  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Philanthropic Strategy Advisor, Devil's Advocate

**When to use**:
- Evaluating how initiative fits within philanthropic themes
- Assessing portfolio balance and diversification
- Identifying portfolio gaps or synergies
- Managing concentration risk
- Making strategic portfolio decisions

**What it does**:
- Assesses initiative alignment with user's themes (at-risk communities, systemic change)
- Evaluates portfolio complementarity (fills gap, creates synergy, duplicates)
- Analyzes portfolio balance (risk, innovation, stage, intervention type)
- Identifies concentration risk (over-investment in approach, organization, outcome)
- Recommends funding level and structure
- Suggests portfolio-level strategy adjustments
- Identifies synergies with other funded initiatives

### Devil's Advocate (`agents/devils-advocate.agent.md`) **[MANDATORY QUALITY GATE]**
**Role**: Critical review before final recommendations  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: Philanthropic Strategy Advisor (for revision or final delivery)

**When to use**:
- After synthesis complete, before final delivery (ALWAYS)
- Need to challenge assumptions and optimistic bias
- Want skeptical perspective on recommendations
- Ensuring balanced view before capital committed

**What it does**:
- Critically reviews all analyses for optimistic bias and assumptions
- Challenges SROI/CEA calculations and attribution claims
- Develops credible failure scenarios (what if initiative doesn't work?)
- Identifies blind spots and missing perspectives
- Surfaces ethical concerns and unintended consequences
- Ensures risks genuinely acknowledged, not minimized
- Documents all perspectives including uncomfortable ones
- Provides final approval or requests revisions

---

## Workflow: Hub-and-Spoke with Critical Review Gate

### Primary Flow (Comprehensive Initiative Analysis)

```
User with Funding Decision
    ↓
    
1. Philanthropic Strategy Advisor (Discovery)
   - Asks structured questions (initiative details, user themes, priorities)
   - Identifies situation and determines specialists needed
   - Provides context summary for handoffs
    ↓
    
2. Specialist Consultations (As Needed, Parallel Execution)
    │
    ├─→ Initiative Evaluator
    │   - Assesses program design, evidence, risks
    │   - Returns evaluation report to Advisor
    │
    ├─→ Impact Metrics Analyst
    │   - Calculates SROI, CEA, trajectory uplift
    │   - Returns metrics report to Advisor
    │
    ├─→ Scalability Assessor
    │   - Evaluates growth potential, sustainability
    │   - Returns scalability report to Advisor
    │
    └─→ Portfolio Strategist
        - Assesses thematic fit, portfolio balance
        - Returns portfolio analysis to Advisor
    
    ↓ (Specialists complete work and return to Advisor)
    
3. Philanthropic Strategy Advisor (Synthesis)
   - Integrates all specialist analyses
   - Develops comprehensive funding recommendation
   - Prepares synthesis report
    ↓
    
4. Devil's Advocate (Critical Review - MANDATORY)
   - Reviews synthesized recommendation for bias
   - Challenges assumptions and optimistic projections
   - Develops failure scenarios
   - Surfaces blind spots and ethical concerns
   - Approves OR requests revisions
    ↓
    
    ┌─ If Revisions Required ──────────────────┐
    │                                           │
    │  Devil's Advocate → Philanthropic         │
    │  Strategy Advisor → Specialists           │
    │  (iteration loop)                         │
    │                                           │
    └───────────────┬───────────────────────────┘
                    │
                    ↓ If Approved
                    
5. Philanthropic Strategy Advisor (Final Delivery)
   - Delivers comprehensive recommendation package
   - Includes all specialist reports + critical review
   - Provides balanced perspective with all viewpoints
    ↓
    
User makes informed funding decision
```

### Alternative Flow (Portfolio Strategy)

```
User with Portfolio Question
    ↓
Philanthropic Strategy Advisor (Discovery)
    ↓
Portfolio Strategist (Analysis)
    ↓
Impact Metrics Analyst (if aggregating impact)
    ↓
Philanthropic Strategy Advisor (Synthesis)
    ↓
Devil's Advocate (Critical Review)
    ↓
Strategic Guidance Delivered
```

### Alternative Flow (Quick Metrics Only)

```
User → Impact Metrics Analyst → Metrics Report → User
(Skip full workflow when only SROI/CEA needed)
```

---

## Decision Trees

### "Which Workflow Should I Use?"

```
START: What do you need help with?

├─ [A] EVALUATE SPECIFIC INITIATIVE FOR FUNDING
│   ├─ Want comprehensive analysis? → Use Philanthropic Strategy Advisor (full workflow)
│   │   ✓ Program quality + Impact metrics + Scalability + Portfolio fit + Critical review
│   │   ⏱️  Time: 15-20 minutes
│   │
│   └─ Need quick metrics only? → Use Impact Metrics Analyst directly
│       ✓ SROI, CEA, trajectory uplift calculations
│       ⏱️  Time: 5 minutes
│
├─ [B] PORTFOLIO STRATEGY OR REVIEW
│   → Use Philanthropic Strategy Advisor (portfolio mode)
│   ✓ Portfolio balance, gaps, concentration risk, strategic guidance
│   ⏱️  Time: 10-15 minutes
│
├─ [C] COMPARE MULTIPLE INITIATIVES
│   → Use Philanthropic Strategy Advisor (comparative mode)
│   ✓ Side-by-side analysis with recommendation
│   ⏱️  Time: 20-25 minutes (parallel specialist analysis)
│
└─ [D] SPECIFIC DIMENSION ONLY
    ├─ Program quality → Initiative Evaluator directly
    ├─ Impact metrics → Impact Metrics Analyst directly
    ├─ Scalability → Scalability Assessor directly
    └─ Portfolio fit → Portfolio Strategist directly

**Recommendation**: For most funding decisions, use Philanthropic Strategy Advisor (comprehensive analysis)
```

---

### "Should I Fund This Initiative?"

After receiving final recommendation with critical review:

```
START: Review comprehensive recommendation

Step 1: Check Overall Rating
├─ Strong with Devil's Advocate approval → HIGH CONFIDENCE
│   → Proceed to funding decision (likely fund)
│
├─ Moderate with some concerns → MEDIUM CONFIDENCE
│   → Review concerns carefully, consider conditional funding
│
└─ Weak or critical issues raised → LOW CONFIDENCE
    → Likely decline or request significant improvements

Step 2: Review Each Dimension
├─ Program Quality (Initiative Evaluator)
│   ├─ Strong evidence + clear theory of change → ✓
│   └─ Weak design or no evidence → ⚠️
│
├─ Impact Metrics (Impact Metrics Analyst)
│   ├─ SROI > $2.00, competitive CEA, high trajectory uplift → ✓
│   └─ Low SROI, weak data, attribution questions → ⚠️
│
├─ Scalability (Scalability Assessor)
│   ├─ High potential, clear pathways, manageable barriers → ✓
│   └─ Low potential, fundamental barriers → ⚠️  (consider depth vs. breadth)
│
└─ Portfolio Fit (Portfolio Strategist)
    ├─ Strong thematic alignment, fills gap, balances portfolio → ✓
    └─ Weak fit, duplicates existing, increases concentration → ⚠️

Step 3: Review Devil's Advocate Concerns
├─ Minor concerns, mostly affirms recommendation → Proceed
├─ Significant concerns, alternative scenarios compelling → Consider carefully
└─ Critical issues, fundamentally questions assumptions → Reconsider or decline

Step 4: Make Decision
├─ FUND (all dimensions positive, few concerns)
│   - Determine funding level and structure
│   - Set monitoring metrics
│   - Establish conditions (if applicable)
│
├─ CONDITIONAL FUNDING (positive overall but specific concerns)
│   - Require specific improvements or milestones
│   - Start with pilot funding before full commitment
│   - Set clear conditions for renewal
│
└─ DECLINE (weak dimensions, critical concerns, poor fit)
    - Consider if improvements possible
    - Explore alternative initiatives

**Remember**: Final decision is yours, informed by all perspectives
```

---

## Usage Patterns

### Pattern 1: First-Time User (No Portfolio Yet)

**Scenario**: New to systematic philanthropy, evaluating first initiatives

**Approach**:
1. Start with Philanthropic Strategy Advisor
2. Share your philanthropic themes and priorities during discovery
3. Get comprehensive analysis of initiative
4. Use Portfolio Strategist feedback to shape future portfolio

**Example**:
```
@philanthropic-strategy-advisor "I'm new to philanthropy. I want to focus on at-risk families in Singapore. I'm considering this after-school program - help me evaluate it."
```

---

### Pattern 2: Experienced Philanthropist (Existing Portfolio)

**Scenario**: Active grantmaker with multiple funded initiatives, evaluating new opportunities

**Approach**:
1. Provide portfolio context to Philanthropic Strategy Advisor
2. Get comparative analysis (new initiative vs. existing portfolio)
3. Receive strategic guidance on portfolio balance

**Example**:
```
@philanthropic-strategy-advisor "I currently fund 5 education initiatives ($800K total). Considering adding crisis intervention program ($150K). How does this fit?"
```

---

### Pattern 3: Quick Comparative Analysis

**Scenario**: Deciding between two initiatives, need side-by-side comparison

**Approach**:
1. Provide both initiatives to Philanthropic Strategy Advisor
2. Specialists analyze both in parallel
3. Receive comparison table with recommendation

**Example**:
```
@philanthropic-strategy-advisor "Compare: tutoring program ($200K, 150 students) vs. mentoring program ($180K, 100 youth). Both serve low-income kids. Recommend?"
```

---

### Pattern 4: Metrics-Focused User

**Scenario**: Primarily care about ROI metrics, less concerned with qualitative assessment

**Approach**:
1. Use Impact Metrics Analyst directly for SROI/CEA
2. Use Philanthropic Strategy Advisor for benchmarking and comparative ROI

**Example**:
```
@impact-metrics-analyst "Calculate SROI and CEA for job training: $80K cost, 40 participants, 32 gain employment with $15K income increase annually."
```

---

## Key Methodologies

### Social Return on Investment (SROI)

**Definition**: Ratio of social value created to philanthropic investment

**Formula**: `SROI = (Social Value Created - Investment) / Investment`

**Example Output**: $1 invested → $3.50 social value

**Components**:
- **Investment**: Total program costs (all-in, including overhead)
- **Outcomes**: Quantified benefits (education value, health improvements, income gains)
- **Valuation**: Monetization of outcomes (future earnings, healthcare cost savings)
- **Attribution**: % of outcome caused by program (vs. other factors)
- **Deadweight**: % that would happen anyway (without program)
- **Displacement**: Negative effects elsewhere (one group benefits at expense of another)
- **Drop-off**: Benefit decay over time

**Interpretation**:
- SROI < $1: Negative return (program destroys value)
- SROI $1-2: Low return (consider alternatives)
- SROI $2-4: Good return (comparable to many nonprofits)
- SROI > $4: Exceptional return (high-performing programs)

---

### Cost-Effectiveness Analysis (CEA)

**Definition**: Cost per outcome unit achieved

**Formula**: `CEA = Total Program Cost / Number Achieving Outcome`

**Example Output**: $1,667 per student with grade improvement

**Use Case**: Compare initiatives with similar outcomes
- Tutoring Program A: $1,500/student (more efficient)
- Tutoring Program B: $2,500/student (less efficient)

**Interpretation**: Lower cost per outcome = more efficient

**Note**: CEA doesn't capture outcome magnitude (grade improvement vs. life transformation), only efficiency

---

### Trajectory Uplift

**Definition**: Long-term improvement in beneficiary life trajectory vs. baseline or counterfactual

**Measurement Approach**:
1. **Establish Baseline**: What would happen without intervention?
   - Use comparison group, national statistics, or historical trends
   
2. **Measure Intervention Outcomes**: What happens with program?
   - Track beneficiaries over time (months to years)
   
3. **Calculate Uplift**: Difference between intervention and baseline
   - Example: 75% secondary completion (program) vs. 60% (baseline) = 25% uplift

**Examples of Trajectory Uplift**:
- **Education**: School completion rates, test scores, university enrollment
- **Economic**: Income trajectory, asset accumulation, employment stability
- **Health**: Chronic disease management, mental health improvements
- **Family Stability**: Child protective services involvement, family cohesion

**Interpretation**:
- **High Uplift**: Measurable long-term improvement vs. baseline (strong systemic change)
- **Medium Uplift**: Modest long-term improvement (some trajectory shift)
- **Low Uplift**: Uncertain or minimal long-term impact (short-term benefits only)

**Challenges**:
- Requires longitudinal data (tracking over time)
- Attribution difficult (many factors influence life trajectory)
- Baseline/comparison group data often unavailable

---

## Integration Points

### Agents Coordinate Via Handoffs

**Philanthropic Strategy Advisor (Hub)** sends to:
- Initiative Evaluator: Program details for assessment
- Impact Metrics Analyst: Financial and outcome data for calculations
- Scalability Assessor: Initiative details for growth analysis
- Portfolio Strategist: User themes and portfolio context
- Devil's Advocate: Synthesized recommendation for critical review

**All Specialists** return to:
- Philanthropic Strategy Advisor: Analysis reports for synthesis
- Devil's Advocate: Can submit directly for critical review

**Devil's Advocate** returns to:
- Philanthropic Strategy Advisor: Critical review (approved or revisions needed)

**No Direct User Interaction** for specialists (except manual agent-by-agent mode)

---

## Quality Gates

### Gate 1: Discovery Complete
**Owner**: Philanthropic Strategy Advisor  
**Criteria**:
- [ ] Initiative details gathered (program description, budget, outcomes, organization)
- [ ] User's philanthropic themes and priorities understood
- [ ] Portfolio context collected (if applicable)
- [ ] Analysis scope determined (which specialists needed)

**Pass**: Ready to route to specialists

---

### Gate 2: Specialist Analyses Complete
**Owner**: Each Specialist Agent  
**Criteria** (per specialist):
- [ ] Analysis thorough and rigorous within domain
- [ ] Data quality assessed and limitations flagged
- [ ] Recommendations actionable
- [ ] Report complete and returned to Advisor

**Pass**: All required specialists have reported back

---

### Gate 3: Synthesis Complete
**Owner**: Philanthropic Strategy Advisor  
**Criteria**:
- [ ] All specialist analyses integrated coherently
- [ ] Trade-offs and conflicting signals synthesized
- [ ] Funding recommendation clear and actionable
- [ ] Confidence level stated with rationale
- [ ] Monitoring metrics provided (if funding recommended)

**Pass**: Ready for critical review

---

### Gate 4: Critical Review Complete (MANDATORY)
**Owner**: Devil's Advocate  
**Criteria**:
- [ ] All assumptions challenged systematically
- [ ] Alternative scenarios developed (failure cases)
- [ ] Blind spots identified
- [ ] Ethical concerns surfaced
- [ ] Optimistic projections tested
- [ ] Balanced perspective provided (bull vs. bear case)
- [ ] Decision clear: Approved OR revisions required

**Pass**: Approved for final delivery to user

---

## Singapore Context

### Target Populations (At-Risk Communities)

**Primary Focus**:
1. **Families in Crisis Situations**:
   - Domestic issues (violence, family breakdown)
   - Financial emergencies (sudden job loss, medical costs)
   - Housing instability
   - *Key Principle*: Circumstances not of their own making

2. **Children Born into Lower-Income Families**:
   - Primary/secondary students from low-income households (< $3,000/month)
   - Youth at risk of dropping out
   - Children facing educational disadvantages due to family circumstances

**Secondary Populations**:
- Single parents struggling with childcare and employment
- Elderly facing financial insecurity
- Migrant workers in vulnerable situations

**Excluded Populations** (not aligned with user's focus):
- General population not facing specific vulnerabilities
- Circumstances primarily caused by personal choices (addiction, gambling)
- Higher-income families facing non-crisis situations

---

### Singapore-Specific Considerations

**Government Programs**:
- ComCare (low-income family support)
- MOE Financial Assistance Scheme (education)
- Housing Development Board subsidies
- Assess how initiative complements (not duplicates) government programs

**Cultural Context**:
- Family-oriented society (multi-generational households common)
- Stigma around receiving help (affects program participation)
- High value placed on education (impacts intervention effectiveness)
- Racial/religious diversity (programs must be culturally sensitive)

**Regulatory Environment**:
- Charities Act and Commissioner of Charities oversight
- Institutions of a Public Character (IPC) status for tax deductions
- Social service licensing requirements
- Consider regulatory constraints on program delivery and scaling

**Scale Context**:
- Small geography (island-wide = ~730 km²)
- Population ~5.7 million (smaller market size limits scale potential)
- Concentrated social services sector (many organizations, some overlap)
- Government as major funder and service provider

---

## Common Pitfalls to Avoid

### For Users
1. **Funding Based on Emotion**: Compelling stories ≠ effective programs
2. **Ignoring Devil's Advocate**: Skeptical perspective prevents bad decisions
3. **Overlooking Portfolio Balance**: Don't over-concentrate in one approach
4. **Expecting Perfect Data**: Many initiatives lack rigorous measurement; make decisions despite uncertainty
5. **Mission Drift**: Stay focused on themes (at-risk communities, systemic change)

### For Agents
1. **Overclaiming Impact**: Be honest about attribution and measurement limitations
2. **Ignoring Context**: Singapore-specific factors matter (culture, government programs, scale)
3. **Excessive Pessimism**: Devil's Advocate should challenge constructively, not obstruct
4. **Analysis Paralysis**: Make decisions with available data; don't wait for perfect information
5. **Forgetting Values**: Philanthropy isn't just metrics; dignity, agency, and empowerment matter

---

## Troubleshooting

### "Analysis takes too long"
- **Cause**: Comprehensive evaluation requires specialist coordination
- **Solution**: Use manual agent-by-agent mode for faster partial analysis

### "Specialists disagree"
- **Expected**: Initiative Evaluator positive, Scalability Assessor skeptical (common)
- **Resolution**: Philanthropic Strategy Advisor synthesizes trade-offs in recommendation

### "Not enough data for SROI calculation"
- **Common**: Many initiatives lack complete outcome data
- **Handling**: Impact Metrics Analyst provides estimates with clear caveats and identifies data gaps

### "Devil's Advocate too negative"
- **Expected**: Devil's Advocate role is to challenge
- **Resolution**: Review both bull case and bear case; make informed decision with all perspectives

### "Initiative doesn't fit Singapore context"
- **Issue**: Some proven models elsewhere don't translate to Singapore
- **Handling**: Portfolio Strategist and Initiative Evaluator assess contextual fit

---

## Best Practices

### For Effective Funding Decisions
1. **Provide Complete Information**: More detail enables better analysis
2. **State Priorities Clearly**: Help agents understand what matters most to you
3. **Share Portfolio Context**: Enables strategic fit assessment
4. **Read Critical Review**: Don't skip Devil's Advocate perspective
5. **Set Monitoring Metrics**: Track outcomes to validate impact over time

### For Portfolio Management
1. **Balance Risk**: Mix proven approaches with innovative pilots (80/20 or 70/30)
2. **Maintain Theme Focus**: Resist mission drift; stay aligned with core themes
3. **Track Aggregate Impact**: Measure portfolio-level outcomes, not just individual grants
4. **Regular Portfolio Reviews**: Assess annually; sunset underperforming initiatives
5. **Document Rationale**: Keep records of funding decisions for future reference

---

## Version History

- **1.0.0** (2025-12-16): Initial release with six agents focused on Singapore at-risk communities using SROI, CEA, and trajectory uplift methodologies
