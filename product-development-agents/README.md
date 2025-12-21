# Product Development Agents

A structured, high-quality product development workflow system for GitHub Copilot with five specialized agents that collaborate to deliver software from requirements to deployment.

## Overview

This system provides a complete product development workflow with built-in quality gates, iterative feedback loops, and clear processes. It's designed to work out-of-the-box while being customizable for your project's specific needs.

### The Five Agents

1. **Product Manager** - Define requirements, user stories, and acceptance criteria
2. **Staff Engineer** - Design technical solutions and implement features
3. **Code Reviewer** - Quality gate ensuring code standards and security
4. **QA** - Comprehensive testing and validation before critical review
5. **Devil's Advocate** - Critical review, assumption challenging, and disagreement capture before PR submission

### Key Features

- ✅ **Structured Workflow**: Clear progression from requirements to deployment
- ✅ **Quality Gates**: Mandatory code review and QA approval stages
- ✅ **Feedback Loops**: Iterative improvement through code review and QA cycles
- ✅ **Comprehensive Examples**: Each agent includes 2-3 detailed examples
- ✅ **Out-of-Box Ready**: Works immediately with sensible defaults
- ✅ **Highly Customizable**: Easy to adapt to your tech stack and standards
- ✅ **Portable**: Drop into any project by renaming directory to `.github`

## Quick Start

### Installation

1. **Copy to Your Project**
   ```bash
   # From your project root
   cp -r /path/to/this-agent-group .github
   ```

2. **Customize for Your Project** (Optional but Recommended)
   
   Edit the "Domain Context (Project-Specific)" section in each agent:
   - `.github/agents/product-manager.md`
   - `.github/agents/staff-engineer.md`
   - `.github/agents/code-reviewer.md`
   - `.github/agents/qa.md`
   - `.github/agents/devils-advocate.md` (uses defaults, customization optional)
   
   Add your:
   - Tech stack (languages, frameworks)
   - Coding standards and conventions
   - Testing requirements (coverage targets, test types)
   - Performance targets (response times, resource limits)
   - Security policies (authentication patterns, compliance)
   - Accessibility standards (WCAG levels)

3. **Start Using**
   
   In GitHub Copilot Chat, reference agents with `@`:
   ```
   @product-manager Create a PRD for user authentication
   ```

### Basic Usage

#### Scenario 1: Building a New Feature

```
Step 1: Define Requirements
You: "@product-manager I need to add a password reset feature for users who forgot their password"

Product Manager will create:
- Complete PRD with problem statement
- User stories (As a user, I want...)
- Detailed acceptance criteria (Given-When-Then)
- Success metrics
- Out of scope items

Step 2: Design and Implement
You: "@staff-engineer Here's the PRD: [paste PRD]. Create technical design and implementation"

Staff Engineer will:
- Create technical design document (architecture, components, security)
- Implement the feature with comprehensive tests
- Self-review before submission

Step 3: Code Review
You: "@code-reviewer Review this implementation: [provide code/PR link]"

Code Reviewer will:
- Review for security, correctness, quality, performance
- Assess product alignment with PRD
- Approve or reject with detailed feedback

If rejected:
  You: "@staff-engineer Address this code review feedback: [paste feedback]"
  (Engineer fixes and resubmits to Code Reviewer)
  Repeat until approved

Step 4: QA Testing
You: "@qa Test this code-reviewer-approved implementation against the PRD"

QA will:
- Execute comprehensive test plan
- Test all acceptance criteria
- Report bugs with detailed reproduction steps
- Approve when all tests pass

If bugs found:
  You: "@staff-engineer Fix these bugs: [paste bug reports]"
  Engineer fixes → "@code-reviewer Review bug fixes"
  Code review approves → "@qa Retest the bug fixes"
  Repeat until all tests pass

Step 5: Deploy
When QA approves, deploy to production!
```

#### Scenario 2: Fixing a Bug

```
You: "@product-manager User reported search fails with quotes and apostrophes"
PM creates mini-PRD with acceptance criteria

You: "@staff-engineer Fix this bug: [paste mini-PRD]"
Engineer reproduces, fixes, adds tests

You: "@code-reviewer Review this bug fix"
Reviewer approves or requests changes

You: "@qa Test that the search bug is fixed"
QA verifies fix and performs regression testing

If QA approves → Deploy hotfix
```

