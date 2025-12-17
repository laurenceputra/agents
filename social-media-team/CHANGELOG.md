# Changelog

All notable changes to the Social Media Team agent group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-12-16

### Changed
- **LinkedIn Specialist**: Refactored for personal brand straight-shooter voice (addressing user feedback: "reduce number of points, align to straight-shooter brand")
  - **Before**: 10-15 tactics per section with multi-layer guidance (WHY/HOW/WHAT/WHEN), corporate strategist tone, examples focused on B2B corporate campaigns
  - **After**: 3-5 focused recommendations per section with single-layer lists, direct personal tone, examples focused on individual thought leaders
  - **Context**: User clarified intent to reduce POINT COUNT (not just length) and align to personal brand voice (not corporate playbooks). Devil's Advocate raised concern about v1.1.0 removing strategic depth—v2 addresses this by refocusing depth for personal brands rather than corporate strategists.
  - **Impact**: Reduced file from 706 lines to ~480 lines through focused guidance approach (32% reduction)
  - **Key Changes**:
    - Reduced tactics per section from 10-15 to 3-5 (60-70% reduction in point count)
    - Removed multi-layer guidance structure (WHY/HOW/WHAT/WHEN labels collapsed into single-layer lists)
    - Shifted tone to straight-shooter voice: "Keep it simple" / "That's it" / "Don't overthink it" (direct, no corporate jargon)
    - Replaced Example 1 (CEO corporate post) with personal product failure lesson
    - Simplified Example 2 from 7-lesson corporate playbook to 3-lesson personal article
    - Streamlined Example 3 poll to focus on individual career insights
  - **Migration**: Users seeking comprehensive corporate B2B strategy depth may find agent too concise. For detailed playbooks, request "detailed strategy with all tactics" in input. Examples now focus on personal brand use cases (individual thought leadership, not corporate campaigns).

## [1.1.0] - 2025-12-16

### Changed
- **LinkedIn Specialist**: Refactored for improved organization and clarity while maintaining strategic depth
  - **Before**: Examples averaged 200+ lines with some redundant subsections
  - **After**: Examples reorganized with layered guidance (WHY/HOW/WHAT/WHEN dimensions) and expanded critical sections
  - **Context**: LinkedIn's professional B2B platform requires more strategic depth than casual social platforms. Refactoring focused on better organization (not arbitrary length reduction) while maintaining all strategic value for thought leadership positioning.
  - **Impact**: Reduced overall agent file from 924 lines to 700-750 lines (~24% reduction through improved organization)
  - **Key Improvements**:
    - Expanded Example 2 Article lessons from 1-line summaries to 8-12 line problem/story/solution/actionable structures (7 lessons now provide execution-ready guidance)
    - Added layered guidance labels across all examples showing strategic progression (Strategic Rationale, Execution Tactics, Algorithm Optimization, Engagement Strategy)
    - Restored engagement timeline specifics ("30 mins before posting" proactive tactics, "first 2 hours critical" post-launch strategy)
    - Added performance benchmark context (50K impressions = 8-12x multiplier explanation, 4-6% engagement vs. 2-3% LinkedIn average)
    - Maintained professional tone, thought leadership focus, and all strategic insights
  - **Migration**: No breaking changes - all agent responsibilities, quality criteria, and handoffs unchanged

## [1.0.0] - 2025-11-15

### Added
- **Social Media Team**: Initial release of coordinated social media specialist agent group
- **Facebook Specialist**: Casual, conversational content strategy for Facebook platform
- **Instagram Specialist**: Visual-first content strategy with Stories, Reels, and carousel focus
- **LinkedIn Specialist**: Professional thought leadership and B2B networking strategy
- **Social Media Coordinator**: Cross-platform campaign coordination and consistency management
- **Devil's Advocate**: Critical review and assumption challenging for all social media strategies
- Group infrastructure: copilot-instructions.md with workflow diagrams, README.md with usage guide

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
  - social-media-coordinator: now v1.0.1
  - facebook-specialist: now v1.0.1
  - instagram-specialist: now v1.0.1
  - linkedin-specialist: now v1.0.1
  - devils-advocate: now v1.0.1
  - **Context**: Patch version increment reflects non-breaking enhancement (documentation/quality improvement)

