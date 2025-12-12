# GitHub Copilot Instructions - Product Development Workflow

## Overview

This is a structured product development workflow system with four specialized agents that work together to deliver high-quality software. The system ensures quality through clear processes, iterative feedback loops, and mandatory quality gates.

## Core Principle

**Quality is built through collaboration and iteration.** Each agent has specialized expertise, and features progress through defined stages with clear approval criteria. Code must pass review before testing, and fixes must be reviewed before retesting.

## The Four Agents

### Product Manager (`agents/product-manager.md`)
**Role**: Define what to build and why it matters
- Creates PRDs with user stories and acceptance criteria
- Defines success metrics
- Prioritizes features
- **Kickstarts every development cycle**

### Staff Engineer (`agents/staff-engineer.md`)
**Role**: Design and implement technical solutions
- Creates technical designs
- Writes code and tests
- Fixes issues from Code Review and QA
- **Iterates based on feedback**

### Code Reviewer (`agents/code-reviewer.md`)
**Role**: Quality gate ensuring code standards
- Reviews all code for quality, security, and product alignment
- Provides detailed feedback
- **Mandatory gate before QA testing**
- Reviews both initial code and bug fixes

### QA (`agents/qa.md`)
**Role**: Validate quality through comprehensive testing
- Designs test strategies
- Executes testing against acceptance criteria
- Reports bugs with detailed reproduction steps
- **Final gate before deployment**

## Development Workflow

### Primary Flow (New Feature)

```
1. Product Manager
   ↓ (PRD with acceptance criteria)
   
2. Staff Engineer
   ↓ (Technical design + implementation)
   
3. Code Reviewer
   ↓ (Approve or reject with feedback)
   │
   ├─ If REJECTED → Back to Staff Engineer (Fix issues → Resubmit)
   │                 ↑________________↓
   │                 (Iterate until approved)
   │
   └─ If APPROVED → Proceed to QA
   
4. QA
   ↓ (Test all acceptance criteria)
   │
   ├─ If BUGS FOUND → Back to Staff Engineer → Code Reviewer → QA
   │                   ↑___________↓___________↑__________↓
   │                   (Fix → Review → Retest until pass)
   │
   └─ If ALL TESTS PASS → Approved for Deployment
   
5. Deployment
```

### Critical Rules

1. **Code Review is Mandatory**: All code must pass Code Review before reaching QA
2. **Fixes Go Through Review**: When QA finds bugs, fixes must be code-reviewed before retesting
3. **No Skipping Stages**: Cannot skip from Engineer directly to QA without Code Review
4. **Iterative Loops**: Expect multiple iterations in Code Review and QA cycles
5. **Clear Exit Criteria**: Each stage has specific approval criteria to proceed

## Workflow Details

### Phase 1: Requirements Definition (Product Manager)

**Agent**: `@product-manager`

**Trigger**: New feature request, bug report, or technical debt identified

**Input**:
- Feature request or problem statement
- User feedback or analytics
- Business objectives

**Activities**:
1. Analyze user needs and business goals
2. Create Product Requirements Document (PRD)
3. Write user stories (As a... I want... So that...)
4. Define acceptance criteria (Given-When-Then)
5. Establish success metrics
6. Review with stakeholders

**Output**:
- Complete PRD with:
  - Problem statement
  - User stories
  - Detailed acceptance criteria
  - Success metrics
  - Out of scope items
  - Dependencies

**Exit Criteria**:
- [ ] All requirements clearly defined
- [ ] Acceptance criteria are testable
- [ ] Success metrics are measurable
- [ ] Stakeholders have reviewed and approved

**Next Stage**: Staff Engineer for technical design

---

### Phase 2: Technical Design & Implementation (Staff Engineer)

**Agent**: `@staff-engineer`

**Trigger**: Approved PRD from Product Manager

**Input**:
- PRD with acceptance criteria
- Existing codebase and patterns
- Technical constraints

**Activities**:
1. **Design Phase**:
   - Create technical design document
   - Define architecture and components
   - Plan implementation approach
   - Identify risks and dependencies
   - Design for performance, security, scalability

2. **Implementation Phase**:
   - Write clean, well-tested code
   - Follow project conventions
   - Implement all acceptance criteria
   - Add comprehensive tests (unit, integration, E2E)
   - Update documentation

