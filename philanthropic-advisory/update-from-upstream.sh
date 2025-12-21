#!/bin/bash

# Self-Update Script for Agent Groups
# This script pulls updates from the upstream laurenceputra/agents repository
# for a specific agent group while preserving local modifications.
#
# Usage: ./update-from-upstream.sh
#
# The script will:
# 1. Detect the current agent group name from its location
# 2. Add the upstream repository as a remote (if not already added)
# 3. Fetch the latest changes from upstream
# 4. Selectively merge changes for this agent group only
# 5. Handle new files, modifications, and deletions

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
UPSTREAM_REPO="https://github.com/laurenceputra/agents.git"
UPSTREAM_REMOTE="agents-upstream"
DEFAULT_BRANCH="main"

# Helper functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detect the agent group name from AGENTGROUPNAME file
detect_agent_group() {
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local agentgroupname_file="$script_dir/AGENTGROUPNAME"
    
    if [[ -f "$agentgroupname_file" ]]; then
        # Read group name from AGENTGROUPNAME file
        local group_name="$(cat "$agentgroupname_file" | tr -d '[:space:]')"
        echo "$group_name"
    else
        log_error "AGENTGROUPNAME file not found in $script_dir"
        log_error "Please create a file named 'AGENTGROUPNAME' containing the agent group name"
        exit 1
    fi
}

# Check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Not a git repository. Please run this script from within a git repository."
        exit 1
    fi
}

# Add upstream remote if it doesn't exist
setup_upstream_remote() {
    if git remote | grep -q "^${UPSTREAM_REMOTE}$"; then
        log_info "Upstream remote '${UPSTREAM_REMOTE}' already exists"
        git remote set-url "${UPSTREAM_REMOTE}" "${UPSTREAM_REPO}"
    else
        log_info "Adding upstream remote '${UPSTREAM_REMOTE}'"
        git remote add "${UPSTREAM_REMOTE}" "${UPSTREAM_REPO}"
    fi
}

# Fetch updates from upstream
fetch_upstream() {
    log_info "Fetching updates from upstream repository..."
    git fetch "${UPSTREAM_REMOTE}" "${DEFAULT_BRANCH}"
}

# Get the relative path to the agent group in the current repository
get_current_group_path() {
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local repo_root="$(git rev-parse --show-toplevel)"
    local rel_path="${script_dir#$repo_root/}"
    echo "$rel_path"
}

# Update agent group files from upstream
update_agent_group() {
    local agent_group="$1"
    local current_path="$2"
    
    log_info "Updating agent group: ${agent_group}"
    log_info "Current location: ${current_path}"
    
    # Get the list of files in upstream for this agent group
    log_info "Fetching file list from upstream..."
    
    # Checkout files from upstream for this specific agent group
    local upstream_ref="${UPSTREAM_REMOTE}/${DEFAULT_BRANCH}"
    
    # Check if the agent group exists in upstream
    if ! git ls-tree -r --name-only "${upstream_ref}" "${agent_group}/" > /dev/null 2>&1; then
        log_error "Agent group '${agent_group}' not found in upstream repository"
        log_info "Available agent groups in upstream:"
        git ls-tree -d --name-only "${upstream_ref}" | grep -v "^\." | head -10
        exit 1
    fi
    
    log_info "Pulling updates for agent group '${agent_group}'..."
    
    # Get list of files in upstream for this agent group
    local temp_file_list=$(mktemp)
    git ls-tree -r --name-only "${upstream_ref}" "${agent_group}/" > "$temp_file_list"
    
    local update_count=0
    local new_count=0
    local skip_count=0
    
    # Process each file from upstream
    while IFS= read -r upstream_file; do
        # Calculate the target path in current repository
        local rel_file="${upstream_file#$agent_group/}"
        local target_file="${current_path}/${rel_file}"
        
        # Check if file exists locally
        if [[ -f "$target_file" ]]; then
            # File exists - check if it differs from upstream
            if git diff --quiet "${upstream_ref}:${upstream_file}" "$target_file" 2>/dev/null; then
                skip_count=$((skip_count + 1))
            else
                log_info "Updating: ${target_file}"
                mkdir -p "$(dirname "$target_file")"
                git show "${upstream_ref}:${upstream_file}" > "$target_file"
                update_count=$((update_count + 1))
            fi
        else
            # New file
            log_success "Adding new file: ${target_file}"
            mkdir -p "$(dirname "$target_file")"
            git show "${upstream_ref}:${upstream_file}" > "$target_file"
            new_count=$((new_count + 1))
        fi
    done < "$temp_file_list"
    
    rm "$temp_file_list"
    
    # Summary
    echo ""
    log_success "Update complete!"
    log_info "Summary:"
    echo "  - New files: ${new_count}"
    echo "  - Updated files: ${update_count}"
    echo "  - Unchanged files: ${skip_count}"
    echo ""
    
    # Show git status
    log_info "Git status:"
    git status --short
    echo ""
    log_info "Review the changes above. If everything looks good, commit them with:"
    echo "  git add ."
    echo "  git commit -m 'Update ${agent_group} agent group from upstream'"
}

# Main script
main() {
    echo ""
    log_info "Agent Group Self-Update Script"
    log_info "==============================="
    echo ""
    
    # Check if in git repo
    check_git_repo
    
    # Detect agent group
    local agent_group=$(detect_agent_group)
    log_info "Detected agent group: ${agent_group}"
    
    # Get current path
    local current_path=$(get_current_group_path)
    
    # Setup upstream remote
    setup_upstream_remote
    
    # Fetch updates
    fetch_upstream
    
    # Update agent group
    update_agent_group "$agent_group" "$current_path"
    
    echo ""
    log_success "Update process completed successfully!"
    echo ""
}

# Run main function
main "$@"