## Workflow

### The Main Flow

```
1. Product Manager
   ↓ Creates PRD with acceptance criteria
   
2. Staff Engineer
   ↓ Designs and implements solution
   
3. Code Reviewer (Quality Gate)
   ↓ Reviews code for quality, security, product alignment
   │
   ├─ REJECTED → Engineer fixes → Resubmit
   │              ↑_______________↓
   │              (Iterate until approved)
   │
   └─ APPROVED → Proceed to QA
   
4. QA (Quality Gate)
   ↓ Tests all acceptance criteria
   │
   ├─ BUGS FOUND → Engineer fixes → Code Review → QA retest
   │                ↑_______________↓____________↑________↓
   │                (Iterate until all tests pass)
   │
   └─ ALL TESTS PASS → Approved for Deployment
   
5. Deploy to Production
```

### Critical Rules

1. **Code Review is Mandatory**: All code must pass code review before QA testing
2. **Fixes Go Through Review**: QA bug fixes must be code-reviewed before retesting
3. **No Skipping Stages**: Cannot go directly from Engineer to QA without Code Review
4. **Iterative by Design**: Expect multiple iterations—this ensures quality

See `copilot-instructions.md` for detailed workflow documentation including:
- Detailed phase descriptions with inputs, activities, outputs, exit criteria
- Feedback loop mechanics (Code Review Loop and QA Loop)
- Workflow variants (new features, bug fixes, refactoring, performance optimization, security fixes)
- Collaboration patterns between agents
- Decision trees for when to consult which agent
- Complete workflow examples with timelines

## Agent Capabilities

### Product Manager Agent

**Purpose**: Define what to build and why it matters

**Key Capabilities**:
- Create comprehensive PRDs (Product Requirements Documents)
- Write user stories in standard format (As a... I want... So that...)
- Define testable acceptance criteria (Given-When-Then format)
- Establish measurable success metrics
- Prioritize features and scope
- Review with stakeholders

**When to Use**:
- Starting any new feature or project
- When you have a user problem to solve
- When requirements need clarification
- When prioritizing multiple features
- Creating bug reports (as mini-PRDs)

**Example Output**:
```
# Password Reset Feature PRD

## Problem Statement
Users who forget passwords have no way to recover...

## User Stories
- As a user who forgot my password, I want to receive a reset link...
- As a user, I want the reset link to expire after 1 hour...

## Acceptance Criteria
- Given user requests password reset
  When they provide valid email
  Then they receive reset link within 2 minutes
  
[... detailed acceptance criteria ...]

## Success Metrics
- Reduce password-related support tickets by 80%
- 95% of reset attempts succeed within 5 minutes
```

### Staff Engineer Agent

**Purpose**: Design and implement technical solutions with quality

**Key Capabilities**:
- Create detailed technical design documents
- Design architecture, components, APIs
- Implement features with comprehensive tests
- Fix bugs based on code review feedback
- Fix bugs based on QA reports
- Self-review code before submission
- Consider security, performance, scalability

**When to Use**:
- Implementing features from PRDs
- Creating technical designs
- Fixing bugs from QA or production
- Responding to code review feedback
- Technical feasibility assessment

**Example Output**:
```
# Technical Design: Password Reset

## Architecture
- Token Service: Generate cryptographically secure tokens
- Email Service: Send reset emails via SendGrid
- API Endpoints: POST /api/password-reset/request, POST /api/password-reset/confirm
- Database: users table + password_reset_tokens table

## Security Considerations
- Use crypto.randomBytes(32) for tokens (not Math.random())
- Hash tokens before storing in database
- Rate limit: 3 requests per email per hour
- Tokens expire after 1 hour
- Clear all tokens for user after successful reset

[... detailed design ...]

## Implementation Plan
1. Create password_reset_tokens table migration
2. Implement TokenService with secure generation
3. Implement EmailService integration
4. Build API endpoints with validation
5. Add frontend forms and flows
6. Write comprehensive tests (unit, integration, E2E)
```

### Code Reviewer Agent

**Purpose**: Quality gate ensuring code meets standards before testing

**Key Capabilities**:
- Review code for security vulnerabilities
- Check correctness and logic bugs
- Assess code quality and maintainability
- Evaluate performance implications
- Verify product alignment with PRD
- Assess user experience decisions
- Review test coverage and quality
- Provide detailed, actionable feedback
- Categorize feedback (Critical, Recommendations, Suggestions)

