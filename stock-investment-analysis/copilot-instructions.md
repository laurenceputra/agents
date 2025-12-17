# Stock Investment Analysis Agent Group

**Version**: 1.2.0  
**Date**: 2024-12-17  
**Status**: Production Ready

## Overview

A comprehensive stock investment analysis system that guides investors from initial research through final recommendation. This agent group coordinates six specialized agents to analyze stocks across fundamental, technical, and risk dimensions, culminating in personalized investment advice tailored to individual risk tolerance and goals.

## Purpose

Investors need systematic, multi-dimensional analysis to make informed stock investment decisions. This agent group provides:
- **Comprehensive Research**: Company financials, industry context, competitive positioning
- **Fundamental Analysis**: Financial health, valuation, intrinsic value assessment
- **Technical Analysis**: Price trends, chart patterns, timing insights
- **Risk Assessment**: Volatility analysis, company/market risks, portfolio fit
- **Personalized Recommendations**: Buy/hold/sell advice with position sizing and monitoring plans

## Scope

**In Scope**:
- Fundamental financial analysis (balance sheets, income statements, cash flow)
- Technical analysis (price charts, indicators, patterns)
- Risk assessment (volatility, diversification, sector exposure)
- Personalized investment recommendations
- Portfolio fit analysis
- Decision documentation and rationale

**Out of Scope**:
- Real-time trading execution
- Tax or legal advice
- Cryptocurrency analysis
- Day trading or high-frequency strategies
- Guarantee of returns
- Licensed financial advisory services

## Workflow

This agent group follows a sequential analysis workflow where each agent builds on the previous agent's work. The workflow proceeds from research through analysis to personalized recommendation, with a mandatory critical review before final delivery.

**Start with**: `@stock-researcher` → then proceed through agents via handoff chain

---

## The Six Agents

### 1. Stock Research Agent (`stock-researcher`) ⭐ START HERE
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Gather comprehensive company data, financials, and market context

**When to Use**: This is the entry point for all stock investment analysis

**What It Does**:
- Collects company overview, business model, competitive advantages
- Retrieves financial statements and key metrics
- Researches recent news and events
- Provides industry and sector context
- Compiles peer comparison data

**Hands Off To**: `fundamental-analyst` AND `technical-analyst` (parallel)

---

### 2. Fundamental Analyst Agent (`fundamental-analyst`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Analyze financial health, valuation, and long-term investment merit

**When to Use**: After receiving research report from `stock-researcher`

**What It Does**:
- Evaluates financial health (liquidity, profitability, leverage)
- Assesses growth trends and drivers
- Calculates valuation metrics (P/E, DCF, fair value)
- Analyzes competitive positioning and moat
- Provides fundamental buy/hold/sell rating

**Hands Off To**: `risk-assessor`

---

### 3. Technical Analyst Agent (`technical-analyst`)
**Model**: Claude Haiku 4.5 (copilot)  
**Role**: Analyze price trends, chart patterns, and momentum for timing insights

**When to Use**: After receiving research report from `stock-researcher`

**What It Does**:
- Analyzes price trends (short, intermediate, long-term)
- Identifies chart patterns and support/resistance
- Evaluates technical indicators (MA, RSI, MACD, volume)
- Determines entry/exit price levels
- Provides technical buy/hold/sell rating

**Hands Off To**: `risk-assessor`

---

### 4. Risk Assessor Agent (`risk-assessor`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Evaluate investment risks and determine risk-adjusted suitability

**When to Use**: After receiving fundamental and technical analyses

**What It Does**:
- Assesses volatility and drawdown risk
- Identifies company-specific risks (competitive, financial, operational)
- Evaluates market and sector risks
- Determines portfolio fit and correlation
- Assigns overall risk rating (conservative/moderate/aggressive)
- Recommends position sizing

**Hands Off To**: `investment-advisor`

---

### 5. Investment Advisor Agent (`investment-advisor`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Synthesize all analyses and provide personalized investment recommendation

**When to Use**: After receiving all prior analyses (research, fundamental, technical, risk)

**What It Does**:
- Synthesizes all analyses into coherent recommendation
- Reconciles conflicting signals
- Matches investment to user's risk tolerance and goals
- Provides clear buy/hold/sell recommendation
- Defines position sizing and entry/exit strategy
- Creates monitoring plan with re-evaluation triggers

**Hands Off To**: `devils-advocate`

---

### 6. Devil's Advocate Agent (`devils-advocate`) **[MANDATORY OBJECTIVITY GATE]**
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Critical review for bias, overconfidence, and blind spots before investor decision

**When to Use**: After Investment Advisor recommendation (MANDATORY final gate)

