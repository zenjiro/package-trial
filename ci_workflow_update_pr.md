# Update CI Workflows for Python 3.10+ Support

## Overview

This PR updates the CI workflows to support Python 3.10+ and adds Python 3.13 support. This is a prerequisite for merging PR #8 which updates the Python version requirement from 3.8+ to 3.10+.

## Changes Made

- Updated CI workflows to test only Python 3.10, 3.11, 3.12, and 3.13
- Removed Python 3.8 and 3.9 from test matrices
- Updated documentation to reflect the new Python version requirements
- Fixed character encoding issues in release.yml
- Updated version to 0.0.6
- Added specific Python version classifiers in pyproject.toml

## Testing

- All CI checks should now pass with Python 3.10-3.13
- No functionality changes, only CI configuration updates

## Related PRs

This PR is a prerequisite for PR #8 which updates the Python version requirement from 3.8+ to 3.10+.