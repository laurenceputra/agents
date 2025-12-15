# GitHub Copilot Instructions - Portfolio Analysis Agent Group

## Overview

This agent group helps you write Python code for comprehensive portfolio analysis. The system includes seven specialized agents working together to generate production-ready code for data loading, financial calculations, risk assessment, visualization, and report generation.

**This is a portable agent group following the standard structure and can be dropped into any repository.**

## Agent Group Purpose

Generate high-quality Python code for analyzing investment portfolios across the complete workflow: data ingestion → financial calculations → risk analysis → visualization → reporting.

## The Seven Agents

### 1. Portfolio Data Engineer (`portfolio-data-engineer.agent.md`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Data loading and validation

**When to use**:
- Loading portfolio data from CSV, Excel, JSON
- Fetching historical prices from Yahoo Finance or Alpha Vantage
- Validating and cleaning data
- Handling missing values and data quality issues

**Handoffs**:
- To **Portfolio Analyst** after data is loaded and cleaned
- To **Devil's Advocate** for critical review of data handling assumptions

---

### 2. Portfolio Analyst (`portfolio-analyst.agent.md`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Financial calculations and performance metrics

**When to use**:
- Calculating returns, volatility, Sharpe ratio
- Computing portfolio performance metrics
- Benchmark comparisons (alpha, beta, tracking error)
- Rolling window analysis

**Handoffs**:
- To **Portfolio Risk Assessor** for risk-specific analysis
- To **Devil's Advocate** for critical review of calculation methodology

---

### 3. Portfolio Risk Assessor (`portfolio-risk-assessor.agent.md`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Risk assessment and scenario analysis

**When to use**:
- Calculating VaR and CVaR
- Monte Carlo simulations
- Stress testing (2008 crisis, COVID crash scenarios)
- Risk decomposition and concentration analysis

**Handoffs**:
- To **Portfolio Visualizer** for risk visualizations
- To **Devil's Advocate** for critical review of risk model assumptions

---

### 4. Portfolio Visualizer (`portfolio-visualizer.agent.md`)
**Model**: Claude Haiku 4.5 (copilot)  
**Role**: Chart and graph generation

**When to use**:
- Creating performance dashboards
- Allocation pie charts and treemaps
- Correlation heatmaps
- Drawdown charts and distribution plots

**Handoffs**:
- To **Portfolio Report Generator** for report assembly
- To **Devil's Advocate** for critical review of visualization choices

---

### 5. Portfolio Report Generator (`portfolio-report-generator.agent.md`)
**Model**: Claude Haiku 4.5 (copilot)  
**Role**: Report assembly and export

**When to use**:
- Generating PDF reports
- Creating HTML reports with embedded charts
- Assembling Jupyter notebooks
- Formatting tables and summaries

**Handoffs**:
- To **Code Quality Reviewer** for final code review
- To **Devil's Advocate** for critical review of report structure

---

### 6. Code Quality Reviewer (`code-quality-reviewer.agent.md`)
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Code quality and best practices review

**When to use**:
- Reviewing generated code for quality
- Checking PEP 8 compliance
- Validating error handling and edge cases
- Suggesting performance optimizations

**Handoffs**:
- To **Devil's Advocate** for final critical review before delivery

---

### 7. Devil's Advocate (`devils-advocate.agent.md`) - MANDATORY
**Model**: Claude Sonnet 4.5 (copilot)  
**Role**: Critical review and assumption challenging

**When to use** (REQUIRED for all deliverables):
- Final quality gate before code delivery to user
- Challenging assumptions made by agents
- Identifying blind spots and edge cases
- Surfacing disagreements between agents
- Documenting trade-offs for human decisions

**Handoffs**:
- Back to originating agents for revisions (if issues found)
- To **Code Quality Reviewer** after approval (for final packaging)
- To **Portfolio Data Engineer** for architectural perspective (if needed)

---

## Workflow Diagram

