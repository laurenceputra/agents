# GitHub Copilot Instructions - Recommendation Letter Writing System

## Overview

This is a structured recommendation letter writing system with four specialized agents that help letter writers (managers, colleagues, mentors) create compelling, professional recommendation letters for software engineers seeking new roles. The system guides writers from initial information gathering through final letter creation with quality assurance and credibility review.

## Core Principle

**Specific examples and authentic voice make recommendation letters effective.** Generic praise is forgettable, but concrete stories with quantifiable impacts help candidates stand out. The system ensures every letter includes specific evidence, maintains appropriate tone for the writer's relationship, and passes credibility review before signature. Devil's Advocate ensures authenticity and believability.

## The Four Agents

### Recommendation Profiler (`agents/recommendation-profiler.agent.md`)
**Role**: Information gathering and candidate analysis  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: recommendation-writer

**When to use**: 
- Starting the recommendation letter process
- Need to gather comprehensive candidate information
- Want structured guidance on what to include

**What it does**:
- Conducts structured interviews with letter writers
- Gathers technical accomplishments, examples, and anecdotes
- Creates comprehensive candidate profile
- Identifies key themes and standout qualities
- Prepares foundation for compelling letter

### Recommendation Writer (`agents/recommendation-writer.agent.md`)
**Role**: Draft recommendation letter creation  
**Model**: Claude Haiku 4.5 (copilot)  
**Handoffs to**: recommendation-reviewer

**When to use**:
- Have complete candidate profile from Profiler
- Ready to create letter draft
- Need help structuring content effectively

**What it does**:
- Structures letter with appropriate sections
- Writes compelling content incorporating specific examples
- Adapts tone based on relationship (manager/peer/mentor)
- Creates strong opening and closing
- Produces 1-2 page professional letter

### Recommendation Reviewer (`agents/recommendation-reviewer.agent.md`)
**Role**: Quality assurance and refinement  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: recommendation-writer (for revisions), devils-advocate

**When to use**:
- Have draft letter from Writer
- Want quality check before finalizing
- Need feedback on how to strengthen letter

**What it does**:
- Reviews letter for clarity, impact, and professionalism
- Verifies specific examples support claims
- Checks technical accuracy and appropriate tone
- Provides actionable improvement suggestions
- Approves when quality standards met

### Devil's Advocate (`agents/devils-advocate.agent.md`) **[MANDATORY CREDIBILITY GATE]**
**Role**: Credibility and authenticity review before signature  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: recommendation-writer (for revisions)

**When to use**:
- After Reviewer approval
- Before letter signature and submission
- Need to ensure credibility and authenticity
- Want skeptical hiring manager perspective

**What it does**:
- Challenges exaggerated or unsubstantiated claims
- Identifies vague praise lacking specific support
- Surfaces red flags that might trigger skepticism
- Assesses authenticity and believability
- Provides final credibility gate before signature

## Workflow

### Primary Flow (Linear with Optional Iteration and Credibility Gate)

```
1. Recommendation Profiler
   ↓ (Comprehensive candidate profile)
   
2. Recommendation Writer
   ↓ (Draft letter)
   
3. Recommendation Reviewer
   ↓ (Quality review)
   │
   ├─ If NEEDS REVISION → Back to Recommendation Writer
   │                       ↑____________↓
   │                       (Iterate until approved)
   │
   └─ If APPROVED → 4. Devil's Advocate (MANDATORY credibility review)
                      ↓ (Authenticity check)
                      │
                      ├─ If CREDIBILITY CONCERNS → Back to Writer
                      │                             ↑____________↓
                      │                             (Fix and resubmit)
                      │
                      └─ If CREDIBLE → Final letter ready for signature
```

### Critical Rules

1. **Profiler First**: Always start with comprehensive information gathering
2. **Specific Examples Required**: Every claim must be supported by concrete evidence
3. **Authentic Voice**: Letter should sound natural for the writer's relationship
4. **Iterative Refinement**: Expect 1-2 revision cycles for best results
5. **Target Role Awareness**: Tailor content to position requirements when known
6. **Devil's Advocate Review Mandatory**: All letters must pass credibility review before signature

## Complete Usage Examples

### Example 1: Manager Writing for Senior Engineer

**Scenario**: Engineering manager recommending senior engineer Sarah for staff-level role at TechCorp