3. **Self-Review**:
   - Review own code before submitting
   - Run all tests (ensure they pass)
   - Check test coverage meets standards
   - Verify all acceptance criteria implemented

**Output**:
- Technical design document
- Code implementation
- Comprehensive tests
- Updated documentation

**Exit Criteria**:
- [ ] All acceptance criteria implemented
- [ ] Tests written and passing
- [ ] Code follows project conventions
- [ ] Documentation updated
- [ ] Self-review completed

**Next Stage**: Code Reviewer for quality gate

---

### Phase 3: Code Review (Code Reviewer)

**Agent**: `@code-reviewer`

**Trigger**: Staff Engineer submits code for review

**Input**:
- Code changes (PR/diff)
- Technical design document
- PRD for context
- Tests

**Activities**:
1. Review code for:
   - **Security**: Vulnerabilities, injection attacks, auth issues
   - **Correctness**: Logic bugs, edge cases, error handling
   - **Quality**: Readability, maintainability, best practices
   - **Performance**: Efficient algorithms, no obvious bottlenecks
   - **Product Alignment**: Meets PRD requirements
   - **User Experience**: Good UX decisions, helpful errors
   - **Testing**: Adequate test coverage, quality tests

2. Provide feedback:
   - **Critical Issues**: Must fix before approval (security, correctness)
   - **Recommendations**: Should consider (quality improvements)
   - **Suggestions**: Nice to have (minor improvements)

3. Make decision:
   - **Approve**: Code meets all quality standards → Proceed to QA
   - **Approve with Suggestions**: Minor improvements suggested but not blocking
   - **Reject**: Critical issues found → Back to Engineer

**Output**:
- Detailed code review report with:
  - Approval decision
  - Issues identified (with severity)
  - Specific, actionable recommendations
  - Product alignment assessment
  - Test coverage evaluation

**Exit Criteria**:
- [ ] No critical security issues
- [ ] No correctness bugs
- [ ] Code quality meets standards
- [ ] Test coverage adequate
- [ ] Meets PRD requirements
- [ ] All feedback from previous review addressed (if resubmission)

**Decision Points**:

**If APPROVED** → Proceed to QA for testing

**If REJECTED** → Engineer Feedback Loop:
```
Code Reviewer (Reject with feedback)
   ↓
Staff Engineer (Fix issues, address feedback)
   ↓
Staff Engineer (Self-review, verify fixes)
   ↓
Code Reviewer (Re-review)
   ↓
(Repeat until approved)
```

**Next Stage** (after approval): QA for testing

---

### Phase 4: Quality Assurance (QA)

**Agent**: `@qa`

**Trigger**: Code Review approved implementation

**Input**:
- PRD with acceptance criteria
- Code-reviewer-approved implementation
- Technical design for context
- Test environment access

**Activities**:
1. **Test Planning** (if not done earlier):
   - Review acceptance criteria
   - Create test plan and test cases
   - Identify edge cases and risk areas
   - Plan non-functional testing

2. **Test Execution**:
   - Execute all test cases systematically
   - Test all acceptance criteria from PRD
   - Test edge cases and error scenarios
   - Perform non-functional testing:
     - Performance (response times, load)
     - Security (injection, auth)
     - Accessibility (WCAG compliance)
   - Cross-browser and device testing
   - Exploratory testing

3. **Bug Reporting**:
   - Document each bug with:
     - Clear reproduction steps
     - Expected vs actual behavior
     - Screenshots/logs/evidence
     - Severity and user impact
     - Which acceptance criteria blocked

4. **Regression Testing**:
   - Ensure existing functionality not broken
   - Test related features
   - Verify no unintended side effects

**Output**:

**If Bugs Found**:
- Detailed bug reports for each issue
- Test results summary
- Failed acceptance criteria list

**If All Tests Pass**:
- Complete test results report
- All acceptance criteria status (all passed)
- Test coverage summary
- Approval for deployment

**Exit Criteria**:
- [ ] All acceptance criteria from PRD tested and passed
- [ ] No critical or high-priority bugs
- [ ] Edge cases validated
- [ ] Non-functional requirements met
- [ ] Regression testing completed (no new issues)
- [ ] Cross-browser/device testing passed

**Decision Points**:

