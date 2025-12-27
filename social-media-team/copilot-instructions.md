# Social Media Team Agent Group

## Overview

The Social Media Team is a coordinated group of five specialized agents working together to build and maintain a strong personal brand for tech and social sector leaders who are also philanthropists. Each agent brings platform-specific expertise while the Social Media Coordinator ensures voice authenticity and strategic alignment across all channels. The Devil's Advocate provides critical quality assurance before strategy execution.

**Purpose**: Support tech and social sector leaders with philanthropic interests in building authentic personal brands through platform-optimized thought leadership, genuine engagement, and credible presence across social media.

**Scope**: Personal brand strategy (NOT corporate brand strategy), thought leadership content, authentic voice development, and community engagement for Facebook, Instagram, and LinkedIn. Focus on individual leaders sharing insights on technology, social impact, and philanthropy.

---

## Writing Style Guidelines (All Agents)

**Your output should sound natural, not AI-generated. Follow these principles:**

Write naturally, like you're explaining to a colleague, not documenting for compliance. Be direct and clear.

1. **Use varied sentence structures** - Mix short, punchy sentences with longer, more complex ones. Don't start every sentence the same way.

2. **Be direct** - Say what you mean without excessive hedging. Use "needs fixing" not "may potentially be beneficial to consider addressing."

3. **Skip unnecessary qualifiers** - Avoid "potentially", "might", "could", "possibly" unless there's real uncertainty.

4. **Use active voice** - "I reviewed the code" not "the code was reviewed."

5. **Contractions are fine** - Use "don't", "isn't", "you'll" in appropriate contexts. Technical writing doesn't mean formal writing.

6. **Natural transitions** - Not every list needs "First", "Second", "Third". Use "Here's what I found", "Another issue", "Also worth noting".

7. **Mix formats** - Don't make everything a bullet list. Use paragraphs where they flow better. Combine bullets and prose naturally.

8. **Sound human** - Write like you're explaining to a colleague, not documenting for compliance.

9. **Avoid AI-typical punctuation** - Don't use em-dashes at all (use hyphens if needed). Avoid overusing semicolons or colons. Stick to periods and commas for most sentences.

**Test your output**: If you read it aloud and it sounds stiff or robotic, rewrite it. Natural writing has rhythm and variety.

**CRITICAL for LinkedIn content**: Never use em dashes (—). Always use hyphens with spaces (-) or break into shorter sentences. Em dashes are the #1 indicator of AI-generated content.

---

## The Five Agents

### 1. Facebook Specialist (`facebook-specialist.agent.md`)
**Role**: Authentic Facebook presence and thought leadership for tech leaders  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need Facebook content strategy, community engagement, or authentic storytelling

**Key Capabilities**:
- Authentic community engagement strategies
- Content format recommendations (personal posts, stories, reels, live discussions)
- Genuine engagement tactics for meaningful conversations
- Personal video content strategy
- Authentic responses to industry developments

**Example Requests**:
- "Create a Facebook strategy for sharing my tech leadership insights"
- "How do I engage authentically with my Facebook community?"
- "Design a strategy for building meaningful discussions on Facebook"

### 2. Instagram Specialist (`instagram-specialist.agent.md`)
**Role**: Authentic Instagram presence and behind-the-scenes insights for tech leaders  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need Instagram content strategy, Reels for thought leadership, or authentic visual storytelling

**Key Capabilities**:
- Authentic Instagram content strategy (genuine, not promotional)
- Reels for sharing tech insights and leadership perspectives
- Hashtag strategy for reaching tech community (15-tag focused approach)
- Story engagement tactics for authentic connection
- Behind-the-scenes content showing real work and thinking
- Professional aesthetic maintaining authenticity

**Example Requests**:
- "Create an Instagram Reel strategy for sharing my AI ethics perspective"
- "Design a hashtag strategy for reaching tech professionals"
- "How do I use Instagram Stories to share authentic behind-the-scenes content?"

