# Changelog

All notable changes to the Stock Investment Analysis Agent Group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-12-21

### Added
- Self-update capability via `update-from-upstream.sh` script
- `UPDATING.md` documentation with complete guide for using the self-update feature
- Support for direct downloads from GitHub repository using HTTP endpoints
- GitHub token support for higher API rate limits (5000 req/hr vs 60 req/hr)
- Automatic file discovery via GitHub API with intelligent fallback to common agent names
- Portable design allowing agent group to be copied to other projects via `cp -r` and updating itself
- Smart file handling: updates changed files, adds new files, preserves unchanged files
- Intentional preservation of local script modifications (update-from-upstream.sh)

### Changed
- Added `AGENTGROUPNAME` file containing the group name for script auto-detection
- Enhanced error handling and logging in update process

## [1.2.0] - 2024-12-17

### Removed
- **stock-analysis-orchestrator**: Removed orchestrator agent to simplify workflow
  - **Rationale**: The orchestrator added complexity by creating dual workflow modes (orchestrated vs manual). Users had to choose between two approaches, adding cognitive overhead.
  - **Impact**: Group reduced from 7 to 6 agents. All analytical capabilities preserved.
  - **New workflow**: Single sequential workflow starting with stock-researcher. Users follow handoff chain naturally.
  - **Migration**: Users who previously used orchestrator should start with stock-researcher and follow handoffs. All analytical depth remains unchanged.

### Changed
- **copilot-instructions.md**: Updated to reflect single workflow mode
  - Removed "Workflow Options" section documenting dual modes
  - Removed orchestrator agent description
  - Updated workflow diagrams to show single sequential path
  - Simplified decision trees to remove workflow selection
  - Updated version to 1.2.0
- **README.md**: Updated to remove orchestrator references and updated version history
- **devils-advocate.agent.md**: Removed handoff references to deleted orchestrator agent

### Deprecated
- Versions 1.3.x below contain planned changes for stock-analysis-orchestrator which was removed in this version. These entries are preserved for historical record but the features described no longer exist.

---

## [1.3.1] - 2024-12-17 [OBSOLETE - orchestrator removed in 1.2.0]

### Changed
- **stock-analysis-orchestrator**: Clarified Response Format section to mandate agent outputs are included (not omitted)
  - **Before**: Response Format showed "Key highlights from [agent]" for sections 1-4, which could be interpreted as optional or that outputs could be omitted
  - **After**: All five sections now explicitly state "Output from [agent] - include [key details]" to require presence of agent outputs
  - **Context**: Fixes issue where agent outputs were not appearing in final reports. Outputs must exist but can be in complete or summarized form as appropriate for the analysis
  - **Migration**: No breaking changes—existing reports remain valid. Future reports must include outputs from all specialist agents.

### Added
- **stock-analysis-orchestrator**: Report Filename Format specification in Response Format section
  - **Format**: `{Ticker}-{Date}.md` for single stocks, `{Ticker1}-vs-{Ticker2}-{Date}.md` for comparisons
  - **Requirements**: Uppercase ticker, YYYY-MM-DD date format, .md extension, hyphen separators
  - **Examples**: `NVDA-2024-12-15.md` (single), `AAPL-vs-MSFT-2024-12-14.md` (comparison)
  - **Rationale**: Consistent naming enables easy date sorting, quick ticker identification, and historical tracking
  - **Context**: Standardizes report filenames across all orchestrator outputs for better organization

- **stock-analysis-orchestrator**: Expanded Example 1 (NVDA) to demonstrate comprehensive output format
  - **Before**: Stock Research Summary showed abbreviated content (~20 lines, "highlights" style)
  - **After**: Stock Research Summary shows comprehensive agent output with all subsections (Company Overview, Financial Performance, Balance Sheet, Competitive Position, Industry Context, Growth Drivers, Management, Citations) spanning ~150 lines
  - **Context**: Provides concrete example of comprehensive output for implementers to follow
  - **Note**: Other example sections (Fundamental, Technical, Risk, Advisor) remain as representative excerpts for readability

- **stock-analysis-orchestrator**: Added filenames to Examples 1 and 2
  - Example 1 (NVDA): `NVDA-2024-12-15.md`
  - Example 2 (AAPL vs MSFT): `AAPL-vs-MSFT-2024-12-14.md`
  - **Context**: Demonstrates standardized filename format in practice

### Fixed
- **stock-analysis-orchestrator**: Ambiguous output inclusion language that led to missing agent outputs
  - **Issue**: "Key highlights" phrasing was unclear and led to agent outputs not appearing in final reports
  - **Resolution**: Explicit "Output from [agent]" language requiring presence of agent outputs in all sections
  - **Impact**: Ensures reports include outputs from all specialist agents, which can be comprehensive or summarized as appropriate

## [1.3.0] - 2024-12-15

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

## [1.2.0] - 2024-12-15

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

## 1.3.1 - 2024-12-17

### Added
- **Writing Style Guidelines**: All agents now include comprehensive writing style guidelines to ensure natural, human-like output
  - Added 9 core principles for natural writing (varied sentence structures, direct language, active voice, natural transitions, etc.)
  - Principle 9 specifically addresses AI-typical punctuation (avoid em-dashes, limit semicolons/colons)
  - Guidelines positioned after Domain Context section in all agent files
  - Ensures all agent outputs avoid robotic, AI-detectable patterns
  - **Context**: Aligns all agent groups with meta-agent system v1.6.1/1.7.1 standards for human-like communication
  - **Migration**: No breaking changes. Existing usage patterns remain valid. Agents will now produce more natural-sounding output.

### Changed
- **Version Numbers**: All agents bumped to next patch version
  - stock-analysis-orchestrator: now v1.3.1
  - stock-researcher: now v1.3.1
  - fundamental-analyst: now v1.3.1
  - technical-analyst: now v1.3.1
  - risk-assessor: now v1.3.1
  - investment-advisor: now v1.3.1
  - devils-advocate: now v1.3.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

