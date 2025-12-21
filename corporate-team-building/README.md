# Corporate Team Building Planning Agent Group

**Version**: 1.0.0

A comprehensive agent group for planning corporate team building events that genuinely strengthen team relationships. Handles activity discovery, dining recommendations, logistics coordination, and critical review to prevent "forced fun" failures.

## Overview

The Corporate Team Building Planning group coordinates five specialized agents to handle every aspect of team building event planning—from understanding team dynamics to creating executable plans with full logistics. The system works for teams of 5-50+ people across different goals (integration, trust-building, celebration) and constraints.

## The Five Agents

### 1. team-profiler
**Role**: Gather team context and create comprehensive profiles  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Starting event planning, need structured requirements gathering

Conducts discovery about team composition, dynamics, goals, constraints, and preferences. Creates comprehensive profile that enables personalized, goal-aligned recommendations.

### 2. activity-scout
**Role**: Recommend team building activities matched to goals  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Have team profile, ready for activity recommendations

Recommends 3-5 activities tailored to team profile with explicit bonding potential analysis. Balances structured/informal, active/relaxed, competitive/collaborative. Provides practical logistics.

### 3. dining-specialist
**Role**: Recommend dining that supports bonding  
**Model**: Claude Haiku 4.5 (copilot)  
**When to use**: Have activities, need dining options

Suggests 3-5 dining venues accommodating dietary restrictions and group size. Evaluates conversation-friendliness, recommends interactive dining styles, provides practical booking details.

### 4. event-coordinator
**Role**: Create integrated event plans with logistics  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Have activities and dining, ready for complete plans

Synthesizes recommendations into 2-3 executable event scenarios with realistic timelines, complete logistics, cost breakdowns, booking checklists, and contingency plans.

### 5. devils-advocate (MANDATORY)
**Role**: Critical review before booking commitments  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Before making any bookings—final quality gate

Challenges assumptions, identifies accessibility barriers, surfaces "forced fun" risks, questions logistics feasibility, provides confidence assessment. Prevents expensive failures.

## Quick Start

### Basic Workflow

```
1. @team-profiler - Create comprehensive team profile
   ↓
2. [Automatic handoff] - Activity recommendations
   ↓
3. [Automatic handoff] - Dining recommendations
   ↓
4. [Automatic handoff] - Integrated event plans
   ↓
5. @devils-advocate - MANDATORY critical review
   ↓
6. Make booking decisions with confidence!
```

### Example: Engineering Team Integration

**Step 1**: Consult @team-profiler
```
"I need to plan team building for my 15-person engineering team. 
Half are new hires who joined in the last 6 months. We want to help 
them integrate with the established team members."
```

**Step 2**: System automatically proceeds through:
- Activity Scout: Recommends collaborative cooking, scavenger hunt, Topgolf, etc.
- Dining Specialist: Suggests family-style restaurants accommodating dietary needs
- Event Coordinator: Creates 2-3 complete scenarios with timelines and costs
- Devil's Advocate: Reviews for integration effectiveness, introvert consideration, logistics

**Result**: Complete event plan addressing new hire integration with activities that mix tenure groups, realistic timing, all logistics handled, and critical review completed.

### Example: Leadership Team Trust-Building

**Step 1**: Consult @team-profiler
```
"I need team building for our 8-person executive leadership team. 
We've had tension between Product and Engineering and need to rebuild 
trust and alignment."
```

**Step 2**: System proceeds with focus on:
- Profiler: Deep dive on tension sources, trust levels, readiness
- Scout: Collaborative activities emphasizing interdependence, not competition
- Specialist: Intimate dining conducive to difficult conversations
- Coordinator: Full-day retreat with facilitation, debrief time
- Advocate: Assesses whether team ready for vulnerable activities, need for professional facilitation

**Result**: Sophisticated retreat plan with activities that address root issues, not just symptoms.

### Example: Large Sales Celebration

**Step 1**: Consult @team-profiler
```
"We need to celebrate our 45-person sales team hitting their annual target. 
Want something fun and memorable that makes them feel valued."
```

