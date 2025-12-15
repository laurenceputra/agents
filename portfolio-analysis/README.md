# Portfolio Analysis Agent Group

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/agents)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A portable GitHub Copilot agent group for generating production-ready Python code to analyze investment portfolios. This agent group covers the complete workflow from data loading through report generation.

## 🚀 Quick Start

### Prerequisites

```bash
# Install required Python packages
pip install pandas numpy matplotlib seaborn yfinance scipy

# Optional: For PDF reports and advanced visualizations
pip install plotly reportlab jinja2 squarify
```

### Basic Usage

**Load and analyze a portfolio:**

```
@portfolio-data-engineer Load my portfolio from portfolio.csv and validate the data
```

**Calculate performance metrics:**

```
@portfolio-analyst Calculate Sharpe ratio, max drawdown, and CAGR for my portfolio
```

**Assess risk:**

```
@portfolio-risk-assessor Calculate 95% VaR and run Monte Carlo simulation
```

**Create visualizations:**

```
@portfolio-visualizer Create a performance dashboard with returns, drawdown, and rolling Sharpe
```

**Generate report:**

```
@portfolio-report-generator Create a PDF report with all metrics and charts
```

---

## 📊 What This Agent Group Does

This agent group generates Python code for comprehensive portfolio analysis:

- **Data Loading**: Import portfolio data from CSV/Excel/JSON, fetch historical prices from APIs
- **Performance Metrics**: Returns, volatility, Sharpe ratio, Sortino ratio, CAGR, max drawdown
- **Risk Assessment**: VaR, CVaR, Monte Carlo simulation, stress testing
- **Benchmark Comparison**: Alpha, beta, tracking error, correlation analysis
- **Visualizations**: Performance charts, allocation breakdowns, risk heatmaps
- **Report Generation**: Professional PDF/HTML reports with all metrics and charts

All code is:
- ✅ Production-ready with error handling
- ✅ Well-documented with docstrings and type hints
- ✅ PEP 8 compliant
- ✅ Performance-optimized for large portfolios
- ✅ Critically reviewed for assumptions and blind spots

---

## 🤖 The Seven Agents

### 1. Portfolio Data Engineer
**Model**: Claude Sonnet 4.5  
**Purpose**: Load and validate portfolio data

**Use for**:
- Loading CSV, Excel, JSON files
- Fetching historical prices (Yahoo Finance, Alpha Vantage)
- Data validation and cleaning
- Handling missing values

**Example**:
```
@portfolio-data-engineer I have holdings.csv with columns: Date, Ticker, Shares. 
Load it and fetch historical prices from Yahoo Finance.
```

---

### 2. Portfolio Analyst
**Model**: Claude Sonnet 4.5  
**Purpose**: Calculate financial metrics

**Use for**:
- Returns and volatility calculations
- Sharpe, Sortino, Calmar ratios
- Benchmark comparisons (alpha, beta)
- Rolling window analysis

**Example**:
```
@portfolio-analyst Calculate comprehensive metrics for my portfolio 
and compare to S&P 500 benchmark.
```

---

### 3. Portfolio Risk Assessor
**Model**: Claude Sonnet 4.5  
**Purpose**: Risk assessment and scenario analysis

**Use for**:
- Value at Risk (VaR) and CVaR
- Monte Carlo simulations
- Stress testing (2008 crisis, COVID crash)
- Correlation and concentration risk

**Example**:
```
@portfolio-risk-assessor Calculate 95% VaR, run 10,000-path Monte Carlo simulation, 
and stress test against the 2008 financial crisis.
```

---

### 4. Portfolio Visualizer
**Model**: Claude Haiku 4.5  
**Purpose**: Create charts and visualizations

**Use for**:
- Performance dashboards
- Allocation pie charts and treemaps
- Correlation heatmaps
- Distribution plots and drawdown charts

**Example**:
```
@portfolio-visualizer Create a 3-panel dashboard showing cumulative returns, 
drawdown, and rolling 60-day Sharpe ratio.
```

---

### 5. Portfolio Report Generator
**Model**: Claude Haiku 4.5  
**Purpose**: Assemble professional reports

**Use for**:
- PDF report generation
- HTML reports with embedded charts
- Jupyter notebook creation
- Executive summaries

**Example**:
```
@portfolio-report-generator Generate a PDF report with all metrics, 
charts, and professional formatting.
```

---

### 6. Code Quality Reviewer
**Model**: Claude Sonnet 4.5  
**Purpose**: Review code quality

**Use for**:
- PEP 8 compliance checking
- Performance optimization suggestions
- Error handling review
- Testing recommendations

**Example**:
```
@code-quality-reviewer Review this portfolio analysis code for quality 
and best practices.
```

---

### 7. Devil's Advocate (MANDATORY)
**Model**: Claude Sonnet 4.5  
**Purpose**: Critical review and assumption challenging

**Use for** (automatically runs before all deliveries):
- Challenging assumptions
- Identifying blind spots
- Surfacing disagreements
- Documenting limitations

**Example**:
```
@devils-advocate Review this risk model for assumptions and blind spots.
```

**Note**: Devil's Advocate automatically reviews all code before delivery to users. This ensures assumptions are documented and edge cases are identified.

---

## 📋 Complete Workflow Example

**User Goal**: Analyze portfolio from CSV file to final PDF report

**Step 1**: Load data
```
@portfolio-data-engineer Load my_portfolio.csv and fetch historical prices for all symbols
```

**Step 2**: Calculate metrics
```
@portfolio-analyst Calculate returns, Sharpe ratio, max drawdown, and compare to SPY benchmark
```