**When to Use**:
- Before QA testing (mandatory gate)
- After Engineer submits implementation
- After Engineer addresses previous feedback
- After Engineer fixes QA bugs
- When assessing code quality

**Example Output**:
```
# Code Review: Password Reset Implementation

## Decision: REJECTED ❌

## Critical Issues (Must Fix Before Approval)

### 1. Security: Insecure Token Generation
**Location**: `src/services/TokenService.ts:15`
**Issue**: Using Math.random() to generate reset tokens
**Risk**: Tokens are predictable, attacker could guess valid tokens
**Recommendation**: Use crypto.randomBytes(32).toString('hex')

### 2. Security: SQL Injection Vulnerability
**Location**: `src/api/passwordReset.ts:42`
**Issue**: Direct string interpolation in SQL query
**Risk**: SQL injection attack vector
**Recommendation**: Use parameterized queries

[... detailed feedback ...]

## Next Steps
Please address all 4 critical issues and resubmit for review.
```

### QA Agent

**Purpose**: Validate quality through comprehensive testing before deployment

**Key Capabilities**:
- Create detailed test plans and test cases
- Execute tests against acceptance criteria
- Test functional requirements
- Test non-functional requirements (performance, security, accessibility)
- Perform edge case and error scenario testing
- Report bugs with detailed reproduction steps
- Assess severity and user impact
- Perform regression testing
- Approve for deployment when all tests pass

**When to Use**:
- Testing code-reviewer-approved implementations
- Creating test plans from PRDs
- Retesting after bug fixes
- Regression testing
- Final approval before deployment
- Exploratory testing

**Example Output**:
```
# Bug Report: Search Special Characters

## Summary
Search fails when query contains quotes or apostrophes, returning 400 error

## Severity: High
- Impact: Users cannot search for common phrases with apostrophes
- User Experience: Confusing error, no clear resolution

## Reproduction Steps
1. Navigate to search page
2. Enter search query: "user's profile"
3. Click search button
4. Observe: 400 Bad Request error displayed

## Expected Behavior
- Search should process queries with quotes and apostrophes
- Return relevant results or "no results found"

## Actual Behavior
- 400 error: "Invalid search query"
- No results displayed

## Environment
- Browser: Chrome 120.0
- Environment: Staging
- URL: https://staging.example.com/search

## Additional Context
- Error occurs with: quotes ("), apostrophes ('), ampersands (&)
- Error does NOT occur with: letters, numbers, spaces
- Frontend validation passes, error comes from backend

## Acceptance Criteria Blocked
- AC-3: "Users can search with special characters in queries"
```

## Customization Guide

### Project-Specific Configuration

Each agent file has a **"Domain Context (Project-Specific)"** section to customize:

#### 1. Tech Stack
```markdown
## Domain Context (Project-Specific)

### Technology Stack
- **Languages**: TypeScript, Python
- **Frontend**: React 18, Next.js 14, TailwindCSS
- **Backend**: Node.js, Express, PostgreSQL
- **Testing**: Jest, React Testing Library, Playwright
- **Infrastructure**: AWS (ECS, RDS, S3), Docker
```

#### 2. Coding Standards
```markdown
### Coding Standards
- **Style**: ESLint config (Airbnb), Prettier
- **Naming**: camelCase for variables/functions, PascalCase for components
- **File Structure**: Feature-based directories
- **Comments**: JSDoc for public APIs
- **Error Handling**: Always use try-catch, log errors with context
```

#### 3. Testing Requirements
```markdown
### Testing Requirements
- **Coverage**: Minimum 80% for new code
- **Required Tests**: Unit tests for all business logic, integration tests for API endpoints
- **E2E Tests**: Required for critical user flows (login, checkout, etc.)
- **Performance**: All API endpoints must respond <200ms for 95th percentile
```

#### 4. Security Policies
```markdown
### Security Policies
- **Authentication**: JWT tokens with 15-minute expiration
- **Authorization**: Role-based access control (admin, user, guest)
- **Input Validation**: Validate all inputs server-side
- **Secrets**: Never commit secrets, use AWS Secrets Manager
- **Compliance**: HIPAA compliance required, encrypt PII at rest and in transit
```

