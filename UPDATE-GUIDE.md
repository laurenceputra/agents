# Agent Group Update Guide

This guide explains how to use the self-updating scripts included in each agent group to pull updates from the upstream repository.

## Overview

Each agent group in this repository includes a self-updating bash script (`update-from-upstream.sh`) that:
- Reads the agent group name from the `AGENTGROUPNAME` file
- Downloads the latest files directly from the upstream repository (`https://github.com/laurenceputra/agents`)
- Selectively updates only the files for that specific agent group
- Updates all files including the update script itself
- Provides a clear summary of what changed
- Works without requiring git operations or adding remotes

## Quick Start

To update an agent group, simply navigate to its directory and run the update script:

```bash
cd path/to/agent-group-name
./update-from-upstream.sh
```

## Detailed Usage

### Prerequisites

- The agent group must have an `AGENTGROUPNAME` file containing the group name
- `curl` must be installed and available in your PATH
- You must have network access to `https://raw.githubusercontent.com` and `https://api.github.com`

### Step-by-Step Update Process

1. **Navigate to the agent group directory:**
   ```bash
   cd recommendation-letter  # or any other agent group
   ```

2. **Run the update script:**
   ```bash
   ./update-from-upstream.sh
   ```

3. **Review the output:**
   The script will show:
   - Agent group detected
   - Upstream remote setup status
   - Files being updated
   - Summary of changes (new, updated, unchanged files)
   - Git status showing modified files

4. **Review the changes:**
   ```bash
   git status              # See what files changed
   git diff                # See detailed changes
   git diff --stat         # See change summary
   ```

5. **Commit the updates (if satisfied):**
   ```bash
   git add .
   git commit -m "Update agent-group-name from upstream"
   ```

## What Gets Updated

The script updates:
- ✅ Agent definition files (`agents/*.agent.md`)
- ✅ Documentation files (`README.md`, `CHANGELOG.md`, `copilot-instructions.md`)
- ✅ The update script itself (`update-from-upstream.sh`)
- ✅ The `AGENTGROUPNAME` file
- ✅ Any other files in the agent group directory

The script **does not** update:
- ❌ Files outside the agent group directory
- ❌ Files not present in the upstream repository

## Update Behavior

### New Files

When a file exists in upstream but not locally, the script will:
- Add it to your local directory
- Log it as a "new file"
- Leave it unstaged for your review

### Modified Files

When a file exists both locally and upstream but differs, the script will:
- Overwrite the local file with the upstream version
- Log it as an "updated file"
- Leave the change unstaged for your review

⚠️ **Warning:** Local modifications to agent files will be overwritten. See "Preserving Local Customizations" below.

### Unchanged Files

When a file matches the upstream version, the script will:
- Skip the file (no action taken)
- Count it as "unchanged"
- Not touch the file at all

### Deleted Files

When a file exists in upstream but was deleted locally:
- The script will restore it from upstream
- It will be counted as a "new file"
- You'll need to stage and commit if you want to keep it

## Preserving Local Customizations

If you've made local modifications to agent files that you want to preserve:

### Option 1: Use a Different Branch
```bash
git checkout -b my-custom-agents
# Make your customizations
git commit -m "Add local customizations"

# Later, to update:
git checkout main
./update-from-upstream.sh
git add . && git commit -m "Update from upstream"
git checkout my-custom-agents
git rebase main  # or merge main
# Resolve any conflicts
```

### Option 2: Use Different File Names
```bash
# Instead of modifying recommendation-writer.agent.md
# Create a new file:
cp agents/recommendation-writer.agent.md agents/my-custom-writer.agent.md
# Edit my-custom-writer.agent.md with your changes
# The update script won't touch your custom file
```

### Option 3: Use Git Stash
```bash
# Before updating:
git stash push -m "My local customizations"
./update-from-upstream.sh
git add . && git commit -m "Update from upstream"
git stash pop
# Resolve any conflicts between your changes and updates
```

## Examples

### Example 1: First-Time Setup

```bash
# Clone the agent group to your project
cp -r /path/to/agents/recommendation-letter .github/

# Initialize git if needed
cd .github/recommendation-letter
git init
git add .
git commit -m "Add recommendation-letter agent group"

# Later, to update:
./update-from-upstream.sh
git add .
git commit -m "Update recommendation-letter from upstream"
```

### Example 2: Regular Update

