# GitHub Copilot Instructions - Corporate Team Building Planning System

## Overview

This is a comprehensive corporate team building planning system with five specialized agents that help event planners discover, evaluate, and execute team building activities and dining experiences that genuinely strengthen team bonds. The system supports different group sizes, event types, and team dynamics while maintaining focus on the primary goal of building team relationships.

## Core Principle

**Team bonding requires intentional design.** Effective team building isn't just about fun activities—it's about creating shared experiences that build trust, improve communication, and strengthen relationships. This system ensures every recommendation considers group dynamics, team goals, accessibility, and the balance between structured activities and organic connection time. Devil's Advocate prevents "forced fun" failures.

## The Five Agents

### Team Profiler (`agents/team-profiler.agent.md`)
**Role**: Gather team context and create comprehensive profiles  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: activity-scout

**When to use**: 
- Starting team building event planning
- Need to understand team composition and goals
- Want structured guidance on requirements gathering

**What it does**:
- Conducts structured discovery about team size, composition, and dynamics
- Understands team challenges (communication gaps, trust issues, new team formation)
- Gathers constraints (budget, location, dates, dietary restrictions, accessibility)
- Identifies preferences and past experiences
- Creates comprehensive team profile for targeted recommendations

### Activity Scout (`agents/activity-scout.agent.md`)
**Role**: Recommend team building activities matched to profile  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: dining-specialist

**When to use**:
- Have complete team profile from Profiler
- Ready for activity recommendations
- Need options that genuinely build bonds, not just entertain

**What it does**:
- Recommends 3-5 activities tailored to team goals and constraints
- Evaluates bonding potential vs entertainment value
- Balances structured and informal, active and relaxed options
- Considers group size, physical abilities, and personality mix
- Provides practical logistics (duration, cost, venue, facilitators)
- Includes innovative options beyond typical escape rooms

### Dining Specialist (`agents/dining-specialist.agent.md`)
**Role**: Recommend dining that supports bonding  
**Model**: Claude Haiku 4.5 (copilot)  
**Handoffs to**: event-coordinator

**When to use**:
- Have activity recommendations
- Need dining venues that continue relationship-building
- Must accommodate dietary restrictions and group size

**What it does**:
- Suggests 3-5 dining venues/experiences matched to team
- Ensures accommodation of all dietary restrictions
- Evaluates conversation-friendly layouts and atmosphere
- Recommends dining styles that encourage interaction (family-style, tasting menus)
- Provides practical details (reservations, parking, accessibility, pricing)
- Considers timing and location relative to activities

### Event Coordinator (`agents/event-coordinator.agent.md`)
**Role**: Create integrated event plans with logistics  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: devils-advocate

**When to use**:
- Have activity and dining recommendations
- Ready to create complete executable plans
- Need realistic timelines and logistics

**What it does**:
- Synthesizes activities and dining into 2-3 cohesive event scenarios
- Creates realistic timelines with proper pacing and buffer time
- Plans all logistics (transportation, materials, facilitators, venues)
- Develops contingency plans for weather, venue issues, timing problems
- Provides booking checklists with lead times
- Calculates total costs for each scenario

### Devil's Advocate (`agents/devils-advocate.agent.md`) **[MANDATORY QUALITY GATE]**
**Role**: Critical review before booking commitments  
**Model**: Claude Sonnet 4.5 (copilot)  
**Handoffs to**: None (final gate)

**When to use**:
- After Event Coordinator creates plans
- Before making any booking commitments
- Need critical assessment of potential issues

**What it does**:
- Challenges assumptions about what creates bonding
- Identifies accessibility barriers and personality mismatches
- Surfaces "forced fun" risks
- Questions budget realism and logistics feasibility
- Highlights overlooked considerations
- Provides confidence assessment and final recommendation

## Workflow

### Primary Flow (Linear with Mandatory Critical Review)

```
1. Team Profiler (gather comprehensive team profile)
   ↓ Profile with goals, constraints, preferences
   
2. Activity Scout (recommend 3-5 bonding activities)
   ↓ Activity options with rationale
   
3. Dining Specialist (recommend 3-5 dining options)
   ↓ Dining venues with accommodations
   
4. Event Coordinator (create 2-3 integrated event plans)
   ↓ Complete scenarios with timelines, costs, logistics
   
5. Devil's Advocate (MANDATORY critical review)
   ↓ Assessment of risks, concerns, recommendations
   
6. Planner makes booking decisions with full information
```

