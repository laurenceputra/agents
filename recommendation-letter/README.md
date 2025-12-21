# Recommendation Letter Writing Agents

A comprehensive recommendation letter writing system for GitHub Copilot with four specialized agents that help letter writers create compelling, professional recommendation letters for software engineers seeking new roles.

## Overview

This system guides letter writers (managers, colleagues, mentors) through creating high-quality recommendation letters by combining structured information gathering, professional writing assistance, and quality assurance. The result is letters with specific examples, quantifiable impacts, and authentic voice that genuinely help candidates stand out.

### The Four Agents

1. **Recommendation Profiler** - Conducts structured discovery to gather comprehensive candidate information
2. **Recommendation Writer** - Creates compelling letter drafts incorporating specific examples and appropriate tone
3. **Recommendation Reviewer** - Ensures quality through critical evaluation and actionable feedback
4. **Devil's Advocate** - Credibility review for authenticity and believability (MANDATORY gate before signature)

### Key Features

- ✅ **Sequential Workflow**: Guided process from information gathering through final approval with credibility gate
- ✅ **Specific Examples**: Ensures every claim is supported by concrete evidence
- ✅ **Tone Adaptation**: Adjusts voice for manager, peer, or mentor relationships
- ✅ **Quality Assurance**: Built-in review process catches generic or weak content
- ✅ **Credibility Review**: Devil's Advocate challenges exaggerations and ensures authenticity
- ✅ **Iterative Refinement**: Supports revision cycles for continuous improvement
- ✅ **Software Engineering Focus**: Tailored for technical roles and accomplishments

## Quick Start

### Installation

1. **Copy to Your Project**
   ```bash
   # From your project root
   cp -r /path/to/recommendation-letter .github/recommendation-letter
   ```

2. **Start Using**
   
   In GitHub Copilot Chat, reference agents with `@`:
   ```
   @recommendation-profiler I need to write a recommendation letter for my team member
   ```

### Basic Usage

#### Scenario 1: Manager Writing Recommendation

```
Step 1: Gather Information
You: "@recommendation-profiler I'm writing a recommendation for Sarah Chen, my Senior Engineer for 3 years, who's applying for a Staff Engineer role."

Profiler will:
- Ask about Sarah's technical accomplishments
- Request specific examples with metrics
- Explore professional qualities with anecdotes
- Identify standout moments
- Create comprehensive candidate profile

Step 2: Create Letter Draft
(Automatic handoff to @recommendation-writer)

Writer will:
- Structure professional business letter
- Write compelling opening establishing your credibility
- Incorporate specific examples from profile
- Use authoritative manager tone
- Create strong endorsement closing

Step 3: Quality Review
(Automatic handoff to @recommendation-reviewer)

Reviewer will:
- Verify specific examples support claims
- Check for quantifiable impacts
- Ensure appropriate tone and authenticity
- Approve or provide improvement suggestions

Step 4: Finalize
- Review approved letter
- Make any personal adjustments
- Add signature
- Submit with candidate's application
```

#### Scenario 2: Peer Writing Recommendation

```
You: "@recommendation-profiler I want to write a recommendation for Marcus, my teammate for 2 years."

System guides you through:
1. Profiler: Gather collaboration examples, pair programming experiences, joint projects
2. Writer: Create letter with collaborative peer tone
3. Reviewer: Ensure peer perspective is clear and authentic

Result: Professional letter emphasizing partnership and firsthand observation
```

#### Scenario 3: Mentor Recommending Mentee

```
You: "@recommendation-profiler I'm recommending Jordan, who I've mentored for 18 months, for a mid-level role."

System guides you through:
1. Profiler: Focus on growth trajectory, learning ability, initiative
2. Writer: Create letter with supportive, growth-focused mentor tone
3. Reviewer: Verify emphasis on development and potential

Result: Compelling letter highlighting mentee's growth and future potential
```

## Workflow