**If ALL TESTS PASS** → Approved for Deployment ✅

**If BUGS FOUND** → QA Feedback Loop:
```
QA (Find bugs, create detailed bug reports)
   ↓
Staff Engineer (Fix bugs, identify root cause)
   ↓
Code Reviewer (Review bug fixes)
   │
   ├─ If issues in fix → Back to Engineer
   └─ If fix looks good → Approve
   ↓
QA (Retest: verify bug fixed + regression test)
   │
   ├─ If still fails or new issues → Back to Engineer
   └─ If passes → Continue testing remaining criteria
   
(Repeat until all tests pass)
```

**Key Rule**: Bug fixes MUST go through Code Review before returning to QA for retest.

**Next Stage** (after full approval): Deployment

---

## Feedback Loops Explained

### Code Review Loop

**When**: Code Reviewer finds issues in submitted code

**Flow**:
```
Staff Engineer submits code
   ↓
Code Reviewer reviews and REJECTS (issues found)
   ↓
Staff Engineer receives detailed feedback
   ↓
Staff Engineer fixes all critical issues
   ↓
Staff Engineer addresses recommendations
   ↓
Staff Engineer self-reviews changes
   ↓
Staff Engineer resubmits for Code Review
   ↓
Code Reviewer re-reviews
   ↓
(If still has issues → Repeat)
(If approved → Proceed to QA)
```

**Exit Condition**: Code Reviewer approval

**Typical Iterations**: 1-3 reviews common; 0 reviews (approve first time) ideal but rare

---

### QA Loop

**When**: QA finds bugs during testing

**Flow**:
```
QA tests code-reviewer-approved implementation
   ↓
QA finds bugs (tests fail)
   ↓
QA creates detailed bug reports
   ↓
Staff Engineer receives bug reports
   ↓
Staff Engineer reproduces and fixes bugs
   ↓
Staff Engineer adds/updates tests to prevent regression
   ↓
Staff Engineer submits fix to Code Reviewer
   ↓
Code Reviewer reviews bug fix
   │
   ├─ If issues in fix → Back to Engineer (fix the fix)
   └─ If fix is good → Approve
   ↓
QA retests the bug fix
   ↓
QA performs regression testing
   ↓
(If still fails or new bugs → Repeat from step 3)
(If passes → Continue testing remaining criteria)
   ↓
When ALL criteria pass → QA approves for deployment
```

**Exit Condition**: All acceptance criteria pass, no bugs found

**Typical Iterations**: 1-4 QA cycles common depending on complexity

**Critical Note**: Bug fixes go **Engineer → Code Review → QA**, NOT directly back to QA

---

## Workflow Variants

### Variant 1: New Feature Development

**Use**: Building new functionality from user stories

**Flow**: Full workflow PM → Engineer → Code Review → QA → Deploy

**Emphasis**:
- Comprehensive PRD with clear acceptance criteria
- Thoughtful technical design
- Thorough testing of all scenarios
- User experience focus

**Typical Timeline**: 1-3 weeks depending on complexity

---

### Variant 2: Bug Fix (from Production)

**Use**: Fixing bugs reported by users or monitoring

**Flow**: 
1. PM: Create bug report in PRD format (treat as mini-PRD)
   - User story: "As a user, I should not experience [bug]"
   - Acceptance criteria: Bug is fixed, regression tests prevent recurrence
   
2. Engineer: Reproduce, fix, add regression tests

3. Code Review: Review fix for correctness and no side effects

4. QA: Verify bug fixed + regression test

**Emphasis**:
- Root cause analysis (fix cause, not symptom)
- Regression tests to prevent recurrence
- Verify related functionality not broken

**Typical Timeline**: 1-3 days for critical bugs, 1 week for others

---

### Variant 3: Refactoring / Technical Debt

**Use**: Improving code quality, architecture, or performance without changing user-facing behavior

**Flow**: Full workflow, but PRD focuses on technical improvements

**PM's Role**:
- Document why refactoring is needed (business case)
- Define success metrics (performance improvement, reduced bugs, developer velocity)
- Acceptance criteria: Functionality unchanged, improvements measurable

**QA's Role**:
- Extensive regression testing (ensure behavior unchanged)
- Validate success metrics (performance, reliability)

**Emphasis**:
- Clear technical justification
- Comprehensive regression testing
- Measurable improvements

