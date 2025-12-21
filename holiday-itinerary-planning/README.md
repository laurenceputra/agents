# Holiday Itinerary Planning Agent Group

**Version**: 1.0.0

A comprehensive agent group for creating personalized vacation itineraries from initial travel ideas to ready-to-execute plans with bookings, schedules, and contingency planning.

## Overview

The Holiday Itinerary Planning group coordinates six specialized agents to handle every aspect of trip planning - from researching destinations to optimizing budgets to ensuring nothing important is overlooked.

## The Six Agents

###  1. destination-researcher
**Role**: Research and recommend destinations matching preferences  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You have travel dates and interests but need destination ideas

Analyzes your preferences, constraints, and budget to recommend 2-3 destinations with pros/cons, seasonal timing, visa requirements, and cultural context.

### 2. activity-planner
**Role**: Design day-by-day activity schedules  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You've chosen a destination and need activities planned

Creates engaging itineraries balancing must-see attractions with local experiences, proper pacing, and backup plans for weather.

### 3. logistics-coordinator
**Role**: Organize transportation, accommodation, and practical details  
**Model**: Claude Haiku 4.5 (copilot)  
**When to use**: You have activities planned and need logistics figured out

Plans flights, accommodation, local transportation, booking timelines, packing lists, and emergency contacts.

### 4. budget-optimizer
**Role**: Track costs and optimize spending allocation  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You need cost analysis and budget optimization

Estimates all trip costs, identifies savings opportunities, suggests splurge-vs-save strategies, and ensures budget feasibility.

### 5. itinerary-integrator
**Role**: Synthesize all components into final itinerary document  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: You have all components and need them unified

Merges destination info, activities, logistics, and budget into one cohesive, traveler-friendly document with quick reference cards and contingency plans.

### 6. devils-advocate (MANDATORY)
**Role**: Critical review before final delivery  
**Model**: Claude Sonnet 4.5 (copilot)  
**When to use**: Before booking anything - final quality gate

Challenges assumptions, identifies blind spots, surfaces agent disagreements, and ensures travelers have complete information for confident booking decisions.

## Quick Start

### Basic Workflow

```
1. @destination-researcher - Get destination recommendations
   ↓
2. [You select preferred destination]
   ↓
3. @activity-planner - Design day-by-day activities
   ↓
4. @logistics-coordinator - Add transportation and accommodation
   ↓
5. @budget-optimizer - Analyze costs and optimize spending
   ↓
6. @itinerary-integrator - Create unified final itinerary
   ↓
7. @devils-advocate - MANDATORY critical review
   ↓
8. Book your trip with confidence!
```

### Example: Family Beach Vacation

**Step 1**: Consult @destination-researcher
```
"We're a family of 4 (kids ages 6 and 9) looking for a beach vacation July 15-22. 
Budget is $4000 total. Kids love snorkeling and animals. We want relaxed pacing. 
Flying from Dallas. What destinations do you recommend?"
```

**Step 2**: Review options, choose Cozumel

**Step 3**: Consult @activity-planner
```
"We've chosen Cozumel for July 15-22. Design activities for our family 
(kids 6 and 9) focused on snorkeling, beach time, and animal experiences. 
Keep it relaxed - not over-scheduled."
```

**Step 4**: Consult @logistics-coordinator
```
"Add logistics to our Cozumel itinerary: flights from Dallas, all-inclusive 
resort on west side, transportation for activities."
```

**Step 5**: Consult @budget-optimizer
```
"Analyze costs for our complete Cozumel trip and optimize within $4000 budget."
```

**Step 6**: Consult @itinerary-integrator
```
"Create final integrated itinerary combining all components with quick reference 
card and booking timeline."
```

**Step 7**: Consult @devils-advocate (REQUIRED)
```
"Critically review this Cozumel itinerary before we book anything. Challenge 
assumptions, identify risks, and surface any issues."
```

## Example Workflows by Trip Type

### Adventure Trip (Solo Traveler)
```
destination-researcher → activity-planner → budget-optimizer (early) → 
logistics-coordinator → itinerary-integrator → devils-advocate
```
*Note: Budget optimizer involved earlier to establish cost constraints for adventure activities.*

### Romantic Anniversary Trip
```
 
budget-optimizer → itinerary-integrator → devils-advocate
```
*Standard workflow with emphasis on special dining and upgraded accommodation in planning.*