### Quick Reference Decision Tree

| Your Situation | Agent to Consult | What They'll Do |
|---|---|---|
| **Starting planning** | @team-profiler | Structured discovery, create team profile |
| **Have team profile** | @activity-scout | Recommend activities matched to goals |
| **Have activities** | @dining-specialist | Suggest dining that continues bonding |
| **Have activities + dining** | @event-coordinator | Create integrated executable plans |
| **Ready to book** | @devils-advocate | Critical review, identify issues |

## Key Features

- ✅ **Goal-Oriented**: Every recommendation ties to stated team bonding objectives
- ✅ **Inclusive Design**: Considers diverse abilities, preferences, personalities
- ✅ **Practical Focus**: Real logistics, real budgets, real constraints
- ✅ **Scalable**: Works for 5-person teams or 50+ groups
- ✅ **Critical Review**: Devil's Advocate prevents forced fun failures
- ✅ **Comprehensive**: Handles activities, dining, logistics, contingencies
- ✅ **Dietary Accommodations**: Ensures no one excluded by food choices

## Quick Start

### Installation

1. **Copy to Your Project**
   ```bash
   # From your project root
   cp -r /path/to/corporate-team-building .github/corporate-team-building
   ```

2. **Start Using**
   
   In GitHub Copilot Chat, reference agents with `@`:
   ```
   @team-profiler I need to plan team building for my engineering team
   ```

### Basic Usage

#### Scenario 1: Small Engineering Team Integration

```
Step 1: Start with Team Profiler
You: "@team-profiler I need to plan team building for my 15-person engineering team. 
      Half are new hires who joined in the last 6 months."

Profiler will:
- Ask about team composition and dynamics
- Understand integration goals
- Gather budget, timing, location constraints
- Identify preferences and past experiences
- Create comprehensive profile

Step 2: Get Activity Recommendations
(Automatic handoff to @activity-scout)

Scout will:
- Recommend 3-5 activities matched to integration goal
- Explain bonding potential for each
- Balance active/relaxed, structured/informal
- Provide logistics and cost estimates

Step 3: Find Dining Options
(Automatic handoff to @dining-specialist)

Specialist will:
- Suggest 3-5 dining venues
- Ensure dietary accommodations
- Evaluate conversation-friendliness
- Recommend family-style or interactive dining

Step 4: Create Integrated Plans
(Automatic handoff to @event-coordinator)

Coordinator will:
- Build 2-3 complete event scenarios
- Timeline with proper pacing
- All logistics and contingencies
- Cost breakdowns and booking checklists

Step 5: Critical Review
(Automatic handoff to @devils-advocate)

Advocate will:
- Challenge assumptions
- Identify potential issues
- Assess "forced fun" risks
- Provide final confidence rating

Step 6: Make Booking Decisions
- Review Devil's Advocate feedback
- Select preferred scenario
- Begin booking process with confidence
```

#### Scenario 2: Leadership Team with Tension

```
You: "@team-profiler I need a team building event for our 8-person executive team. 
      We've had some tension between Product and Engineering."

System guides you through:
1. Profiler: Deep dive on team dynamics, tension sources, trust levels
2. Scout: Activities emphasizing collaboration over competition, trust-building
3. Specialist: Intimate dining conducive to conversations
4. Coordinator: Full-day or multi-day retreat options with facilitation
5. Advocate: Critical review of whether team is ready, facilitation needs

Result: Sophisticated event plan that addresses root issues
```

#### Scenario 3: Large Sales Team Celebration

```
You: "@team-profiler We need to celebrate our 45-person sales team hitting annual target."

System guides you through:
1. Profiler: Celebratory goals, high-energy preferences, large group logistics
2. Scout: Activities that scale to 45 people, competitive but fun
3. Specialist: Premium dining that accommodates large groups
4. Coordinator: Logistics for large group (transportation, venue capacity)
5. Advocate: Reality check on budget, logistics, and timeline

Result: Memorable celebration that makes team feel valued
```

