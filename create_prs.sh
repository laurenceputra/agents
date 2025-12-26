#!/bin/bash
# Script to create PRs for all vulnerability fix branches

echo "PR Creation Script for Agent Vulnerability Fixes"
echo "=================================================="
echo

# Check if gh CLI is available
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) not installed. Install with: sudo apt install gh"
    echo "Or create PRs manually on GitHub.com"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub. Run: gh auth login"
    exit 1
fi

# Array of branches and their PR titles
declare -A prs=(
    ["feature/optimize-agent-sizes"]="fix(critical): Optimize oversized agents approaching character limit"
    ["feature/sync-group-versions"]="fix: Sync agent group versions for consistency"
)

# Create PRs for each branch
for branch in "${!prs[@]}"; do
    title="${prs[$branch]}"
    
    echo "Creating PR for $branch..."
    echo "Title: $title"
    
    # Check if branch exists
    if git show-ref --verify --quiet "refs/heads/$branch"; then
        gh pr create \
            --base main \
            --head "$branch" \
            --title "$title" \
            --body-file ".pr_details/${branch}.md" \
            --label "vulnerability-fix"
        
        echo "✓ PR created for $branch"
    else
        echo "⚠ Branch $branch does not exist, skipping..."
    fi
    
    echo
done

echo "=================================================="
echo "PR creation complete!"
echo
echo "View PRs: gh pr list"
echo "Or visit: https://github.com/$(gh repo view --json nameWithOwner -q .nameWithOwner)/pulls"
