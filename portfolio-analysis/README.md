# Portfolio Analysis Agent Group

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yourusername/agents)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A portable GitHub Copilot agent group providing a **Python library + code-writing agent** for comprehensive portfolio analysis. Use the `portfolio_toolkit` library directly in your code, or have the `portfolio-code-writer` agent generate complete scripts for you.

**🎉 NEW in v2.0.0**: Complete architecture redesign! Replaced 5 code-generation agents with a unified agent + library approach. Faster, more consistent, and more maintainable.

## 🚀 Quick Start

### Installation

```bash
# Install the portfolio_toolkit library
cd portfolio-analysis
pip install -e .

# This installs core dependencies: pandas, numpy, matplotlib, seaborn, scipy

# Optional: Install extras
pip install -e ".[data]"      # Add yfinance for price data
pip install -e ".[reports]"   # Add jinja2, reportlab for reports
pip install -e ".[full]"      # Install all optional dependencies
```

### Two Ways to Use

#### Option A: Beginner (Agent-Assisted)

Talk to the `portfolio-code-writer` agent to generate complete scripts:

```
@portfolio-code-writer Analyze my portfolio in portfolio.csv. 
Calculate performance metrics, assess risk, and create visualizations.
```

You'll receive a complete, executable Python script with error handling and usage instructions.

#### Option B: Advanced (Direct Library Usage)

Import `portfolio_toolkit` modules and write your own code:

```python
from portfolio_toolkit import data, metrics, risk, viz, reports

# Load data
portfolio = data.load_portfolio_csv('portfolio.csv')
prices = data.fetch_price_history(symbols, '2023-01-01', '2024-12-31')

# Calculate metrics
returns = metrics.calculate_returns(prices)
stats = metrics.calculate_portfolio_statistics(returns)

# Risk assessment
var_95 = risk.calculate_var(returns, 0.95)
mc_results = risk.monte_carlo_simulation(returns)

# Visualizations
fig = viz.plot_cumulative_returns(returns)
viz.save_figure(fig, 'performance.png')

# Generate report
reports.generate_html_report(stats, {'performance': 'performance.png'})
```

---

---

## 📊 What This System Provides

### portfolio_toolkit Library (NEW in v2.0.0)

A comprehensive Python library with five modules:

**1. data module** - Data loading and cleaning
- `load_portfolio_csv()`, `load_portfolio_excel()`
- `fetch_price_history()` - Historical prices from yfinance
- `clean_portfolio_data()`, `validate_portfolio_data()`
- `merge_portfolio_with_prices()`

**2. metrics module** - Financial calculations
- `calculate_returns()`, `calculate_cagr()`, `calculate_volatility()`
- `calculate_sharpe_ratio()`, `calculate_sortino_ratio()`, `calculate_calmar_ratio()`
- `calculate_max_drawdown()`, `calculate_alpha_beta()`
- `calculate_portfolio_statistics()` - All metrics at once

**3. risk module** - Risk assessment
- `calculate_var()`, `calculate_cvar()` - Value at Risk
- `monte_carlo_simulation()` - Future value distributions
- `stress_test()` - Historical scenario analysis
- `calculate_correlation_matrix()`, `calculate_risk_metrics()`

**4. viz module** - Visualizations
- `plot_cumulative_returns()`, `plot_drawdown()`, `plot_rolling_metric()`
- `plot_return_distribution()`, `plot_correlation_heatmap()`
- `plot_allocation_pie()`, `plot_performance_dashboard()`

**5. reports module** - Report generation
- `generate_html_report()`, `generate_markdown_report()`
- `export_metrics_to_excel()`

All library functions are:
- ✅ Tested and documented with docstrings
- ✅ Type-hinted for IDE autocomplete
- ✅ Vectorized for performance
- ✅ Error-handling built-in
- ✅ Industry-standard formulas

---

## 🤖 The Three Agents

### 1. Portfolio Code Writer (NEW in v2.0.0)
**Model**: Claude Sonnet 4.5  
**Purpose**: Generate complete portfolio analysis scripts using portfolio_toolkit library

**Use for**:
- Generating complete, executable Python scripts
- Customizing analysis workflows to your needs
- Chaining data → metrics → risk → visualization → reports

**Example**:
```
@portfolio-code-writer Generate a script to analyze portfolio.csv, 
calculate all metrics, assess risk with VaR and Monte Carlo, 
create visualizations, and generate an HTML report.
```

**What you receive**: A complete Python script that:
- Imports portfolio_toolkit modules
- Handles errors gracefully
- Includes usage instructions
- Is immediately executable

---

### 2. Code Quality Reviewer
**Model**: Claude Sonnet 4.5  
**Purpose**: Review generated scripts for quality and best practices

**Use for**:
- PEP 8 compliance checking
- Error handling validation
- Performance optimization suggestions

**Example**:
```
@code-quality-reviewer Review this portfolio analysis script for best practices
```

---

### 3. Devil's Advocate (MANDATORY)
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

### v2.0.0 Workflow (Agent-Assisted)

**User Goal**: Analyze portfolio from CSV file to final HTML report

