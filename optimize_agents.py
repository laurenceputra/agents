#!/usr/bin/env python3
"""
Agent Optimization Script
Optimizes three oversized agent files based on specification.
"""

import re
from pathlib import Path

def optimize_impact_evaluator():
    """Optimize philanthropic-advisory/agents/impact-evaluator.agent.md"""
    
    file_path = Path("philanthropic-advisory/agents/impact-evaluator.agent.md")
    content = file_path.read_text()
    
    # 1. Update Domain Context section - add reference to REFERENCE.md
    domain_context_old = re.search(
        r'## Domain Context\n\n.*?(?=## Writing Style Guidelines|## Input Requirements)',
        content,
        re.DOTALL
    )
    
    if domain_context_old:
        domain_context_new = """## Domain Context

Impact evaluation in philanthropy bridges the gap between program activities and measurable social change. Singapore's context includes:

**Key Concepts**:
- **SROI (Social Return on Investment)**: Monetizes social outcomes to calculate return on investment
- **CEA (Cost-Effectiveness Analysis)**: Compares cost per standardized outcome unit across programs
- **Trajectory Uplift**: Change in beneficiary life trajectory attributable to intervention
- **Systemic Impact**: Addresses root causes (upstream) vs treats symptoms (downstream)

**For detailed methodologies, calculation formulas, Singapore demographic data, and policy landscape, see [Philanthropic Advisory Reference Guide](../REFERENCE.md).**

"""
        content = content.replace(domain_context_old.group(0), domain_context_new)
    
    # 2. Compress Example 2 (FamilyStability Now) - remove calculation iterations
    # Find and compress the "Wait, let me recalculate" section
    calc_iteration = re.search(
        r'Wait, let me recalculate.*?Rounding to \*\*3\.8:1\*\*.*?\n\n',
        content,
        re.DOTALL
    )
    
    if calc_iteration:
        compressed = """**SROI Ratio**: $1,801,590 / $500,000 = **3.8:1**

"""
        content = content.replace(calc_iteration.group(0), compressed)
    
    # 3. Compress CEA benchmark table - keep only 2-3 benchmarks
    cea_table = re.search(
        r'\| Program \|.*?\| MSF ComCare.*?\n\n',
        content,
        re.DOTALL
    )
    
    if cea_table:
        compressed_table = """| Program | Cost/Outcome | Success Rate |
|---------|--------------|--------------|
| FamilyStability Now | $4,167 | 80% |
| TRANS Family Services | $3,800 | 75% |
| MSF ComCare (crisis) | $6,500 | 65% |

"""
        content = content.replace(cea_table.group(0), compressed_table)
    
    # 4. Consolidate Quality Checklist from 11 to 9 items
    quality_checklist_old = re.search(
        r'## Quality Checklist\n\nWhen completing an impact evaluation, verify:\n\n(- \[ \].*?\n)+',
        content,
        re.DOTALL
    )
    
    if quality_checklist_old:
        quality_checklist_new = """## Quality Checklist

When completing an impact evaluation, verify:

- [ ] **Impact Metrics Calculated**: SROI, CEA, trajectory uplift with clear methodology, investment amount, outcomes valued, adjustments applied
- [ ] **Systemic Impact Scored**: Upstream/midstream/downstream classification with rationale and Singapore-specific factors
- [ ] **Data Quality & KPIs Assessed**: Availability, rigor, comparison group, sample size assessed; output/outcome/impact metrics specified with targets
- [ ] **Singapore Context Integrated**: Demographics, policies, existing initiatives referenced throughout analysis
- [ ] **Red Flags Surfaced**: Implementation risks, data concerns, and limitations proactively identified
- [ ] **Assumptions Documented**: Key assumptions explicitly stated, limitations acknowledged transparently
- [ ] **Confidence Level Stated**: Percentage confidence provided with rationale for rating
- [ ] **Recommendation Clear**: Proceed/Proceed with Conditions/Decline with specific rationale and next steps
- [ ] **Output is natural and human-like**: Follows writing style guidelines (varied sentences, direct language, active voice)
"""
        content = content.replace(quality_checklist_old.group(0), quality_checklist_new)
    
    # 5. Write optimized content
    file_path.write_text(content)
    
    # Return character count
    return len(content)


