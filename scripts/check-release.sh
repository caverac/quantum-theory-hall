#!/bin/bash
# Script to check if there are releasable changes since the last tag

set -e

echo "Checking for releasable changes..."

# Check if commitizen is available
if ! uv run cz version > /dev/null 2>&1; then
    echo "Error: Commitizen not installed. Run 'uv sync --group dev'"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(uv run cz version --project)
echo "Current version: $CURRENT_VERSION"

# Get the last tag
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")

if [ -z "$LAST_TAG" ]; then
    echo "No previous tags found. First release will be created."
    exit 0
fi

echo "Last tag: $LAST_TAG"

# Check for conventional commits since last tag
echo ""
echo "Conventional commits since $LAST_TAG:"
git log ${LAST_TAG}..HEAD --oneline --grep="^feat" --grep="^fix" --grep="^perf" --grep="^refactor" --grep="^BREAKING CHANGE" --extended-regexp || echo "None found"

echo ""
echo "To create a release, use conventional commits:"
echo "  feat: new feature (minor version bump)"
echo "  fix: bug fix (patch version bump)"
echo "  perf: performance improvement (patch version bump)"
echo "  BREAKING CHANGE: breaking change (major version bump)"