**Step 1**: Generate complete script
```
@portfolio-code-writer I have my_portfolio.csv with columns: date, symbol, shares, price.
Analyze performance, calculate risk metrics (VaR, Monte Carlo), create charts, 
and generate an HTML report. Compare against S&P 500.
```

**Step 2**: Code review (automatic)
```
@code-quality-reviewer reviews generated script for best practices
```

**Step 3**: Critical review (automatic)
```
@devils-advocate challenges assumptions, identifies edge cases, documents limitations
```

**Result**: Complete, executable Python script with:
- Data loading and validation
- Performance metrics calculation
- Risk assessment (VaR, CVaR, Monte Carlo)
- Benchmark comparison
- Visualizations (returns, drawdown, distributions)
- HTML report generation
- Error handling and usage instructions
- Documented assumptions and limitations

**Benefits over v1.0.0**:
- ⚡ **3 steps instead of 8** (single code generation handoff)
- 🎯 **Single script** instead of scattered code snippets
- 📚 **Uses tested library** functions instead of generated formulas
- 🐛 **Easier debugging** (library functions are tested)

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

**v2.0.0 Approach**:
```
@portfolio-code-writer Generate a script to analyze portfolio.csv, 
calculate returns and Sharpe ratio, and create a performance chart.
```

**Output**: Python script with data loading, metrics, and visualization

---

### Use Case 2: Risk Assessment
"I need to understand my portfolio's risk exposure."

**v2.0.0 Approach**:
```
@portfolio-code-writer Calculate 95% VaR, run Monte Carlo simulation, 
perform stress testing, and create risk distribution charts.
```

**Output**: Python script with comprehensive risk assessment

---

### Use Case 3: Client Reporting
"I need professional reports for my clients."

**v2.0.0 Approach**:
```
@portfolio-code-writer Generate a complete analysis with all metrics, 
risk assessment, visualizations, and HTML report.
```

**Output**: Python script that generates professional HTML report

---

### Use Case 4: Advanced Custom Analysis
"I want full control over my analysis."

**v2.0.0 Approach** (Direct library usage):
```python
from portfolio_toolkit import data, metrics, risk, viz

# Write your own custom analysis code
# Full access to all library functions
```

**Output**: Your own Python code with portfolio_toolkit imported

---

## ⚙️ Installation

### Option 1: Install as Library (Recommended)

```bash
cd portfolio-analysis
pip install -e .  # Installs portfolio_toolkit in development mode
```

This automatically installs core dependencies:
- pandas, numpy, matplotlib, seaborn, scipy

### Option 2: Install with Optional Features

```bash
# For data fetching (yfinance)
pip install -e ".[data]"

# For report generation (jinja2, reportlab)
pip install -e ".[reports]"

# All features
pip install -e ".[full]"
```

### Option 3: Drop into Existing Repository

```bash
# Copy portfolio-analysis folder to your repo
cp -r portfolio-analysis /path/to/your/repo/

# Install the library
cd /path/to/your/repo/portfolio-analysis
pip install -e .
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

## 🔄 Migration from v1.0.0

If you used v1.0.0 agents (@portfolio-data-engineer, @portfolio-analyst, etc.):

### What Changed

**v1.0.0**: 5 agents generated code snippets → sequential handoffs → scattered code  
**v2.0.0**: 1 agent + library → single script → tested functions

### Migration Options

**Option A: Regenerate Scripts**
- Use @portfolio-code-writer to generate new scripts using portfolio_toolkit
- Fastest migration path

**Option B: Refactor Existing Code**
```python
# Old (v1.0.0 - inline functions)
def calculate_sharpe_ratio(returns, rf_rate=0.02):
    excess_returns = returns - rf_rate/252
    return np.sqrt(252) * excess_returns.mean() / returns.std()

# New (v2.0.0 - import from library)
from portfolio_toolkit.metrics import calculate_sharpe_ratio
sharpe = calculate_sharpe_ratio(returns, risk_free_rate=0.02)
```

**Option C: Keep Using v1.0.0 Code**
- Your existing v1.0.0 generated code still works (no forced migration)
- v1.0.0 agent definitions archived in `archive/v1/` for reference

**Migration Benefits**:
- ✅ Tested library functions (no formula bugs)
- ✅ Consistent code across all analyses
- ✅ Faster development (1 handoff vs 5)
- ✅ Easy updates (change library, not agents)

See `CHANGELOG.md` for complete migration guide.

---

## 📝 Version History

- **2.0.0** (2025-12-16) - **BREAKING CHANGE**: Architecture redesign - replaced 5 code-generation agents with 1 unified agent + portfolio_toolkit library. Workflow simplified from 8 handoffs to 3. Library-first approach with agent assistance. See CHANGELOG.md for migration guide.
- **1.0.0** (2024-12-15) - Initial release with 7 agents: Data Engineer, Analyst, Risk Assessor, Visualizer, Report Generator, Code Quality Reviewer, and Devil's Advocate

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

**Ready to analyze your portfolio?**

**Beginner**: Start with the agent:
```
@portfolio-code-writer Analyze my portfolio in portfolio.csv and create a complete report!
```

**Advanced**: Use the library directly:
```python
from portfolio_toolkit import data, metrics, risk, viz, reports
# Write your own analysis code
```