```
User Request
     ↓
Portfolio Data Engineer (load & validate data)
     ↓
Portfolio Analyst (calculate metrics)
     ↓
Portfolio Risk Assessor (risk analysis)
     ↓
Portfolio Visualizer (create charts)
     ↓
Portfolio Report Generator (assemble report)
     ↓
Code Quality Reviewer (code review)
     ↓
Devil's Advocate (critical review - MANDATORY)
     ↓
User (final code delivery)

[Any agent can handoff to Devil's Advocate at any point for critical review]
```

---

## Decision Trees

### Master Decision: What do you want to do?

```
START: What portfolio analysis task do you need?
  │
  ├─ [A] LOAD PORTFOLIO DATA
  │   → Use @portfolio-data-engineer
  │   Examples:
  │   - "Load my portfolio from holdings.csv"
  │   - "Fetch historical prices for my stocks"
  │   - "Validate portfolio data quality"
  │
  ├─ [B] CALCULATE PERFORMANCE METRICS
  │   → Use @portfolio-analyst
  │   Examples:
  │   - "Calculate Sharpe ratio and max drawdown"
  │   - "Compare my portfolio to S&P 500"
  │   - "Compute rolling 30-day volatility"
  │
  ├─ [C] ASSESS RISK
  │   → Use @portfolio-risk-assessor
  │   Examples:
  │   - "Calculate 95% VaR for my portfolio"
  │   - "Run Monte Carlo simulation for 1 year"
  │   - "Stress test against 2008 financial crisis"
  │
  ├─ [D] CREATE VISUALIZATIONS
  │   → Use @portfolio-visualizer
  │   Examples:
  │   - "Create performance dashboard"
  │   - "Plot correlation heatmap"
  │   - "Show allocation by sector"
  │
  ├─ [E] GENERATE REPORT
  │   → Use @portfolio-report-generator
  │   Examples:
  │   - "Create PDF portfolio report"
  │   - "Generate HTML report with charts"
  │   - "Export to Jupyter notebook"
  │
  ├─ [F] REVIEW CODE QUALITY
  │   → Use @code-quality-reviewer
  │   Examples:
  │   - "Review this portfolio analysis code"
  │   - "Check for best practices"
  │   - "Suggest optimizations"
  │
  ├─ [G] COMPLETE END-TO-END ANALYSIS
  │   → Start with @portfolio-data-engineer, flow through all agents
  │   Example:
  │   - "Analyze my portfolio from CSV to final report"
  │
  └─ [H] CHALLENGE ASSUMPTIONS / CRITICAL REVIEW
      → Use @devils-advocate (also runs automatically before delivery)
      Examples:
      - "Review this risk model for blind spots"
      - "Challenge assumptions in this calculation"
      - "What edge cases are missing?"
```

---

## Quality Gates

### Gate 1: Data Quality (Portfolio Data Engineer)
- [ ] Data loaded without errors
- [ ] Missing values handled appropriately
- [ ] Date ranges validated
- [ ] Symbols recognized by API
- [ ] Currency consistency checked

### Gate 2: Calculation Accuracy (Portfolio Analyst)
- [ ] Formulas match industry standards
- [ ] Annualization factors correct (252 for daily, 12 for monthly)
- [ ] Edge cases handled (zero volatility, negative returns)
- [ ] Benchmark alignment correct
- [ ] Results make financial sense

### Gate 3: Risk Model Validity (Portfolio Risk Assessor)
- [ ] Confidence levels correctly implemented
- [ ] Time horizons appropriate
- [ ] Distributional assumptions documented
- [ ] Stress scenarios realistic
- [ ] Limitations clearly stated

### Gate 4: Visualization Quality (Portfolio Visualizer)
- [ ] Charts are publication-quality
- [ ] Axes labeled with units
- [ ] Color schemes accessible (colorblind-friendly)
- [ ] Legends positioned appropriately
- [ ] Titles descriptive

### Gate 5: Report Completeness (Portfolio Report Generator)
- [ ] All metrics included
- [ ] Charts embedded properly
- [ ] Professional formatting
- [ ] Disclaimers present
- [ ] Export successful