#### 5. Performance Targets
```markdown
### Performance Targets
- **API Response Time**: <200ms (p95), <500ms (p99)
- **Page Load Time**: <2s Time to Interactive
- **Database Queries**: <50ms for simple queries, <500ms for complex
- **Bundle Size**: <500KB initial bundle
```

#### 6. Accessibility Standards
```markdown
### Accessibility Standards
- **WCAG Level**: AA compliance required
- **Testing**: Use axe-core in tests, manual screen reader testing
- **Requirements**: Keyboard navigation, ARIA labels, sufficient color contrast
```

### Workflow Adjustments

You can adjust the workflow in `copilot-instructions.md`:

#### Define Review SLAs
```markdown
### Review Turnaround Times
- **Code Review**: 24 hours for normal priority, 4 hours for urgent
- **QA Testing**: 48 hours for features, 4 hours for bug fixes
- **PM Approval**: 48 hours for PRD reviews
```

#### Define Approval Thresholds
```markdown
### Approval Exceptions
- **Skip Code Review**: Documentation-only changes (README, comments)
- **Expedited QA**: Security fixes get priority testing
- **Skip Full Regression**: Minor bug fixes can skip full regression suite
```

#### Define Testing Levels
```markdown
### Testing Requirements by Feature Type
- **Critical Flows**: Unit + Integration + E2E tests required
- **Standard Features**: Unit + Integration tests required
- **Internal Tools**: Unit tests sufficient
- **Bug Fixes**: Regression test mandatory
```

### Adding Custom Agents

You can extend the system with additional agents:

#### Example: DevOps Agent
```markdown
---
name: devops-engineer
description: Handles deployment, infrastructure, and monitoring
---

# DevOps Engineer

## Purpose
Manage infrastructure, deployment pipelines, and production monitoring.

## Responsibilities
- Deploy code to production
- Monitor system health
- Manage infrastructure as code
- Respond to production incidents

[... rest of agent definition ...]
```

Place in `.github/agents/devops-engineer.md` and reference in workflow.

## Troubleshooting

### Common Issues

#### "Requirements keep changing during implementation"
**Symptoms**: Engineer keeps getting new requirements mid-implementation

**Root Cause**: PRD was not thorough enough

**Solution**:
1. Pause implementation
2. Update PRD with Product Manager
3. Get stakeholder approval
4. Resume implementation

**Prevention**: More thorough discovery phase; involve Engineer in PRD review to catch gaps early

---

#### "Code review keeps rejecting my implementation"
**Symptoms**: Multiple code review cycles with recurring issues

**Root Cause**: Misalignment on standards or insufficient self-review

**Solution**:
1. Engineer and Code Reviewer align on standards
2. Engineer does more thorough self-review before submission
3. Review existing approved PRs as examples

**Prevention**:
- Document coding standards clearly
- Provide examples of good code
- Use pair programming for complex features
- Implement automated linting/formatting

---

#### "QA keeps finding bugs"
**Symptoms**: High number of QA iterations, many bugs reported

**Root Cause**: Insufficient testing by Engineer before submission

**Solution**:
1. Engineer increases test coverage before submission
2. Engineer manually tests happy path and edge cases
3. Add automated tests for common failure scenarios

**Prevention**:
- Require minimum test coverage (e.g., 80%)
- Use test-driven development (write tests first)
- Add pre-commit hooks to run tests
- Engineer self-testing checklist

---

#### "Workflow is too slow"
**Symptoms**: Features take too long to reach production

**Root Cause**: Bottlenecks in review stages, or excessive rework

**Solution**:
1. Identify bottleneck:
   - Track review turnaround times
   - Measure rework rates (how often code is rejected)
2. Address specific issue:
   - If review is slow: Set SLAs, add more reviewers
   - If high rework: Improve requirements, better standards docs

**Prevention**:
- Clear, documented standards reduce review time
- Better requirements reduce rework
- Parallel work where possible (QA can create test plan during implementation)
- Smaller, incremental changes (easier to review and test)

---

#### "Bug fixes introduce new bugs"
**Symptoms**: Fixing one bug breaks something else

**Root Cause**: Insufficient understanding of root cause, or poor regression testing

**Solution**:
1. Require root cause analysis before fixing
2. Engineer must explain why bug occurred, not just how to fix
3. Increase regression test coverage
4. Code Reviewer specifically checks for regression risk