```bash
cd .github/recommendation-letter
./update-from-upstream.sh

# Output shows:
# [SUCCESS] Update complete!
# [INFO] Summary:
#   - New files: 1
#   - Updated files: 2
#   - Unchanged files: 5

git diff                  # Review changes
git add .
git commit -m "Update recommendation-letter: add new reviewer features"
```

### Example 3: Update with Local Changes

```bash
cd .github/recommendation-letter
git status
# On branch main
# Changes not staged for commit:
#   modified:   agents/recommendation-writer.agent.md

./update-from-upstream.sh
# Your local changes to recommendation-writer.agent.md will be overwritten!

# If you want to keep your changes:
git stash
./update-from-upstream.sh
git add .
git commit -m "Update from upstream"
git stash pop  # Reapply your changes
```

## Troubleshooting

### "Not a git repository"

**Problem:** The script reports "Not a git repository"

**Solution:**
```bash
cd path/to/agent-group
git init
git add .
git commit -m "Initial commit"
./update-from-upstream.sh
```

### "Agent group 'X' not found in upstream repository"

**Problem:** The script can't find your agent group in the upstream repo

**Possible causes:**
1. The agent group name doesn't match upstream (check the folder name)
2. The agent group is custom and doesn't exist in upstream
3. Network issues prevented fetching from upstream

**Solution:**
- Verify the folder name matches an agent group in `https://github.com/laurenceputra/agents`
- Check your network connection
- Ensure you can access GitHub

### "Remote 'agents-upstream' already exists"

**Not a problem:** This is informational. The script reuses the existing remote.

### "Permission denied (publickey)"

**Problem:** Can't access the upstream repository

**Solution:** The script uses HTTPS, not SSH, so this shouldn't happen. If it does:
```bash
git remote remove agents-upstream
# Run the script again to recreate the remote with HTTPS
./update-from-upstream.sh
```

### Script shows "0 new, 0 updated, 0 unchanged"

**Problem:** Script appears to do nothing

**Possible causes:**
1. You're already up to date
2. The upstream remote hasn't been fetched properly
3. The agent group path doesn't match upstream

**Solution:**
```bash
git remote remove agents-upstream
./update-from-upstream.sh  # Will re-fetch everything
```

## Best Practices

1. **Update regularly:** Run the update script periodically (weekly/monthly) to get bug fixes and improvements

2. **Review before committing:** Always review changes with `git diff` before committing updates

3. **Keep a clean working tree:** Commit or stash local changes before running updates

4. **Test after updating:** If your project uses the agents, test them after updating to ensure compatibility

5. **Read the CHANGELOG:** After updating, check `CHANGELOG.md` for breaking changes or important notes

6. **Backup before major updates:** If the agent group reports a major version bump (e.g., 1.x → 2.x), backup your current version first

## Available Agent Groups

The following agent groups include update scripts:

- `corporate-team-building` - Corporate team building planning
- `holiday-itinerary-planning` - Holiday and travel itinerary planning
- `legacy-planning` - Estate and legacy planning
- `philanthropic-advisory` - Philanthropic investment advisory
- `portfolio-analysis` - Investment portfolio analysis
- `product-development-agents` - Software product development
- `recommendation-letter` - Recommendation letter writing
- `social-media-team` - Social media content planning
- `stock-investment-analysis` - Stock investment analysis

## Script Internals

For those interested in how the script works:

1. **Reads agent group name:** Reads the group name from the `AGENTGROUPNAME` file in the script's directory
2. **Fetches file list:** Uses GitHub API to get the list of files in the agent group from upstream
3. **Downloads files:** Uses `curl` to download each file from `https://raw.githubusercontent.com/laurenceputra/agents/main/`
4. **Compares and updates:** For each upstream file:
   - If it doesn't exist locally → add as new file
   - If it exists but differs → overwrite with upstream version
   - If it exists and matches → skip (no action)
5. **Updates all files:** Including the update script itself and AGENTGROUPNAME
6. **Shows summary:** Displays counts of new, updated, and unchanged files

## Related Documentation

- **PORTABILITY.md** - Complete guide to portable agent groups
- **README.md** (in each agent group) - Usage guide for that specific agent group
- **CHANGELOG.md** (in each agent group) - Version history and change notes

## Support

For issues with the update script:
1. Check this guide's Troubleshooting section
2. Verify you can access `https://github.com/laurenceputra/agents`
3. Check the script syntax: `bash -n update-from-upstream.sh`
4. Report issues to the repository maintainer

---

**Version:** 1.0.0  
**Last Updated:** 2024-12-21