```
Step 1: Information Gathering

You: "@recommendation-profiler I need to write a recommendation letter for Sarah Chen, who's applying for a Staff Engineer position at TechCorp. I've been her manager for 3 years."

Profiler: "Thank you for helping Sarah! I'll ask questions to gather what we need.

How would you describe Sarah's most significant technical accomplishments during your time working together?"

You: "She led our microservices migration, which was a huge project. Also introduced TypeScript to the team and mentored five junior engineers."

Profiler: "Excellent. Let's dive into the microservices migration. What was Sarah's specific role, and what was the impact?"

You: "She designed the overall architecture, established patterns for service communication, and implemented the first three critical services. The migration reduced our deployment time from 2 hours to 15 minutes and improved system reliability from 99.5% to 99.9%."

[Conversation continues through technical accomplishments, professional qualities, examples...]

Profiler: "Based on our conversation, I've created a comprehensive profile. [Shows profile] Does this accurately capture your experience with Sarah?"

You: "Yes, perfect!"

Profiler: "Great! Handing off to @recommendation-writer to create your letter draft."

---

Step 2: Letter Creation

Writer: "Based on the profile, I've created a recommendation letter for Sarah. The letter emphasizes her technical leadership and mentorship with an authoritative manager tone.

[Shows complete draft letter]

This letter is approximately 480 words and highlights:
- Microservices migration with specific impact metrics
- Technical leadership through architecture review facilitation
- Mentorship of 5 engineers with outcome data
- Initiative demonstrated through weekend incident resolution

I'll hand off to the Recommendation Reviewer for quality assurance.

@recommendation-reviewer: Please review this letter."

---

Step 3: Quality Review

Reviewer: "# Recommendation Letter Review: Sarah Chen

**Status**: APPROVED ✓
**Confidence**: High

**Summary**: This is an outstanding recommendation letter that powerfully demonstrates Sarah's readiness for a Staff Engineer role. The letter uses specific, quantifiable examples and showcases technical leadership through concrete anecdotes.

**Strengths**:
- Exceptional opening establishing credibility
- Specific metrics throughout (deployment time, reliability improvements)
- Compelling growth narrative
- Strong specific examples of initiative
- Powerful closing with unambiguous endorsement

**Decision**: APPROVED - This letter exceeds quality standards and is ready for your signature.

---

Next Steps: Review the letter one final time, make any personal adjustments, and add your signature. This letter is ready to strongly support Sarah's candidacy."

You: "This looks great, thank you!"
```

---

### Example 2: Peer Recommending Colleague

**Scenario**: Software engineer recommending teammate Marcus for similar role at new company

```
Step 1: Information Gathering

You: "@recommendation-profiler I want to write a recommendation for Marcus Thompson, my teammate for the past 2 years. We're both Senior Engineers."

Profiler: "Great! I'll help you gather the right information. Can you tell me about some projects where you worked closely with Marcus?"

You: "We built the entire payment processing system together. We also collaborated on the API redesign last quarter."

Profiler: "Let's focus on the payment processing system. What was Marcus's contribution, and what impressed you most about his work?"

You: "Marcus took ownership of the fraud detection component, which was the trickiest part. He researched different approaches, designed an elegant solution, and handled all the edge cases I wouldn't have thought of. The system processes 50,000 transactions daily with zero fraud incidents in the past year."

[Conversation continues...]

Profiler: "Here's the comprehensive profile I've created. [Shows profile] Does this capture your experience accurately?"

You: "Yes, looks good!"

Profiler: "@recommendation-writer: Please create the letter based on this profile."

---

Step 2: Letter Creation

Writer: "I've created a recommendation letter with a collaborative peer tone appropriate for your relationship.

[Shows draft letter with peer perspective, pair programming examples]

@recommendation-reviewer: Please review for quality."

---

Step 3: Quality Review

Reviewer: "**Status**: APPROVED ✓

This letter effectively showcases Marcus's capabilities through a peer lens. Excellent use of pair programming collaboration story and specific technical examples. The tone is authentic and professional.

The letter is ready for your signature."
```

---

### Example 3: Mentor Recommending Junior Engineer

**Scenario**: Senior engineer mentoring junior engineer Jordan for 18 months, writing recommendation for mid-level role