**Typical Timeline**: 1-4 weeks depending on scope

---

### Variant 4: Performance Optimization

**Use**: Improving system performance (speed, resource usage, scalability)

**Flow**: Full workflow with heavy performance testing

**PM's Role**:
- Define performance targets (specific metrics: response time, throughput, etc.)
- User story focused on user experience improvement
- Acceptance criteria with measurable performance benchmarks

**Engineer's Role**:
- Baseline current performance
- Implement optimizations
- Benchmark improvements

**QA's Role**:
- Performance testing against targets
- Load testing
- Verify no functionality regressions

**Emphasis**:
- Measurable baselines and targets
- Comprehensive performance testing
- Ensure optimizations don't break functionality

**Typical Timeline**: 1-2 weeks

---

### Variant 5: Security Fix

**Use**: Addressing security vulnerabilities

**Flow**: Expedited workflow with heavy security focus

**PM's Role**:
- Brief PRD documenting vulnerability and impact
- Acceptance criteria focused on closing vulnerability

**Engineer's Role**:
- Fix vulnerability
- Add security tests

**Code Review's Role**:
- Thorough security review
- Verify fix doesn't introduce new vulnerabilities
- Fast turnaround (high priority)

**QA's Role**:
- Security testing (penetration testing, injection attempts)
- Verify vulnerability closed
- Regression testing

**Emphasis**:
- Speed (security is urgent)
- Thoroughness (ensure complete fix)
- Security testing

**Typical Timeline**: 1-3 days (critical), 1 week (high priority)

---

## Collaboration Patterns

### Agent-to-Agent Communication

#### PM ↔ Staff Engineer
- **PM to Engineer**: Provide PRD, clarify requirements, answer questions
- **Engineer to PM**: Ask clarifying questions, raise feasibility concerns, suggest requirement adjustments
- **When**: Design phase, implementation phase (when blockers arise)

#### Staff Engineer ↔ Code Reviewer
- **Engineer to Reviewer**: Submit code, respond to feedback, explain design decisions
- **Reviewer to Engineer**: Provide feedback, ask clarifying questions, approve/reject
- **When**: After implementation, during fix iterations

#### Staff Engineer ↔ QA
- **QA to Engineer**: Report bugs with reproduction steps, verify fixes work
- **Engineer to QA**: Provide fix details, explain root cause, request specific testing
- **When**: After QA testing begins, during bug fix cycles

#### Code Reviewer ↔ QA
- **Code Reviewer to QA**: Confirm code is approved and ready for testing
- **QA to Code Reviewer**: Provide feedback on test coverage adequacy, highlight patterns causing bugs
- **When**: Coordination on test strategy, post-mortem on quality issues

#### PM ↔ QA
- **PM to QA**: Provide acceptance criteria, clarify expected behavior
- **QA to PM**: Provide test results, report when requirements are ambiguous or untestable
- **When**: Test planning, test results reporting

### Concurrent Work

Some activities can happen in parallel:

**During Implementation Phase**:
- Engineer writes code
- QA creates test plan and test cases (from PRD)
- PM prepares next feature PRD

**During Code Review**:
- Code Reviewer reviews code
- QA finalizes test environment setup
- PM gathers feedback on current features

**Efficiency Tip**: Don't wait for everything to be perfect. QA can start test planning as soon as PRD exists, even before implementation begins.

---

## Decision Trees

### When to Consult Which Agent

#### "I have a user problem or feature idea"
→ Start with **Product Manager**
- PM will create PRD with user stories and acceptance criteria

#### "I have a PRD and need to implement it"
→ Consult **Staff Engineer**
- Engineer will create technical design and implementation

#### "I have code that needs review"
→ Consult **Code Reviewer**
- Reviewer will evaluate quality, security, and product alignment

#### "I have code-reviewer-approved code that needs testing"
→ Consult **QA**
- QA will test against acceptance criteria and report bugs

#### "I received code review feedback"
→ Work with **Staff Engineer**
- Engineer will fix issues and resubmit for review

#### "I received a bug report from QA"
→ Work with **Staff Engineer**
- Engineer will fix bugs, then submit to **Code Reviewer**, then back to **QA**

#### "I need to know if requirements are clear"
→ Ask **Staff Engineer** and **QA**
- Engineer checks technical feasibility
- QA checks testability