**What It Does**:
- Challenges optimistic bias in analysis
- Develops credible bear case scenarios
- Identifies overconfident statements
- Surfaces blind spots and tail risks
- Ensures risks are genuinely acknowledged, not minimized
- Provides balanced bull/bear perspective

**Hands Off To**: Investor (final assessment with balanced perspective)

---

## Complete Workflow

```
User Request
    ↓
[Stock Research Agent] ⭐ START HERE
    ↓
    ├───→ [Fundamental Analyst] ──→ [Risk Assessor]
    │                                     ↓
    └───→ [Technical Analyst] ─────────→  |
                                          ↓
                                [Investment Advisor]
                                          ↓
                                [Devil's Advocate] (MANDATORY)
                                          ↓
                                Final Recommendation
```

**Estimated Time**: 5-7 minutes for standard single-stock analysis

### Workflow Steps

1. **User Provides**:
   - Stock ticker symbol (e.g., AAPL, MSFT, TSLA)
   - Risk tolerance (conservative/moderate/aggressive)
   - Time horizon (short/medium/long-term)
   - Investment goals (capital preservation, income, growth)
   - Existing portfolio (optional, for diversification analysis)

2. **Stock Research Agent** gathers data:
   - Company overview and financials
   - Industry context and peer comparison
   - Recent news and events
   - → Hands off to Fundamental AND Technical (parallel)

3. **Fundamental Analyst** evaluates financial merit:
   - Financial health assessment
   - Valuation analysis (fair value estimate)
   - Growth prospects and competitive moat
   - → Hands off to Risk Assessor

4. **Technical Analyst** evaluates price action:
   - Trend and momentum analysis
   - Entry/exit price levels
   - Technical outlook
   - → Hands off to Risk Assessor

5. **Risk Assessor** evaluates risks:
   - Volatility and drawdown potential
   - Company-specific and market risks
   - Portfolio fit and position sizing
   - → Hands off to Investment Advisor

6. **Investment Advisor** provides final recommendation:
   - Buy/hold/sell recommendation
   - Position sizing and entry/exit strategy
   - Monitoring plan and re-evaluation triggers
   - → Delivers to user

---

## Decision Trees

### Tree 1: When Should I Use This Agent Group vs. Manual Research?

**Use this agent group when**:
- You want systematic, multi-dimensional analysis
- You need to reconcile fundamental and technical views
- You want personalized advice tailored to your risk tolerance
- You need structured monitoring and re-evaluation plans

**Use manual research when**:
- You already have strong conviction and just need to validate
- You're analyzing highly specialized or niche situations
- You have proprietary data or insights not available publicly

---

### Tree 2: How to Interpret Conflicting Signals?

**Scenario A: Strong Fundamentals, Weak Technicals**
- **Example**: Company undervalued (P/E 15x vs. fair 25x) but stock in downtrend
- **Advisor Recommendation**: 
  - **Long-term investors**: Prioritize fundamentals; consider staged entry as technicals improve
  - **Short-term investors**: Wait for technical reversal before entry

**Scenario B: Weak Fundamentals, Strong Technicals**
- **Example**: Company overvalued (P/E 50x) but stock in strong uptrend
- **Advisor Recommendation**:
  - **Most investors**: Avoid or exit; momentum trades are high-risk
  - **Short-term traders only**: Can trade momentum with tight stop-loss

**Scenario C: High Risk, High Reward**
- **Example**: Small-cap with breakthrough product but volatile and unprofitable
- **Advisor Recommendation**:
  - **Conservative/Moderate**: Avoid (risk exceeds tolerance)
  - **Aggressive/Speculative**: Consider small position (1-2% max) if aligned with goals

---

## Quality Gates

### Gate 1: Research Complete
**Checkpoint**: After Stock Research Agent  
**Criteria**:
- [ ] Company background comprehensive
- [ ] Financial data retrieved (income statement, balance sheet, cash flow)
- [ ] Key metrics calculated
- [ ] Recent news summarized
- [ ] Sector context provided

**Pass**: Fundamental and Technical analysts can proceed independently

---

### Gate 2: Fundamental Analysis Complete
**Checkpoint**: After Fundamental Analyst  
**Criteria**:
- [ ] Financial health evaluated
- [ ] Valuation metrics calculated (P/E, DCF, fair value)
- [ ] Growth trends analyzed
- [ ] Competitive moat assessed
- [ ] Fundamental rating provided

**Pass**: Risk Assessor has financial context for risk evaluation

---

### Gate 3: Technical Analysis Complete
**Checkpoint**: After Technical Analyst  
**Criteria**:
- [ ] Price trends identified (multiple timeframes)
- [ ] Chart patterns analyzed
- [ ] Technical indicators evaluated
- [ ] Key price levels identified (entry, stop-loss, targets)
- [ ] Technical outlook provided

