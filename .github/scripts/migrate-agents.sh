#!/bin/bash
# Agent Group Migration Script
# 
# Migrates a portable agent group from one repository to another.
# Usage: ./migrate-agents.sh source-path target-path [group-name]
#
# Examples:
#   ./migrate-agents.sh ~/src-repo/legacy-planning ~/target-repo/.github/agents
#   ./migrate-agents.sh . ~/target-repo/.github/agents legacy-planning

set -e

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ ${1}${NC}"
}

print_success() {
    echo -e "${GREEN}✓ ${1}${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ ${1}${NC}"
}

print_error() {
    echo -e "${RED}✗ ${1}${NC}"
}

# Function to show usage
show_usage() {
    cat << EOF
${BLUE}Agent Group Migration Script${NC}

Migrates a portable agent group from one repository to another.

${BLUE}Usage:${NC}
  ./migrate-agents.sh <source-path> <target-path> [group-name]

${BLUE}Arguments:${NC}
  source-path    Path to agent group source (e.g., ~/src-repo/legacy-planning)
  target-path    Destination directory (e.g., ~/target-repo/.github/agents)
  group-name     Name of agent group (if not in source path)

${BLUE}Examples:${NC}
  # Migrate with group name from path
  ./migrate-agents.sh ~/agents/legacy-planning ~/target-repo/.github/agents

  # Migrate with explicit group name
  ./migrate-agents.sh . ~/target-repo/.github/agents my-agents

${BLUE}This script will:${NC}
  1. Validate the source agent group structure
  2. Copy the entire group to target directory
  3. Run validation in target location
  4. Generate migration report

${BLUE}Requirements:${NC}
  - Python 3.7+ with PyYAML
  - .github/scripts/validate-agents.py in target repository

EOF
}

# Check arguments
if [[ $# -lt 2 ]]; then
    show_usage
    exit 1
fi

SOURCE_PATH="$1"
TARGET_PATH="$2"
GROUP_NAME="${3:$(basename "$SOURCE_PATH")}"

print_info "Agent Group Migration"
print_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Source:      $SOURCE_PATH"
echo "Target:      $TARGET_PATH"
echo "Group Name:  $GROUP_NAME"
echo ""

# Step 1: Validate source exists
if [[ ! -d "$SOURCE_PATH" ]]; then
    print_error "Source path does not exist: $SOURCE_PATH"
    exit 1
fi
print_success "Source path exists"

# Step 2: Check for agents subdirectory
if [[ ! -d "$SOURCE_PATH/agents" ]]; then
    print_error "Source is not a valid agent group (missing agents/ subdirectory)"
    exit 1
fi
print_success "Valid agent group structure found"

# Step 3: Count agents
AGENT_COUNT=$(find "$SOURCE_PATH/agents" -name "*.agent.md" | wc -l)
if [[ $AGENT_COUNT -eq 0 ]]; then
    print_error "No agent files found in agents/ directory"
    exit 1
fi
print_success "Found $AGENT_COUNT agent file(s)"

# Step 4: Create target directory
if [[ ! -d "$TARGET_PATH" ]]; then
    print_info "Creating target directory: $TARGET_PATH"
    mkdir -p "$TARGET_PATH"
fi
print_success "Target directory ready"

# Step 5: Copy agent group
print_info "Copying agent group..."
cp -r "$SOURCE_PATH" "$TARGET_PATH/$GROUP_NAME"
print_success "Agent group copied to $TARGET_PATH/$GROUP_NAME"

# Step 6: Run validation if available
VALIDATOR_PATH="$(dirname "$TARGET_PATH")/../scripts/validate-agents.py"
if [[ ! -f "$VALIDATOR_PATH" ]]; then
    # Try to find validator in target repo
    VALIDATOR_PATH="$TARGET_PATH/../../scripts/validate-agents.py"
fi

if [[ -f "$VALIDATOR_PATH" ]]; then
    print_info "Running validation..."
    cd "$(dirname "$VALIDATOR_PATH")/../.."
    
    if python "$VALIDATOR_PATH" "$TARGET_PATH/$GROUP_NAME"; then
        print_success "Validation passed"
    else
        print_warning "Validation found issues (see above)"
        print_info "Review the validation output and fix any errors"
    fi
else
    print_warning "Validator script not found at $VALIDATOR_PATH"
    print_info "Manually run validation after migration:"
    print_info "  python .github/scripts/validate-agents.py .github/agents/$GROUP_NAME/"
fi

# Step 7: Summary
echo ""
print_success "Migration Complete!"
echo ""
print_info "Next steps:"
echo "  1. Review the agent group at: $TARGET_PATH/$GROUP_NAME"
echo "  2. Update .github/copilot-instructions.md to include the new agent group"
echo "  3. Add the group to your README.md with integration instructions"
echo "  4. Test one of the agents to ensure it works in your environment"
echo "  5. Commit and push the changes"
echo ""
print_info "Example next commands:"
echo "  cd $TARGET_PATH/../.."
echo "  git add .github/agents/$GROUP_NAME/"
echo "  git commit -m 'Add $GROUP_NAME agents from upstream'"
echo "  git push origin main"
echo ""

# Generate migration report
REPORT_FILE="migration-report-$(date +%Y%m%d-%H%M%S).txt"
print_info "Generating migration report: $REPORT_FILE"

cat > "$TARGET_PATH/$GROUP_NAME/$REPORT_FILE" << EOF
Agent Group Migration Report
Generated: $(date)

Source Repository: $SOURCE_PATH
Target Repository: $TARGET_PATH/$GROUP_NAME
Group Name: $GROUP_NAME

Agents Migrated: $AGENT_COUNT

Agent Files:
$(find "$TARGET_PATH/$GROUP_NAME/agents" -name "*.agent.md" -exec basename {} \;)

Files Copied:
$(find "$TARGET_PATH/$GROUP_NAME" -type f | sed 's|'$TARGET_PATH/$GROUP_NAME/'|  - |g')

Next Steps:
1. Review agents in new location
2. Test agents in target environment
3. Update documentation
4. Commit and merge

Support:
See PORTABILITY.md in source repository for troubleshooting guide.
EOF

print_success "Migration report created: $REPORT_FILE"
echo ""
print_success "Ready to use in target repository!"
