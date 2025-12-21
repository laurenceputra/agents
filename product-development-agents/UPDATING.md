# Updating Your Agent Group

This agent group includes a self-update script that allows you to pull the latest changes from the upstream repository.

## Quick Start

```bash
./update-from-upstream.sh
```

This will:
1. Fetch the latest files from the [laurenceputra/agents](https://github.com/laurenceputra/agents) repository
2. Compare them with your local versions
3. Update changed files, add new files, and preserve unchanged files
4. Skip updating the update script itself (to preserve your local version)
5. Show a summary of changes made

## Setup & Configuration

### Basic Usage

The script reads your agent group name from the `AGENTGROUPNAME` file and uses it to fetch updates.

### GitHub API Rate Limits

By default, GitHub allows 60 API requests per hour for unauthenticated requests. For agent groups with many agents, this may not be sufficient.

**To increase your limit to 5,000 requests per hour**, create a GitHub personal access token and set it before running the script:

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
./update-from-upstream.sh
```

**How to create a token:**
1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Check the `public_repo` scope
4. Generate and copy the token
5. Set the environment variable as shown above

## Portable Usage: Using in Other Repositories

This agent group is designed to be portable. You can copy it into other repositories and it will update itself.

### Copy to Your Project

```bash
# Copy the entire agent group into your project's .github directory
cp -r ../agents/agent-group ./.github

# Run the update script from your project
cd .github
./update-from-upstream.sh
```

The script will:
- Automatically detect the agent group name from `AGENTGROUPNAME`
- Work from any location (uses relative paths, not hardcoded paths)
- Update all agent files from the upstream repository
- Preserve any local modifications you've made to other files

### One-Time Setup After Copying

After copying the agent group to `./.github/agent-group`, ensure the update script is executable:

```bash
chmod +x .github/agent-group/update-from-upstream.sh
```

## Workflow: Keeping Your Copy Updated

### Periodic Updates

Run the script regularly to stay up-to-date with upstream changes:

```bash
cd ./.github/agent-group
./update-from-upstream.sh
git status
git add .
git commit -m "Update agent group from upstream"
git push
```

### Before Running Updates

1. **Commit local changes**: Ensure your repository is clean before updating
   ```bash
   git status
   git commit -am "Save local changes"
   ```

2. **Review the update script version**: The script is intentionally not auto-updated (to preserve your version)
   - Check the original at: https://github.com/laurenceputra/agents/blob/main/{agent-group-name}/update-from-upstream.sh
   - If you want the latest script, copy it manually

### After Running Updates

1. **Review changes**:
   ```bash
   git diff
   git status
   ```

2. **Test the agents**:
   - Verify that agents still work as expected
   - Test any new agents added
   - Check for breaking changes in agent specifications

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update {agent-group-name} from upstream"
   git push
   ```

## What Gets Updated

The script updates:
- ✅ Agent definitions (`.agent.md` files)
- ✅ Documentation (README.md, CHANGELOG.md, copilot-instructions.md)
- ✅ Configuration files (AGENTGROUPNAME)
- ✅ The update script itself (`update-from-upstream.sh`)

### Auto-Updating the Update Script

The update script now automatically updates itself when you run it. This ensures you always have the latest version with bug fixes and improvements.

**What happens when the script updates itself:**
1. The currently running script downloads the latest version
2. It replaces itself with the new version
3. The old code in memory continues executing (this is safe)
4. The new version will be used on the next run

If you've made local customizations to `update-from-upstream.sh`, they will be overwritten. To preserve custom versions:
1. Create a separate script file (e.g., `update-custom.sh`)
2. Or use version control to track your changes and rebase them after updates

## Troubleshooting

### "Could not fetch file list"

**Cause**: GitHub API is unreachable or rate-limited

**Solutions**:
- Check internet connection
- Set `GITHUB_TOKEN` environment variable for higher rate limits
- Wait an hour and try again (if you hit the 60-request limit)
- Check your GitHub token is valid

### "AGENTGROUPNAME file not found"

**Cause**: The script is in the wrong directory or AGENTGROUPNAME is missing

**Solutions**:
- Ensure you run the script from the agent group directory
- Verify AGENTGROUPNAME file exists in the same directory as the script
- The file should contain only the agent group name (e.g., `corporate-team-building`)

### Script fails during download

**Cause**: Specific file can't be downloaded (network issue, file deleted upstream)

**Solutions**:
- The script continues even if individual files fail to download
- Check the summary at the end to see which files failed
- Try running again - transient network issues often resolve on retry
- If a file is consistently missing, check if it was deleted upstream

### My local changes are being overwritten

This is expected behavior! The script overwrites all files except `update-from-upstream.sh` itself.

**Best practices**:
- Don't modify agent definitions (`.agent.md` files) unless coordinating with upstream
- Use local branches or forks for experimental modifications
- Document local customizations in your own files outside the agent group
- Consider contributing valuable changes back upstream

## File Discovery Details

The script discovers files in this order:

1. **Root-level files** (via HTTP HEAD requests):
   - AGENTGROUPNAME
   - README.md
   - CHANGELOG.md
   - copilot-instructions.md
   - update-from-upstream.sh

2. **Agent files** (via GitHub API):
   - Queries `/agents` directory in the remote repository
   - Falls back to checking common agent names if API fails
   - Supports any `.agent.md` file (not limited to predefined names)

## Requirements

- **curl**: Required for downloading files and GitHub API calls
- **bash**: Script requires bash 4.0+
- **jq**: Optional (JSON parsing is available without it, but slower)
- **Internet connection**: Required to access the GitHub repository
- **GitHub token**: Optional (recommended for large agent groups)

## More Information

- [Agent Group Portability Guide](https://github.com/laurenceputra/agents/blob/main/PORTABILITY.md)
- [Repository](https://github.com/laurenceputra/agents)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