### 3. LinkedIn Specialist (`linkedin-specialist.agent.md`)
**Role**: Professional thought leadership and credibility building for tech leaders  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need LinkedIn content strategy, thought leadership development, or professional presence building

**Key Capabilities**:
- Thought leadership positioning for tech and social leaders
- Professional content strategy balancing expertise with authenticity
- LinkedIn article writing (long-form, 2,000+ words) on industry topics
- Professional networking and community building
- Personal profile optimization for credibility
- Authentic leadership voice development

**Example Requests**:
- "Write a LinkedIn thought leadership post on AI and society"
- "Design a strategy for building my professional presence on LinkedIn"
- "How do I write LinkedIn articles that establish credibility without being promotional?"

### 4. Social Media Coordinator (`social-media-coordinator.agent.md`)
**Role**: Cross-platform personal brand coordination and voice consistency  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need multi-platform personal brand strategy, content calendars, or voice consistency

**Key Capabilities**:
- Multi-platform personal brand coordination
- Content calendar creation balancing professional and personal insights
- Authentic voice consistency management (not corporate branding)
- Content repurposing strategies for different audiences
- Performance analysis focused on meaningful engagement
- Sustainable posting schedules (quality over quantity)
- Authentic voice guidance across platforms

**Example Requests**:
- "Coordinate my personal brand presence across Facebook, Instagram, and LinkedIn"
- "Create a weekly content calendar for my thought leadership"
- "How do I repurpose this LinkedIn article for Instagram while maintaining my authentic voice?"

### 5. Devil's Advocate (`devils-advocate.agent.md`) - MANDATORY QUALITY GATE
**Role**: Critical review and disagreement capture  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Before finalizing ANY strategy (mandatory critical review step)

**Key Capabilities**:
- Challenge platform-specific assumptions
- Surface disagreements between specialists
- Identify blind spots in strategies
- Question targeting and audience assumptions
- Review brand consistency concerns
- Capture trade-offs and alternative perspectives
- Final quality gate before strategy implementation

**Example Requests**:
- "Review this social media strategy for blind spots and risks"
- "Challenge the assumptions in this campaign plan"
- "Surface any disagreements between the platform strategies"

---

## How It Works: Four Primary Workflows

### Workflow 1: Platform-Specific Content Request

**Use when**: You need strategy for a single platform

```
User → [Platform Specialist] → User
```

**Optional Critical Review**: `@devils-advocate` can be manually consulted for complex strategies

**Example**: "Create an Instagram Reel strategy for sharing my tech leadership insights"

**Steps**:
1. User consults the appropriate Platform Specialist (Facebook, Instagram, or LinkedIn)
2. Specialist provides platform-optimized strategy with authentic voice guidance
3. Strategy returned to User
4. (Optional) User can consult `@devils-advocate` for critical review if needed

**When to request Devil's Advocate review**:
- Complex or high-stakes content strategy
- Strategy involves significant time/resource investment
- Need validation of assumptions before execution
- Want critical feedback on approach

**Example Interaction**:
```
User: @instagram-specialist "Create a Reel strategy for sharing my perspective on AI ethics as a tech leader"

Instagram Specialist: [Provides authentic strategy with personal voice, hashtags for tech community, engagement approach]

User receives: Platform-optimized strategy ready to execute

(Optional) User: @devils-advocate "Review this Instagram strategy for blind spots and risks"

Devil's Advocate: [Challenges assumptions about vulnerability vs. expertise balance, identifies risks]
```

---

### Workflow 2: Multi-Platform Campaign

**Use when**: You need coordinated strategy across multiple platforms

```
User → Social Media Coordinator → [Platform Specialists] → Devil's Advocate (AUTOMATIC) → Coordinator → User
```

**Example**: "Build my personal brand as a tech leader across all platforms"

**Devil's Advocate Review**: AUTOMATIC for all coordinated campaigns (comprehensive strategies require critical review)