### The Sequential Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                  RECOMMENDATION LETTER WORKFLOW              │
└─────────────────────────────────────────────────────────────┘

                    ┌──────────────────┐
                    │  Letter Writer   │
                    │  (Manager/Peer/  │
                    │     Mentor)      │
                    └────────┬─────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  RECOMMENDATION PROFILER     │
              │  • Structured interview      │
              │  • Gather accomplishments    │
              │  • Collect examples          │
              │  • Create comprehensive      │
              │    candidate profile         │
              └──────────┬───────────────────┘
                         │
                         │ Profile with specific examples
                         ▼
              ┌──────────────────────────────┐
              │  RECOMMENDATION WRITER       │
              │  • Structure letter          │
              │  • Incorporate examples      │
              │  • Adapt tone to relationship│
              │  • Create compelling draft   │
              │    (1-2 pages)               │
              └──────────┬───────────────────┘
                         │
                         │ Draft letter
                         ▼
              ┌──────────────────────────────┐
              │  RECOMMENDATION REVIEWER     │
              │  • Check for specificity     │
              │  • Verify evidence           │
              │  • Validate tone             │
              │  • Provide feedback          │
              └──────┬──────────────┬────────┘
                     │              │
          NEEDS      │              │        APPROVED
          REVISION   │              │
                     ▼              ▼
           ┌─────────────┐   ┌─────────────┐
           │  Back to    │   │   Final     │
           │  Writer     │   │   Letter    │
           │  (Iterate)  │   │   Ready!    │
           └──────┬──────┘   └─────────────┘
                  │
                  │ Revised draft
                  │
                  └──────> Return to Reviewer
                          (Iterate until approved)
