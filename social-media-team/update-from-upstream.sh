#!/bin/bash

# Self-Update Script for Agent Groups
# This script downloads updates from the upstream laurenceputra/agents repository
# for a specific agent group using direct file downloads.
#
# Usage: ./update-from-upstream.sh
#
# The script will:
# 1. Read the agent group name from the AGENTGROUPNAME file
# 2. Fetch the list of files from the upstream repository
# 3. Download each file and compare with local version
# 4. Handle new files, modifications, and unchanged files
# 5. Show a summary of changes

# Note: We don't use 'set -e' globally because we want to continue processing
# even if individual file downloads fail. We check error codes explicitly instead.

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GITHUB_REPO="laurenceputra/agents"
DEFAULT_BRANCH="main"
RAW_BASE_URL="https://raw.githubusercontent.com/${GITHUB_REPO}/${DEFAULT_BRANCH}"
API_BASE_URL="https://api.github.com/repos/${GITHUB_REPO}/contents"

# GitHub token for API rate limiting (optional, set via GITHUB_TOKEN env var)
GITHUB_TOKEN="${GITHUB_TOKEN:-}"

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

# Check if curl is available
check_curl() {
    if ! command -v curl &> /dev/null; then
        log_error "curl is not installed. Please install curl to use this script."
        exit 1
    fi
    
    # Check for jq (optional, for better JSON parsing)
    if ! command -v jq &> /dev/null; then
        log_warning "jq is not installed. JSON parsing will be limited but the script will still work."
    fi
}

# Get list of files from upstream using GitHub API
get_upstream_files() {
    local agent_group="$1"
    local temp_dir="$2"
    
    log_info "Fetching file list from upstream..."
    
    > "${temp_dir}/file_list.txt"  # Initialize empty file
    
    # Build auth header if token is available
    local auth_header=""
    if [[ -n "$GITHUB_TOKEN" ]]; then
        auth_header="-H \"Authorization: token ${GITHUB_TOKEN}\""
    fi
    
    # Step 1: Get root-level files
    log_info "Discovering root-level files..."
    local root_api_url="${API_BASE_URL}/${agent_group}"
    local root_response=$(curl -s -f $auth_header "${root_api_url}" 2>/dev/null)
    local root_api_status=$?
    
    if [[ $root_api_status -eq 0 ]] && [[ -n "$root_response" ]]; then
        # Successfully got root files from API
        # Extract filenames (not directories) from JSON response
        # Look for entries where "type": "file"
        if command -v jq &> /dev/null; then
            # Use jq for reliable JSON parsing
            echo "$root_response" | jq -r '.[] | select(.type == "file") | .name' | while read -r root_file; do
                echo "${agent_group}/${root_file}" >> "${temp_dir}/file_list.txt"
            done
        else
            # Fall back to awk-based parsing
            echo "$root_response" | awk '/"name":/ {name=$0} /"type": "file"/ {print name}' | sed 's/.*"name"[[:space:]]*:[[:space:]]*"//g' | sed 's/".*//g' | while read -r root_file; do
                echo "${agent_group}/${root_file}" >> "${temp_dir}/file_list.txt"
            done
        fi
    else
        # API failed, fall back to hardcoded list
        log_warning "Could not discover root files via API, attempting with common filenames..."
        local root_files=(
            "AGENTGROUPNAME"
            "README.md"
            "CHANGELOG.md"
            "COMMON-PATTERNS.md"
            "UPDATING.md"
            "copilot-instructions.md"
            "update-from-upstream.sh"
        )
        
        for file in "${root_files[@]}"; do
            local url="${RAW_BASE_URL}/${agent_group}/${file}"
            if curl -s -f -I "$url" &>/dev/null; then
                echo "${agent_group}/${file}" >> "${temp_dir}/file_list.txt"
            fi
        done
    fi
    
    # Step 2: Get agents directory
    log_info "Discovering agent files..."
    local agents_api_url="${API_BASE_URL}/${agent_group}/agents"
    local agents_response=$(curl -s -f $auth_header "${agents_api_url}" 2>/dev/null)
    local agents_api_status=$?
    
    if [[ $agents_api_status -eq 0 ]] && [[ -n "$agents_response" ]]; then
        # Successfully got agents from API
        # Extract agent filenames from JSON response
        echo "$agents_response" | grep -o '"name"[[:space:]]*:[[:space:]]*"[^"]*\.agent\.md"' | sed 's/.*"name"[[:space:]]*:[[:space:]]*"//g' | sed 's/"//g' | while read -r agent_file; do
            echo "${agent_group}/agents/${agent_file}" >> "${temp_dir}/file_list.txt"
        done
    else
        # API failed or no agents found, try direct downloads with common agent names
        log_warning "Could not discover all agents via API, attempting with common agent names..."
        local common_agents=(
            "activity-scout"
            "activity-planner"
            "beneficiary-planning"
            "budget-optimizer"
            "code-quality-reviewer"
            "destination-researcher"
            "devils-advocate"
            "dining-specialist"
            "event-coordinator"
            "impact-evaluator"
            "itinerary-integrator"
            "legacy-planning-advisor"
            "letter-of-wishes-composer"
            "portfolio-code-writer"
            "portfolio-strategist"
            "principles-framework-definer"
            "recommendation-synthesizer"
            "risk-opportunity-analyst"
            "team-profiler"
            "trust-structure-designer"
        )
        
        for agent_name in "${common_agents[@]}"; do
            local agent_url="${RAW_BASE_URL}/${agent_group}/agents/${agent_name}.agent.md"
            if curl -s -f -I "$agent_url" &>/dev/null; then
                echo "${agent_group}/agents/${agent_name}.agent.md" >> "${temp_dir}/file_list.txt"
            fi
        done
    fi
    
    if [[ ! -s "${temp_dir}/file_list.txt" ]]; then
        log_error "Could not fetch file list for agent group '${agent_group}'"
        log_error "Please check that the agent group exists in the upstream repository"
        return 1
    fi
    
    return 0
}