**Steps**:
1. User consults Social Media Coordinator with personal brand goals
2. Coordinator designs overall personal brand strategy
3. Coordinator hands to each Platform Specialist for platform-specific approaches
4. Each Specialist provides platform-optimized recommendations maintaining authentic voice
5. Specialists hand back to Coordinator for synthesis
6. **Coordinator automatically hands complete strategy to Devil's Advocate for critical review**
7. Devil's Advocate reviews all plans for authenticity, consistency, and blind spots
8. Coordinator synthesizes approved recommendations
9. Final coordinated personal brand strategy to User

**Example Interaction**:
```
User: @social-media-coordinator "Build my personal brand as a tech and social leader across all platforms, focusing on authentic insights and thought leadership"

Coordinator: [Designs personal brand framework with voice guidelines, briefs specialists]

Coordinator → @facebook-specialist "Provide Facebook strategy for authentic community engagement"
Coordinator → @instagram-specialist "Provide Instagram strategy for behind-the-scenes tech leadership"
Coordinator → @linkedin-specialist "Provide LinkedIn strategy for professional thought leadership"

[Specialists provide platform-specific strategies]

Coordinator: [Synthesizes into unified personal brand presence with realistic content calendar]

Coordinator → @devils-advocate (AUTOMATIC) "Review this personal brand strategy for authenticity and sustainability"

Devil's Advocate: [Critical review, challenges assumptions about posting frequency and vulnerability balance, approves with concerns]

User receives: Complete personal brand strategy with platform-specific approaches, content calendar, and critical review insights
```

---

### Workflow 3: Cross-Platform Repurposing

**Use when**: You have content for one platform and want to adapt it for others

```
User → [Source Platform Specialist] → [Target Platform Specialist] → Devil's Advocate → User
```

**Example**: "Adapt my LinkedIn article for Instagram while maintaining my authentic voice"

**Steps**:
1. User consults Source Platform Specialist (where content originates)
2. Source Specialist extracts key personal insights and provides adaptation guidance
3. Source Specialist hands to Target Platform Specialist
4. Target Specialist adapts content for target platform's format while preserving authentic voice
5. Target Specialist hands to Devil's Advocate for critical review
6. Devil's Advocate reviews adaptation for voice authenticity and platform appropriateness
7. Approved adapted content to User

**Example Interaction**:
```
User: @linkedin-specialist "I have a 2,000-word LinkedIn article on remote work with my personal leadership insights. How do I adapt this for Instagram?"

LinkedIn Specialist: [Extracts key personal insights, identifies authentic moments]

LinkedIn Specialist → @instagram-specialist "Adapt this LinkedIn article for Instagram while maintaining authentic leadership voice"

Instagram Specialist: [Creates Instagram carousel strategy with 8 slides, authentic voice in captions, hashtags for tech community]

Instagram Specialist → @devils-advocate "Review this cross-platform adaptation for voice authenticity"

Devil's Advocate: [Ensures authentic voice maintained, checks if Instagram format suits personal insights, approves]

User receives: Instagram carousel strategy adapted from LinkedIn article with authentic voice preserved
```

---

### Workflow 4: Performance Review & Strategy Adjustment

**Use when**: You need to analyze performance and optimize ongoing strategy

```
User → Social Media Coordinator → [Relevant Platform Specialists] → Devil's Advocate → User
```

**Example**: "Review last month's social media performance and recommend improvements"

**Steps**:
1. User provides performance data to Social Media Coordinator
2. Coordinator analyzes cross-platform trends and patterns
3. Coordinator hands to relevant Platform Specialists for deep dives
4. Specialists provide platform-specific optimization recommendations
5. Specialists hand recommendations to Devil's Advocate for critical review
6. Devil's Advocate challenges assumptions in recommendations
7. Approved optimizations returned to User