```

### Critical Rules

1. **Start with Profiler**: Always begin with information gathering for best results
2. **Specific Examples Required**: Every claim must have concrete supporting evidence
3. **Authentic Voice**: Letter should sound natural, not templated
4. **Expect Iteration**: 1-2 revision cycles typically needed for optimal quality
5. **Follow Handoffs**: Trust the workflow - each agent hands off to the next automatically

## Agent Descriptions

### Recommendation Profiler

**Purpose**: Comprehensive information gathering  
**Model**: Claude Sonnet 4.5 (copilot)

**Capabilities**:
- Conducts structured interviews with 10-15 focused questions
- Extracts technical accomplishments with specific details
- Identifies professional qualities with supporting anecdotes
- Captures standout moments and growth trajectory
- Creates comprehensive profile ready for letter writing

**When to use**:
- Starting fresh with recommendation letter
- Need guidance on what information to gather
- Want to ensure you have all necessary details

**Output**: Structured candidate profile with specific examples

---

### Recommendation Writer

**Purpose**: Professional letter draft creation  
**Model**: Claude Haiku 4.5 (copilot)

**Capabilities**:
- Structures letters with appropriate sections
- Writes compelling openings and closings
- Incorporates specific examples naturally
- Adapts tone for manager/peer/mentor relationships
- Maintains professional yet warm voice
- Produces 1-2 page letters (300-600 words)

**When to use**:
- Have candidate profile from Profiler
- Ready to create letter draft
- Need help with structure and flow

**Output**: Complete draft recommendation letter

---

### Recommendation Reviewer

**Purpose**: Quality assurance and refinement  
**Model**: Claude Sonnet 4.5 (copilot)

**Capabilities**:
- Reviews for clarity, impact, and professionalism
- Verifies specific examples support claims
- Checks quantifiable impacts are included
- Ensures appropriate tone and authenticity
- Provides actionable improvement suggestions
- Approves when quality standards met

**When to use**:
- Have draft letter from Writer
- Want quality check before finalizing
- Need feedback on strengthening letter

**Output**: Structured review with approval or revision recommendations

## What Makes a Strong Recommendation Letter

### Essential Elements

1. **Clear Relationship Context**
   - State your role and relationship to candidate
   - Indicate duration of working together
   - Establish your credibility as reference

2. **Specific Technical Accomplishments**
   - Name actual projects with concrete details
   - Include technologies and approaches used
   - Provide quantifiable impacts (metrics, timeframes, scale)
   - Explain candidate's specific contributions

3. **Professional Qualities with Evidence**
   - Demonstrate qualities through stories, don't just state them
   - Use specific anecdotes showing behaviors
   - Include outcomes and impacts of these qualities
   - Balance technical with interpersonal skills

4. **Authentic Voice**
   - Sound like yourself, not a template
   - Match tone to your relationship (manager/peer/mentor)
   - Show genuine enthusiasm appropriate to your experience
   - Avoid clichés and generic statements

5. **Strong Endorsement**
   - Clear statement of recommendation strength
   - Contact information for follow-up
   - Confident closing that reinforces support

### Example Comparison

**❌ Weak (Generic)**:
> "John is an excellent software engineer who writes clean code and works well with others. He's very skilled and would be great for your team."

**✅ Strong (Specific)**:
> "John designed our caching layer that reduced API response times by 60% while handling complex edge cases like distributed cache invalidation. When I was stuck on a race condition that had stumped our team for weeks, John methodically traced it through multiple services and designed a distributed locks solution that eliminated the issue entirely."

## Tips for Different Writer Types

### Managers

**Your Strengths**:
- Comprehensive view of candidate's work
- Authoritative perspective on capabilities
- Can compare to other engineers at similar level
- Organizational impact visibility

**Letter Approach**:
- Use authoritative, comprehensive tone
- Provide broad assessment of technical and leadership skills
- Include comparisons to team or industry standards
- Emphasize impact on team/organization
- Express strong confidence in recommendations

**Example Opening**:
> "As [Candidate]'s Engineering Manager for the past three years at [Company], I have had the privilege of watching them evolve from a strong Senior Engineer into a technical leader who consistently drives significant impact across our entire engineering organization."

---

### Peers/Colleagues

**Your Strengths**:
- Firsthand collaboration experience
- Detailed technical knowledge of candidate's work
- Authentic partnership stories
- Day-to-day interaction insights

**Letter Approach**:
- Use collaborative, observational tone
- Focus on specific partnership examples
- Emphasize teamwork and collaboration quality
- Share pair programming or joint project experiences
- Express genuine appreciation for working together

**Example Opening**:
> "I have worked alongside [Candidate] as a teammate at [Company] for the past two years, and they have consistently been one of the most talented and reliable engineers I've had the pleasure of collaborating with."

---

### Mentors

**Your Strengths**:
- Visibility into growth and development
- Understanding of learning approach
- Perspective on potential
- Long-term career trajectory insights

**Letter Approach**:
- Use supportive, growth-focused tone
- Emphasize development and learning ability
- Highlight initiative and response to feedback
- Focus on potential and future capabilities
- Express pride in mentee's progress

**Example Opening**:
> "I have had the privilege of mentoring [Candidate] for the past 18 months at [Company], and I have been consistently impressed by their rapid growth, initiative, and potential."

## Troubleshooting

### "I don't know the candidate that well"

**Solution**: Be honest with the Profiler. Options:
1. Focus letter on specific areas where you do have direct experience
2. Suggest candidate ask someone with closer working relationship
3. Provide limited scope recommendation for what you genuinely know

---

### "I can't think of specific examples"

**Solution**: The Profiler will help with structured questions:
- What projects did you work on together?
- When did they impress you most?
- How do they compare to others at similar level?
- What would you tell a friend asking about them?

---

### "The letter sounds too generic"

**Solution**: The Reviewer will catch this and request:
- Add specific project names and technologies
- Include quantifiable impacts (percentages, timeframes)
- Replace general statements with concrete anecdotes
- Add memorable details that make candidate stand out

---

### "I'm not sure about the tone"

**Solution**: Tell the Profiler your relationship type:
- Manager → Authoritative, comprehensive assessment
- Peer → Collaborative, observational perspective
- Mentor → Supportive, growth-focused narrative

The Writer will adapt automatically.

---

### "The letter needs to be shorter/longer"

**Solution**: Standard is 1-2 pages (300-600 words). The Reviewer will:
- Flag if letter is too short (<250 words) - needs more detail
- Flag if letter is too long (>700 words) - loses impact
- Suggest which sections to expand or condense

## Sample Letter Structure

```
[Date]