## What Makes Effective Team Building

### Essential Elements

1. **Clear Team Goals**
   - Trust building through vulnerable activities
   - Communication improvement via collaborative challenges
   - Cross-functional bonding to break silos
   - New team formation to create initial connections
   - Celebration to recognize achievements

2. **Intentional Mixing**
   - Small groups that mix tenure, roles, personalities
   - Rotation to maximize relationship formation
   - Activities requiring interdependence
   - Multiple interaction opportunities

3. **Inclusive Design**
   - Physical activities with alternatives
   - Dietary restrictions fully accommodated
   - Introvert-friendly pacing and breaks
   - No financial barriers to participation
   - Cultural and religious sensitivity

4. **Practical Logistics**
   - Realistic timelines with buffer time
   - Clear transportation between venues
   - Weather contingencies for outdoor activities
   - Advance communication to participants
   - Booking checklists and confirmations

5. **Bonding Mechanisms**
   - Shared challenges creating interdependence
   - Conversation time for organic connection
   - Shared meals with family-style service
   - Reflection or debrief on experiences
   - Inside jokes and memorable moments

### Example Comparison

**❌ Weak Approach**:
> "Let's do an escape room and then get dinner somewhere."
> - No understanding of team dynamics
> - Generic activity selection
> - No thought to dietary restrictions
> - No logistics planning
> - No contingencies

**✅ Strong Approach**:
> "For your 15-person engineering team with integration goals, I recommend a collaborative cooking class (naturally mixes new/established members in small teams, requires communication, equalizing activity) followed by French bistro dinner (private room for conversation, dietary accommodations confirmed, different seating than cooking to maximize connections). Timeline: 3pm-8pm Friday with transportation buffers. Budget: $73/person. Contingency: If venue issues, backup is Topgolf + Loro with similar dynamics and cost. Devil's Advocate notes: Add facilitation structure to ensure quieter engineers contribute."

## Workflow Rules

1. **Start with Team Profiler**: Always begin with comprehensive discovery
2. **Trust the Handoffs**: Each agent automatically passes to the next
3. **Devil's Advocate is Mandatory**: Never skip critical review before booking
4. **Iterate if Needed**: Can request adjustments at any stage
5. **Be Honest About Constraints**: Better to plan realistically than aspirationally

## Tips for Different Team Types

### Small Teams (5-12 people)
- **Advantages**: Can do almost anything, everyone participates equally, intimate conversations
- **Considerations**: Absence of even one person is noticeable, need activities that scale down
- **Recommendations**: Focus on depth over scale, choose venues that accommodate small groups

### Medium Teams (13-30 people)
- **Advantages**: Good energy, can split into smaller groups, most activities work
- **Considerations**: May need breakout groups, stronger facilitation, venue capacity
- **Recommendations**: Mix whole-group and small-group activities, plan for moderate logistics

### Large Teams (31-50+ people)
- **Advantages**: High energy, can support premium experiences, create buzz
- **Considerations**: Requires professional facilitation, limited venue options, complex logistics
- **Recommendations**: Focus on scalable activities, consider professional event companies, plan far ahead

### Teams with Conflict or Low Morale
- **Approach**: Build trust before vulnerability, neutral activities before deep work
- **Activities**: Collaborative problem-solving, service projects, creative workshops
- **Avoid**: High competition, forced sharing, activities requiring existing trust

### New Teams or First-Time Meetings
- **Approach**: Focus on icebreakers, learning about each other, low-stakes fun
- **Activities**: Scavenger hunts, cooking classes, team games, discovery experiences
- **Avoid**: Activities requiring established relationships or inside knowledge

### Remote Teams Meeting In Person
- **Approach**: Balance structured activities with unstructured social time
- **Activities**: Mix of collaborative work and pure fun, touring shared location
- **Avoid**: All work/no play, or all play/no bonding opportunity

## Common Pitfalls & How to Avoid

### Pitfall 1: "Forced Fun" Syndrome
**Problem**: Mandatory "fun" feels like obligation  
**Solution**: Devil's Advocate identifies mismatches, recommends opt-in elements, ensures activities genuinely match team personality

