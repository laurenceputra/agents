# Changelog

All notable changes to the Meta-Agent System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.5.0 - 2025-12-26

### Changed
- **Issue #9: Workflow Agent Scope Creep - Refactored Architect and Implementer**: Extracted workflow orchestration from agents to centralize in copilot-instructions.md
  - **Problem**: Architect (29k chars) and Implementer (26k chars) bloated with workflow orchestration details, approaching 30k limit
  - **Solution**: Separated "what to do" (agent responsibilities) from "how to orchestrate" (workflow coordination)
  - **Changes**:
    - **Agent Architect (v2.2.0 → v2.3.0)**:
      - Reduced from 29,110 to 14,575 characters (50% reduction, saved ~14.5k)
      - Removed detailed workflow diagrams, phase descriptions, gate specifications
      - Removed lengthy template sections and redundant troubleshooting
      - Kept core responsibilities, specification design process, model recommendations
      - Added "Workflow Position" section referencing copilot-instructions.md
      - Streamlined examples to condensed format
    - **Agent Implementer (v2.1.0 → v2.2.0)**:
      - Reduced from 26,371 to 13,891 characters (47% reduction, saved ~12.5k)
      - Removed detailed workflow steps (Workflow A/B), extensive infrastructure specs
      - Removed redundant template sections and verbose formatting guidelines
      - Kept core responsibilities, implementation standards, validation requirements
      - Added "Workflow Position" section referencing copilot-instructions.md
      - Streamlined documentation requirements section
    - **copilot-instructions.md**:
      - Enhanced from 19,725 to 25,450 characters (added ~5.7k)
      - Added comprehensive "Workflow Orchestration Details" section
      - Documented phase transitions and handoff mechanics
      - Added feedback loop handling patterns
      - Added branch management guidance
      - Added character count management workflow
      - Expanded troubleshooting guide with 10+ scenarios
  - **Rationale**: Centralized orchestration provides single source of truth, agents stay focused on capabilities
  - **Impact**: Total system reduction of ~21k characters, agents well under 20k target with 10k buffer for growth
  - **Benefits**:
    - Easier maintenance: Workflow changes update 1 file (copilot-instructions.md) not 5 agents
    - Better clarity: Agents read faster with less workflow noise
    - Future-proof: Both agents have 15k+ characters buffer under 30k limit

## 2.4.0 - 2025-12-26

### Fixed
- **Issue #3: Handoff Chain Inconsistency (Option 2b)**: Fixed workflow gap where Devil's Advocate Phase 1.5 approval had no clear path forward
  - **Root Cause**: Workflow showed DA reviewing specs, but Architect had direct handoff to Implementer that bypassed DA, and DA had no approval handoff
  - **Solution**: Implemented Option 2b (Architect orchestrates with explicit approval)
  - **Changes**:
    - **Agent Architect (v2.1.0 → v2.2.0)**:
      - Added back "Hand to Implementer (after Devil's Advocate approval)" handoff with clear usage instructions
      - Updated "Workflow Enforcement" section with Phase 1 → 1.5 → 2 transition instructions
      - Added guidance on when to use Implementer handoff (after DA approval)
      - Updated Integration Points to reflect DA as primary handoff, Implementer as secondary
      - Updated Feedback Loops to document DA approval status handling
    - **Devil's Advocate (v2.0.0 → v2.1.0)**:
      - Added "Return to Architect with approval (Phase 1.5)" handoff
      - Updated Phase 1.5 responsibilities to clarify approval decision path
      - Now has explicit handoff for both critical issues AND approval scenarios
    - **copilot-instructions.md**:
      - Updated workflow diagram to show DA returns to Architect, who then invokes Implementer
      - Updated Phase 1.5 decision point documentation
      - Updated Architect and Devil's Advocate descriptions in Five Meta-Agents section
  - **Rationale**: Separates review (DA's job) from orchestration (Architect's job), keeps DA focused on critical analysis
  - **Impact**: Resolves workflow deadlock where Phase 1.5 approval had no documented next step

- **Issue #8: Devil's Advocate Model Clarification (Option C)**: Updated model rationale to be more general and future-proof
  - **Problem**: Model rationale didn't mention new `send_default` policy review responsibility
  - **Solution**: Generalized rationale to cover current and future responsibilities without needing updates
  - **Change**: Updated "Recommended Model" section in Devil's Advocate (v2.1.0)
  - **New Rationale**: Emphasizes general capabilities (nuanced judgment, multi-criteria policy evaluation, risk assessment) rather than specific task lists
  - **Benefit**: Model rationale now covers Phase 1.5 and Phase 3.5 duties without requiring updates when responsibilities expand

### Changed
- **Workflow Pattern**: Phase 1.5 approval requires Architect to use designated "Hand to Implementer (after Devil's Advocate approval)" handoff for controlled transition
- **Handoff Chains**: All specification workflows route through Architect after DA review, with clear handoff mechanism for proceeding to implementation

## 2.3.0 - 2025-12-26

### Added
- **Default Handoff Policy Documentation**: Added comprehensive "Default Handoff Policy" section to copilot-instructions.md
  - Documented `send_default: true` for meta-agent group with rationale
  - Rationale: Meta-agents prioritize velocity and automation for agent infrastructure work, with human oversight at quality gates
  - Testing & Observability: Specified testing plan, observability metrics, and rollback plan
  - Migration Note: Clarified no user behavior changes required
  - Resolves meta-agent-issue-2: architect-send-default-missing specification

### Changed
- **copilot-instructions.md**: Added 16-line "Default Handoff Policy" section after "Core Principle"

## 2.2.0 - 2025-12-22

### Added
- **Character Limit Enforcement**: GitHub Copilot enforces a 30,000 character hard limit on agent files
  - **Agent Architect**: Designs concise specifications (target 15,000-20,000 characters), flags specifications approaching 25,000 characters, recommends agent splits for complex specifications
  - **Agent Implementer**: Validates character count before completion, alerts if agent exceeds 25,000 characters (yellow flag) or 30,000 characters (red flag), provides optimization recommendations
  - **Quality Reviewer**: Verifies character count under 30,000 (CRITICAL), flags for optimization if exceeding 25,000, rejects with critical feedback if over 30,000
  - **Size Management Guidelines**: Added to COMMON-PATTERNS.md with character count targets, validation requirements, and optimization strategies
  - **Checking Command**: `wc -c path/to/agent.agent.md` documented for character count validation

- **Version History Prohibition Enforcement**: Agents must not contain version history sections
  - **Rationale**: Version history accumulates over time, bloats file size, duplicates CHANGELOG.md content, makes agents harder to read
  - **Enforcement**: Architect specifications exclude version history sections, Implementer does not create them, Quality Reviewer rejects implementations with version history (CRITICAL)
  - **Single Source of Truth**: All version tracking managed in CHANGELOG.md only
  - **Exception**: COMMON-PATTERNS.md (reference document, not agent) may contain version history

### Changed
- **Agent File Structure**: Updated from 11 to 10 required sections (removed Version History as section 11)
  - **COMMON-PATTERNS.md**: Updated Agent File Structure documentation, added explicit prohibition and character limit guidance
  - **copilot-instructions.md**: Added "Size and Versioning Constraints" section, updated Quality Gates with new validation checks, changed reference from 11 to 10 sections

- **Agent Architect (v2.0.0 → v2.1.0)**:
  - Added conciseness guidance to Responsibilities section
  - Added "Size Guidance" section to specification output template
  - Specification template now includes size targets and guidance
  
- **Agent Implementer (v2.0.0 → v2.1.0)**:
  - Updated Quick Validation Checklist to include version history check and character count validation
  - Added character count validation steps to both individual and group workflows
  - Updated Responsibilities to include character count validation and version history prohibition
  - Workflow Step 2.5 added: Validate Character Count with `wc -c` command
  - Submit to Quality Reviewer step now includes character count reporting
  