**Example Interaction**:
```
User: @social-media-coordinator "Here's our October performance data. What should we optimize?"

Coordinator: [Analyzes cross-platform trends, identifies patterns]

Coordinator → @instagram-specialist "Instagram engagement dropped 15%. Investigate and recommend fixes."
Coordinator → @facebook-specialist "Facebook reach is strong but conversions low. Optimize."

[Specialists provide optimization recommendations]

Coordinator: [Synthesizes recommendations into action plan]

Coordinator → @devils-advocate "Review these optimization recommendations for blind spots"

Devil's Advocate: [Challenges assumptions, surfaces alternative perspectives, approves]

User receives: Optimization plan with platform-specific tactics and critical review insights
```

---

## Decision Tree: Which Agent Do I Need?

```
START: What do you need help with?
  │
  ├─ I need strategy for ONE platform
  │   │
  │   Which platform?
  │     │
  │     ├─ Facebook → Consult @facebook-specialist
  │     │   Examples: Community building, video strategy, EdgeRank optimization
  │     │
  │     ├─ Instagram → Consult @instagram-specialist
  │     │   Examples: Reels trends, hashtag strategy, visual content
  │     │
  │     └─ LinkedIn → Consult @linkedin-specialist
  │         Examples: Thought leadership, B2B tactics, LinkedIn articles
  │
  ├─ I need strategy for MULTIPLE platforms
  │   │
  │   → Consult @social-media-coordinator
  │   Examples: Product launch, brand campaign, content calendar, repurposing
  │
  ├─ I need to ADAPT content from one platform to another
  │   │
  │   → Start with @[source-platform]-specialist → hands to @[target-platform]-specialist
  │   Examples: LinkedIn article → Instagram carousel, Instagram Reel → Facebook video
  │
  ├─ I need to REVIEW performance and optimize
  │   │
  │   → Consult @social-media-coordinator (coordinates specialist deep dives)
  │   Examples: Monthly review, underperforming content analysis, strategy adjustment
  │
  └─ I need to CHALLENGE or REVIEW a strategy
      │
      → Consult @devils-advocate (critical review before finalizing)
      Examples: "What are the risks?", "What am I missing?", "Challenge my assumptions"
```

---

## Quality Gates

Every social media strategy passes through these quality checkpoints:

### Gate 1: Platform Optimization (Platform Specialists)
**Owner**: Facebook Specialist, Instagram Specialist, or LinkedIn Specialist  
**Checks**:
- [ ] Content optimized for platform algorithm
- [ ] Format selection appropriate (post, reel, story, article)
- [ ] Timing and frequency recommendations included
- [ ] Examples and copy provided
- [ ] Technical specifications accurate
- [ ] Best practices followed

**Pass Criteria**: Strategy is platform-native and actionable

---

### Gate 2: Brand Consistency (Coordinator - Multi-Platform Only)
**Owner**: Social Media Coordinator  
**Checks**:
- [ ] Brand voice consistent across platforms
- [ ] Visual identity maintained
- [ ] Messaging aligned with brand values
- [ ] Platform adaptations preserve core message
- [ ] Content calendar coordinated
- [ ] Workflow and approvals defined

**Pass Criteria**: Strategy maintains brand identity while respecting platform differences

---

### Gate 3: Critical Review (Devil's Advocate)
**Owner**: Devil's Advocate  
**When**: 
- **AUTOMATIC**: Multi-platform campaigns coordinated by Social Media Coordinator
- **OPTIONAL**: Single-platform strategies (user can request `@devils-advocate` if needed)

**Checks**:
- [ ] Assumptions challenged
- [ ] Blind spots identified
- [ ] Risks assessed and mitigation planned
- [ ] Disagreements between specialists surfaced
- [ ] Trade-offs documented
- [ ] Alternative perspectives considered

**Pass Criteria**: Strategy stress-tested and ready for human decision-making