### Gate 6: Code Quality (Code Quality Reviewer)
- [ ] PEP 8 compliant
- [ ] Type hints present
- [ ] Docstrings comprehensive
- [ ] Error handling robust
- [ ] Performance optimized
- [ ] Testing recommendations provided

### Gate 7: Critical Review (Devil's Advocate) - MANDATORY
- [ ] All assumptions challenged
- [ ] Blind spots identified
- [ ] Disagreements documented
- [ ] Edge cases considered
- [ ] Trade-offs analyzed
- [ ] Human decisions flagged
- [ ] Residual risks documented

**CRITICAL**: No code is delivered to users without Devil's Advocate approval.

---

## Common Patterns

### Pattern 1: Quick Portfolio Analysis
```
User: "Analyze my portfolio in portfolio.csv"

Flow:
1. @portfolio-data-engineer → Load and validate data
2. @portfolio-analyst → Calculate basic metrics
3. @portfolio-visualizer → Create performance chart
4. @devils-advocate → Critical review
5. Deliver code to user
```

### Pattern 2: Risk-Focused Analysis
```
User: "What's my portfolio risk?"

Flow:
1. @portfolio-data-engineer → Load data
2. @portfolio-analyst → Calculate returns and volatility
3. @portfolio-risk-assessor → VaR, CVaR, stress tests
4. @portfolio-visualizer → Risk distribution charts
5. @devils-advocate → Critical review
6. Deliver code to user
```

### Pattern 3: Full Report Generation
```
User: "Create complete portfolio report"

Flow:
1. @portfolio-data-engineer → Load data
2. @portfolio-analyst → All performance metrics
3. @portfolio-risk-assessor → Risk assessment
4. @portfolio-visualizer → All charts
5. @portfolio-report-generator → Assemble PDF
6. @code-quality-reviewer → Review code
7. @devils-advocate → Critical review
8. Deliver code to user
```

---

## Python Dependencies

### Core Libraries
```python
pandas>=2.0.0          # Data manipulation
numpy>=1.24.0          # Numerical operations
matplotlib>=3.7.0      # Basic plotting
seaborn>=0.12.0        # Statistical visualizations
yfinance>=0.2.28       # Yahoo Finance API (free)
scipy>=1.10.0          # Statistical functions
```

### Optional Libraries
```python
plotly>=5.14.0         # Interactive charts
reportlab>=4.0.0       # PDF generation
weasyprint>=59.0       # HTML to PDF
jinja2>=3.1.2          # HTML templating
squarify>=0.4.3        # Treemap charts
alpha-vantage>=2.3.0   # Alpha Vantage API
```

### Installation
```bash
pip install pandas numpy matplotlib seaborn yfinance scipy
# Optional:
pip install plotly reportlab jinja2 squarify
```

---

## Examples

### Example 1: Load and Analyze Portfolio

**User Request**:
```
"I have a CSV file with my portfolio holdings. Load it, calculate Sharpe ratio, 
and create a performance chart."
```

**Agent Sequence**:
```
1. @portfolio-data-engineer
   → Generates code to load CSV and validate data

2. @portfolio-analyst
   → Generates code to calculate Sharpe ratio and other metrics

3. @portfolio-visualizer
   → Generates code to create performance dashboard

4. @devils-advocate
   → Reviews assumptions (forward-fill strategy, data quality, calculation methods)
   → Flags any issues for human decision
   → Approves for delivery

5. User receives complete, executable Python code
```

### Example 2: Risk Assessment

**User Request**:
```
"Calculate 95% VaR for my portfolio and run a Monte Carlo simulation 
showing potential outcomes over 1 year."
```

**Agent Sequence**:
```
1. @portfolio-risk-assessor
   → Generates VaR calculation code (historical and parametric)
   → Generates Monte Carlo simulation code (10,000 paths)
   → Documents assumptions (normal distribution, historical data relevance)

2. @portfolio-visualizer
   → Generates distribution histogram
   → Generates simulation path plot

3. @devils-advocate
   → Challenges normal distribution assumption
   → Identifies blind spot: correlation breakdown in crises
   → Documents limitation: tail risk may be underestimated
   → Approves with documented limitations

4. User receives code with clear documentation of assumptions and limitations
```