#### "I want to skip code review and go straight to QA"
→ **Not allowed** ❌
- All code must pass Code Review before QA testing
- This ensures consistent quality standards

---

## Best Practices

### For Efficient Workflow

1. **Start with Clear Requirements**: Vague PRDs cause rework. Invest time in PM phase.

2. **Engineer Self-Review**: Review your own code thoroughly before submitting to Code Reviewer. Catch obvious issues yourself.

3. **Code Review Fast Feedback**: Reviewers should provide feedback within [project SLA, e.g., 24 hours]. Engineers should address feedback quickly.

4. **QA Early Involvement**: QA should review PRD and create test plan during design/implementation phase, not after.

5. **Communicate Blockers Early**: Don't wait until deadline to raise issues. Alert the team immediately.

6. **Document Decisions**: Capture important decisions in PRD, technical design, or bug reports. Future you will thank current you.

7. **Iterate Quickly**: Small, frequent iterations are better than one giant change. Shorter feedback loops catch issues earlier.

### For Quality

1. **Security First**: Security issues are always critical priority. Don't ship vulnerable code.

2. **Test Early, Test Often**: Engineer should run tests continuously during development. Catch bugs before Code Review.

3. **Comprehensive Testing**: QA should test not just happy path, but edge cases, error scenarios, and non-functional requirements.

4. **Regression Testing is Mandatory**: Always verify fixes don't break existing functionality.

5. **User Perspective**: Always ask "Would I want to use this?" Keep user experience top of mind.

### For Collaboration

1. **Be Respectful**: Feedback is about the work, not the person. Assume good intent.

2. **Be Specific**: Vague feedback ("this needs work") is unhelpful. Provide specific, actionable guidance.

3. **Be Constructive**: Don't just point out problems; suggest solutions or ask questions to understand reasoning.

4. **Be Responsive**: Respond to questions and feedback promptly. Don't let work sit idle.

5. **Celebrate Success**: Recognize good work. Positive feedback motivates and builds team culture.

---

## Quality Gates Summary

### Gate 1: Product Manager Approval
- **Criteria**: Requirements are clear, testable, and stakeholder-approved
- **Output**: Approved PRD
- **Prevents**: Building the wrong thing

### Gate 2: Code Review Approval
- **Criteria**: Code meets quality, security, and product alignment standards
- **Output**: Approved code changes
- **Prevents**: Poor quality code reaching testing and production

### Gate 3: QA Approval
- **Criteria**: All acceptance criteria pass, no critical bugs, regression tests pass
- **Output**: Test results report approving deployment
- **Prevents**: Buggy or incomplete features reaching production

---

## Metrics and Success Criteria

### Workflow Efficiency Metrics

- **Cycle Time**: Time from PRD approval to deployment
  - Target: Depends on complexity, typically 1-3 weeks for medium features

- **Code Review Iterations**: Number of review cycles before approval
  - Target: 1-2 reviews (0 reviews ideal, >3 indicates issues)

- **QA Iterations**: Number of QA cycles before approval  
  - Target: 1-2 cycles (0 bugs ideal, >4 indicates quality issues upstream)

- **Rework Rate**: Percentage of code requiring significant rework
  - Target: <20%

### Quality Metrics

- **Bugs Found in QA**: Number of bugs QA finds
  - Lower is better, but some bugs are expected
  - Track trends: Increasing bugs suggests quality issues

- **Bugs Found in Production**: Bugs that escaped QA
  - Target: <1% of deployments have critical bugs

- **Test Coverage**: Percentage of code covered by tests
  - Target: 80%+ for critical paths

- **Security Issues**: Critical/high security vulnerabilities found
  - Target: 0 in production, minimize in code review

---

## Troubleshooting Common Issues

### "Requirements keep changing during implementation"
- **Root Cause**: PRD was not thorough enough, or new information emerged
- **Solution**: Pause implementation, update PRD with PM, get stakeholder approval, then resume
- **Prevention**: More thorough discovery and design phase; involve Engineer in PRD review

### "Code review keeps rejecting implementation"
- **Root Cause**: Misalignment on standards, or quality issues
- **Solution**: Engineer and Reviewer should align on standards; Engineer should self-review more thoroughly
- **Prevention**: Documented coding standards; examples of good code; pair programming for complex features

