# Changelog

## [1.2.1] - 2025-12-27

### Fixed
- **Version History Removal**: Removed "Version History" sections from infrastructure files per meta-agent system standards
  - **Before**: copilot-instructions.md and README.md contained duplicate version history sections
  - **After**: Version history only in CHANGELOG.md (single source of truth)
  - **Rationale**: Prevents file bloat, eliminates duplication, aligns with agent file standards
  - **Files Changed**: copilot-instructions.md (removed lines 410-412), README.md (removed lines 246-250)
  - **Impact**: Documentation hygiene improvement, no functional changes

### Added
- **Send Default Policy Documentation**: Comprehensive documentation of handoff auto-send behavior
  - **What**: New "Send Default Policy" section in copilot-instructions.md explaining `send: true/false` patterns
  - **Policy**: Workflow advances require human confirmation (`send: false`), critical reviews auto-send (`send: true`)
  - **Rationale**: High-stakes funding decisions need checkpoints, but mandatory quality gates (devils-advocate) auto-send to prevent bypass
  - **Coverage**: Documents all handoff patterns, testing strategy, rollback plan
  - **Impact**: Transparency improvement (users understand when manual confirmation needed), no behavioral changes

- **REFERENCE.md Usage Guide**: Documentation of which agents should reference REFERENCE.md and why
  - **Current**: impact-evaluator and portfolio-strategist reference REFERENCE.md
  - **Recommended**: devils-advocate and recommendation-synthesizer should add REFERENCE.md links (v1.3.0)
  - **Rationale**: Both agents use SROI/CEA concepts but don't link to methodology documentation
  - **Impact**: Clarity improvement for future enhancements

- **Agent Size Monitoring**: Size distribution tracking and management strategy
  - **Current Distribution**: principles-framework-definer (26,716 chars), portfolio-strategist (26,071 chars) approaching limits
  - **Justification**: Size imbalance reflects complexity differences (core analytical agents vs supporting agents)
  - **Strategy**: Optimization plan, monitoring thresholds, potential split criteria documented
  - **Impact**: Proactive size management, prevents hitting 30k hard limit

- **Quality Checklist Standards**: Documentation of checklist size variation rationale
  - **Range**: 8-12 items per agent depending on complexity
  - **Justification**: Complex analytical agents need more verification items than focused functional agents
  - **Impact**: Explains checklist variation is intentional, not inconsistency

### Changed
- **Documentation Optimization**: Condensed newly added sections to meet 30k character limit for infrastructure files
  - **Before**: copilot-instructions.md was 31,400 characters (1,400 over 30k limit)
  - **After**: copilot-instructions.md is 23,499 characters (well under 30k limit)
  - **Method**: Condensed Send Default Policy, REFERENCE.md guide, and Agent Size sections while preserving essential information
  - **Impact**: Meets meta-agent system size requirements, improved readability through conciseness

### Context
Addresses philanthropic-advisory-issue-1-version-history-infrastructure.md specification and all Devil's Advocate critical review concerns:
- ✅ CRITICAL: Added missing send_default policy documentation
- ✅ MEDIUM: Documented REFERENCE.md underutilization and future enhancement plan
- ✅ MEDIUM: Explained handoff chain send: true/false consistency in policy section
- ✅ MINOR: Documented agent size imbalance rationale and monitoring strategy
- ✅ MINOR: Documented quality checklist variation standards
- ✅ ORIGINAL: Removed version history from infrastructure files
- ✅ SIZE COMPLIANCE: Optimized to meet 30k character limit (23,499 chars final)

## [1.1.2] - 2025-12-22

### Changed
- **Writing Style Guidelines**: Replaced embedded writing style guidelines in agent files with references to COMMON-PATTERNS.md
  - **Before**: marketing-content-writer.agent.md contained embedded style guidelines (~1400 characters)
  - **After**: Agent file references centralized guidelines in COMMON-PATTERNS.md (3 lines, ~150 characters)
  - **Impact**: Maintenance improvement (single source of truth), ~1250 characters saved, no functional changes

## [1.1.1] - 2025-12-22

### Changed
- **Examples Restoration**: Restored comprehensive examples (minimum 2 per agent with full input/output)
  - **Before**: Many agents had only 1 truncated example after size optimization (commit ee14332)
  - **After**: All agents now have 2+ complete examples demonstrating full workflow
  - **Impact**: Significantly improved agent clarity and usability while maintaining <30k character limit


