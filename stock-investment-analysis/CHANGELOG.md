# Changelog

All notable changes to the Stock Investment Analysis Agent Group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-12-14

### Added
- **Stock Analysis Orchestrator Agent**: New automated workflow option that collects user inputs upfront and coordinates all five specialized agents automatically
  - Structured questionnaire for input collection (ticker, risk tolerance, time horizon, goals, portfolio)
  - Automated agent coordination: research → (fundamental + technical parallel) → risk → advisor
  - Comprehensive report synthesis aggregating all agent outputs
  - Progress tracking with stage indicators (1/5, 2/5, etc.)
  - Error handling for invalid tickers and agent failures
  - Support for single stock and comparison (two stocks) modes
  - Estimated completion time: 5-7 minutes for standard single-stock analysis
- **Workflow Options Documentation**: Added two workflow modes in copilot-instructions.md
  - Option 1: Automated Orchestration (recommended for most users)
  - Option 2: Manual Agent-by-Agent (advanced users)
- **Decision Tree Updates**: Added "Which Workflow Should I Use?" decision tree
- **README Examples**: Added Example 0 demonstrating orchestrator usage with NVIDIA analysis

### Changed
- **Version Bump**: Updated agent group from 1.0.0 to 1.1.0
- **Agent Count**: Updated from "five agents" to "six agents" throughout documentation
- **Quick Start Section**: Restructured to show orchestrator as recommended Option 1, manual workflow as Option 2
- **Agent Table**: Added orchestrator as first row with ⭐ indicator for recommended entry point

### Context
The orchestrator addresses user feedback requesting a single-entry automated workflow. Previously, users had to manually hand off between five agents, which was time-consuming and required understanding the workflow. The orchestrator automates this process while preserving the option for advanced users to call agents individually.

### Migration
No breaking changes. Existing manual agent-by-agent workflow remains fully functional. Users can choose between:
- New automated workflow: `@stock-analysis-orchestrator`
- Existing manual workflow: `@stock-researcher` → subsequent agents

---

## [1.0.0] - 2024-12-14

### Added
- Initial release of Stock Investment Analysis Agent Group
- **Five Specialized Agents**:
  - `stock-researcher`: Gather company data, financials, industry context
  - `fundamental-analyst`: Evaluate financial health, valuation, intrinsic value
  - `technical-analyst`: Analyze price trends, chart patterns, momentum
  - `risk-assessor`: Assess volatility, risks, portfolio fit
  - `investment-advisor`: Provide personalized investment recommendations
- **Sequential Workflow**: Research → (Fundamental + Technical parallel) → Risk → Advisor
- **Handoff Coordination**: Agents pass context to downstream agents automatically
- **Personalized Recommendations**: Tailored to user's risk tolerance, time horizon, and goals
- **Portfolio Fit Analysis**: Considers existing holdings and diversification
- **Comprehensive Documentation**: copilot-instructions.md, README.md, individual agent files

### Context
Built to provide institutional-grade stock analysis to individual investors through systematic multi-dimensional analysis combining fundamental, technical, and risk perspectives.