- **Quality Reviewer (v2.0.0 → v2.1.0)**:
  - Added version history check and character count validation to Responsibilities
  - Updated Review Standards to include new critical issues (version history present, >30,000 characters)
  - Added "Character Count Validation" section to Output Format
  - Updated Step 1 of Response Format to include version history and character count checks
  - Updated Quality Checklist with three new critical validations at top of list

### Files Modified
- `.github/agents/COMMON-PATTERNS.md`: Updated Agent File Structure (11→10 sections), added Size Management Guidelines section with character count targets, validation requirements, optimization strategies, version history prohibition, and checking command
- `.github/copilot-instructions.md`: Added "Size and Versioning Constraints" section (64 lines), updated Quality Gates with new validation checks, updated Common Patterns Reference (11→10 sections)
- `.github/agents/architect.agent.md`: Added conciseness guidance to Responsibilities, added Size Guidance section to specification template, version bumped to 2.1.0
- `.github/agents/implementer.agent.md`: Updated Portable Output Standards and Quick Validation Checklist, added character count validation to Responsibilities and workflows, added Step 2.5 for character count validation, version bumped to 2.1.0
- `.github/agents/quality-reviewer.agent.md`: Added version history and character count checks to Responsibilities, updated Review Standards, added Character Count Validation section, updated Quality Checklist, version bumped to 2.1.0
- `.github/CHANGELOG.md`: Added 2.2.0 entry documenting all changes

### Rationale
GitHub Copilot has a hard 30,000 character limit for agent files:
- **Problem**: Files exceeding this limit fail to load in GitHub Copilot with no warning during development
- **Solution**: Proactive enforcement in meta-agent workflow at specification, implementation, and review stages
- **Size Management**: Target 15,000-20,000 characters, yellow flag at 25,000, hard limit at 30,000
- **Optimization Strategies**: Reduce example verbosity, consolidate sections, extract to README, split agents
- **Version History Impact**: Removing version history sections is the most impactful size reduction strategy (reclaims thousands of characters per agent)

### Success Criteria
1. 100% of new agent implementations pass version history check (no version history sections)
2. 100% of new agent implementations comply with 30,000 character limit
3. Size issues caught by Implementer before Quality Reviewer in 80%+ of cases
4. Implementers receive actionable optimization guidance when agents approach limits
5. Zero agents fail to load in GitHub Copilot due to size limits

## 2.1.0 - 2025-12-22

### Changed
- **Removed Version History from Agent Files**: Version history now exclusively maintained in CHANGELOG.md files
  - **Before**: Duplicate version history sections in every agent file (51 agent files × 3-8 lines = ~300 lines duplication)
  - **After**: Agent files reference CHANGELOG.md; version tracking centralized in project-level CHANGELOG.md files
  - **Impact**: Reduces agent file size, eliminates duplication, single source of truth for version history
  - **Migration**: All version history removed from `.github/agents/*.agent.md` and all agent group agent files; refer to CHANGELOG.md for version information

- **Removed Reference Content from copilot-instructions.md**: Extracted non-instructional content to appropriate homes
  - **Removed Sections**:
    - "Best Practices" (GitHub Copilot reference documentation) - belongs in GitHub Copilot official docs
    - "Tips for Effective Agents" (design guidance) - belongs in COMMON-PATTERNS.md or agent specifications
    - "Version History" (version tracking) - belongs in CHANGELOG.md
  - **Before**: copilot-instructions.md was 388 lines (workflow instructions mixed with reference content)
  - **After**: copilot-instructions.md is 351 lines (pure workflow instructions and specifications)
  - **Result**: Clear focus on actionable workflow guidance vs. design reference material

### Files Modified
- `.github/copilot-instructions.md`: Removed Best Practices, Tips for Effective Agents, Version History sections
- `.github/agents/architect.agent.md`: Removed 9-line Version History section
- `.github/agents/implementer.agent.md`: Removed 2 version history template sections (7 lines total)
- `.github/agents/quality-reviewer.agent.md`: Removed 1-line Version History section
- `.github/agents/pr-manager.agent.md`: Removed 1-line Version History section
- `.github/agents/devils-advocate.agent.md`: Removed 3-line Version History section
- **Agent Groups**: Removed Version History sections from 45 agent group agent files across 10 groups:
  - social-media-team (5 agents): ~9 lines removed
  - philanthropic-advisory (6 agents): ~10 lines removed
  - holiday-itinerary-planning (6 agents): ~10 lines removed
  - corporate-team-building (5 agents): ~9 lines removed
  - portfolio-analysis (3 agents): ~6 lines removed
  - legacy-planning (5 agents): ~10 lines removed
  - stock-investment-analysis (6 agents): ~12 lines removed
  - recommendation-letter (4 agents): ~8 lines removed
  - product-development-agents (5 agents): ~10 lines removed

### Rationale
Version history in agent files creates maintenance burden and duplication:
1. **Duplication**: 51 agent files each maintain their own version history (51 × 3-8 lines = ~300 lines total)
2. **Inconsistency**: Different agents use different version formats and detail levels
3. **Single Source of Truth**: Project CHANGELOG.md already documents all changes; agent files duplicate this
4. **Agent File Focus**: Version history distracts from core agent instructions and responsibilities
5. **Maintenance**: Updating version information requires changes across 51 files instead of 1 centralized location

CHANGELOG.md files now serve as the definitive version history source for each project:
- `.github/CHANGELOG.md`: Meta-agent system versions (architect, implementer, quality-reviewer, pr-manager, devils-advocate)
- `{agent-group}/CHANGELOG.md`: Individual agent group versions

## 2.0.0 - 2025-12-17

### Changed
- **BREAKING: Validator Split into Two Specialized Agents**: Split validator.agent.md (2261 lines) into quality-reviewer.agent.md (618 lines) and pr-manager.agent.md (385 lines)
  - **Before**: Single Validator agent handled both quality review and PR management (2261 lines, causing context loss)
  - **After**: Quality Reviewer focuses on implementation quality, PR Manager handles PR logistics (1003 lines total, 56% reduction)
  - **Breaking Change**: Users must use @quality-reviewer for reviews, @pr-manager for PR submission
  - **Workflow**: Implementer → Quality Reviewer → Devil's Advocate → PR Manager → PR
  - **Migration**: Replace @agent-validator with @quality-reviewer for quality reviews, @pr-manager for PR coordination

### Added
- **COMMON-PATTERNS.md Reference Document**: Extracted common patterns, schemas, and guidelines to reduce duplication
  - **Content**: Frontmatter schema, agent file structure, writing style guidelines, model recommendations, changelog format
  - **Purpose**: Single source of truth for shared patterns across all meta-agents
  - **Location**: `agents/COMMON-PATTERNS.md` (146 lines)
  - **Impact**: Reduces redundancy in agent files, simplifies maintenance