All notable changes to the Philanthropic Advisory agent group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-12-21

### Added
- **Marketing Content Writer Agent**: New agent for creating marketing content and writeups for philanthropic programs
  - Generates website copy, social media posts, and program descriptions
  - Ensures content aligns with philanthropic framework from principles-framework-definer
  - Submits content to devils-advocate for critical review (mandatory quality gate)
  - Supports multiple content formats (short, medium, long) and platforms (LinkedIn, Facebook, Instagram, Twitter, website)
  - Adapts tone for different audiences (donors, beneficiaries, public, partners)
  - Uses Claude Haiku 4.5 (copilot) for creative writing tasks
  - Handoffs to devils-advocate (content review) and principles-framework-definer (clarification)
  - **Context**: Addresses need for consistent, principles-aligned marketing communications
  - **Use case**: Generate marketing content for approved programs, standalone content creation, pre-launch communications

### Changed
- **Agent Group Expansion**: Philanthropic-advisory now has seven agents (was six)
  - Core evaluation workflow unchanged (impact → portfolio → risk → synthesis → devils-advocate → decision)
  - Marketing-content-writer operates as optional agent, can be called independently or after evaluation
- **Documentation Updates**: Updated copilot-instructions.md, README.md to reflect new agent and expanded capabilities
  - Added decision tree option [H] for marketing content needs
  - Added Example 3 showing marketing content creation workflow
  - Updated agent count references from "six" to "seven"



## [1.0.0] - 2024-12-16

### Added
- **Impact Evaluator Agent**: Quantitative impact evaluation using SROI, CEA, and trajectory uplift frameworks for Singapore philanthropic programs
  - SROI calculation with deadweight, attribution, and drop-off adjustments
  - CEA analysis with benchmarking against comparable programs
  - Trajectory uplift assessment (baseline vs intervention)
  - Systemic impact scoring (upstream/midstream/downstream)
  - Data quality rating and measurement gap identification
  
- **Portfolio Strategist Agent**: Strategic fit and portfolio composition analysis
  - Mission alignment scoring (1-10 scale) with detailed rationale
  - Portfolio diversification analysis (intervention types, demographics, geographies)
  - Strategic gap identification and prioritization
  - Synergy mapping across funded programs
  - Concentration risk assessment and mitigation recommendations
  
- **Risk-Opportunity Analyst Agent**: Comprehensive risk assessment and opportunity identification
  - Five risk categories: implementation, financial, impact, external, organizational
  - Risk matrix with likelihood × impact ratings
  - Mitigation strategies with specific actions and owners
  - Upside opportunity identification (scaling, partnerships, policy influence)
  - Scenario analysis (pessimistic/realistic/optimistic) with confidence intervals
  - Exit and pivot strategy planning
  
- **Recommendation Synthesizer Agent**: Integrated funding recommendations
  - Synthesis of impact + portfolio + risk analyses
  - Clear recommendation (fund/decline/modify/pilot) with confidence level
  - Decision rationale with quantitative, strategic, and risk-adjusted cases
  - Trade-off transparency (what you gain vs what you accept)
  - Funding terms specification (amount, duration, conditions)
  - Monitoring framework with KPIs and early warning indicators
  - Implementation roadmap and exit strategy
  
- **Devil's Advocate Agent (MANDATORY)**: Critical review and assumption challenging
  - SROI/CEA methodology challenges with alternative interpretations
  - Strategic fit assumption questioning (mission alignment, gap analysis)
  - Risk assessment testing (optimism/pessimism balance)
  - Disagreement facilitation between agents
  - Blind spot identification (unconsidered perspectives)
  - Cultural and contextual challenge (Singapore-specific assumptions)
  - Questions for decision-maker preparation
  - Approval status (approved/needs revision/needs more data)
  
- **Infrastructure Files**:
  - `copilot-instructions.md`: Comprehensive workflow documentation with decision trees, quality gates, ROI frameworks, examples
  - `README.md`: Quick start guide, agent descriptions, usage patterns, troubleshooting
  - `CHANGELOG.md`: Version history and change tracking