### Budget Backpacking
```
destination-researcher → budget-optimizer → activity-planner → 
logistics-coordinator → itinerary-integrator → devils-advocate
```
*Note: Budget optimizer sets constraints before activities planned - prioritizes cheap/free activities.*

### Accessible Cultural Trip
```
destination-researcher (with accessibility focus) → activity-planner 
(accessible activities) → logistics-coordinator (critical for accessibility) → 
budget-optimizer → itinerary-integrator → devils-advocate
```
*Logistics coordinator plays crucial role verifying accessibility of all components.*

## Planning with Accessibility Needs

For travelers with mobility, sensory, or other accessibility requirements, accessibility should be **the primary filter** throughout planning - not an afterthought.

### Accessibility-First Workflow

When accessibility is a core requirement:

**1. Start with explicit accessibility requirements**
```
@destination-researcher: "Recommend beach destinations for wheelchair user. 
Must have wheelchair-accessible beaches, level sidewalks, accessible restaurants. 
July dates, $3000 budget, flying from Atlanta."
```

**2. Filter activities through accessibility lens**
```
@activity-planner: "Design activities for wheelchair user in San Diego. 
All activities must be wheelchair accessible - verify entrance accessibility, 
bathroom facilities, terrain. Include specific accessibility details for each venue."
```

**3. Logistics becomes CRITICAL - verify everything**
```
@logistics-coordinator: "Add logistics with detailed accessibility verification:
- Airport assistance and wheelchair transport
- Accessible hotel room (roll-in shower, grab bars)
- Accessible rental van or ride services
- Verify each activity venue called ahead for accessibility
- Backup plans if venues aren't actually accessible"
```

**4. Budget may need adjustment for accessibility**
```
@budget-optimizer: "Factor in accessibility costs: accessible accommodation 
premium, specialized transport, potential tour guide needs."
```

**5. Final check for accessibility gaps**
```
@devils-advocate: "Critical review focused on accessibility: Are there 
unstated assumptions? Hidden barriers? Verify all venues truly accessible."
```

### Key Principles for Accessible Planning

- **Verify, don't assume**: Just because a venue claims accessibility doesn't mean it meets your needs. Agents should recommend calling ahead.
- **Accessibility is primary, not secondary**: Filter destinations and activities through accessibility first, not as a constraint added later.
- **Build in buffer time**: Accessible travel often takes longer. Account for extra time between activities.
- **Multiple backup plans**: Inaccessible venues are common. Always have alternatives.
- **Specific details matter**: "Wheelchair accessible" means different things. Specify: ramp grade, door widths, bathroom facilities, seating options.

### Example: Mobility-Focused Trip

**Bad approach**: Plan trip, then try to make it accessible  
**Good approach**: Filter every decision through accessibility from the start

The difference shows up everywhere - destination choice (cities with accessible public transit), activity selection (venues with verified accessibility), logistics (ground-floor accommodation near amenities), and budget (realistic costs for accessible options).

## What Makes a Great Itinerary

 **Clear daily schedule** - Know what you're doing when  
 **Realistic pacing** - Mix of active days and rest time  
 **Budget transparency** - Know what things cost, no surprises  
 **Contingency plans** - Backup options for weather or issues  
 **Accessibility considered** - Mobility, dietary, sensory needs addressed  
 **Cultural sensitivity** - Local customs and etiquette guidance  
 **Actionable booking timeline** - Know what to book when  
 **Emergency preparedness** - Contacts, backup plans documented

## Tips for Best Results

### Be Specific About Preferences
**Instead of**: "We want a fun trip"  
**Say**: "We love trying local food, hate crowds, prefer walking to taxis, and need to be back at the hotel by 8pm for kids' bedtime"

### Communicate Constraints Clearly
**Include**:
- Budget (total or daily)
- Dates (exact or flexible)
- Mobility limits
- Dietary restrictions
- Deal-breakers

### Review Critically Before Booking
Use @devils-advocate to challenge everything. Better to catch problems during planning than during the trip.

### Trust the Process
The workflow has feedback loops. If budget-optimizer finds you're over budget, you'll iterate with activity-planner or logistics-coordinator to adjust. This is normal and leads to better results.

## Workflow Flexibility

### Linear vs. Flexible Approach

The workflows shown above are **recommended starting points**, especially for first-time users. However, **agents can be consulted in any order** based on your needs.