**Step 2**: System handles scale challenges:
- Profiler: Celebratory goals, high-energy preferences, large group logistics
- Scout: Activities that scale to 45+ people, competitive but fun
- Specialist: Premium dining accommodating large groups
- Coordinator: Transportation, venue capacity, staggered timing
- Advocate: Reality check on logistics and budget for this scale

**Result**: Memorable celebration with premium feel, manageable logistics for large group.

## Key Features

- ✅ **Goal-Driven**: Every recommendation explicitly ties to stated team bonding objectives
- ✅ **Scalable**: Works for 5-person teams to 50+ groups
- ✅ **Inclusive**: Considers dietary restrictions, physical abilities, personality diversity
- ✅ **Practical**: Real budgets, realistic timelines, actual venue suggestions
- ✅ **Comprehensive**: Activities, dining, logistics, contingencies—everything covered
- ✅ **Safe**: Devil's Advocate prevents forced fun failures and accessibility oversights
- ✅ **Efficient**: 30-60 minute planning process for complete event

## What Makes This Different

### Bonding-Focused, Not Just Fun
Generic team building: "Let's do an escape room!"  
This system: "For trust-building with your newly merged teams, I recommend collaborative cooking (requires vulnerability and interdependence) over escape rooms (can increase tension through competition)."

### Truly Inclusive
Generic: "We'll do a ropes course!"  
This system: "Team profile shows one person uses wheelchair and two have acrophobia. Recommending collaborative cooking or design thinking workshop instead. Both create equivalent bonding without physical barriers."

### Critical Review Built In
Generic: Plans without reality check  
This system: Devil's Advocate identifies "Wait, your Friday 6pm reservation requires 30 minutes cross-town drive during rush hour with street parking at destination. This will create stress and late arrivals."

### Complete, Not Piecemeal
Generic: Activity recommendation, figure out the rest yourself  
This system: Complete scenarios with activities, dining, timeline, transportation, contingencies, costs, and booking checklists.

## Use Cases

### Team Integration
- **Challenge**: New hires feel disconnected from established team
- **Approach**: Activities requiring mixed-tenure small groups, rotation for maximum connections
- **Example**: Collaborative cooking with deliberately mixed teams, followed by dinner with different seating

### Trust Building
- **Challenge**: Recent conflict or low trust within team
- **Approach**: Vulnerable activities with proper facilitation, reflection time, professional guidance
- **Example**: Sailboat racing (requires interdependence), followed by facilitated debrief and intimate dinner

### Cross-Functional Collaboration
- **Challenge**: Silos between departments (Product/Engineering, Sales/Marketing)
- **Approach**: Activities requiring diverse skill sets, neutral territory, shared goals
- **Example**: Design thinking workshop on real business challenge, collaborative problem-solving

### Celebration & Appreciation
- **Challenge**: Recognize achievement, boost morale, create positive memories
- **Approach**: Premium experiences, fun without forced growth, photo opportunities
- **Example**: Private museum event, game show experience, upscale dinner

### Remote Team First Meeting
- **Challenge**: Team works remotely but meeting in person for first time
- **Approach**: Balance structured activities with unstructured social time, city discovery
- **Example**: City scavenger hunt (learn location together), casual dinner with conversation prompts

## Agent Capabilities