### Example 3: Complete Portfolio Report

**User Request**:
```
"Generate a complete portfolio analysis report in PDF format."
```

**Agent Sequence**:
```
1. @portfolio-data-engineer → Load data, fetch prices
2. @portfolio-analyst → All metrics (returns, Sharpe, CAGR)
3. @portfolio-risk-assessor → VaR, CVaR, stress tests
4. @portfolio-visualizer → Performance, allocation, correlation charts
5. @portfolio-report-generator → Assemble PDF with all metrics and charts
6. @code-quality-reviewer → Review code quality, suggest improvements
7. @devils-advocate → Final critical review, challenge assumptions
8. User receives production-ready report generation code
```

---

## Troubleshooting

### Issue: "No data available for symbol XYZ"
**Agent**: Portfolio Data Engineer  
**Solution**: 
- Verify symbol is correct (check ticker on Yahoo Finance)
- Some delisted stocks may not have data
- Use alternative data source (Alpha Vantage) if available

### Issue: "Sharpe ratio is NaN"
**Agent**: Portfolio Analyst  
**Cause**: Zero volatility (all returns identical)  
**Solution**:
- Check if data has sufficient variation
- Verify returns are calculated correctly
- Use longer time period for more data points

### Issue: "Correlation matrix is singular"
**Agent**: Portfolio Risk Assessor  
**Cause**: Perfect correlation between assets  
**Solution**:
- Check for duplicate symbols in portfolio
- Remove perfectly correlated assets
- Use regularization techniques

### Issue: "PDF generation fails"
**Agent**: Portfolio Report Generator  
**Cause**: Missing dependencies (ReportLab or WeasyPrint)  
**Solution**:
```bash
pip install reportlab
# or
pip install weasyprint
```

### Issue: "Code is slow for large portfolios"
**Agent**: Code Quality Reviewer  
**Solution**:
- Use vectorized pandas operations
- Avoid loops over DataFrame rows
- Cache API results
- Consider chunking for very large datasets (>10,000 symbols)

---

## Best Practices

### Data Handling
1. Always validate input data before calculations
2. Handle missing values explicitly (don't silently forward-fill)
3. Use adjusted close prices (split-adjusted)
4. Validate date ranges (no future dates)
5. Check for delisted securities

### Financial Calculations
1. Use industry-standard formulas
2. Annualize correctly (252 trading days for daily data)
3. Handle edge cases (zero volatility, negative returns)
4. Document all assumptions clearly
5. Provide multiple risk measures (not just one)

### Code Quality
1. Include type hints on all functions
2. Write comprehensive docstrings
3. Use proper error handling with informative messages
4. Add logging for debugging
5. Make code testable (modular functions)

### Risk Management
1. Always calculate multiple risk metrics (VaR, CVaR, stress tests)
2. Document distributional assumptions
3. Provide confidence intervals
4. Include disclaimers about limitations
5. Consider tail risks explicitly

---

## Version History

- **1.0.0** - Initial portfolio analysis agent group with 7 agents: Data Engineer, Analyst, Risk Assessor, Visualizer, Report Generator, Code Quality Reviewer, and Devil's Advocate (mandatory critical review)

---

## Integration Notes

This agent group is portable and can be dropped into any repository. To use:

1. Copy `portfolio-analysis/` folder to your repository
2. Install Python dependencies: `pip install pandas numpy matplotlib seaborn yfinance scipy`
3. Start with @portfolio-data-engineer or follow decision tree for your use case
4. All deliverables automatically go through Devil's Advocate critical review

---

## Disclaimer

This agent group generates code for portfolio analysis. The generated code is for informational and educational purposes only and does not constitute financial advice. Always validate calculations independently and consult with qualified financial advisors before making investment decisions.
