# Stock Investment Analysis Agent Group

**Version**: 1.0.0  
**Status**: Production Ready  
**License**: MIT  
**Requires**: GitHub Copilot CLI

---

## Overview

A comprehensive, AI-powered stock investment analysis system that guides investors from initial research through personalized recommendations. Five specialized agents work together to analyze stocks across fundamental, technical, and risk dimensions, providing institutional-grade analysis accessible to individual investors.

## Quick Start

### 1. Analyze a Stock

```bash
# Start with stock research
@stock-researcher "Analyze Apple Inc. (AAPL)"

# Proceed to fundamental analysis
@fundamental-analyst "Evaluate AAPL's financial health and valuation"

# Get technical analysis
@technical-analyst "Analyze AAPL's price trends and entry points"

# Assess risks
@risk-assessor "Evaluate investment risks for AAPL"

# Get final recommendation
@investment-advisor "Provide personalized AAPL investment recommendation for moderate risk tolerance, long-term horizon"
```

### 2. Complete Workflow (Recommended)

Follow the sequential workflow for best results:
1. **Research** → 2. **Fundamental** → 3. **Technical** → 4. **Risk** → 5. **Advisor**

See [Usage Examples](#usage-examples) below for detailed walkthroughs.

---

## What This Agent Group Does

### For Investors
- **Comprehensive Analysis**: Get institutional-quality research on any publicly traded stock
- **Multiple Perspectives**: See fundamental value, technical trends, and risk profile in one place
- **Personalized Advice**: Receive recommendations tailored to your risk tolerance and goals
- **Actionable Plans**: Get specific entry prices, stop-losses, targets, and monitoring triggers

### For Portfolio Managers
- **Systematic Process**: Standardize investment decisions across team
- **Risk Management**: Ensure proper position sizing and diversification
- **Documentation**: Maintain audit trail of investment rationale
- **Rebalancing Support**: Quarterly re-analysis for portfolio adjustments

---

## The Five Agents

| Agent | Role | Model | When to Use |
|-------|------|-------|-------------|
| **stock-researcher** | Gather company data and context | Claude Sonnet 4.5 | Always start here |
| **fundamental-analyst** | Evaluate financial health and valuation | Claude Sonnet 4.5 | After research |
| **technical-analyst** | Analyze price trends and timing | Claude Haiku 4.5 | After research (parallel) |
| **risk-assessor** | Assess risks and portfolio fit | Claude Sonnet 4.5 | After fundamental + technical |
| **investment-advisor** | Provide personalized recommendation | Claude Sonnet 4.5 | Final step |

---

## Usage Examples

### Example 1: Analyzing a Large-Cap Stock (Apple Inc.)

**Scenario**: You're a moderate-risk investor with a long-term horizon (5+ years) seeking quality growth stocks for a $150K portfolio.

#### Step 1: Research
```bash
@stock-researcher "Analyze Apple Inc. (AAPL). Focus on Services segment growth and China exposure."
```

**Output Summary**: 
- Business: Consumer electronics (iPhone, Mac, iPad) + Services (App Store, iCloud, Apple Music)
- Financials: $99B free cash flow, $153B cash, fortress balance sheet
- Risks: Regulatory (App Store fees), China (20% revenue), market maturation

#### Step 2: Fundamental Analysis
```bash
@fundamental-analyst "Evaluate AAPL's financial health, valuation, and investment merit based on the research report."
```

**Output Summary**:
- Financial Health: Strong (ROE 147%, minimal debt, exceptional cash generation)
- Valuation: Fair to slight undervalued (P/E 33.5x, fair value $195 vs. current $185)
- Rating: Buy (quality business, moderate growth, reasonable price)

#### Step 3: Technical Analysis
```bash
@technical-analyst "Analyze AAPL's price trends, chart patterns, and optimal entry points."
```

**Output Summary**:
- Trend: Bullish (price above all major MAs, breakout confirmed at $180)
- Entry Points: Primary $183-184 (pullback), Secondary $180-181 (retest)
- Stop-Loss: $175 (5.4% risk)
- Targets: $195 (first), $210 (second)

#### Step 4: Risk Assessment
```bash
@risk-assessor "Evaluate investment risks for AAPL including volatility, company-specific risks, and portfolio fit for moderate investor."
```

**Output Summary**:
- Risk Rating: Moderate (22% volatility, beta 1.15, max drawdown -32%)
- Primary Risks: Regulatory (App Store), China exposure, valuation premium
- Suitability: Highly suitable for moderate investor at 5-8% allocation
- Position Sizing: 6% of portfolio ($9,000-12,000)

#### Step 5: Investment Recommendation
```bash
@investment-advisor "Synthesize all analyses and provide personalized AAPL recommendation for:
- Risk Tolerance: Moderate
- Time Horizon: Long-term (5+ years)
- Goals: Growth
- Portfolio Size: $150,000 (currently 15% tech)"
```

**Output Summary**:
- **Recommendation**: Buy
- **Conviction**: Medium-High
- **Position Size**: 6% ($9,000 = 50 shares at $183)
- **Entry Strategy**: Staged entry at $183-184 (primary), $180-181 (secondary)
- **Stop-Loss**: $175 (5.4% risk = $500 max loss)
- **Targets**: $195 (sell 25%), $210 (sell 50%), $225 (sell remaining)
- **Expected Return**: +13.5% (12 months)
- **Monitoring**: Monthly checks; re-evaluate if Services growth <8% or price breaks $175

---

### Example 2: Evaluating a High-Risk Stock (Tesla)

**Scenario**: You're considering Tesla but want to understand the risks.

#### Workflow
```bash
# Step 1: Research
@stock-researcher "Analyze Tesla (TSLA) focusing on growth prospects, competition, and Elon Musk key man risk."

# Step 2: Fundamental Analysis
@fundamental-analyst "Evaluate TSLA's valuation (P/E 95x), path to profitability, and competitive position vs. BYD."

# Step 3: Technical Analysis
@technical-analyst "Analyze TSLA's price volatility, trend, and key support/resistance levels."

# Step 4: Risk Assessment
@risk-assessor "Assess TSLA's risk profile including bankruptcy risk, valuation risk, and suitability for conservative vs. aggressive investors."

# Step 5: Recommendation
@investment-advisor "Provide TSLA recommendation for aggressive investor with 3-year horizon."
```

**Likely Outcome**:
- **Fundamental**: Hold to Sell (P/E 95x extremely high, growth decelerating, margin compression)
- **Technical**: Mixed (volatile, trend depends on momentum)
- **Risk**: Aggressive to Speculative (high volatility, valuation risk, key man risk)
- **Advisor**: Buy with Caution (only for aggressive investors, max 3-5% position) OR Avoid (if risks exceed reward)

---

### Example 3: Comparing Multiple Stocks

**Scenario**: You want to choose between Apple (AAPL) and Microsoft (MSFT) for your portfolio.

#### Workflow
```bash
# Analyze AAPL (as in Example 1)
# Then analyze MSFT:

@stock-researcher "Analyze Microsoft (MSFT) focusing on cloud (Azure) growth and AI strategy."
@fundamental-analyst "Evaluate MSFT's financial health, valuation, and competitive moat vs. AAPL."
@technical-analyst "Analyze MSFT's price trends and compare setup to AAPL."
@risk-assessor "Compare MSFT and AAPL risks for moderate investor."
@investment-advisor "Compare AAPL vs. MSFT and recommend allocation for $150K portfolio (moderate risk, long-term)."
```

**Likely Outcome**:
- **AAPL**: Mature growth (5-7%), higher dividend, more defensive, moderate risk
- **MSFT**: Faster growth (10-12%), cloud-focused, slightly higher valuation, moderate risk
- **Advisor Recommendation**: Both suitable; consider 5% AAPL + 5% MSFT for diversification (total 10% in two quality mega-cap tech)

---

## Installation

### Prerequisites
- GitHub Copilot CLI installed and authenticated
- Access to Claude models (Sonnet 4.5 and Haiku 4.5)

### Setup
1. **Copy Agent Group to Repository**:
   ```bash
   # Clone or copy stock-investment-analysis folder to your project
   cp -r stock-investment-analysis /path/to/your/project/
   ```

2. **Verify Agent Files**:
   ```bash
   # Check that all 5 agents are present
   ls stock-investment-analysis/agents/
   # Should show: stock-researcher.agent.md, fundamental-analyst.agent.md, 
   #              technical-analyst.agent.md, risk-assessor.agent.md, 
   #              investment-advisor.agent.md
   ```

3. **Test with Simple Query**:
   ```bash
   @stock-researcher "Analyze Microsoft (MSFT)"
   ```

---

## Agent Reference Guide

### Stock Research Agent
- **Purpose**: Gather company data, financials, industry context
- **Inputs**: Ticker symbol, research questions (optional), depth preference
- **Outputs**: Research report with company overview, financials, news, peer comparison
- **Typical Use**: "Analyze [TICKER]" or "Research [TICKER] focusing on [specific area]"

### Fundamental Analyst Agent
- **Purpose**: Evaluate financial health, valuation, investment merit
- **Inputs**: Research report from stock-researcher
- **Outputs**: Financial health score, fair value estimate, buy/hold/sell rating
- **Typical Use**: "Evaluate [TICKER]'s fundamentals" or "What is [TICKER]'s fair value?"

### Technical Analyst Agent
- **Purpose**: Analyze price trends, chart patterns, timing
- **Inputs**: Research report (with price data)
- **Outputs**: Trend assessment, entry/exit levels, technical outlook
- **Typical Use**: "Analyze [TICKER]'s technical setup" or "What are good entry points for [TICKER]?"

### Risk Assessor Agent
- **Purpose**: Evaluate risks, volatility, portfolio fit
- **Inputs**: Fundamental + technical analyses, user risk tolerance (optional)
- **Outputs**: Risk rating, primary risks, position sizing recommendation
- **Typical Use**: "Assess risks for [TICKER]" or "Is [TICKER] suitable for [conservative/moderate/aggressive] investor?"

### Investment Advisor Agent
- **Purpose**: Synthesize analyses, provide personalized recommendation
- **Inputs**: All prior analyses + user profile (risk tolerance, time horizon, goals)
- **Outputs**: Buy/hold/sell recommendation, position sizing, entry/exit strategy, monitoring plan
- **Typical Use**: "Provide investment recommendation for [TICKER] for [risk profile] investor with [time horizon]"

---

## Troubleshooting

### Issue: "Agent not found" error
**Solution**: Ensure you're in the correct directory (should contain `stock-investment-analysis/agents/`)

### Issue: Conflicting fundamental and technical signals
**Solution**: Investment Advisor will reconcile based on your time horizon:
- Long-term investors: Prioritize fundamentals
- Short-term investors: Wait for technical alignment

### Issue: Stock looks expensive but I like the company
**Solution**: 
1. Check Fundamental Analyst's fair value estimate
2. If overvalued, Investment Advisor will likely say "Wait for pullback" or "Hold if already own"
3. Set price alerts for better entry points from Technical Analyst

### Issue: Risk rating doesn't match my tolerance
**Solution**: Investment Advisor will adjust position sizing:
- Conservative investor + Aggressive stock → 0-1% position (speculative) or Avoid
- Moderate investor + Moderate stock → 5-8% position (core holding)

---

## Best Practices

### Do's
 Always start with `stock-researcher` (don't skip to advisor)  
 Provide complete user profile (risk tolerance, time horizon, goals)  
 Use staged entry strategy (buy in tranches, not all at once)  
 Set stop-losses as recommended by technical analyst  
 Monitor quarterly and re-evaluate if triggers hit  
 Respect position sizing limits (typically 5-10% per stock)  

### Don'ts
 Don't chase momentum (wait for pullbacks to technical support)  
 Don't ignore stop-losses (discipline prevents large losses)  
 Don't exceed recommended allocation (over-concentration increases risk)  
 Don't skip risk assessment (even "safe" stocks have risks)  
 Don't trade based on emotion (stick to the plan from Investment Advisor)  
 Don't analyze without user profile (recommendations will be generic)  

---

## Limitations

1. **Data Recency**: Analysis based on publicly available data as of query time; may not reflect intraday changes
2. **No Real-Time Execution**: Provides analysis and recommendations only; does not execute trades
3. **No Tax Advice**: Does not provide tax optimization strategies; consult tax advisor
4. **No Guarantees**: Past performance and fair value estimates do not guarantee future returns
5. **U.S. Focus**: Optimized for U.S. stocks and ETFs; international coverage limited
6. **Not Licensed Advice**: Informational only; does not constitute licensed financial advisory services

---

## Contributing

This agent group is designed to be self-contained and portable. To customize:

1. **Modify Agent Instructions**: Edit agent definition files in `agents/` folder
2. **Adjust Models**: Change `model` field in agent frontmatter (e.g., upgrade technical-analyst to Sonnet if needed)
3. **Add Custom Indicators**: Extend technical-analyst with additional technical indicators
4. **Add Asset Classes**: Adapt for ETFs, bonds, or other securities (may require new agents)

---

## Support and Resources

- **Documentation**: See `copilot-instructions.md` for detailed workflow and decision trees
- **Agent Definitions**: See `agents/` folder for individual agent specifications
- **GitHub Copilot Docs**: [https://docs.github.com/copilot](https://docs.github.com/copilot)

---

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Disclaimer

**Investment Risk Warning**: This software provides analysis and recommendations for informational purposes only and does not constitute licensed financial advice, investment advisory services, or a solicitation to buy or sell securities. Stock market investments carry risk of loss, including potential total loss of principal. Past performance does not guarantee future results.

You are solely responsible for your investment decisions. Consult licensed financial, tax, and legal advisors before making investment decisions. The authors and contributors are not liable for any losses resulting from use of this software.

---

## Version History

- **1.0.0** (2024-12-14): Initial release with five coordinated agents providing end-to-end stock investment analysis

---

**Built with GitHub Copilot CLI** 🤖