**Pass**: Risk Assessor has price action context for volatility assessment

---

### Gate 4: Risk Assessment Complete
**Checkpoint**: After Risk Assessor  
**Criteria**:
- [ ] Overall risk rating assigned
- [ ] Company-specific risks identified
- [ ] Market/sector risks evaluated
- [ ] Portfolio fit assessed
- [ ] Position sizing recommended

**Pass**: Investment Advisor has complete risk profile for recommendation

---

### Gate 5: Recommendation Complete
**Checkpoint**: After Investment Advisor  
**Criteria**:
- [ ] Clear recommendation (buy/hold/sell)
- [ ] Position sizing suggested
- [ ] Entry/exit strategy defined
- [ ] Monitoring plan outlined
- [ ] Risk warnings provided

**Pass**: User has actionable recommendation with implementation plan

---

## User Input Requirements

### Required Inputs
1. **Stock Ticker**: Symbol to analyze (e.g., AAPL, TSLA, NVDA)
2. **Risk Tolerance**: Conservative / Moderate / Aggressive
3. **Time Horizon**: Short-term (<1 year) / Medium (1-5 years) / Long-term (>5 years)
4. **Investment Goals**: Capital preservation, income, growth, speculation

### Optional Inputs
5. **Existing Portfolio**: Current holdings for diversification analysis
6. **Portfolio Size**: Dollar amount for position sizing
7. **Specific Constraints**: Tax considerations, ESG preferences, liquidity needs
8. **Analysis Depth**: Quick overview vs. deep dive

---

## Examples

### Example 1: Analyzing Apple (AAPL) for Long-Term Growth

**User Input**:
```
Ticker: AAPL
Risk Tolerance: Moderate
Time Horizon: Long-term (5+ years)
Goals: Growth
Portfolio: $150,000 (15% tech currently)
```

**Workflow**:
1. **@stock-researcher** gathers AAPL data → Research report shows strong fundamentals, China exposure
2. **@fundamental-analyst** analyzes financials → Buy rating, fair value $195, P/E 33.5x slight premium
3. **@technical-analyst** reviews charts → Bullish trend, entry at $183-184 optimal, support at $175
4. **@risk-assessor** evaluates risks → Moderate risk, regulatory concerns, suitable at 5-8% allocation
5. **@investment-advisor** synthesizes → **Buy recommendation, 6% position ($9,000), entry $183-184, stop $175, target $210**

**Final Recommendation**: Buy AAPL at $183-184 (50 shares = $9,150 = 6% of portfolio), set stop-loss at $175, target $210 (12 months), monitor quarterly earnings for Services growth.

---

### Example 2: Evaluating High-Risk Stock (Spirit Airlines)

**User Input**:
```
Ticker: SAVE
Risk Tolerance: Moderate
Time Horizon: Medium-term (2 years)
Goals: Growth
```

**Workflow**:
1. **@stock-researcher** gathers data → Finds heavy debt (D/E 2.9x), cash burn, failed merger
2. **@fundamental-analyst** analyzes → Sell rating, critical financial distress, bankruptcy risk 60%
3. **@technical-analyst** reviews charts → Death cross, descending triangle, bearish
4. **@risk-assessor** evaluates → Speculative risk (extreme), unsuitable for moderate investor
5. **@investment-advisor** synthesizes → **Avoid recommendation, redirect to quality alternatives**

**Final Recommendation**: Avoid SAVE (bankruptcy risk 60%, unsuitable for moderate risk tolerance). Consider alternatives: Southwest Airlines (LUV) or Delta (DAL) for airline exposure with better financial health.

---

### Example 3: Comparing Two Tech Stocks

**User Input**:
```
Compare: AAPL vs. MSFT
Risk Tolerance: Moderate
Time Horizon: Long-term
Goals: Growth
```

**Workflow**:
1. Run full analysis for AAPL (as in Example 1)
2. Run full analysis for MSFT:
   - Research: Cloud-focused, higher growth (+12% revenue), strong margins
   - Fundamental: Buy, fair value $450, P/E 35x, growth premium justified
   - Technical: Uptrend, entry $420-425, target $480
   - Risk: Moderate, cloud concentration, suitable 5-8%
   - Advisor: Buy MSFT at $420-425, 6% position

3. **Comparison**:
   - **AAPL**: Mature growth (5-7%), higher dividend (0.5%), more regulatory risk, P/E 33.5x
   - **MSFT**: Faster growth (10-12%), lower dividend (0.8%), cloud cyclicality, P/E 35x
   - **Recommendation**: Both suitable for moderate, long-term investor; MSFT offers higher growth, AAPL more defensive; consider 5% each for diversification

