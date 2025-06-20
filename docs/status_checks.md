# GitHub Status Checks

This document explains how GitHub Status Checks are configured and used in this repository.

## What are GitHub Status Checks?

GitHub Status Checks are automated tests that run whenever code is pushed to a repository or a pull request is created. They help ensure code quality, test coverage, and other standards are maintained.

## Status Checks in This Repository

This repository uses the following status checks:

### 1. Quick Tests
- Runs basic tests to quickly validate code functionality
- Uses Python 3.10 for testing
- Executed on every pull request

### 2. Code Quality
- Checks code formatting using Black and isort
- Performs linting with flake8
- Runs type checking with mypy
- Ensures consistent code style and quality

### 3. Security Check
- Scans dependencies for known vulnerabilities using safety
- Performs security analysis with bandit
- Identifies potential security issues before they reach production

### 4. Build Check
- Builds the Python package
- Tests installation of the built package
- Verifies the package can be properly installed and used

### 5. Python Compatibility
- Tests the code with multiple Python versions (3.10, 3.11, 3.12, 3.13)
- Ensures compatibility across different Python environments

### 6. Status Summary
- Provides an overall summary of all status checks
- Creates a badge indicating the status of all checks

## Required Status Checks

For pull requests to be merged into the main branch, the following status checks must pass:
- Quick Tests
- Code Quality
- Security Check
- Build Check
- Python Compatibility

## Troubleshooting Failed Checks

If a status check fails:

1. Click on the failed check to view details
2. Review the logs to identify the specific error
3. Make necessary changes to your code
4. Push the changes to update the pull request
5. The status checks will automatically run again

## Adding New Status Checks

To add a new status check:

1. Create or modify a workflow file in `.github/workflows/`
2. Define the new job and its steps
3. Update branch protection rules to require the new check if necessary

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Status Checks API](https://docs.github.com/en/rest/reference/checks)