```
Step 1: Information Gathering

You: "@recommendation-profiler I'm writing a recommendation for Jordan Lee, who I've mentored for 18 months. They're moving from Junior to Mid-Level Engineer."

Profiler: "Wonderful! As Jordan's mentor, you've seen their growth firsthand. Can you tell me about Jordan's development during your mentorship?"

You: "Jordan started with solid fundamentals but limited production experience. Within six months, they independently designed and implemented a caching layer that reduced our API response times by 60%. I was impressed by how quickly they took on mid-level work."

Profiler: "That's excellent. Can you describe Jordan's approach to learning and growth?"

You: "Very proactive. Rather than waiting for assignments, Jordan actively asked for challenging work and sought feedback constantly. They also identified data consistency issues in our database migration that even senior engineers missed."

[Conversation continues about growth, initiative, collaboration...]

Profiler: "Here's the profile focusing on Jordan's growth trajectory and potential. [Shows profile]"

You: "Perfect representation!"

Profiler: "@recommendation-writer: Create letter emphasizing growth and potential."

---

Step 2: Letter Creation

Writer: "I've created a letter with a supportive, growth-focused mentor tone.

[Shows letter emphasizing learning ability, initiative, growth from junior to mid-level capabilities]

@recommendation-reviewer: Please review."

---

Step 3: Quality Review

Reviewer: "**Status**: APPROVED ✓

Excellent mentor perspective emphasizing growth trajectory and potential. The specific example of the caching layer implementation demonstrates Jordan's readiness for mid-level work. Strong narrative about proactive learning approach.

Letter is ready for signature."
```

## Decision Trees

### Quick Reference

| Your Situation | Agent to Use | What They'll Do |
|---|---|---|
| **Starting fresh** | @recommendation-profiler | Guide you through information gathering |
| **Have candidate profile** | @recommendation-writer | Create letter draft |
| **Have draft letter** | @recommendation-reviewer | Review and provide feedback |
| **Need revisions** | @recommendation-writer | Incorporate feedback and revise |

### Master Decision Tree

```
START: Need to write recommendation letter
  │
  Do you have a comprehensive candidate profile?
  │
  ├─ NO → Use @recommendation-profiler
  │        │
  │        Profiler asks structured questions:
  │        - Your relationship to candidate
  │        - Duration of working together
  │        - Technical accomplishments with examples
  │        - Professional qualities with anecdotes
  │        - Standout moments and growth
  │        │
  │        Profiler creates comprehensive profile
  │        ↓
  │        Proceed to letter creation
  │
  └─ YES → Do you have a draft letter?
           │
           ├─ NO → Use @recommendation-writer
           │        │
           │        Writer creates draft letter:
           │        - Structures content appropriately
           │        - Incorporates specific examples
           │        - Adapts tone to relationship
           │        - Creates strong opening/closing
           │        │
           │        Writer produces 1-2 page letter
           │        ↓
           │        Proceed to quality review
           │
           └─ YES → Use @recommendation-reviewer
                    │
                    Reviewer evaluates letter:
                    - Checks for specific examples
                    - Verifies appropriate tone
                    - Ensures professional quality
                    - Provides actionable feedback
                    │
                    Decision Point:
                    │
                    ├─ NEEDS REVISION
                    │   │
                    │   Reviewer provides specific feedback
                    │   ↓
                    │   @recommendation-writer revises
                    │   ↓
                    │   Return to reviewer
                    │   (Iterate until approved)
                    │
                    └─ APPROVED
                        │
                        Letter ready for signature!
                        ↓
                        DONE
```

## Quality Gates

### Gate 1: Profile Complete (Profiler → Writer Handoff)

Must have:
- [ ] Writer's relationship to candidate clearly documented
- [ ] At least 2-3 specific technical accomplishments with details
- [ ] Each accomplishment includes technologies and quantifiable impact
- [ ] At least 2-3 professional qualities with concrete examples
- [ ] Standout moments identified
- [ ] Recommendation strength assessed

**Pass Criteria**: Profile contains enough specific information to write compelling letter

---

### Gate 2: Draft Letter Created (Writer → Reviewer Handoff)

Must have:
- [ ] Proper business letter formatting
- [ ] Clear opening establishing relationship
- [ ] 2-3 body paragraphs with specific examples
- [ ] Strong closing with endorsement
- [ ] Appropriate length (300-600 words)
- [ ] Contact information included