---

## Integration with Portfolio Management

### Use Results for Portfolio Construction
- **Position Sizing**: Follow Investment Advisor's allocation recommendations (3-12% depending on conviction and risk)
- **Diversification**: Monitor sector concentration (Tech should be <30% of portfolio)
- **Rebalancing**: Quarterly review; trim winners if position grows >10%, add to laggards if thesis intact

### Monitoring and Surveillance
- **Key Metrics**: Track metrics from Investment Advisor's monitoring plan (e.g., Services growth for AAPL)
- **Triggers**: Re-evaluate immediately if trigger hit (e.g., earnings miss >5%, price breaks stop-loss)
- **Frequency**: Follow recommended monitoring (monthly for stable, weekly for volatile)

### Rebalancing Workflow
1. Quarterly: Check if positions drifted from target allocations
2. Trim: Sell partial positions if >10% of portfolio (take profits)
3. Add: Increase positions that dropped but thesis intact
4. Re-analyze: Run stock through agents again if major changes (earnings, leadership, regulation)

---

## Best Practices

### For Getting Quality Recommendations
1. **Provide Complete Profile**: Include risk tolerance, time horizon, goals, and portfolio context
2. **Start with Research**: Always begin with `stock-researcher` (don't skip to advisor)
3. **Be Patient**: Allow each agent to complete analysis before moving to next
4. **Ask Follow-Ups**: If conflicting signals, ask Investment Advisor to explain trade-offs
5. **Update Regularly**: Re-run analysis quarterly or when major events occur

### For Risk Management
1. **Respect Position Sizing**: Don't exceed recommended allocation (usually 5-10% per stock)
2. **Use Stop-Losses**: Set stops as recommended by Technical Analyst and Advisor
3. **Diversify**: Don't concentrate; balance across sectors, geographies, market caps
4. **Monitor Triggers**: Watch for re-evaluation triggers from Advisor's monitoring plan
5. **Have Exit Plan**: Know profit-taking targets and conditions for selling

### For Long-Term Success
1. **Focus on Quality**: Prioritize fundamentally strong companies (fortress balance sheets, wide moats)
2. **Be Contrarian When Safe**: Buy quality stocks on pullbacks (technical support), not at highs
3. **Avoid FOMO**: Don't chase momentum; wait for better entry points
4. **Stay Disciplined**: Stick to Investment Advisor's plan; don't deviate emotionally
5. **Learn from Mistakes**: Review past recommendations quarterly; identify what worked and what didn't

---

## Troubleshooting

### Issue: Conflicting Fundamental and Technical Signals
**Symptom**: Fundamental Analyst says "Buy" but Technical Analyst says "Sell"  
**Solution**: Investment Advisor will reconcile based on your time horizon:
- Long-term investors: Prioritize fundamentals
- Short-term investors: Wait for technical alignment

### Issue: Risk Rating Doesn't Match My Tolerance
**Symptom**: Risk Assessor rates stock "Aggressive" but I'm moderate investor  
**Solution**: Investment Advisor will either:
- Recommend smaller position size (e.g., 3% instead of 8%)
- Suggest avoiding and provide alternative investments

### Issue: Fair Value Below Current Price
**Symptom**: Fundamental Analyst says fair value $150 but stock trades at $200  
**Solution**: Investment Advisor will likely recommend Sell or Avoid; suggests waiting for better entry or finding alternative investments

### Issue: All Analyses Complete but No Recommendation
**Symptom**: Reached Investment Advisor but unclear what to do  
**Solution**: Ensure you provided required inputs (risk tolerance, time horizon, goals). Investment Advisor needs these to personalize recommendation.

---

## Disclaimers

**Investment Risk Warning**: This agent group provides analysis and recommendations for informational purposes only. It does not constitute licensed financial advice. Stock market investments carry risk of loss, including potential total loss of principal. Past performance does not guarantee future results.

**User Responsibility**:
- Conduct your own due diligence before investing
- Consult licensed financial advisor, tax advisor, and/or attorney
- Understand tax implications and ensure alignment with overall financial plan
- Diversify across multiple holdings; do not concentrate in single stock
- Ensure investments match your risk tolerance

**Limitations**:
- Recommendations based on publicly available data as of analysis date
- Assumptions may not materialize; actual outcomes may differ
- Technical analysis cannot predict unexpected events
- Risk assessments based on historical data; future volatility may differ
- No guarantee of investment returns

---

## Version History

- **1.0.0** (2024-12-14): Initial release with seven coordinated agents (stock-analysis-orchestrator, stock-researcher, fundamental-analyst, technical-analyst, risk-assessor, investment-advisor, devils-advocate) providing end-to-end stock investment analysis and personalized recommendations