def optimize_portfolio_strategist():
    """Optimize philanthropic-advisory/agents/portfolio-strategist.agent.md"""
    
    file_path = Path("philanthropic-advisory/agents/portfolio-strategist.agent.md")
    content = file_path.read_text()
    
    # 1. Add reference to REFERENCE.md in Domain Context
    domain_context_pattern = r'(## Domain Context\n\n)(.*?)((?=## Writing Style Guidelines|## Input Requirements))'
    
    match = re.search(domain_context_pattern, content, re.DOTALL)
    if match:
        new_domain = match.group(1) + """Portfolio strategy ensures philanthropic giving aligns with values, balances risk, and maximizes collective impact. Key frameworks include concentration risk management, portfolio balance principles, and strategic gap analysis.

**For detailed portfolio strategy frameworks, concentration risk guidelines, and Singapore-specific gaps, see [Philanthropic Advisory Reference Guide](../REFERENCE.md#portfolio-strategy-frameworks).**

""" + match.group(3)
        content = re.sub(domain_context_pattern, new_domain, content, flags=re.DOTALL)
    
    # 2. Reduce quality checklist if needed (find and optimize)
    # 3. Compress examples if present
    
    file_path.write_text(content)
    return len(content)


def optimize_event_coordinator():
    """Optimize corporate-team-building/agents/event-coordinator.agent.md"""
    
    file_path = Path("corporate-team-building/agents/event-coordinator.agent.md")
    content = file_path.read_text()
    
    # 1. Add reference to REFERENCE.md in relevant sections
    # Add after Responsibilities section
    responsibilities_pattern = r'(## Responsibilities\n\n.*?\n\n)(## Domain Context|## Writing Style Guidelines)'
    
    match = re.search(responsibilities_pattern, content, re.DOTALL)
    if match:
        reference_note = match.group(1) + """**For detailed event planning principles, pacing formulas, group size dynamics, and logistics frameworks, see [Corporate Team Building Reference Guide](../REFERENCE.md).**

""" + match.group(2)
        content = re.sub(responsibilities_pattern, reference_note, content, flags=re.DOTALL)
    
    # 2. Compress examples - show 2 scenarios instead of 3
    # This requires more sophisticated pattern matching based on actual content
    
    file_path.write_text(content)
    return len(content)


def main():
    print("Agent Optimization Script")
    print("=" * 60)
    
    # Change to repository root
    import os
    os.chdir("/home/appuser/code/agents")
    
    print("\n1. Optimizing impact-evaluator.agent.md...")
    chars1 = optimize_impact_evaluator()
    print(f"   New size: {chars1:,} characters")
    
    print("\n2. Optimizing portfolio-strategist.agent.md...")
    chars2 = optimize_portfolio_strategist()
    print(f"   New size: {chars2:,} characters")
    
    print("\n3. Optimizing event-coordinator.agent.md...")
    chars3 = optimize_event_coordinator()
    print(f"   New size: {chars3:,} characters")
    
    print("\n" + "=" * 60)
    print("Optimization complete!")
    print(f"\nTotal characters: {chars1 + chars2 + chars3:,}")
    print(f"Average per agent: {(chars1 + chars2 + chars3) // 3:,}")
    
    # Verify all under 25,000
    if chars1 < 25000 and chars2 < 25000 and chars3 < 25000:
        print("\n✓ All agents under 25,000 character target!")
    else:
        print("\n⚠ Warning: Some agents still over 25,000 characters")
        if chars1 >= 25000:
            print(f"  - impact-evaluator: {chars1:,} ({chars1 - 25000:+,})")
        if chars2 >= 25000:
            print(f"  - portfolio-strategist: {chars2:,} ({chars2 - 25000:+,})")
        if chars3 >= 25000:
            print(f"  - event-coordinator: {chars3:,} ({chars3 - 25000:+,})")


if __name__ == "__main__":
    main()