**Pass Criteria**: Letter is complete draft ready for quality review

---

### Gate 3: Letter Approved (Reviewer → Final)

Must have:
- [ ] At least 2-3 specific examples with concrete details
- [ ] Technical accomplishments include quantifiable impacts
- [ ] Professional qualities demonstrated through anecdotes
- [ ] Tone matches writer's relationship authentically
- [ ] No vague or generic praise without evidence
- [ ] Professional standards met (grammar, formatting, structure)

**Pass Criteria**: Letter meets quality standards and will effectively support candidate

## Best Practices

### For Letter Writers

**Do**:
- ✅ Provide specific examples with concrete details
- ✅ Include quantifiable impacts (metrics, timeframes, scope)
- ✅ Share memorable moments that demonstrate character
- ✅ Be honest about relationship and experience with candidate
- ✅ Maintain authentic voice (don't try to sound overly formal)
- ✅ Focus on what makes candidate exceptional or standout

**Don't**:
- ❌ Use vague, generic praise ("excellent engineer," "team player")
- ❌ Exaggerate or include false information
- ❌ Write for candidates you don't know well
- ❌ Copy template language that sounds impersonal
- ❌ Make claims without supporting evidence
- ❌ Write overly long letters (stick to 1-2 pages)

### For Effective Letters

**Strong Opening** (establishes credibility):
- State relationship clearly (manager, peer, mentor)
- Indicate duration of working relationship
- Provide clear recommendation thesis
- Preview candidate's key strengths

**Compelling Body** (provides evidence):
- Use specific examples, not general statements
- Include quantifiable impacts and metrics
- Show qualities through stories, don't just tell
- Balance technical and interpersonal skills
- Adapt tone to relationship type

**Powerful Closing** (reinforces endorsement):
- Summarize why candidate is exceptional
- State recommendation strength clearly
- Offer to provide additional information
- Include contact information

## Common Pitfalls and Solutions

### Pitfall 1: Generic Praise Without Evidence
**Problem**: "John is an excellent engineer who always delivers high-quality work"  
**Solution**: "John designed our caching layer that reduced API response times by 60%, handling edge cases like cache invalidation and distributed consistency that prevented production issues"

### Pitfall 2: Vague Technical Claims
**Problem**: "Sarah improved our systems"  
**Solution**: "Sarah led our microservices migration that reduced deployment time from 2 hours to 15 minutes and improved system reliability from 99.5% to 99.9%"

### Pitfall 3: Stating Qualities Without Showing
**Problem**: "Marcus is a great collaborator"  
**Solution**: "As my preferred pair programming partner, Marcus creates an environment where we both learn. When we encountered a race condition that stumped the team for weeks, he methodically traced it through multiple services with me and designed a distributed locks solution"

### Pitfall 4: Inappropriate Tone for Relationship
**Problem**: Peer writing with overly authoritative tone  
**Solution**: Use collaborative language ("we worked together," "I observed") appropriate for peer relationship

### Pitfall 5: Missing Contact Information
**Problem**: Letter ends without way to follow up  
**Solution**: Always include email and optionally phone before signature

## Tips for Different Relationships

### Manager Writing for Direct Report
- Use authoritative, comprehensive tone
- Provide broad assessment of capabilities
- Compare to other engineers at similar level
- Emphasize organizational impact
- Express strong confidence in recommendations

### Peer Writing for Colleague
- Use collaborative, observational tone
- Focus on firsthand partnership experiences
- Emphasize teamwork and collaboration
- Share specific joint project examples
- Express genuine appreciation for working together

### Mentor Writing for Mentee
- Use supportive, growth-focused tone
- Emphasize learning ability and development
- Highlight initiative and response to feedback
- Focus on potential and future capabilities
- Express pride in mentee's progress

## Version History

- **1.0.0** - Initial recommendation letter writing system with Profiler, Writer, Reviewer, and Devil's Advocate agents

---

## Quick Start Reminder

1. **Start here**: `@recommendation-profiler` - Information gathering
2. **Then**: `@recommendation-writer` - Draft creation (automatic handoff)
3. **Finally**: `@recommendation-reviewer` - Quality assurance (automatic handoff)
4. **Iterate**: If revisions needed, Writer and Reviewer iterate until approved

The system guides you through the entire process from start to finish!