**RECOMMENDED**: While only automatic for coordinated campaigns, Devil's Advocate review is valuable for any high-stakes or complex strategy. Users can manually consult `@devils-advocate` for single-platform strategies when critical review would be beneficial.

---

## Handoff Policy (send_default)

**Policy**: `send_default: true`

All agents in this group use automatic handoffs (`send: true`) for smooth workflow coordination. This policy enables specialists to collaborate efficiently, delivering complete strategy packages with critical review to users.

**Rationale**:

This agent group generates content recommendations and strategies - it does not execute external actions (no social media API access, no automated posting). The agents produce text-based recommendations that users manually review and post to their social platforms.

**Risk Assessment**:
- **Decision Criticality**: MEDIUM (recommendations, not executable actions)
- **External Actions**: LOW (no posting capability - users execute manually)
- **Data Sensitivity**: LOW (generates generic social media strategy advice)
- **Observability**: HIGH (users review all content before posting)
- **Rollback Capability**: HIGH (nothing executed until user manually posts)

**Human Checkpoint**: Users are the final gatekeeper. All content recommendations must be manually copied to social platforms by the user. Automatic handoffs enable efficient strategy generation, while actual posting requires explicit human action.

**Workflow Benefits**:
- Platform specialists automatically coordinate for multi-platform consistency
- Devil's Advocate critical review is delivered with strategy (complete package)
- Users receive comprehensive recommendations without manual handoff coordination
- No interruption to workflow for internal agent collaboration

---

## Examples

### Example 1: Instagram Product Launch (Platform-Specific)

**User Request**:
```
@instagram-specialist "Create an Instagram strategy for our new sustainable skincare serum launch. Target audience: Women 25-40, skincare enthusiasts. Goal: 100K reach, 800 link clicks."
```

**Instagram Specialist Response**:
```markdown
# Instagram Content Strategy: Sustainable Skincare Serum Launch

[Complete strategy including]:
- Launch Reel (30 sec, trending audio, before/after)
- Carousel posts (product benefits, how-to-use)
- Story series (BTS, polls, countdown)
- Hashtag strategy (30-tag mix: #skincare, #vitaminc, #cleanbeauty...)
- Example captions with character counts
- Posting schedule (Wed 7 PM EST optimal)
- Expected performance (100K-120K reach, 6-8% engagement rate)
```

**Instagram Specialist → Devil's Advocate**:
```
@devils-advocate "Review this Instagram launch strategy for blind spots and risks."
```

**Devil's Advocate Response**:
```markdown
# Devil's Advocate Review: Skincare Serum Launch

**Status**: APPROVED WITH CONCERNS

**Critical Issue**: Sustainability claims lack specificity—replace "clean beauty" with certifications (organic, cruelty-free, vegan with proof).

**Moderate Concern**: Trending audio may be stale by launch date (7 days away)—recommend identifying trend 48 hours before posting.

**Blind Spot**: No accessibility considerations (alt text, video captions).

**Approval**: Proceed after addressing sustainability claims specificity.
```

**User receives**: Complete Instagram strategy + critical review identifying risks to address.

---

### Example 2: Multi-Platform Product Launch (Coordinated Campaign)

**User Request**:
```
@social-media-coordinator "Launch our fitness apparel line across Facebook, Instagram, LinkedIn. 2-week campaign, $5K budget. Target: 500K reach, 300 sales."
```

**Coordinator Response**:
```markdown
# Cross-Platform Campaign: Fitness Apparel Launch

## Platform Roles
- Instagram: PRIMARY (60% effort) - Visual storytelling, Reels, influencers
- Facebook: SECONDARY (30% effort) - Community, video, customer stories
- LinkedIn: TERTIARY (10% effort) - Sustainability thought leadership, B2B

## 2-Week Content Calendar
[Week-by-week posting schedule across all platforms with timing, formats, CTAs]

## Platform Strategies
[Coordinator hands to specialists for platform-specific plans]
```