### Features
- **Five-Agent Coordinated Workflow**: Sequential handoffs (impact → portfolio → risk → synthesis → devils-advocate) with feedback loops
- **Quantitative Rigor**: SROI and CEA frameworks standardized across agents, trajectory uplift methodology, data quality standards
- **Strategic Portfolio Management**: Mission alignment, gap analysis, synergy mapping, concentration risk assessment
- **Comprehensive Risk Management**: Multi-category risk matrix, mitigation strategies, scenario planning, exit strategies
- **Mandatory Critical Review**: Devils-advocate as final quality gate ensures assumptions challenged, disagreements surfaced, blind spots identified
- **Singapore Context Integration**: Demographics, policies, existing initiatives referenced throughout analyses
- **Handoff Object Format**: All agents use GitHub Copilot handoff schema (label, agent, prompt, send: false) for VSCode validation compliance
- **Quality Gates**: Five gates (impact complete, portfolio assessed, risk evaluated, recommendation synthesized, critical review complete) ensure thoroughness
- **Portable Structure**: Folder-agnostic, self-contained, consistent naming (all agents use Claude Sonnet 4.5 for high-stakes decisions)

### Context
Initial release focuses on Singapore philanthropic giving for at-risk communities (families in crisis, children from lower-income families) with measurable impact potential. All agents emphasize data-driven decision-making, transparency in assumptions, and balanced assessment of quantitative metrics vs strategic fit vs risk tolerance.

### Design Rationale
- **Five agents (not fewer)**: Separation of concerns (impact ≠ portfolio ≠ risk ≠ synthesis ≠ critical review) enables expertise depth in each domain
- **Claude Sonnet 4.5 for all agents**: High-stakes philanthropic decisions require highest-quality reasoning across all analytical domains
- **Mandatory Devil's Advocate**: Assumption challenging and disagreement surfacing essential for informed decision-making (philanthropists benefit from full picture, not just consensus)
- **Linear workflow with feedback loops**: Natural progression (impact → strategy → risk → synthesis → critical review) mirrors decision-making process, while devils-advocate can route back to any agent for revision

[1.0.0]: https://github.com/your-repo/philanthropic-advisory-agents/releases/tag/v1.0.0

## [1.1.0] - 2025-12-21

### Added
- **Principles & Framework Definer Agent**: New agent for establishing philanthropic principles and decision-making frameworks before program evaluation
  - Guides philanthropists through 8 predefined foundational question areas (values, beneficiaries, problem areas, theory of change, decision criteria, risk tolerance, portfolio strategy, non-negotiables)
  - Produces comprehensive framework documents with quantitative thresholds (SROI, cost-effectiveness, mission alignment)
  - Operates standalone (framework only) or integrates with philanthropic-advisory workflow (framework → evaluation)
  - Facilitates values articulation and strategic coherence before funding decisions
  - Singapore context integration (demographics, policies, landscape gaps)
  - Handoffs to impact-evaluator (with framework criteria) or devils-advocate (framework challenge)
  - **Context**: Addresses common philanthropist need to define clear principles before making ad-hoc funding decisions
  - **Use case**: Run principles-framework-definer first, establish criteria, then evaluate programs against explicit standards

- **Self-Update Capability**: Added via `update-from-upstream.sh` script
  - `UPDATING.md` documentation with complete guide for using the self-update feature
  - Support for direct downloads from GitHub repository using HTTP endpoints
  - GitHub token support for higher API rate limits (5000 req/hr vs 60 req/hr)
  - Automatic file discovery via GitHub API with intelligent fallback to common agent names
  - Portable design allowing agent group to be copied to other projects via `cp -r` and updating itself
  - Smart file handling: updates changed files, adds new files, preserves unchanged files
  - Intentional preservation of local script modifications (update-from-upstream.sh)

### Changed
- **Workflow Enhancement**: Philanthropic-advisory workflow now supports optional "framework definition first" path
  - Original workflow remains: Program → @impact-evaluator → ... (no framework needed)
  - New workflow option: @principles-framework-definer → Framework → Program → @impact-evaluator (uses framework criteria) → ...
  - **Context**: Flexible integration - philanthropists can define framework upfront or evaluate programs without explicit framework
- Added `AGENTGROUPNAME` file containing the group name for script auto-detection
- Enhanced error handling and logging in update process

## 1.0.1 - 2025-12-17

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
  - portfolio-strategist: now v1.0.1
  - impact-evaluator: now v1.0.1
  - risk-opportunity-analyst: now v1.0.1
  - recommendation-synthesizer: now v1.0.1
  - devils-advocate: now v1.0.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

