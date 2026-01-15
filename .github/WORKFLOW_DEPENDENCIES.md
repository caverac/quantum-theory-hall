# GitHub Actions Workflow Dependencies

This document describes how the CI/CD workflows in this repository interact.

## Workflows Overview

### 1. CI (`ci.yml`)
**Trigger:** Push to `main`, Pull Requests

Runs quality checks:
- Flake8 (linting)
- Black (formatting)
- Pylint (code analysis)
- Pydocstyle (docstring checking)
- MyPy (type checking)
- Pytest (tests with 100% coverage)

### 2. Release (`release.yml`)
**Trigger:** Push to `main` (excluding bump commits)

Handles semantic versioning:
- Checks for conventional commits since last tag
- Bumps version in `pyproject.toml`
- Updates `CHANGELOG.md`
- Creates git tag and GitHub release

### 3. Docs (`docs.yml`)
**Trigger:** Push to `main`, After successful Release

Builds and deploys documentation:
- Generates assets (plots)
- Builds MkDocs in strict mode
- Deploys to GitHub Pages

## Workflow Dependencies

```
Push to main
    |
    v
+-------+     +----------+
|  CI   |     | Release  |
+-------+     +----------+
                   |
                   v (on success)
              +--------+
              |  Docs  |
              +--------+
```

## Conventional Commits

The release workflow uses [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature (minor version bump)
- `fix:` - Bug fix (patch version bump)
- `perf:` - Performance improvement (patch version bump)
- `refactor:` - Code refactoring (patch version bump)
- `BREAKING CHANGE:` - Breaking change (major version bump)