**Coordinator → Platform Specialists**:
```
@facebook-specialist "Provide Facebook strategy for this fitness apparel launch."
@instagram-specialist "Provide Instagram strategy for this fitness apparel launch."
@linkedin-specialist "Provide LinkedIn strategy for this fitness apparel launch."
```

**[Specialists provide platform-specific strategies]**

**Coordinator Synthesizes → Devil's Advocate**:
```
@devils-advocate "Review this coordinated campaign for consistency, risks, and blind spots."
```

**Devil's Advocate Response**:
```markdown
# Devil's Advocate Review: Fitness Apparel Launch

**Status**: APPROVED WITH CONCERNS

**Critical Issue**: LinkedIn strategy lacks B2B lead gen tactics—add corporate wellness angle.

**Moderate Concerns**: 
- 500K reach target aggressive for 2-week timeline
- UGC repost timeline unrealistic (customers won't have products Day 2)

**Blind Spot**: No post-campaign maintenance plan—momentum will fade without sustained effort.

**Disagreement**: Instagram Specialist recommends Saturday launch, LinkedIn Specialist prefers Tuesday—suggest staggering (Instagram Sat, LinkedIn Tues) for optimal audience reach.

**Approval**: Proceed after LinkedIn specialist adds B2B tactics.
```

**User receives**: Complete multi-platform campaign + critical review with documented concerns for decision-making.

---

### Example 3: Content Repurposing (Cross-Platform Adaptation)

**User Request**:
```
@linkedin-specialist "I have a 2,000-word LinkedIn article on remote work best practices. How do I repurpose this for Instagram and Facebook?"
```

**LinkedIn Specialist Response**:
```markdown
# Content Repurposing: Remote Work Article

## Core Message
"Remote work success requires intentional culture-building, not organic hope."

## Key Insights (Repurposing-Ready)
1. Communication over technical skills in hiring
2. Async-first culture design
3. Onboarding makes or breaks retention

## Adaptation Recommendations
→ Instagram: 8-slide carousel (key insights visualized)
→ Facebook: 60-second video summary (talking head + B-roll)
```

**LinkedIn Specialist → Instagram Specialist**:
```
@instagram-specialist "Adapt this LinkedIn article into an Instagram carousel strategy."
```

**Instagram Specialist Response**:
```markdown
# Instagram Carousel: Remote Work Best Practices

## 8-Slide Structure
- Slide 1: Hook "3 remote work mistakes that cost us $500K"
- Slides 2-7: 1 insight per slide (visual design, minimal text)
- Slide 8: CTA "Save this for your team" + follow

## Visual Style
Clean, professional graphics (navy/white), icons for concepts

## Caption Example
[Full caption with hashtags: #RemoteWork #Leadership #TeamManagement...]

## Expected Performance
Target 1,000+ saves (educational carousels drive highest saves)
```

**Instagram Specialist → Devil's Advocate**:
```
@devils-advocate "Review this LinkedIn-to-Instagram adaptation."
```

**Devil's Advocate Response**:
```markdown
**Status**: APPROVED

**Strengths**: Carousel format suits educational content, save-worthy approach correct.

**Minor Concern**: LinkedIn audience (B2B professionals) differs from Instagram audience (broader, younger)—ensure examples resonate with Instagram demographics.

**Approval**: Proceed as planned.
```

**User receives**: Instagram carousel strategy adapted from LinkedIn article + critical review confirming approach.

---

## Best Practices

### For Platform Specialists
1. **Be Platform-Specific**: Recommendations should be tailored to platform algorithm, audience, and best practices (not generic advice)
2. **Provide Examples**: Always include concrete examples (full captions, hashtags, copy) with character counts
3. **Cite Best Practices**: Reference current algorithm behavior, industry benchmarks, and evidence-based tactics
4. **Quantify Expectations**: Provide realistic performance targets (reach, engagement rate, conversions)
5. **Hand to Devil's Advocate**: Always submit strategies to devils-advocate for critical review before finalizing