- **quality-reviewer.agent.md**: New agent for quality review responsibilities
  - **Responsibilities**: Reviews implementations for quality, completeness, best practices
  - **Model**: Claude Sonnet 4.5 (copilot)
  - **Handoffs**: To Implementer (revisions), Architect (spec issues), PR Manager (approval)
  - **Size**: 618 lines (vs original Validator's 2261 lines)

- **pr-manager.agent.md**: New agent for PR management responsibilities
  - **Responsibilities**: Creates PR details files, coordinates Devil's Advocate review, submits PRs
  - **Model**: Claude Haiku 4.5 (copilot)
  - **Handoffs**: To Quality Reviewer (more review), Devil's Advocate (critical review)
  - **Size**: 385 lines

### Fixed
- **Complexity Reduction - copilot-instructions.md**: Simplified from 1542 lines to 388 lines (75% reduction)
  - **Removed**: Redundant workflow details (duplicated in agent files), verbose decision trees, duplicate version history sections
  - **Consolidated**: Agent descriptions (97 → 40 lines), workflow diagram (163 → 60 lines), workflows (645 → 200 lines), decision trees (187 → 80 lines)
  - **Extracted**: Common patterns moved to COMMON-PATTERNS.md, troubleshooting moved to README.md
  - **Result**: Clearer focus on essential workflow, easier to understand and navigate

- **Agent File Size Reduction**: Reduced total agent size by 44% (7039 → 3912 lines)
  - **architect.agent.md**: 988 → 950 lines (4% reduction) - references COMMON-PATTERNS.md for schemas
  - **implementer.agent.md**: 1419 → 1382 lines (3% reduction) - references COMMON-PATTERNS.md for portable standards
  - **devils-advocate.agent.md**: 829 → 831 lines (stable) - updated references to quality-reviewer and pr-manager
  - **validator.agent.md**: REMOVED (2261 lines) - replaced by quality-reviewer + pr-manager
  - **quality-reviewer.agent.md**: NEW (618 lines) - quality review focus
  - **pr-manager.agent.md**: NEW (385 lines) - PR logistics focus
  - **COMMON-PATTERNS.md**: NEW (146 lines) - shared patterns reference

### Migration Guide

#### For All Users
- **Workflow Change**: Use @quality-reviewer for implementation reviews (not @agent-validator)
- **PR Submission**: @pr-manager handles PR coordination and submission
- **Complete Flow**: Implementer → Quality Reviewer → Devil's Advocate → PR Manager → PR

#### For Agent Groups
- Update handoffs from `agent-validator` to `quality-reviewer` (for quality feedback)
- Update handoffs for PR submission to `pr-manager` (for PR coordination)
- See COMMON-PATTERNS.md for frontmatter schema and portable structure

#### For Documentation
- Reference COMMON-PATTERNS.md for frontmatter schema, writing guidelines, changelog format
- copilot-instructions.md now focuses on workflow overview
- README.md includes troubleshooting (moved from copilot-instructions.md)

### Context
This breaking change addresses complexity issues causing context loss during agent development. By splitting the Validator's dual responsibilities (quality review + PR management) into two focused agents and extracting common patterns to a shared reference, the system is now 40-50% smaller while maintaining all quality gates and workflow integrity.

### Version Numbers
- **All meta-agents**: Updated to 2.0.0 (breaking change)
- **Infrastructure**: copilot-instructions.md 1.5.1 → 2.0.0, README.md 1.5.0 → 2.0.0

## 1.6.4 - 2025-12-17

### Fixed
- **Agent Validator Workflow Steps: Enforced Devil's Advocate Review Gate**: Fixed Steps 3b and 5b to prevent PR creation without Devil's Advocate review
  - **Issue**: Steps 3b ("Approved → Submit PR") and 5b showed Validator creating PR immediately after approval, bypassing Devil's Advocate review
  - **Root Cause**: Workflow steps not updated when Devil's Advocate gate was added in v1.5.0
  - **Fixed Sections**:
    - **Step 3b (Individual Agent)**: Changed from "Approved → Submit PR" to "Approved → Handoff to Devil's Advocate" with 6-step sequence including Devil's Advocate review
    - **Step 5b (Agent Group)**: Changed from "Approved → Submit PR" to "Approved → Handoff to Devil's Advocate" with 6-step sequence including Devil's Advocate review
    - **PR Details File Template**: Split "APPROVED" status into two states: "APPROVED BY VALIDATOR" (awaiting Devil's Advocate) and "APPROVED FOR PR SUBMISSION" (both approvals complete)
    - **When to Update PR Details**: Added "After Devil's Advocate Approval" section with steps for final status update
    - **Example 3**: Updated security scanner example to show complete workflow with Devil's Advocate review step between Validator approval and PR submission
  - **Before**: Steps 3b/5b showed direct path from Validator approval to human creating PR, bypassing Devil's Advocate
  - **After**: Steps 3b/5b explicitly show handoff to Devil's Advocate as mandatory gate before PR submission
  - **Context**: Every implementation MUST pass through Devil's Advocate critical review before PR submission. This is a mandatory quality gate that cannot be skipped.
  - **Migration**: No breaking changes. Clarifies enforcement of existing Devil's Advocate workflow requirement introduced in v1.5.0.

## 1.6.3 / 1.7.3 - 2025-12-17

### Fixed
- **Workflow Documentation: PR Timing Clarity**: Corrected misunderstanding about when Validator and Devil's Advocate reviews occur
  - **Issue**: Documentation implied reviews happened after PR creation, causing agents to push branches and create PRs before reviews were complete
  - **Root Cause**: Phase 3 "Path C: Approved → PR Submission" showed Validator creating PR immediately after approval without Devil's Advocate review step
  - **Fixed Sections**:
    - **Phase 3 (Path C)**: Changed from "Approved → PR Submission" to "Approved → Handoff to Devil's Advocate" with explicit note to see Phase 4
    - **Phase 4**: Added complete "Critical Review (Devil's Advocate)" section to both Individual Agent Workflow and Agent Group Workflow
    - **BRANCH WORKFLOW diagram**: Added "Critical Review by Devil's Advocate" step between "Validation Review" and "PR Submission"
    - **Workflow Rules**: Added Rule 6 clarifying reviews happen ON THE BRANCH before PR creation
    - **Workflow Rules**: Updated Rule 7 to show complete sequence: Validator approves → Devil's Advocate approves → Validator submits PR → Human reviews PR
  - **Before**: Documentation suggested creating PR after Validator approval, with reviews happening during PR process
  - **After**: Documentation explicitly states all reviews (Validator + Devil's Advocate) complete on feature branch before PR submission
  - **Context**: PR submission is the final step after all agent reviews are complete. The PR is for human decision-makers who need full context (including Devil's Advocate writeup) to make informed decisions.
  - **Migration**: No breaking changes. Clarifies existing workflow intent. Agents should complete all review cycles on feature branch before Validator creates PR.

## 1.6.2 / 1.7.2 - 2025-12-17

### Added
- **AI-Typical Punctuation Warning**: Added 9th writing principle warning against AI-typical punctuation patterns
  - **Agent Architect (v1.7.1 → 1.7.2)**:
    - Added principle 9: "Avoid AI-typical punctuation" - no em-dashes at all (use hyphens instead), avoid overusing semicolons/colons
    - Updated specification templates to require 9 principles (was 8)
    - Updated Quality Checklists (individual and group) with new criterion: "No AI-typical punctuation"
    - Context: Specifications will now require agents to avoid em-dashes entirely and limit semicolons/colons
  - **Agent Implementer (v1.6.1 → 1.6.2)**:
    - Added principle 9: "Avoid AI-typical punctuation" to Writing Style Guidelines
    - Updated agent definition template to ban em-dashes (recommend hyphens instead)
    - Updated Quality Checklists (individual and group) with "No AI-typical punctuation" criterion
    - Context: Agents created will automatically warn against em-dashes and excessive semicolons/colons
  - **Agent Validator (v1.6.1 → 1.6.2)**:
    - Added principle 9: "Avoid AI-typical punctuation" to Writing Style Guidelines
    - Updated Quality Checklists (individual and group) to verify no em-dashes used
    - Updated validation criteria from 8 to 9 core principles
    - Context: Validator will verify agents don't use em-dashes and limit semicolons/colons
  - **Devil's Advocate (v1.6.1 → 1.6.2)**:
    - Added principle 9: "Avoid AI-typical punctuation" to Writing Style Guidelines
    - Updated Quality Checklist to verify no em-dashes
    - Context: Critical reviews will avoid em-dashes entirely
  - **Before**: No guidance on punctuation patterns that make text appear AI-generated
  - **After**: All meta-agents and created agents now instructed to never use em-dashes (use hyphens instead), avoid overusing semicolons/colons (stick to periods and commas for most sentences)
  - **Migration**: No breaking changes. Existing agents remain valid. New agents will include stricter punctuation guidance.

## 1.6.1 / 1.7.1 - 2025-12-17

### Added
- **Writing Style Guidelines Propagation**: Meta-agents now ensure all created agents follow natural writing principles
  - **Agent Architect (v1.7.0 → 1.7.1)**: 
    - Specification templates now include "Writing Style Guidelines" section requirement for created agents
    - Added 8 core principles and agent-specific examples requirement to specifications
    - Quality Checklist updated with 2 new criteria verifying specifications include writing style guidelines
    - Context: Ensures agents created by meta-agents inherit natural, human-like output standards
  - **Agent Implementer (v1.6.0 → 1.6.1)**:
    - Agent definition template now includes "Writing Style Guidelines" section with 8 principles and placeholder for agent-specific examples
    - Quality Checklist template includes 8 human-like output criteria
    - Quality Checklist updated with 2 new criteria verifying created agents include writing style guidelines
    - Context: All new agents will automatically include writing style guidance
  - **Agent Validator (v1.6.0 → 1.6.1)**:
    - Quality Checklist updated with 3 new criteria verifying agents include Writing Style Guidelines section, agent-specific examples, and quality checklist style criteria
    - Both individual and group validation checklists enhanced
    - Context: Validation now catches missing writing style guidance during review
  - **Devil's Advocate (v1.6.0 → 1.6.1)**:
    - Version bump for consistency with other meta-agents (no functional changes)
  - **Migration**: No breaking changes. Existing agents remain valid. New agents created by meta-agents will automatically include Writing Style Guidelines.

## 1.6.0 / 1.7.0 - 2025-12-17

### Changed
- **Human-Like Output Enhancement**: All four meta-agents updated to produce more natural, human-like outputs that avoid AI-detectable patterns
  - **Before**: Agents produced outputs with excessive hedging, robotic language, repetitive sentence structures, and overly formal tone
  - **After**: Agents now write with varied sentence structures, natural conversational tone, direct statements, and appropriate informality while maintaining technical precision
  - **Context**: Addresses AI detection concerns by eliminating common patterns (excessive "may/might/could/potentially", passive voice, formulaic transitions, rigid templates) without sacrificing quality or accuracy
  - **Migration**: No action required - agents will automatically produce more natural outputs. Existing agent implementations remain valid. Users will notice more readable, conversational outputs from all meta-agents.

- **Agent Architect (architect.agent.md v1.6.2 → 1.7.0)**:
  - Added "Writing Style Guidelines" section with 8 principles for natural language output and anti-patterns to avoid
  - Updated Quality Checklist with 8 new human-like output criteria (varied sentence structure, natural tone, appropriate informality, direct statements, mixed formats, active voice, varied transitions, natural flow)
  - Updated Version History with v1.7.0 entry
  - Technical specifications and design capabilities unchanged - only output style enhanced

- **Agent Implementer (implementer.agent.md v1.5.1 → 1.6.0)**:
  - Added "Writing Style Guidelines" section with 8 principles for natural language and implementation-specific examples
  - Updated Quality Checklist (both individual and group) with 8 human-like output criteria
  - Updated Version History with v1.6.0 entry
  - Implementation workflow and requirements unchanged - only output style enhanced

- **Agent Validator (validator.agent.md v1.5.1 → 1.6.0)**:
  - Added "Writing Style Guidelines" section with 8 principles for natural validation feedback and reviewer-specific examples
  - Updated Quality Checklist (both individual and group) with 8 human-like output criteria
  - Updated Version History with v1.6.0 entry
  - Validation standards and criteria unchanged - only feedback style enhanced

- **Devil's Advocate (devils-advocate.agent.md v1.5.1 → 1.6.0)**:
  - Added "Writing Style Guidelines" section with 8 principles for natural critical review and skeptic-specific examples
  - Updated Quality Checklist with 8 human-like output criteria
  - Updated Version History with v1.6.0 entry
  - Critical review responsibilities and standards unchanged - only output style enhanced

## 1.5.1 - 2025-12-16

### Fixed
- **Workflow Automation**: Added explicit handoff steps to Response Format sections to enable automatic workflow continuation
  - **Issue 1**: Devil's Advocate was creating separate review files instead of only providing conversational output (PR details managed by Validator)
  - **Issue 2**: Users had to manually invoke Validator and Devil's Advocate instead of automatic handoffs completing the workflow
  - **Root Cause**: Response Format sections did not explicitly instruct agents to use handoffs as final step, leading to manual workflow triggers
  - **Fixed Agents**:
    - `devils-advocate.agent.md` (v1.5.0 → v1.5.1): Clarified Output Format (creates no files, all output conversational) and added Step 6 "Execute Handoff" to Response Format
    - `validator.agent.md` (v1.5.0 → v1.5.1): Clarified Output Format (creates/manages `.pr_details/{branch-name}.md`) and added Step 7/9 "Execute Handoff" to Response Format (individual/group)
    - `implementer.agent.md` (v1.5.0 → v1.5.1): Added Step 5/6 "Submit to Validator" to Response Format (individual/group) with explicit handoff instruction
    - `architect.agent.md` (v1.6.1 → v1.6.2): Version bump for consistency (no functional changes)
  - **Migration**: Agents will now automatically hand off work to next agent in workflow without manual user invocation

### Changed
- **Devil's Advocate (devils-advocate.agent.md)**: Clarified file management responsibilities
  - **Before**: Output Format implied separate review files might be created
  - **After**: Explicitly states Devil's Advocate creates zero files - all output is conversational until PR approval, then provides writeup for Validator to add to `.pr_details/`
  - **Context**: PR details are exclusively managed by Agent Validator throughout review process
  - **Updated Sections**:
    - **Output Format**: Added "IMPORTANT" note clarifying no files created, file management by Validator
    - **Response Format**: Added Step 6 "Execute Handoff" with conditional logic (to Validator/Implementer/Architect)
    - **Example 3**: Added note showing handoff workflow automation
    - **Version History**: Added v1.5.1 entry

- **Agent Validator (validator.agent.md)**: Clarified PR details file management
  - **Before**: Output Format didn't explicitly state Validator creates/manages `.pr_details/` files
  - **After**: Explicitly states Validator creates `.pr_details/{branch-name}.md` at review start and updates throughout process
  - **Context**: Ensures clear ownership of PR details file management (not Devil's Advocate or Architect)
  - **Updated Sections**:
    - **Output Format**: Added "IMPORTANT" note clarifying Validator manages `.pr_details/{branch-name}.md`
    - **Response Format**: Added Step 7/9 "Execute Handoff" with conditional logic (to Implementer/Architect/Devil's Advocate)
    - **Version History**: Added v1.5.1 entry

- **Agent Implementer (implementer.agent.md)**: Added explicit handoff instruction
  - **Before**: Response Format ended at "Validation Notes" without explicit handoff instruction
  - **After**: Added Step 5/6 "Submit to Validator" requiring handoff after implementation complete
  - **Context**: Enables workflow automation - Validator automatically invoked after implementation
  - **Updated Sections**:
    - **Response Format**: Added Step 5 (individual) and Step 6 (group) "Submit to Validator" with handoff requirement
    - **Version History**: Added v1.5.1 entry

- **Agent Architect (architect.agent.md)**: Version bump for consistency
  - **Before**: v1.6.1
  - **After**: v1.6.2 (patch bump for consistency with meta-agent group refactor)
  - **Context**: No functional changes - version bump to align with other meta-agents' workflow automation changes
  - **Updated Sections**:
    - **Version History**: Added v1.6.2 entry documenting the version bump

### Migration Guide

#### For All Meta-Agent Users
Workflow will now automatically continue through handoffs without manual agent invocation:
1. **Implementer** completes work → automatically hands to **Validator** (no manual `@agent-validator` needed)
2. **Validator** reviews → automatically hands to **Implementer** (feedback) or **Devil's Advocate** (approved)
3. **Devil's Advocate** reviews → automatically hands to **Validator** (PR ready) or **Implementer** (revisions)
4. **No action required** - handoffs are automatic if agents follow their Response Format sections

#### For Devil's Advocate Users
If you were expecting separate Devil's Advocate review files:
1. **Stop expecting separate files** - Devil's Advocate output is conversational only
2. **PR details in `.pr_details/{branch}.md`** - managed by Validator, includes Devil's Advocate writeup when approved
3. **No action required** - this clarifies existing behavior (Devil's Advocate never should have created separate files)

#### For Agent Validator Users
No changes required - Validator already managed `.pr_details/` files since v1.2.0. This update clarifies ownership in documentation.

---

## 1.6.1 - 2025-12-16

### Fixed
- **PR Details Storage Location**: Corrected documentation inconsistency where copilot-instructions.md referenced legacy `.pr_details.md` (singular file) while Agent Validator uses `.pr_details/` directory with branch-specific files
  - **Issue**: When following copilot-instructions.md, PR details were not stored in the expected `.pr_details/` directory structure
  - **Root Cause**: Agent Validator was updated in v1.2.0 to use `.pr_details/{branch}.md` format, but copilot-instructions.md and Agent Architect still referenced the old single-file approach
  - **Fixed Files**:
    - `copilot-instructions.md`: Updated "Specification Storage Convention" section to show `.pr_details/` directory with branch-specific files
    - `architect.agent.md`: Removed PR details output requirement (now exclusively managed by Validator)
  - **Migration**: PR details management is handled by Agent Validator during review process. Agent Architect no longer creates `.pr_details.md` file.

### Changed
- **Agent Architect (architect.agent.md)**: Removed PR details creation responsibility (v1.6.0 → v1.6.1 patch bump)
  - **Before**: Architect created `.pr_details.md` file in repository root after completing specification
  - **After**: Architect only creates specification files in `.specifications/` directory. PR details are managed exclusively by Validator in `.pr_details/` directory
  - **Context**: Aligns Architect responsibilities with Validator's v1.2.0 implementation of branch-specific PR details files
  - **Updated Sections**:
    - **Output Artifacts**: Removed "Generate `.pr_details.md` file" requirement
    - **Specification Storage Location**: Changed "Exception" note to clarify Validator manages PR details
    - **PR Details Output (Required)**: Replaced entire section with "Note on PR Details Management" clarifying Validator ownership
    - **Response Format**: Removed "PR Details" steps from both individual and group specification response formats
    - **Example 1**: Removed PR details example output
    - **Version History**: Added v1.6.1 entry and updated v1.2.0 entry to note deprecation
  - **Migration**: If using Agent Architect, do not expect `.pr_details.md` file creation. Rely on Agent Validator to create `.pr_details/{branch}.md` during review.

- **copilot-instructions.md**: Updated documentation to reflect current PR details management approach
  - **Before**: Directory structure showed `.pr_details.md` (singular file in root)
  - **After**: Directory structure shows `.pr_details/` directory with branch-specific files
  - **Updated Sections**:
    - **Specification Storage Convention**: Updated directory structure diagram
    - **Workflow steps**: Added step showing Validator creates/updates PR details files
  - **Context**: Ensures documentation matches Validator's v1.2.0 implementation

### Migration Guide

#### For Agent Architect Users
If you were previously expecting `.pr_details.md` file from Architect:
1. **Stop expecting Architect to create PR details** - this is no longer Architect's responsibility
2. **Rely on Agent Validator** to create `.pr_details/{branch}.md` during review process
3. **No action required** - this is a documentation fix, not a behavior change (Validator was already managing PR details since v1.2.0)

#### For Agent Validator Users
No changes required - Validator behavior unchanged since v1.2.0.

#### For Documentation Readers
- When reading copilot-instructions.md, note that `.pr_details/` is a directory (not `.pr_details.md` file)
- PR details are created by Validator during review, not by Architect after specification

## 1.6.0 - 2025-12-15

### Changed
- **Agent Architect (architect.agent.md)**: Made Devil's Advocate MANDATORY for all agent group specifications
  - **Before**: Devil's Advocate was optional in agent groups (added in v1.5.0 but not enforced)
  - **After**: Agent Architect MUST include Devil's Advocate agent in every agent group specification without exception
  - **Context**: Ensures critical review and disagreement capture is consistently applied across all agent groups, preventing oversight and ensuring quality
  - **Updated Sections**:
    - **Responsibilities**: Added "For Agent Groups" section explicitly requiring Devil's Advocate inclusion
    - **Domain Context**: Added CRITICAL REQUIREMENT emphasizing Devil's Advocate is non-negotiable for all groups
    - **Output Format (Agent Group Specification)**: Added MANDATORY REQUIREMENT header and devils-advocate agent template
    - **Handoff Chain Design**: Updated to show Devil's Advocate as final quality gate in all examples
    - **Quality Gates**: Added requirement for Devil's Advocate critical review gate
    - **Testing Agent Group Example**: Expanded from 3 agents to 4 agents including devils-advocate
    - **Handoff Chain Example**: Updated workflow to include devils-advocate after test-validator
    - **Frontmatter Schema**: Added devils-advocate to agent list and handoff examples
    - **Quality Checklist**: Added "Devil's Advocate Included" as mandatory criterion for agent group specs
    - **Design Rationale**: Updated from "three agents" to "four agents" with Devil's Advocate explanation
    - **Implementation Sequence**: Added devils-advocate as fourth agent in step-by-step implementation order
  - **Migration**: All future agent group specifications created by Architect will automatically include Devil's Advocate. Existing specifications created before v1.6.0 should be updated to include devils-advocate agent for consistency.

- **copilot-instructions.md**: Enforced Devil's Advocate as mandatory requirement for agent groups throughout workflow documentation
  - **Before**: Devil's Advocate mentioned but not explicitly required in all contexts
  - **After**: Devil's Advocate is explicitly MANDATORY in all agent group workflows with enforcement language
  - **Updated Sections**:
    - **Workflow: Building Agent Groups**: Added CRITICAL REQUIREMENT header at section start
    - **Phase 1 (Architect)**: Added explicit requirement to include devils-advocate in group specification
    - **Exit Criteria (Phase 1)**: Added checklist items for devils-advocate inclusion and handoff definition
    - **Portable Agent Group Pattern**: Added devils-advocate.agent.md to required structure example with CRITICAL note
    - **Quality Gates (Gate 1)**: Added "Devil's Advocate agent included" and "handoffs to devils-advocate defined" to Architect checklist
    - **Common Agent Categories**: Added "Universal Agent (MANDATORY)" section documenting devils-advocate as required for all groups
  - **Context**: Reinforces at every workflow stage that Devil's Advocate is not optional, preventing accidental omission during specification or implementation

- **Version Numbers**: Synchronized version bump for Architect and infrastructure
  - **Architect Agent**: 1.5.0 → 1.6.0 (breaking change to specification requirements)
  - **Infrastructure**: copilot-instructions.md updated with v1.6.0 requirements
  - **Context**: Minor version bump because this changes specification requirements (all future agent groups must include devils-advocate)

### Migration Guide

#### For Agent Architect
If designing agent group specifications after v1.6.0:
1. **Always include Devil's Advocate agent** in group specification:
   - Define devils-advocate with standard responsibilities (critical review, challenge assumptions, surface disagreements)
   - Recommend model: Claude Sonnet 4.5 (copilot) for analytical reasoning
   - Document handoffs: devils-advocate receives from all agents, hands back to agents or orchestrator
2. **Document handoff to devils-advocate** for all agents in group:
   - Every agent should have handoff to devils-advocate for critical review
   - Devils-advocate positioned as final quality gate before completion
3. **Update handoff chain diagram** to show devils-advocate as final gate
4. **Include devils-advocate in implementation sequence** (typically after validator role)

#### For Existing Agent Groups (Before v1.6.0)
Existing agent groups without Devil's Advocate remain valid but should be updated for consistency:
1. Add devils-advocate.agent.md to agents/ folder
2. Update all agents' handoffs to include devils-advocate
3. Update copilot-instructions.md workflow to show devils-advocate gate
4. Update README.md to document devils-advocate role

No breaking changes to existing implementations; this is an enhancement for future consistency.

## 1.5.0 - 2025-12-15

### Added
- **Devil's Advocate Agent (devils-advocate.agent.md)**: New fourth meta-agent for critical review and disagreement capture
  - **Purpose**: Critically reviews agent work, challenges assumptions, surfaces disagreements between agents
  - **Position in Workflow**: Pre-PR quality gate between Agent Validator approval and PR submission
  - **Key Capabilities**: 
    - Critical review of work from Architect, Implementer, and Validator
    - Assumption challenge and blind spot identification
    - Disagreement facilitation between agents with full perspective capture
    - PR writeup preparation with all disagreements marked for human decision
  - **Model**: Claude Sonnet 4.5 (copilot) - requires strong reasoning for multi-perspective synthesis
  - **Context**: Addresses need to surface and document disagreements between agents (e.g., Staff Engineer vs Code Reviewer) before PR submission, ensuring human decision-makers see full context and trade-offs

- **Quality Gate 4 (Critical Review Complete)**: Added mandatory pre-PR gate after Validator approval
  - **Owner**: Devil's Advocate
  - **Requirements**: Assumptions challenged, blind spots identified, disagreements documented, all perspectives captured
  - **Context**: Ensures all viewpoints are surfaced before PR submission, enabling informed human decisions

### Changed
- **Meta-Agent Count**: System now has four meta-agents (was three)
  - **Before**: Architect, Implementer, Validator
  - **After**: Architect, Implementer, Validator, Devil's Advocate
  - **Migration**: All workflows now include Devil's Advocate review after Validator approval

- **Agent Validator Workflow**: Updated to handoff to Devil's Advocate after approval
  - **Before**: Validator approval → PR submission
  - **After**: Validator approval → Devil's Advocate review → PR submission
  - **Added Handoff**: "Send to Devil's Advocate" for critical review after approval
  - **Context**: Validator still gates PR submission but now works with Devil's Advocate for comprehensive quality assurance
  - **Migration**: No breaking changes—Validator still submits PRs, just with additional review step

- **Workflow Diagram (copilot-instructions.md)**: Updated to show four-agent workflow with Devil's Advocate gate
  - **Before**: Three-agent linear workflow (Architect → Implementer → Validator → PR)
  - **After**: Four-agent workflow with decision points (Architect → Implementer → Validator → Devil's Advocate → [Revision/Escalation/Approval] → PR)
  - **Context**: Visualizes new critical review phase and feedback loops

- **Decision Trees (copilot-instructions.md)**: Added section [D] for Devil's Advocate critical review
  - **Before**: [C] Have implementation to review → Validator → PR submission
  - **After**: [C] Validator review → [D] Devil's Advocate critical review → [E] PR submission
  - **Added Decision Points**: Revision needed (to Implementer), Specification issue (to Architect), Approved for PR (to Validator)
  - **Context**: Clarifies when and how to use Devil's Advocate in workflow

- **Workflow Rules (copilot-instructions.md)**: Updated PR submission rule to require Devil's Advocate approval
  - **Before**: Rule 3 - "Only Validator submits PRs" (after Validator approval)
  - **After**: Rule 3 - "Only Validator submits PRs" (after Devil's Advocate approval); Rule 5 - "Devil's Advocate is mandatory"
  - **Context**: Reinforces that critical review is not optional

- **Quick Reference Table (copilot-instructions.md)**: Added Devil's Advocate entry
  - **New Row**: [D] Have approved implementation → @devils-advocate → Critical review, challenge assumptions
  - **Updated Row**: [E] Want to merge → @agent-validator only → Validator submits PR after Devil's Advocate approval

- **README.md Workflow**: Updated from three-phase to four-phase workflow
  - **Added Phase 4**: Critical Review (Pre-PR Gate) with Devil's Advocate
  - **Updated Quick Start**: Added step 5 for Devil's Advocate consultation
  - **Context**: Ensures users understand new workflow step

- **Version Numbers**: Synchronized minor version bump across all meta-agents
  - **All Agents**: 1.4.0 → 1.5.0 (Architect, Implementer, Validator, Devil's Advocate)
  - **Infrastructure**: copilot-instructions.md, README.md version badges updated to 1.5.0
  - **Context**: Synchronized minor bump per meta-agent versioning strategy (workflow change affects all agents)

### Migration Guide
- **Existing Workflows**: Add Devil's Advocate review step after Validator approval, before PR submission
- **No Breaking Changes**: Existing agents and specifications remain valid; workflow extended, not replaced
- **New Agent Groups**: Include Devil's Advocate in agent list with appropriate handoffs from final quality gate agent

## 1.4.0 - 2025-12-13

### Changed
- **Agent Frontmatter**: Updated handoff format to GitHub Copilot object schema across all three meta-agents
  - **Before**: Handoffs were simple string arrays (`handoffs: [agent-implementer, agent-validator]`)
  - **After**: Handoffs are structured objects with `label`, `agent`, `prompt`, and optional `send` fields
  - **Context**: VSCode validation was failing because GitHub Copilot extension expects handoff objects, not strings. This change ensures compliance with the official schema and improves handoff UX with clear labels and context prompts.
  - **Migration**: All meta-agents (Architect, Implementer, Validator) now use object format. No breaking changes to workflow semantics—handoff relationships remain unchanged, only format updated.

- **Agent Architect (Schema Documentation)**: Updated Portable Agent Group Schema section to document new handoff object format
  - **Before**: Schema showed handoffs as simple string array
  - **After**: Schema documents handoff object structure with field requirements (label, agent, prompt, send)
  - **Context**: Ensures future agent specifications follow the correct format from the start
  - **Migration**: New agents designed after v1.4.0 will automatically use object format. Existing agents require manual update.

- **copilot-instructions.md (Schema Documentation)**: Updated Agent Frontmatter Schema section with handoff object format and field requirements
  - **Before**: Example showed string array for handoffs
  - **After**: Example shows object format with inline documentation of field requirements
  - **Context**: Provides clear reference for handoff format across all documentation
  - **Migration**: Documentation change only; no action required for existing agents unless updating them.

### Added
- **Handoff Field Requirements**: Added documentation for all handoff object fields
  - `label`: Short, action-oriented phrase (3-6 words, starts with verb) for user-facing actions
  - `agent`: Target agent name in kebab-case matching target's `name` frontmatter field
  - `prompt`: Context-specific instruction for receiving agent (1-2 sentences describing handoff context and expected action)
  - `send`: Optional boolean for automatic handoffs (default: false, use sparingly)

### Fixed
- **VSCode Validation**: Resolved handoff format validation errors in VSCode GitHub Copilot extension
  - **Issue**: All agent files showed validation warnings about handoff format
  - **Resolution**: Updated all 14 agent files across 4 agent groups to use GitHub Copilot-compliant object format
  - **Impact**: VSCode validation now passes without errors; handoff UI displays clear labels and prompts

### Context
This refactoring addresses VSCode validation failures while maintaining all existing workflow semantics. No handoff relationships were added or removed—only the format changed from simple strings to structured objects. The new format provides better UX (clear labels in handoff menu) and passes GitHub Copilot extension validation.

## 1.3.0 - 2025-12-12

### Changed
- **Agent Architect**: All specification documents now created in `./.specifications/` directory at repository root (previously ad-hoc locations)
  - **Before**: Specifications created without defined location, leading to inconsistent storage
  - **After**: All specifications must be created in `./.specifications/` directory with consistent naming
  - **Migration**: Existing specifications in `.github/specifications/` can remain as historical artifacts; new specifications go to `./.specifications/`
- **Workflow**: Added specification storage convention requiring `.specifications/` directory for all Architect outputs
  - Phase 1 workflows updated for both individual agents and agent groups
  - Architect must create `.specifications/` directory if it doesn't exist before writing specs
- **Version Control**: Added `.specifications/` to `.gitignore` to exclude specifications from repository commits

### Added
- **Documentation**: New "Specification Storage Convention" section in copilot-instructions.md explaining specification directory structure and rationale
  - Documents why specifications are working documents (not final artifacts)
  - Provides clear workflow showing specification lifecycle
  - Includes directory structure diagram for clarity
- **Agent Architect**: Added "Specification Storage Location" subsection documenting directory requirements and naming conventions
  - Path requirement: `./.specifications/` (relative to repository root)
  - Naming convention: `{agent-name}-specification.md` or `{group-name}-group-specification.md`
  - Examples for individual agents, agent groups, and refactorings
  - Exception documented for `.pr_details.md` (remains in root)

### Context
Specifications are working documents created during agent design phase. Storing them in a consistent, gitignored location keeps the repository clean while maintaining local access for reference during implementation and review. This addresses specification storage inconsistency and prevents accidental commits of intermediate artifacts.

## 1.2.0 - 2025-12-12

### Added

#### Documentation Enforcement
- **Mandatory CHANGELOG.md updates**: All version bumps now require CHANGELOG.md entries
  - Implementer must add changelog entry following Keep a Changelog format
  - Entry must include date (YYYY-MM-DD), specific component names, and context
  - Breaking changes require migration guidance (Before/After/Migration sections)
  - Added comprehensive changelog entry format guidelines with examples

- **Mandatory README.md updates**: Significant changes require README.md updates
  - Update when agents added/removed, responsibilities change, workflow changes
  - Update when new user-facing features added or breaking changes made
  - Update version badge for synchronized version bumps
  - Added clear criteria for when README.md updates are required vs optional

- **Documentation validation gate**: Validator now checks documentation completeness
  - CHANGELOG.md validation checklist (format, completeness, specificity, context)
  - README.md validation checklist (consistency, user-facing clarity, version badge)
  - Version consistency validation across all files
  - Added severity levels for documentation issues (Critical vs Recommendation)

- **Documentation requirements section**: Agent Implementer enhanced with documentation guidance
  - Self-review checklist for documentation updates
  - Examples of good vs poor changelog entries
  - Criteria for when to update README.md
  - Format guidelines and quality criteria

### Changed

#### Implementer Workflow (Phase 2)
- **Added Step 2.5 (Individual Agents)**: Update Documentation (MANDATORY)
  - **Before**: Documentation updates were optional or informal
  - **After**: CHANGELOG.md required for all version bumps, README.md required for significant changes
  - **Migration**: Review existing agents and ensure CHANGELOG.md exists for versions > 1.0.0

- **Added Step 2.7 (Agent Groups)**: Update Documentation (MANDATORY)
  - **Before**: Group implementations could skip documentation updates
  - **After**: Same documentation requirements as individual agents apply to groups
  - **Migration**: Ensure all agent groups have CHANGELOG.md if version > 1.0.0

- **Updated exit criteria**: Added documentation update verification to Phase 2 exit gates
  - **Before**: Exit criteria focused on agent file completeness only
  - **After**: Must verify CHANGELOG.md and README.md updates before submission to Validator
  - **Migration**: No breaking changes; new criteria apply to future implementations

#### Validator Workflow (Phase 3)
- **Added Section 3.1.1 (Individual Agents)**: Documentation Validation (MANDATORY)
  - **Before**: Validator focused primarily on agent definition file quality
  - **After**: Validator must check CHANGELOG.md and README.md for every PR
  - **Migration**: No breaking changes; new validation criteria apply to future reviews

- **Enhanced group validation**: Added documentation validation to group-specific criteria
  - **Before**: Group validation focused on structure and handoff integrity
  - **After**: Also validates documentation updates across all agents in group
  - **Migration**: No breaking changes; applies to future agent group submissions

- **Expanded feedback examples**: Added documentation-specific feedback templates
  - Critical issues for missing/vague changelog entries
  - Critical issues for version mismatches
  - Critical issues for missing README updates
  - Recommendation-level feedback for documentation clarity improvements

### Quality Improvements

#### Documentation Standards
- **Changelog format standardized**: All entries follow Added/Changed/Fixed/Deprecated/Removed/Security categories
- **Version consistency enforced**: Version numbers must match across agent frontmatter, CHANGELOG.md, and README.md
- **Context requirement**: All changelog entries must explain why changes were made, not just what changed
- **Migration guidance**: Breaking changes must include Before/After/Migration sections

#### Self-Review Process
- **Enhanced checklist**: Implementer self-review now includes 10 documentation-specific items
- **Quality criteria**: Clear distinction between good vs poor changelog/README updates
- **Examples provided**: Both positive examples and anti-patterns documented

### Migration Guide

#### For Implementers

If implementing agents after v1.2.0:

1. **Always update CHANGELOG.md** with every agent change:
   ```markdown
   ## [Version] - YYYY-MM-DD
   
   ### Added/Changed/Fixed
   - **Component**: Description
     - Context: Why the change was made
     - Migration: How to adapt (if breaking)
   ```

2. **Update README.md when** (use judgment):
   - Agent added/removed
   - Responsibilities change significantly
   - Workflow changes
   - New user-facing features
   - Breaking changes
   - Synchronized version bumps (always update version badge)

3. **Verify version consistency** before submitting to Validator:
   - Agent frontmatter matches CHANGELOG.md
   - README.md badge matches (if synchronized bump)
   - Date is current (YYYY-MM-DD)

4. **Use self-review checklist** in agent-implementer.md before submission

#### For Validators

If validating agents after v1.2.0:

1. **Always check CHANGELOG.md**:
   - Entry exists for current version
   - Follows standard format
   - Includes specific component names
   - Provides context (why changed)
   - Includes migration guidance for breaking changes

2. **Check README.md if applicable**:
   - Updated when responsibilities/workflow/agents change
   - Version badge updated for synchronized bumps
   - No outdated information

3. **Verify version consistency**:
   - Frontmatter matches CHANGELOG.md
   - README.md badge matches (if synchronized)
   - Date is current

4. **Use severity levels appropriately**:
   - Critical: Missing changelog, vague entries, version mismatches
   - Recommendation: Could be clearer, more specific

#### For Existing Agents (No Breaking Changes)

No migration required for existing agents. New requirements apply only to:
- New implementations after v1.2.0
- Updates to existing agents after v1.2.0
- PRs submitted after v1.2.0

Existing agents with versions > 1.0.0 should have CHANGELOG.md, but retroactive updates are not required.

## 1.1.0 - 2025-12-12

### Added

#### Workflow Enforcement
- **Feature branch workflow**: All agent implementations must be created on feature branches (`feature/agent-{name}` or `feature/group-{name}`)
- **Quality gates**: Three mandatory gates (Architect specification approval, Implementer completion, Validator approval)
- **Decision trees**: Added comprehensive decision trees for users to navigate the meta-agent system ("Should I build an individual agent or group?", "I need a new agent", etc.)
- **Agent group workflow**: Complete workflow for building coordinated agent groups with infrastructure files

#### Validator Enhancements
- **PR gatekeeper pattern**: Agent Validator now exclusively submits PRs after approval
- **Iteration workflow**: Structured feedback loops between Validator and Implementer with severity levels (Critical/Recommendation/Enhancement)
- **Specification escalation**: Validator can escalate specification issues back to Architect
- **Validation report structure**: Standardized feedback format with approval criteria status

#### Agent Coordination
- **Handoff chains**: Added `handoffs` field to agent frontmatter for defining agent coordination
- **Integration points**: Required documentation of how agents coordinate within groups
- **Handoff integrity validation**: Validator checks for broken handoff references and validates graph structure

#### Frontmatter Schema
- **Version field**: Added optional `version` field to agent frontmatter (semantic versioning)
- **Handoffs field**: Added optional `handoffs` array for agent coordination
- **Model field**: Made model recommendation mandatory in agent specifications

#### Portability Features
- **Portable agent group pattern**: Enforced folder-agnostic structure (`group-name/agents/`, `copilot-instructions.md`, `README.md`)
- **Infrastructure file requirements**: Defined copilot-instructions.md and README.md standards for agent groups
- **Cross-agent references**: Guidelines for relative references (no hardcoded paths)

### Changed

#### Role Boundaries
- **Architect**: Explicitly prohibited from implementing agents (planning only)
- **Implementer**: Must work on feature branches and submit to Validator (cannot merge directly)
- **Validator**: Now responsible for PR submission and merge approval (gatekeeper role)

#### Workflow Process
- **Mandatory validation**: All agent implementations must pass through Validator before merge
- **Branch-based development**: Replaced direct-to-main commits with feature branch workflow
- **Approval criteria**: Expanded validation criteria for individual agents and agent groups

#### Documentation Standards
- **Quality checklist**: Increased from 5-10 items to 6-10 items (individual) and 8-15 items (groups)
- **Examples**: Minimum 2 examples required (ideally 3)
- **Integration points**: Now required section for documenting agent coordination

### Breaking Changes

⚠️ **These changes fundamentally alter the meta-agent workflow and require process updates:**

1. **Architect cannot implement agents**
   - **Before**: Architect could create agent definition files
   - **After**: Architect only creates specifications; Implementer creates files
   - **Migration**: If working on agent implementation, handoff to Implementer

2. **Implementer cannot merge to main**
   - **Before**: Implementer could create PR and merge directly
   - **After**: Implementer submits to Validator; only Validator creates PR
   - **Migration**: All feature branches must be submitted to Validator for review

3. **Validator is mandatory PR gatekeeper**
   - **Before**: PRs could be submitted by anyone after self-review
   - **After**: Only Validator submits PRs after approval
   - **Migration**: Wait for Validator approval before any agent goes live

4. **Feature branches are mandatory**
   - **Before**: Could commit directly to main branch
   - **After**: All work on `feature/agent-{name}` or `feature/group-{name}` branches
   - **Migration**: Create feature branch for any new agent work

5. **Handoff chains required for agent groups**
   - **Before**: Agent coordination was informal
   - **After**: Must define `handoffs` in frontmatter and validate graph integrity
   - **Migration**: Add handoffs field to existing agent groups

### Migration Guide

#### For In-Progress Agent Work

If you have agent work in progress before v1.1.0:

1. **Create feature branch** (if not already on one):
   ```bash
   git checkout -b feature/agent-{your-agent-name}
   ```

2. **Add frontmatter fields** to your agent file:
   ```yaml
   ---
   name: your-agent-name
   description: Brief description
   model: Claude Sonnet 4.5 (copilot)
   version: 1.0.0
   handoffs:  # Optional, if agent coordinates with others
     - other-agent-name
   ---
   ```

3. **Submit to Validator** (do not create PR yourself):
   - Commit and push your feature branch
   - Notify Agent Validator that implementation is ready
   - Wait for Validator review and feedback

4. **Iterate based on feedback**:
   - Make changes on same feature branch
   - Push updates and notify Validator
   - Repeat until approved

5. **Validator submits PR**:
   - When approved, Validator will create and submit PR
   - PR will be merged to main

#### For Existing Agent Groups

If you have existing agent groups without v1.1.0 features:

1. **Add CHANGELOG.md** (if version > 1.0.0)
2. **Add handoffs to frontmatter** for all agents
3. **Document integration points** showing agent coordination
4. **Validate handoff chains** (no broken references)
5. **Submit to Validator** for compliance review

#### For New Agent Work

Follow the new workflow from the start:
1. Consult Architect for specification
2. Implementer creates on feature branch
3. Submit to Validator (do not merge)
4. Iterate until approved
5. Validator submits PR

## 1.0.0 - 2024-12-01

### Added

#### Core Meta-Agent System
- **Three-agent pattern**: Architect (design), Implementer (implement), Validator (review)
- **Separation of concerns**: Strict role boundaries for each agent
- **Agent definition structure**: Standard markdown format with frontmatter

#### Agent Architect
- **Specification design**: Translates user needs into actionable agent specifications
- **Scope definition**: Defines boundaries, responsibilities, inputs/outputs
- **Success criteria**: Establishes measurable quality metrics
- **Model recommendations**: Suggests appropriate AI models for agents

#### Agent Implementer
- **Agent file creation**: Generates agent definition markdown files from specifications
- **Template structure**: Applies consistent sections (Purpose, Responsibilities, Domain Context, etc.)
- **Example generation**: Creates comprehensive examples for agent behavior
- **Quality checklists**: Designs measurable validation criteria

#### Agent Validator
- **Quality review**: Validates agent implementations against specifications
- **Best practices compliance**: Checks adherence to GitHub Copilot guidelines
- **Feedback provision**: Provides actionable improvement suggestions
- **Approval decision**: Determines if agent meets quality standards

#### Documentation
- **copilot-instructions.md**: Meta-agent system workflow and integration guide
- **README.md**: Getting started guide and agent overview
- **Agent templates**: Standard structure for agent definitions

#### Best Practices
- **GitHub Copilot guidelines**: Integrated official best practices
- **Clarity standards**: Instructions for clear, actionable agent definitions
- **Example requirements**: Minimum 2 examples per agent
- **Quality criteria**: 5-10 measurable checklist items per agent

### Workflow (v1.0.0)
1. User describes need → Architect designs specification
2. Architect hands specification → Implementer creates agent file
3. Implementer hands agent → Validator reviews quality
4. Validator provides feedback or approval

---

## Version Comparison

| Feature | v1.0.0 | v1.1.0 |
|---------|--------|--------|
| Feature branches | Optional | **Mandatory** |
| PR submission | Anyone | **Validator only** |
| Handoff chains | Informal | **Formalized in frontmatter** |
| Validation | Optional | **Mandatory gate** |
| Architect role | Could implement | **Specification only** |
| Implementer role | Could merge | **Submit to Validator** |
| Validator role | Review only | **PR gatekeeper** |
| Agent groups | Basic support | **Full infrastructure** |
| Quality gates | 1 (Validator) | **3 (Architect, Implementer, Validator)** |

---

## Links

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [GitHub Copilot Best Practices](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