**Prevention**:
- Comprehensive unit tests (catch regressions early)
- Better code design (reduce coupling)
- More thorough code review of bug fixes
- Automated regression test suite

---

#### "Agents aren't responding correctly"
**Symptoms**: Agent responses don't match expected format or quality

**Root Cause**: Insufficient context provided, or agent needs customization

**Solution**:
1. Provide more context in your request:
   - Include relevant code snippets
   - Link to PRD or previous work
   - Specify which acceptance criteria to focus on
2. Customize agent with project-specific info
3. Reference specific sections of agent (e.g., "Use the bug report format from QA agent")

**Prevention**:
- Fill in Domain Context sections in all agents
- Provide examples of good outputs in your project
- Be specific in requests (don't just say "review this", say "review this for security vulnerabilities")

## Best Practices

### For Product Managers
- ✅ **Be Specific**: Vague requirements cause rework. Define clear, testable acceptance criteria.
- ✅ **Include Why**: Explain the user problem and business value, not just what to build.
- ✅ **Think Edge Cases**: Consider error scenarios, edge cases, accessibility needs.
- ✅ **Define Success**: Specify measurable metrics to evaluate if solution works.
- ✅ **Involve Team Early**: Review PRD with Engineer and QA before finalizing.

### For Engineers
- ✅ **Design Before Code**: Create technical design document for non-trivial features.
- ✅ **Test As You Go**: Write tests during implementation, not after.
- ✅ **Self-Review Thoroughly**: Catch obvious issues yourself before code review.
- ✅ **Think Security**: Consider authentication, authorization, input validation, injection attacks.
- ✅ **Consider UX**: Put yourself in user's shoes—is this intuitive? Are errors helpful?
- ✅ **Document Decisions**: Explain non-obvious choices in code comments or design doc.

### For Code Reviewers
- ✅ **Be Specific**: Don't say "this needs work"—explain exactly what and why.
- ✅ **Be Constructive**: Suggest solutions, don't just point out problems.
- ✅ **Prioritize**: Clearly mark what's critical vs nice-to-have.
- ✅ **Explain Why**: Help engineer understand the reasoning behind feedback.
- ✅ **Praise Good Work**: Recognize well-written code, not just problems.

### For QA
- ✅ **Test More Than Happy Path**: Edge cases, error scenarios, boundary conditions.
- ✅ **Reproduce Reliably**: Ensure bug is reproducible before reporting.
- ✅ **Be Detailed**: Provide exact steps, screenshots, logs to help engineer fix.
- ✅ **Think Like User**: Test not just functionality, but user experience.
- ✅ **Regression Test**: Always verify fixes don't break existing functionality.

### For Everyone
- ✅ **Communicate Early**: Don't wait until deadline to raise blockers.
- ✅ **Assume Good Intent**: Feedback is about work, not person.
- ✅ **Iterate Quickly**: Small, frequent iterations catch issues earlier.
- ✅ **Document Decisions**: Capture important decisions for future reference.
- ✅ **Celebrate Success**: Recognize good work and wins.

## Examples

### Example 1: Password Reset Feature
A complete walkthrough of building a new feature from requirements to deployment, including code review rejections and QA bug fixes. See `copilot-instructions.md` for full details.

**Timeline**: 2 weeks
**Iterations**: 2 code review cycles, 2 QA cycles
**Outcome**: Successful deployment, 85% reduction in support tickets

---

### Example 2: Search Bug Fix
Quick turnaround on fixing a production bug with special characters. See `copilot-instructions.md` for full details.

**Timeline**: 1.5 days
**Iterations**: 1 code review (approved first time), 1 QA cycle (passed first time)
**Outcome**: Hotfix deployed, bug resolved

---

### Example 3: Authentication Refactoring
Technical debt refactoring with extensive regression testing. See Product Manager agent for full example.

**Focus**: Improve code quality without changing functionality
**Key**: Extensive regression testing to ensure no behavior changes
**Outcome**: Reduced technical debt, improved maintainability

## FAQ

### General Questions

**Q: Is this only for GitHub Copilot?**
A: Yes, this system is designed specifically for GitHub Copilot's agent system.

**Q: Can I use this with other AI tools?**
A: The agent definitions could be adapted, but they're optimized for GitHub Copilot's capabilities.

**Q: Does this work for solo developers or only teams?**
A: Works for both! Solo developers can use agents to ensure they think through all perspectives (PM, engineering, review, testing).

### Workflow Questions

**Q: Can we skip code review for trivial changes?**
A: You can define exceptions in your customization (e.g., documentation-only changes), but be careful—even "trivial" changes can introduce issues.

**Q: What if QA finds bugs after deployment to production?**
A: Treat as new bug report. Follow bug fix workflow: PM creates mini-PRD → Engineer fixes → Code Review → QA → Deploy hotfix.

**Q: Can Engineer and Code Reviewer be the same person?**
A: Not recommended—code review should be independent. If team size requires it, at minimum use self-review checklist and be extra thorough.

**Q: How do we handle urgent production issues?**
A: Expedited workflow: Quick PM bug report → Engineer fix → Fast code review (2-hour target) → QA retest critical path → Deploy. Still maintain quality gates, just faster.

**Q: What if we disagree on whether code should be approved/rejected?**
A: Escalate to tech lead or senior engineer. Document decision and reasoning for future reference.

### Customization Questions

**Q: Do we need to fill in all Domain Context sections?**
A: Not required, but highly recommended. The more project-specific info you provide, the better agent responses will be.

**Q: Can we add more agents?**
A: Yes! Add agents for DevOps, Security Specialist, UX Designer, Data Analyst, etc. Follow the template structure from existing agents.

**Q: Can we change the workflow order?**
A: You can adjust, but carefully consider quality implications. The current flow ensures code is reviewed before testing, and fixes are reviewed before retesting.

**Q: How do we version control agent changes?**
A: Track changes in git like any other code. Consider adding version numbers to agent files and maintaining a changelog.

### Technical Questions

**Q: What programming languages does this support?**
A: All languages! The agents are language-agnostic. Customize Domain Context sections with your specific tech stack.

**Q: Does this integrate with CI/CD?**
A: Agents focus on planning and quality. You can add a DevOps agent for deployment, or integrate your existing CI/CD with the workflow.

**Q: Can we automate parts of this workflow?**
A: Yes! Consider automating:
- Code review linting/formatting checks
- Test execution and coverage reporting
- Deployment pipeline after QA approval

**Q: How do we measure if this is working?**
A: Track metrics like:
- Cycle time (PRD to deployment)
- Code review iterations (target 1-2)
- QA iterations (target 1-2)
- Bugs found in production (should decrease)
- Team satisfaction (survey quarterly)

## Additional Resources

- **copilot-instructions.md** - Detailed workflow documentation with examples
- **agents/product-manager.md** - Product Manager agent definition with 3 examples
- **agents/staff-engineer.md** - Staff Engineer agent definition with 3 examples
- **agents/code-reviewer.md** - Code Reviewer agent definition with 3 examples
- **agents/qa.md** - QA agent definition with 3 examples

## Contributing

This agent system is designed to evolve with your project. Improvements to make:

1. **Add Examples**: Capture real examples from your project in agent files
2. **Refine Standards**: Document your team's specific conventions and patterns
3. **Extend Agents**: Add project-specific responsibilities and guidance
4. **Improve Workflow**: Adjust process based on what works for your team
5. **Share Learnings**: Document lessons learned and best practices

## License

This agent system is provided as-is for use in your projects. Customize freely to fit your needs.

## Support

For questions or issues:
1. Review the Troubleshooting section above
2. Check the detailed workflow in `copilot-instructions.md`
3. Review agent examples for similar scenarios
4. Customize agents with project-specific guidance

## Updating This Agent Group

This agent group can be updated from the upstream repository to get the latest improvements, bug fixes, and new features.

**To update:**

```bash
cd product-development-agents  # or wherever you installed this agent group
./update-from-upstream.sh
```

The script will:
- Fetch the latest changes from the upstream repository
- Update agents and documentation files
- Preserve the update script itself
- Show a summary of changes

After running the update:
```bash
git status              # Review what changed
git diff                # See detailed changes
git add .              # Stage the updates
git commit -m "Update product-development-agents from upstream"
```

**Note:** If you've made local customizations to agent files, the update will overwrite them. Consider keeping local modifications in a separate branch or using different file names.

---

**Version**: 1.0.0

**Last Updated**: 2024

Built with ❤️ for high-quality software development