### Pitfall 2: Accessibility Oversights
**Problem**: Activities exclude people with disabilities, dietary restrictions, or different abilities  
**Solution**: Dining Specialist ensures full accommodation, Activity Scout provides alternatives, Team Profiler captures all needs upfront

### Pitfall 3: Over-Scheduling
**Problem**: Cramming too much into timeline creates stress  
**Solution**: Event Coordinator builds in 20% buffer time, realistic transitions, allows organic conversation

### Pitfall 4: Goal Disconnect
**Problem**: Fun activities that don't serve team bonding goals  
**Solution**: Activity Scout explicitly evaluates bonding potential, every recommendation ties to stated goals

### Pitfall 5: Budget Blindspots
**Problem**: Hidden costs or expenses beyond some participants' means  
**Solution**: Event Coordinator provides complete cost breakdown, Devil's Advocate questions budget realism

### Pitfall 6: Introvert Exhaustion
**Problem**: Continuous socializing without breaks  
**Solution**: Event Coordinator plans natural breaks, Activity Scout balances active/passive, Team Profiler identifies energy preferences

## Troubleshooting

### "I don't have a clear goal"
**Solution**: Team Profiler will help you identify what your team needs—trust, communication, celebration, integration, etc.

### "My budget is tight"
**Solution**: Activity Scout and Dining Specialist provide options across price ranges. Event Coordinator helps optimize spending.

### "My team has diverse abilities/preferences"
**Solution**: This is exactly what the system is designed for. Team Profiler captures all considerations, agents recommend inclusive options.

### "I'm worried about logistics"
**Solution**: Event Coordinator creates minute-by-minute timelines, booking checklists, and contingency plans. Takes the stress out of planning.

### "The recommendations don't feel quite right"
**Solution**: You can request adjustments at any stage. Agents iterate based on your feedback.

### "I want to skip the Devil's Advocate review"
**Solution**: Don't. This is your safety net. Better to surface concerns now than have issues during the event.

## Frequently Asked Questions

**Q: How long does the planning process take?**  
A: Typically 30-60 minutes for complete workflow from initial profiling through final review. Can iterate faster if you have clear requirements upfront.

**Q: Can I start in the middle (skip Team Profiler)?**  
A: Yes, if you have comprehensive requirements. But starting with Team Profiler typically produces better-matched recommendations.

**Q: What if my team is really large (100+ people)?**  
A: The system works up to 50 people. For 100+, consider splitting into multiple simultaneous events or consulting professional event companies.

**Q: Do I need to use all recommendations?**  
A: No. Agents provide 3-5 options for activities and dining. You choose what fits best. Event Coordinator creates multiple scenarios—pick your favorite.

**Q: What if weather ruins outdoor plans?**  
A: Event Coordinator builds contingency plans into every scenario. Devil's Advocate assesses weather risk and backup plan feasibility.

**Q: Can this work for virtual or hybrid teams?**  
A: This system is optimized for in-person events. For virtual team building, different approaches are needed.

**Q: How far in advance should I start planning?**  
A: Ideally 4-6 weeks for best venue availability. Can work with shorter timelines but options may be limited.

**Q: What if Devil's Advocate says not to proceed?**  
A: Take it seriously. If concerns are significant, address them before booking. Better to adjust plans or reschedule than have event fail.

## Version History

- **1.0.0** - Initial corporate team building planning system with five specialized agents

## Support and Feedback

This agent system helps planners create team building events that genuinely strengthen relationships. If you encounter issues or have suggestions:
- Provide feedback through your organization's agent management process
- Note specific scenarios where agents could improve
- Share examples of particularly successful events created with the system

---

## Getting Started Checklist

Before planning your first team building event:

- [ ] Understand your team's primary goal (trust, communication, integration, celebration, etc.)
- [ ] Have approximate team size and composition
- [ ] Know budget range (even if flexible)
- [ ] Have general timeframe (dates or season)
- [ ] Start with `@team-profiler` in GitHub Copilot Chat
- [ ] Trust the workflow—let agents hand off automatically
- [ ] Review Devil's Advocate feedback before booking
- [ ] Use booking checklists to ensure nothing overlooked

**Ready to start? Use: `@team-profiler [describe your team and needs]`**
