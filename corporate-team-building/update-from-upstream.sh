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

set -e  # Exit on error

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
}

# Get list of files from upstream using GitHub API
get_upstream_files() {
    local agent_group="$1"
    local temp_dir="$2"
    
    log_info "Fetching file list from upstream..."
    
    # Function to recursively fetch files from a directory
    fetch_directory() {
        local path="$1"
        local api_url="${API_BASE_URL}/${path}"
        
        # Fetch directory contents
        local response=$(curl -s -f "${api_url}" 2>/dev/null)
        
        if [[ $? -ne 0 ]]; then
            return 1
        fi
        
        # Parse JSON response to get files and directories
        echo "$response" | grep -o '"path":"[^"]*"' | sed 's/"path":"//g' | sed 's/"//g' | while read -r item_path; do
            # Get the type of this item
            local item_type=$(echo "$response" | grep -A 2 "\"path\":\"${item_path}\"" | grep '"type"' | sed 's/.*"type":"\([^"]*\)".*/\1/')
            
            if [[ "$item_type" == "file" ]]; then
                echo "$item_path"
            elif [[ "$item_type" == "dir" ]]; then
                fetch_directory "$item_path"
            fi
        done
    }
    
    # Try to fetch files using API
    fetch_directory "$agent_group" > "${temp_dir}/file_list.txt" 2>/dev/null
    
    # If API fetch failed or returned empty, try a simpler approach
    if [[ ! -s "${temp_dir}/file_list.txt" ]]; then
        log_warning "GitHub API approach failed, using alternative method..."
        
        # Download the directory structure from a known structure
        # For agent groups, we know they typically have: agents/, README.md, CHANGELOG.md, etc.
        local common_files=(
            "AGENTGROUPNAME"
            "README.md"
            "CHANGELOG.md"
            "copilot-instructions.md"
            "update-from-upstream.sh"
        )
        
        # Try to download each common file to see if it exists
        for file in "${common_files[@]}"; do
            local url="${RAW_BASE_URL}/${agent_group}/${file}"
            if curl -s -f -I "$url" &>/dev/null; then
                echo "${agent_group}/${file}" >> "${temp_dir}/file_list.txt"
            fi
        done
        
        # Try to get agents directory
        local agents_api_url="${API_BASE_URL}/${agent_group}/agents"
        local agents_response=$(curl -s -f "${agents_api_url}" 2>/dev/null)
        
        if [[ $? -eq 0 ]]; then
            echo "$agents_response" | grep -o '"name":"[^"]*\.agent\.md"' | sed 's/"name":"//g' | sed 's/"//g' | while read -r agent_file; do
                echo "${agent_group}/agents/${agent_file}" >> "${temp_dir}/file_list.txt"
            done
        fi
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
        
        # Download file to temp location
        local temp_download="${temp_dir}/$(basename "$rel_file")"
        
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
    
    # Get script directory
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Detect agent group
    local agent_group=$(detect_agent_group)
    log_info "Detected agent group: ${agent_group}"
    
    # Update agent group
    update_agent_group "$agent_group" "$script_dir"
    
    echo ""
    log_success "Update process completed successfully!"
    echo ""
}

# Run main function
main "$@"