### "QA keeps finding bugs"
- **Root Cause**: Insufficient testing by Engineer, or complex feature
- **Solution**: Engineer should improve test coverage; Increase testing rigor before submitting
- **Prevention**: Test-driven development; More thorough self-testing; Automated test requirements

### "Workflow is too slow"
- **Root Cause**: Bottlenecks in review stages, or excessive rework
- **Solution**: Identify bottleneck (review SLAs, rework rates); Address specific issue
- **Prevention**: Clear standards reduce review time; Better requirements reduce rework; Parallel work where possible

### "Bug fixes introduce new bugs"
- **Root Cause**: Insufficient understanding of root cause, or poor regression testing
- **Solution**: Require root cause analysis before fixing; Increase regression test coverage
- **Prevention**: Comprehensive unit tests; Better code design (less coupling); More thorough bug fix review

---

## Customization

This workflow is designed to work out-of-the-box, but you can customize it for your project:

### Project-Specific Configuration

Each agent has a "Domain Context (Project-Specific)" section. Customize with:

- **Tech Stack**: Languages, frameworks, libraries
- **Coding Standards**: Linting rules, naming conventions
- **Testing Requirements**: Coverage targets, required test types
- **Performance Targets**: Response time SLAs, resource limits
- **Security Policies**: Authentication patterns, compliance requirements
- **Accessibility Standards**: WCAG level (AA, AAA)

### Process Adjustments

You can adjust the workflow for your team:

- **Review SLAs**: Define expected turnaround times for reviews (e.g., 24 hours)
- **Approval Thresholds**: Define when code review can be skipped (e.g., trivial docs changes)
- **Testing Levels**: Define which features need E2E tests vs just unit tests
- **Deployment Process**: Add deployment agent or integrate with CI/CD

### Extension Points

You can add agents for additional roles:

- **DevOps Engineer**: Handles deployment, infrastructure, monitoring
- **Security Specialist**: Dedicated security reviews for high-risk features
- **UX Designer**: Designs interfaces, user flows before implementation
- **Data Analyst**: Validates analytics instrumentation, reviews metrics

---

## Examples: Complete Workflows

### Example 1: Password Reset Feature (Success Path)

**Day 1: Requirements**
1. PM creates PRD for password reset feature
   - User stories: "As a user who forgot my password..."
   - Acceptance criteria: Reset via email, 1-hour token expiration, rate limiting, etc.
   - Success metrics: Reduce support tickets by 80%
2. PM reviews PRD with stakeholders → Approved

**Day 2-3: Technical Design**
3. Engineer reviews PRD, asks clarifying questions to PM
4. Engineer creates technical design document
   - Architecture: Token service, email service, API endpoints, database schema
   - Security considerations: Cryptographic tokens, rate limiting, etc.
5. Engineer reviews design with PM → Aligned on approach

**Day 4-7: Implementation**
6. Engineer implements password reset feature
   - API endpoints, token service, frontend forms
   - Unit tests (90% coverage), integration tests, E2E tests
7. Engineer self-reviews code, runs all tests → All passing

**Day 8: Code Review (First Iteration)**
8. Engineer submits code to Code Reviewer
9. Code Reviewer reviews → **REJECTS** ❌
   - Critical Issue 1: Token generation uses Math.random() (not secure)
   - Critical Issue 2: SQL injection vulnerability
   - Critical Issue 3: Rate limiting by IP (should be by email)
   - Critical Issue 4: Tokens logged (sensitive data exposure)
10. Engineer receives feedback, understands issues

**Day 9: Code Review (Second Iteration)**
11. Engineer fixes all four critical issues
    - Uses crypto.randomBytes() for tokens
    - Parameterized SQL queries
    - Rate limit by email
    - Removes tokens from logs
12. Engineer self-reviews fixes, adds tests for issues
13. Engineer resubmits to Code Reviewer
14. Code Reviewer re-reviews → **APPROVED** ✅
    - All critical issues resolved
    - Test coverage good
    - Ready for QA

**Day 10-11: QA Testing (First Iteration)**
15. QA receives code-reviewer-approved implementation
16. QA executes test plan (27 test cases)
17. QA finds 2 bugs:
    - Bug #1: Token expiration edge case (exactly 1 hour boundary)
    - Bug #2: Password strength validation inconsistent on backend vs frontend