[Recipient Name/Title - if known]
[Company Name - if known]

Dear Hiring Manager [or specific name],

[OPENING PARAGRAPH]
- State your relationship to candidate
- Indicate duration of working together
- Clear recommendation statement
- Brief preview of candidate's strengths

[BODY PARAGRAPH 1: Technical Accomplishments]
- Specific project or achievement
- Candidate's role and contributions
- Technologies and impact metrics
- What this demonstrates

[BODY PARAGRAPH 2: Professional Qualities]
- Key qualities (collaboration, leadership, etc.)
- Specific examples showing these qualities
- Impact on team or organization

[OPTIONAL PARAGRAPH 3: Additional Strengths]
- Standout moments or achievements
- Growth trajectory
- Unique differentiators

[CLOSING PARAGRAPH]
- Summarize why candidate is exceptional
- Direct recommendation statement
- Offer for additional information
- Contact details

Sincerely,

[Your Name]
[Your Title]
[Company]
[Email]
[Phone - optional]
```

## Frequently Asked Questions

**Q: How long does the process take?**  
A: Typically 20-40 minutes for the complete workflow from profiling through final approval.

**Q: Can I skip the Profiler and go straight to the Writer?**  
A: Yes, if you already have a comprehensive candidate profile with specific examples. But starting with Profiler typically produces better letters.

**Q: What if I disagree with the Reviewer's feedback?**  
A: Reviewer feedback is suggestions, not requirements. You can choose which recommendations to incorporate. The goal is to help, not dictate.

**Q: Can I use this for academic recommendations?**  
A: This system is optimized for professional software engineering roles. Academic letters have different requirements and conventions.

**Q: What if the candidate has both strengths and weaknesses?**  
A: Focus on genuine strengths without fabricating or exaggerating. An authentic positive recommendation is better than an inflated one. If you can't write a strong letter, it may be better to decline.

**Q: Should I let the candidate see the letter before submitting?**  
A: Check your company's policy. Some organizations allow this, others don't. When in doubt, focus on writing an honest, supportive letter you'd be comfortable with the candidate seeing.

## Version History

- **1.0.0** - Initial recommendation letter writing system with sequential workflow and four specialized agents

## Updating This Agent Group

This agent group can be updated from the upstream repository to get the latest improvements, bug fixes, and new features.

**To update:**

```bash
cd recommendation-letter  # or wherever you installed this agent group
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
git commit -m "Update recommendation-letter agents from upstream"
```

**Note:** If you've made local customizations to agent files, the update will overwrite them. Consider keeping local modifications in a separate branch or using different file names.

## Support and Feedback

This agent system is designed to help you create compelling recommendation letters efficiently. If you encounter issues or have suggestions:
- Provide feedback through your organization's agent management process
- Note specific scenarios where the agents could improve
- Share examples of particularly successful letters created with the system

---

## Getting Started Checklist

Before writing your first recommendation letter with this system:

- [ ] Confirm you're comfortable recommending this candidate
- [ ] Gather basic information (candidate name, target role if known, your relationship)
- [ ] Set aside 20-40 minutes for the complete process
- [ ] Start with `@recommendation-profiler` in GitHub Copilot Chat
- [ ] Trust the workflow - let agents hand off automatically
- [ ] Review and refine based on Reviewer feedback
- [ ] Add your signature to approved letter

**Ready to start? Use: `@recommendation-profiler [your scenario]`**
