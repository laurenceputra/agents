# Changelog

## [1.1.1] - 2025-12-22

### Changed
- **Examples Restoration**: Restored comprehensive examples (minimum 2 per agent with full input/output)
  - **Before**: Many agents had only 1 truncated example after size optimization (commit ee14332)
  - **After**: All agents now have 2+ complete examples demonstrating full workflow
  - **Impact**: Significantly improved agent clarity and usability while maintaining <30k character limit


All notable changes to the Corporate Team Building Planning agent group will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-21

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

## [1.0.0] - 2025-12-20

### Added
- Initial release of Corporate Team Building Planning agent group
- **team-profiler** agent (v1.0.0) - Conducts structured discovery to create comprehensive team profiles with goals, constraints, and preferences
- **activity-scout** agent (v1.0.0) - Recommends 3-5 team building activities matched to profile with bonding potential analysis
- **dining-specialist** agent (v1.0.0) - Suggests dining experiences accommodating dietary restrictions and supporting team bonding
- **event-coordinator** agent (v1.0.0) - Synthesizes activities and dining into 2-3 complete event scenarios with timelines, logistics, and contingencies
- **devils-advocate** agent (v1.0.0) - Provides mandatory critical review before booking commitments to identify risks and prevent failures
- Complete workflow documentation in copilot-instructions.md covering all five agents and their interactions
- Comprehensive README.md with quick start guide, examples, and troubleshooting
- Support for diverse team sizes (5-50+ people) and event types (integration, trust-building, celebration)
- Inclusive design considering dietary restrictions, physical abilities, and personality diversity
- Goal-oriented approach ensuring activities genuinely strengthen team bonds
- Built-in quality gate (Devil's Advocate) to prevent "forced fun" failures
- Practical logistics coverage including transportation, timing, costs, and contingencies

### Features
- Sequential workflow with automatic handoffs between agents
- Team profiling with structured discovery (10-15 questions)
- Activity recommendations with explicit bonding mechanisms
- Dining recommendations with conversation-friendly evaluation
- Complete event scenarios with minute-by-minute timelines
- Cost breakdowns and booking checklists with lead times
- Contingency planning for weather, venues, and timing issues
- Critical review challenging assumptions and identifying blind spots
- Support for various team goals: integration, trust-building, cross-functional collaboration, celebration
- Accommodation for dietary restrictions: vegetarian, vegan, gluten-free, allergies, religious requirements
- Scalability from small (5-12) to large (50+) teams
- Multiple event duration options: half-day, full-day, evening, multi-day

[1.0.0]: https://github.com/laurenceputra/agents/releases/tag/corporate-team-building-v1.0.0