# Download a file from upstream
download_file() {
    local upstream_path="$1"
    local output_file="$2"
    
    local url="${RAW_BASE_URL}/${upstream_path}"
    
    # Download to temporary location first
    local temp_file="${output_file}.tmp"
    
    if curl -s -f -o "$temp_file" "$url" 2>/dev/null; then
        mv "$temp_file" "$output_file"
        return 0
    else
        rm -f "$temp_file"
        return 1
    fi
}

# Update agent group files from upstream
update_agent_group() {
    local agent_group="$1"
    local script_dir="$2"
    
    log_info "Updating agent group: ${agent_group}"
    log_info "Current location: ${script_dir}"
    
    # Create temporary directory for tracking
    local temp_dir=$(mktemp -d)
    trap "rm -rf $temp_dir" EXIT
    
    # Get list of files from upstream
    if ! get_upstream_files "$agent_group" "$temp_dir"; then
        log_error "Failed to get file list from upstream"
        exit 1
    fi
    
    log_info "Processing updates..."
    
    local update_count=0
    local new_count=0
    local skip_count=0
    local error_count=0
    
    # Process each file from upstream
    while IFS= read -r upstream_file; do
        # Calculate the target path in current repository
        local rel_file="${upstream_file#$agent_group/}"
        local target_file="${script_dir}/${rel_file}"
        
        # Download file to temp location (preserve directory structure to avoid collisions)
        local temp_download="${temp_dir}/${rel_file}"
        mkdir -p "$(dirname "$temp_download")"
        
        if download_file "$upstream_file" "$temp_download"; then
            # Check if file exists locally
            if [[ -f "$target_file" ]]; then
                # File exists - check if it differs from upstream
                if cmp -s "$temp_download" "$target_file"; then
                    skip_count=$((skip_count + 1))
                else
                    log_info "Updating: ${rel_file}"
                    mkdir -p "$(dirname "$target_file")"
                    cp "$temp_download" "$target_file"
                    update_count=$((update_count + 1))
                fi
            else
                # New file
                log_success "Adding new file: ${rel_file}"
                mkdir -p "$(dirname "$target_file")"
                cp "$temp_download" "$target_file"
                new_count=$((new_count + 1))
            fi
            
            rm -f "$temp_download"
        else
            log_warning "Failed to download: ${upstream_file}"
            error_count=$((error_count + 1))
        fi
    done < "${temp_dir}/file_list.txt"
    
    # Summary
    echo ""
    log_success "Update complete!"
    log_info "Summary:"
    echo "  - New files: ${new_count}"
    echo "  - Updated files: ${update_count}"
    echo "  - Unchanged files: ${skip_count}"
    if [[ $error_count -gt 0 ]]; then
        echo "  - Failed downloads: ${error_count}"
    fi
    echo ""
    
    log_info "Changes have been applied to your local files."
    log_info "Review the changes and commit them if you use version control:"
    echo "  git status"
    echo "  git add ."
    echo "  git commit -m 'Update ${agent_group} agent group from upstream'"
}

# Main script
main() {
    echo ""
    log_info "Agent Group Self-Update Script"
    log_info "==============================="
    echo ""
    
    # Check if curl is available
    check_curl
    
    # Check for GITHUB_TOKEN and inform user about rate limits
    if [[ -z "$GITHUB_TOKEN" ]]; then
        log_warning "GITHUB_TOKEN environment variable not set"
        log_info "GitHub API requests are limited to 60/hour without authentication"
        log_info "To increase the limit, set: export GITHUB_TOKEN=<your-github-token>"
        log_info "Create a token at: https://github.com/settings/tokens"
        echo ""
    fi
    
    # Get script directory
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Detect agent group
    local agent_group=$(detect_agent_group)
    if [[ $? -ne 0 ]]; then
        exit 1
    fi
    log_info "Detected agent group: ${agent_group}"
    
    # Update agent group
    update_agent_group "$agent_group" "$script_dir"
    
    echo ""
    log_success "Update process completed successfully!"
    echo ""
}

# Run main function with error handling
main "$@"
if [[ $? -ne 0 ]]; then
    log_error "Update process failed"
    exit 1
fi
