---
name: Bug report
about: Create a report to help us improve
title: '[BUG] Broken CI and Issues badge links in README'
labels: bug, documentation
assignees: ''
---

**Describe the bug**
The CI and Issues badge links in the README.md file are broken. They point to a non-existent repository URL (package_trial_zenjiro instead of package-trial).

**To Reproduce**
1. View the README.md file
2. Click on the CI or Issues badges
3. Observe 404 error page

**Expected behavior**
Clicking on the badges should navigate to the correct GitHub Actions or Issues pages.

**Actual behavior**
Clicking on the badges leads to a 404 error page because the URLs contain incorrect repository name.

**Code example**
The problematic lines in README.md:
```markdown
[![CI](https://github.com/zenjiro/package_trial_zenjiro/workflows/CI/badge.svg)](https://github.com/zenjiro/package_trial_zenjiro/actions)
[![Issues](https://img.shields.io/github/issues/zenjiro/package_trial_zenjiro)](https://github.com/zenjiro/package_trial_zenjiro/issues)
```

**Proposed solution**
Update the URLs to use the correct repository name:
```markdown
[![CI](https://github.com/zenjiro/package-trial/workflows/CI/badge.svg)](https://github.com/zenjiro/package-trial/actions)
[![Issues](https://img.shields.io/github/issues/zenjiro/package-trial)](https://github.com/zenjiro/package-trial/issues)
```