### Team Profiler Gathers
- Team size, composition, seniority mix, tenure
- Primary goals (trust, communication, integration, celebration)
- Constraints (budget, dates, location, duration)
- Dietary restrictions and accessibility needs
- Past experiences (what worked, what didn't)
- Team personality (energy level, activity preferences)

### Activity Scout Evaluates
- Bonding potential vs entertainment value
- Scalability to group size
- Physical and cognitive accessibility
- Weather dependencies
- Competitive vs collaborative dynamics
- Structured vs informal balance
- Innovative options beyond typical choices

### Dining Specialist Considers
- Dietary accommodation (vegetarian, vegan, GF, allergies, religious)
- Conversation-friendliness (noise levels, layout)
- Group capacity and seating configurations
- Dining styles that encourage interaction
- Timing relative to activities
- Practical details (parking, accessibility, cost)

### Event Coordinator Creates
- Realistic minute-by-minute timelines
- Proper pacing with buffer time (20% overhead)
- Smooth transitions between activities and venues
- Complete logistics (transportation, materials, facilitators)
- Cost breakdowns by component
- Booking checklists with lead times
- Contingency plans for common issues

### Devil's Advocate Identifies
- Assumptions about what creates bonding
- Accessibility barriers (physical, cognitive, financial)
- Personality mismatches (forced fun risks)
- Logistics vulnerabilities (weather, traffic, parking)
- Budget realism and hidden costs
- Overlooked considerations
- Confidence level in plan success

## Planning Timeline

### 6+ Weeks Before Event
- Complete Team Profiler discovery
- Review Activity Scout and Dining Specialist recommendations
- Select preferred Event Coordinator scenario
- Get Devil's Advocate critical review
- Begin bookings (venues, facilitators, restaurants)

### 4 Weeks Before Event
- Confirm all major bookings
- Collect dietary restrictions from all participants
- Create participant communication

### 2 Weeks Before Event
- Final headcount confirmations
- Weather check for outdoor activities
- Finalize transportation plans
- Send detailed participant information

### 1 Week Before Event
- Confirmation calls to all vendors
- Create day-of coordination plan
- Emergency contact list
- Materials and supplies ready

### Day of Event
- Arrive early to first venue
- Have all contact information
- Monitor timing and adjust as needed
- Coordinate with restaurants on arrival

## Success Metrics

Effective team building events typically show:
- **Immediate**: Laughter, engagement, participation from quiet members
- **Short-term** (next week): New relationships continuing, inside jokes, positive references
- **Medium-term** (next month): Improved communication, willingness to ask for help, cross-functional collaboration
- **Long-term** (next quarter): Lower conflict, higher trust, better team performance

This system optimizes for all four timeframes.

## Troubleshooting

### "My team is skeptical about team building"
Start with Team Profiler to understand why. Often previous "forced fun" experiences. System's inclusive design and critical review helps avoid repetition.

### "Budget is very limited"
Activity Scout provides options across price ranges. Budget-conscious options can be just as effective (outdoor games + BBQ can bond as well as premium experiences).

### "Very diverse team abilities"
This is the system's strength. Dining Specialist ensures dietary accommodation, Activity Scout provides alternatives, Devil's Advocate catches accessibility oversights.

### "Short planning timeline"
System can work with 2-3 week timelines, but venue availability may limit options. Focus on venues with shorter booking requirements.

### "Don't know what our team needs"
Team Profiler will help identify through structured questions. Often goals emerge through discovery process.

## Frequently Asked Questions

**Q: How long does planning take?**  
A: 30-60 minutes for complete workflow. Can iterate faster with clear requirements.

**Q: Can I modify recommendations?**  
A: Yes. Agents provide options and iterate based on feedback.

**Q: What if Devil's Advocate says don't proceed?**  
A: Take seriously. Address concerns before booking. Better to adjust than have event fail.

**Q: Do I need all five agents?**  
A: Team Profiler and Devil's Advocate are most critical. Others can be used selectively if you have requirements or plans already.

**Q: How current are venue recommendations?**  
A: Agents provide example venues but can work with any location. Verify availability and details.

**Q: Works for virtual teams?**  
A: Optimized for in-person events. Virtual team building needs different approaches.

**Q: Maximum team size?**  
A: Designed for 5-50 people. 50+ may need professional event companies for execution.

## Version History

- **1.0.0** - Initial corporate team building planning system with five specialized agents

## Updating This Agent Group

This agent group can be updated from the upstream repository to get the latest improvements, bug fixes, and new features.

**To update:**

```bash
cd corporate-team-building  # or wherever you installed this agent group
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
git commit -m "Update corporate-team-building agents from upstream"
```

**Note:** If you've made local customizations to agent files, the update will overwrite them. Consider keeping local modifications in a separate branch or using different file names.

## Getting Started

Ready to plan team building that genuinely strengthens your team?

**Start here:**
```
@team-profiler I need to plan team building for [describe your team]
```

The system will guide you through complete planning process with automatic handoffs between agents.

---

## Support

For issues, feedback, or suggestions, provide feedback through your organization's agent management process.