**Linear workflow (recommended for beginners)**:
- Provides structured progression
- Ensures nothing is overlooked
- Natural flow from research to execution
- Each agent builds on previous work

**Flexible workflow (for experienced travelers)**:
- Start where you need help most
- Maybe you already know your destination - skip to @activity-planner
- Budget-conscious? Start with @budget-optimizer to set constraints
- Have a specific logistics question? Jump straight to @logistics-coordinator
- Always end with @devils-advocate regardless of path

### Common Flexible Patterns

**Budget-first planning**:
```
budget-optimizer (establish constraints) → destination-researcher (within budget) → 
activity-planner → logistics-coordinator → itinerary-integrator → devils-advocate
```

**Destination already chosen**:
```
activity-planner → logistics-coordinator → budget-optimizer → 
itinerary-integrator → devils-advocate
```

**Specific logistics question**:
```
logistics-coordinator (answer specific question) → 
[return to normal workflow or iterate]
```

**Activity idea validation**:
```
activity-planner (test idea) → devils-advocate (critical review) → 
[iterate or continue to logistics]
```

The key: **Use the agents that add value for your situation.** The only non-negotiable step is @devils-advocate as the final review before booking.

## Common Questions

**Q: Do I have to follow the workflow in order?**  
A: No! The linear workflow is recommended for beginners, but you can consult agents in any order. Start where you need help. Always end with @devils-advocate.

**Q: Can I skip agents in the workflow?**  
A: You can, but you'll miss value. Each agent adds a layer of refinement. At minimum, always use @devils-advocate as the final review.

**Q: What if agents disagree?**  
A: @devils-advocate documents all disagreements with reasoning from each perspective. You make the final call based on your priorities.

**Q: Do I need to provide all information upfront?**  
A: No - agents will ask clarifying questions. But the more context you provide initially, the better the first draft.

**Q: Can I change my mind mid-planning?**  
A: Yes! Maybe @budget-optimizer shows Destination A is too expensive, so you go back to @destination-researcher to pick Destination B. The workflow is iterative.

**Q: Can I consult an agent multiple times?**  
A: Absolutely! You might consult @activity-planner three times as you refine your daily schedule. Iteration is expected.

**Q: How long does this take?**  
A: Depends on trip complexity. Simple weekend trip might take 2-3 hours of planning. Complex 2-week international trip could take 6-8 hours spread over several days.

## Integration with Booking Platforms

This agent group creates **recommendations** - it doesn't make actual bookings. Once you have your itinerary:

- **Flights**: Use airline websites, Google Flights, or travel agencies
- **Accommodation**: Booking.com, Airbnb, hotel direct websites
- **Activities**: Direct booking with tour operators, Viator, GetYourGuide
- **Insurance**: Travel insurance companies (World Nomads, Allianz, etc.)

The itinerary includes specific booking timelines, websites, and confirmation tracking.

## Troubleshooting

### "The budget is way over"
 Consult @budget-optimizer for optimization recommendations, then iterate with @activity-planner (cheaper activities) or @logistics-coordinator (cheaper accommodation)

### "The schedule feels too packed"
 @devils-advocate will catch this. Return to @activity-planner to adjust pacing

### "Logistics don't make sense"
 @devils-advocate flags logistics issues. Return to @logistics-coordinator for fixes

### "Agents disagree on approach"
 This is expected! @devils-advocate documents both perspectives. You decide based on your priorities.

### "I'm not sure which destination to choose"
 @destination-researcher provides 2-3 options with trade-offs. Pick one, or ask for different options with adjusted criteria

## Version History

- **1.0.0** (2024-12-18): Initial release with six agents (destination-researcher, activity-planner, logistics-coordinator, budget-optimizer, itinerary-integrator, devils-advocate)

## Updating This Agent Group

This agent group can be updated from the upstream repository to get the latest improvements, bug fixes, and new features.

**To update:**

```bash
cd holiday-itinerary-planning  # or wherever you installed this agent group
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
git commit -m "Update holiday-itinerary-planning agents from upstream"
```

**Note:** If you've made local customizations to agent files, the update will overwrite them. Consider keeping local modifications in a separate branch or using different file names.

## Support

This is an open-source agent system. For issues or suggestions, refer to the specification document in `.specifications/holiday-itinerary-planning-group-specification.md`.