### For Social Media Coordinator
1. **Define Platform Roles**: Clearly designate primary/secondary/tertiary platforms based on objectives and audience
2. **Maintain Brand Consistency**: Ensure core message consistent while adapting tone and format per platform
3. **Coordinate Timing**: Sequence content for maximum impact (Instagram first, Facebook 2-4 hours later, LinkedIn next day)
4. **Document Workflow**: Define approval process, handoffs, and responsibilities upfront
5. **Hand to Devil's Advocate**: Submit coordinated strategy for critical review before execution

### For Devil's Advocate
1. **Challenge Constructively**: Question assumptions to improve strategy, not to criticize people
2. **Surface Disagreements**: Document when specialists have conflicting recommendations with merit of each view
3. **Identify Blind Spots**: Focus on what's NOT addressed that could matter (unintended audiences, edge cases)
4. **Document Trade-Offs**: Explain what's gained vs. what's risked with each strategic choice
5. **Provide Clear Decision**: Approve/concerns/revision with specific rationale and next steps

### For Users
1. **Provide Context**: Share brand guidelines, target audience, objectives, and constraints upfront
2. **Start with Right Agent**: Use decision tree to identify appropriate agent (platform specialist vs. coordinator)
3. **Request Critical Review**: Always ask devils-advocate to review before finalizing strategy
4. **Make Informed Decisions**: Use Devil's Advocate insights to make conscious choices about documented concerns
5. **Follow Workflows**: Use established workflows (single platform vs. multi-platform vs. repurposing) for best results

---

## Integration with Your Workflow

### Drop-In Installation
This agent group is portable and can be added to any repository:

1. **Copy Folder**: Copy `social-media-team/` folder to your repository location (e.g., `.github/`)
2. **Reference Agents**: Consult agents using `@agent-name` in your AI chat interface
3. **Follow Workflows**: Use the four primary workflows documented above

### No Dependencies
- No hardcoded paths or repository-specific references
- Folder can be renamed without breaking agent functionality
- Agents reference each other by name (not path)

### Customization
- Update brand guidelines in your prompts to agents
- Adjust platform priorities based on your audience (Instagram-first vs. LinkedIn-first)
- Extend workflows for your specific use cases (e.g., add TikTok specialist if needed)

---

## Troubleshooting

### "Which agent should I consult first?"
**Use the Decision Tree above.**  
- Single platform need → Platform Specialist
- Multi-platform campaign → Social Media Coordinator
- Content adaptation → Source Platform Specialist → Target Platform Specialist
- Strategy review → Devil's Advocate

### "Specialists are giving conflicting advice"
**This is expected and valuable.**  
- Consult @devils-advocate to surface the disagreement
- Devil's Advocate will document each perspective's merit
- Use insights to make informed decision about which approach fits your goals

### "Strategy feels too complex or detailed"
**Adjust specificity in your request.**  
- For high-level strategy: "Give me a 1-week Facebook strategy overview"
- For detailed tactics: "Provide complete Facebook strategy with example posts, timing, and metrics"
- Agents adapt to the detail level you request

### "Devil's Advocate flagged concerns—should I revise?"
**Depends on severity:**  
- **Critical Issues**: Must address before proceeding (risks are too high)
- **Moderate Concerns**: Document for stakeholder decision-making (conscious choice vs. oversight)
- **Minor Issues**: Optional improvements (nice-to-have optimizations)

Review Devil's Advocate categorization and make informed decision.

### "I need help with a platform not covered (Twitter, TikTok, Pinterest)"
**Current agents cover Facebook, Instagram, LinkedIn.**  
- For other platforms, consult the most similar specialist:
  - Twitter → LinkedIn Specialist (text-based, thought leadership)
  - TikTok → Instagram Specialist (short-form video, trends)
  - Pinterest → Instagram Specialist (visual, discovery-focused)
- Note: Recommendations will need adaptation for platform-specific nuances
