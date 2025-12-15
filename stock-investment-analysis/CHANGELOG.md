# Changelog

All notable changes to the Stock Investment Analysis Agent Group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-12-15

### Added
- **Feature Enhancement**: Improved quality checklist usability across all agents

### Changed
- **fundamental-analyst**: Consolidated quality checklist from 11 to 10 items for improved focus and clarity
- **risk-assessor**: Consolidated quality checklist from 12 to 10 items for improved focus and clarity
- **stock-analysis-orchestrator**: Expanded quality checklist from 10 to 15 items (complexity-appropriate standard for orchestrator agents)
- **stock-researcher**: Consolidated quality checklist from 12 to 10 items for improved focus and clarity
- **technical-analyst**: Consolidated quality checklist from 12 to 10 items for improved focus and clarity
- **devils-advocate**: Version synchronized to 1.3.0 for group consistency (no changes to agent)
- **investment-advisor**: Version synchronized to 1.3.0 for group consistency (no changes to agent)

### Fixed
- Quality checklist item count inconsistencies across agent groups

### Note
**stock-analysis-orchestrator** uses a 15-item checklist (not 10) due to higher complexity of coordinating 6 specialist agents. This follows the revised complexity-appropriate standard: simple agents 6-10 items, complex agents (orchestrators) 12-18 items.

## [1.2.0] - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New seventh agent for objectivity and bias detection
  - **Purpose**: Critically reviews investment recommendations for optimistic bias, overconfidence, and blind spots before investor decision
  - **Position in Workflow**: Final objectivity gate after Investment Advisor recommendation, before investor commits capital
  - **Key Capabilities**:
    - Challenges optimistic bias in fundamental and technical analysis
    - Develops credible bear case scenarios where investment thesis fails
    - Identifies overconfident price targets and return projections
    - Surfaces tail risks and black swan scenarios not addressed
    - Ensures risks are genuinely acknowledged, not minimized
    - Provides balanced bull/bear comparison
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for skeptical evaluation
  - **Context**: Prevents overconfident investment decisions by ensuring investors see complete risk picture including bearish scenarios

### Changed
- **All Agents**: Added handoff to Devil's Advocate for critical review (version 1.0.0 → 1.2.0)
  - **Affected Agents**: Stock Researcher, Fundamental Analyst, Technical Analyst, Risk Assessor, Investment Advisor
  - **Before**: Investment Advisor recommendation went directly to investor
  - **After**: All recommendations go through Devil's Advocate objectivity gate before finalization
  - **Added Handoff**: "Submit to Devil's Advocate" for bias detection and bear case development
  - **Context**: Ensures objectivity and prevents confirmation bias in investment analysis
  - **Migration**: No breaking changes—workflow extended with quality gate, existing process preserved

- **Stock Analysis Orchestrator**: Updated to coordinate seven agents including Devil's Advocate (version 1.1.0 → 1.2.0)
  - **Before**: Orchestrated five specialists (researcher, fundamental, technical, risk, advisor)
  - **After**: Orchestrates six specialists plus Devil's Advocate review before final report
  - **Added Step 6**: Devil's Advocate critical review with bear case development
  - **Context**: Automated workflow now includes mandatory objectivity check

- **Workflow (copilot-instructions.md)**: Updated from six-agent to seven-agent workflow with objectivity gate
  - **Before**: Orchestrator → Researcher → Fundamental/Technical → Risk → Advisor → Report
  - **After**: Orchestrator → Researcher → Fundamental/Technical → Risk → Advisor → Devil's Advocate → Report
  - **Added Step 6**: Devil's Advocate reviews for bias, overconfidence, blind spots
  - **Context**: Visualizes mandatory critical review phase before investor decision

- **README.md**: Updated agent count and workflow description
  - **Before**: Six agents (including orchestrator)
  - **After**: Seven agents including Devil's Advocate as objectivity gate
  - **Context**: Clarifies complete workflow including critical review for balanced perspective

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after Investment Advisor, before final investor decision
- **No Breaking Changes**: Existing agents and workflow remain valid; workflow extended with objectivity gate, not replaced
- **Objectivity Focus**: Devil's Advocate specializes in bearish scenario development and overconfidence detection—different from Risk Assessor's risk enumeration

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