18. QA creates detailed bug reports with reproduction steps

**Day 12: Engineer Fixes Bugs**
19. Engineer reproduces both bugs
20. Engineer fixes both issues:
    - Fix #1: Use >= for expiration check (boundary condition)
    - Fix #2: Centralize validation logic, use on both frontend and backend
21. Engineer adds regression tests for both bugs
22. Engineer submits fixes to Code Reviewer

**Day 12: Code Review (Bug Fix)**
23. Code Reviewer reviews bug fixes → **APPROVED** ✅
    - Fixes are correct
    - Tests prevent regression
    - No new issues introduced

**Day 13: QA Retesting**
24. QA retests both bugs → Both fixed ✅
25. QA performs regression testing → No regressions ✅
26. QA completes remaining test cases → All 27 tests pass ✅
27. QA approves for deployment ✅

**Day 14: Deployment**
28. Feature deployed to production
29. PM monitors success metrics (support tickets decreased by 85%)

**Summary**: 2 weeks, 2 code review iterations, 2 QA iterations, successful deployment

---

### Example 2: Search Bug Fix (Quick Turnaround)

**Day 1 Morning: Bug Reported**
1. User reports search fails with special characters
2. PM creates mini-PRD (bug report format)
   - User story: "As a user, I should be able to search with quotes, apostrophes"
   - Acceptance criteria: Search handles special chars, no errors

**Day 1 Afternoon: Investigation & Fix**
3. Engineer reproduces bug
4. Engineer identifies root cause: Overly restrictive validation regex
5. Engineer implements fix:
   - Updates regex to allow common special characters
   - Adds URL encoding in frontend
   - Maintains security (blocks dangerous chars like <, >)
6. Engineer adds 8 new test cases for special characters
7. Engineer self-tests fix → Works ✅

**Day 1 End of Day: Code Review**
8. Engineer submits fix to Code Reviewer
9. Code Reviewer reviews → **APPROVED** ✅
   - Fix addresses root cause
   - Security maintained (injection prevention verified)
   - Test coverage excellent

**Day 2 Morning: QA Testing**
10. QA retests original bug → Fixed ✅
11. QA tests with various special characters → All work ✅
12. QA performs regression testing → No new issues ✅
13. QA approves for deployment ✅

**Day 2 Afternoon: Deployment**
14. Hotfix deployed to production
15. Bug resolved

**Summary**: 1.5 days, 1 code review (approved first time), 1 QA cycle (passed first time), successful fix

---

## Getting Started

### For New Projects

1. **Install**: Copy this agent group directory to your project root
2. **Rename**: Rename directory to `.github` (or keep current name if preferred)
3. **Customize**: Fill in "Domain Context (Project-Specific)" sections in each agent
4. **Test**: Run through workflow with a small feature to validate
5. **Iterate**: Adjust workflow as needed for your team

### For Existing Projects

1. **Install**: Copy this agent group directory to your project
2. **Customize**: Update agents with your existing standards and processes
3. **Phase In**: Start with one phase (e.g., code review) and expand
4. **Train**: Ensure team understands workflow and agents
5. **Measure**: Track metrics to assess impact and adjust

---

## Support

### Common Questions

**Q: Can we skip code review for trivial changes (typos, docs)?**
A: You can define exceptions in your customization, but be careful—even "trivial" changes can introduce issues.

**Q: What if QA finds bugs after deployment?**
A: Treat as new bug report. Follow Bug Fix variant: PM creates bug report PRD → Engineer fixes → Code Review → QA → Deploy hotfix.

**Q: Can Engineer and Code Reviewer be the same person?**
A: Not recommended. Code review should be an independent quality gate. If needed due to team size, at minimum require self-review checklist.

**Q: How do we handle urgent production issues?**
A: Expedited workflow: Quick PM bug report → Engineer fix → Fast code review (target 2-hour turnaround) → QA retest critical path → Deploy. Still maintain quality gates, just faster.

**Q: What if we disagree on whether code review should approve/reject?**
A: Escalate to tech lead or senior engineer. Document decision for future reference.

---

## Version History

- **1.0.0** - Initial product development workflow with PM, Engineer, Code Reviewer, QA agents
