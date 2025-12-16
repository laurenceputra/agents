# Changelog

All notable changes to the Social Media Team agent group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-16

### Changed
- **LinkedIn Specialist**: Refactored for conciseness optimization
  - **Before**: Examples averaged 200+ lines with extensive subsections and redundant explanations
  - **After**: Examples reduced to 100-120 lines while maintaining strategic depth and actionable guidance
  - **Context**: Aligned LinkedIn example length with Facebook and Instagram specialists for consistent user experience across platform agents
  - **Impact**: Reduced overall agent file from 924 lines to ~450 lines (51% reduction in examples section)
  - Streamlined Response Format from 8 sections to 6 sections (consolidated Algorithm Optimization + Engagement Strategy; merged Performance Guidance + Thought Leadership Development)
  - Eliminated redundant explanations and over-detailed subsections across all three examples
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