**Step 3**: Assess risk
```
@portfolio-risk-assessor Calculate VaR, CVaR, and run Monte Carlo simulation for 1 year
```

**Step 4**: Create visualizations
```
@portfolio-visualizer Create performance dashboard, allocation chart, and correlation heatmap
```

**Step 5**: Generate report
```
@portfolio-report-generator Assemble all metrics and charts into a professional PDF report
```

**Step 6**: Critical review (automatic)
```
Devil's Advocate reviews all code, challenges assumptions, identifies blind spots
```

**Result**: Complete, production-ready Python code with documented limitations

---

## 📂 Portfolio Data Format

### CSV Example

```csv
date,symbol,shares,cost_basis
2024-01-15,AAPL,100,18000.00
2024-01-15,MSFT,50,18500.00
2024-01-15,GOOGL,30,4200.00
```

### Supported Columns

- **Required**: `date`, `symbol`, `shares`
- **Optional**: `cost_basis`, `price`, `market_value`, `sector`

### Supported File Formats

- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)
- JSON (`.json`)
- Python dictionaries

---

## 🎯 Common Use Cases

### Use Case 1: Personal Portfolio Tracking
"I want to track my investment portfolio performance over time."

**Agents**: Data Engineer → Analyst → Visualizer  
**Output**: Performance charts and key metrics

---

### Use Case 2: Risk Assessment
"I need to understand my portfolio's risk exposure."

**Agents**: Data Engineer → Analyst → Risk Assessor → Visualizer  
**Output**: VaR, CVaR, stress test results, risk distributions

---

### Use Case 3: Client Reporting
"I need professional reports for my clients."

**Agents**: Full workflow (all 7 agents)  
**Output**: PDF report with metrics, charts, disclaimers

---

### Use Case 4: Investment Strategy Backtesting
"I want to test how my strategy would have performed."

**Agents**: Data Engineer → Analyst → Risk Assessor → Visualizer  
**Output**: Historical performance analysis with risk metrics

---

## ⚙️ Installation

### Option 1: Drop into Existing Repository

```bash
# Copy the portfolio-analysis folder to your repo
cp -r portfolio-analysis /path/to/your/repo/

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Use as Standalone

```bash
# Clone repository
git clone <repo-url>
cd agents/portfolio-analysis

# Install dependencies
pip install pandas numpy matplotlib seaborn yfinance scipy
```

---

## 🧪 Testing Your Code

All generated code should be tested with your actual data. Here's a testing checklist:

### Data Loading
- [ ] File loads without errors
- [ ] All required columns present
- [ ] Dates parsed correctly
- [ ] No missing critical data

### Calculations
- [ ] Metrics match expected values
- [ ] Edge cases handled (zero volatility, negative returns)
- [ ] Benchmark comparisons align correctly
- [ ] Annualization factors correct

### Visualizations
- [ ] Charts render correctly
- [ ] Labels and legends present
- [ ] Colors accessible (colorblind-friendly)
- [ ] Export works (PNG, PDF, SVG)

### Reports
- [ ] All metrics included
- [ ] Charts embedded properly
- [ ] Professional formatting
- [ ] Disclaimers present

---

## 🚨 Limitations and Disclaimers

### Known Limitations

1. **Data Quality**: Assumes clean, accurate input data
2. **Single Currency**: Default assumes USD (multi-currency requires manual conversion)
3. **Delisted Securities**: May not handle delisted stocks automatically
4. **Corporate Actions**: Stock splits should be handled by API (adjusted close prices)
5. **Transaction Costs**: Not included in calculations (gross returns)
6. **Taxes**: Not considered in performance metrics

### Risk Model Limitations

1. **Normal Distribution**: Parametric VaR assumes normality (underestimates tail risk)
2. **Historical Data**: Past performance doesn't guarantee future results
3. **Correlation Stability**: Correlations may change during market stress
4. **No Leverage**: Assumes unleveraged portfolio

### Important Disclaimer

**This agent group generates code for educational and informational purposes only. The code does not constitute financial advice. Always validate calculations independently and consult with qualified financial advisors before making investment decisions.**

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: API rate limits exceeded  
**Solution**: Use caching (`use_cache=True`) or reduce API calls

**Issue**: Missing price data for symbol  
**Solution**: Check ticker symbol is correct, try alternative data source

**Issue**: Sharpe ratio is NaN  
**Solution**: Check for zero volatility (insufficient data variation)

**Issue**: Memory error with large portfolios  
**Solution**: Process in chunks, use vectorized operations

**Issue**: PDF generation fails  
**Solution**: Install ReportLab or WeasyPrint: `pip install reportlab`

---

## 🤝 Contributing

This is a portable agent group. To improve it:

1. Follow the meta-agent workflow in `/.github/copilot-instructions.md`
2. Submit changes through Agent Architect → Implementer → Validator → Devil's Advocate
3. All changes must pass critical review before merge

---

## 📝 Version History

- **1.0.0** (2025-12-15) - Initial release with 7 agents: Data Engineer, Analyst, Risk Assessor, Visualizer, Report Generator, Code Quality Reviewer, and Devil's Advocate

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 Support

For issues or questions:
- Review the `copilot-instructions.md` file for detailed workflow
- Check the Troubleshooting section above
- Consult individual agent files in `agents/` directory

---

## 🌟 Acknowledgments

Built using GitHub Copilot agent best practices and the portable agent group pattern.

---

**Ready to analyze your portfolio?** Start with:

```
@portfolio-data-engineer Load my portfolio data and let's begin!
```
