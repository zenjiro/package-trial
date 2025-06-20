## Description

Fix broken CI and Issues badge links in README.md by updating the repository name from `package_trial_zenjiro` to `package-trial`.

## Type of Change

- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [x] Documentation update
- [ ] Code refactoring
- [ ] Test improvements

## Related Issues

Fixes #(issue number for the broken badge links)

## Changes Made

- [ ] Added/modified functionality in `src/`
- [ ] Added/updated tests in `tests/`
- [x] Updated documentation
- [ ] Updated dependencies in `pyproject.toml`

## Testing

### Test Coverage
- [x] All tests pass locally
- [x] Code coverage remains at 100%
- [ ] Added tests for new functionality
- [ ] Updated existing tests if needed

### Manual Testing
Verified that the updated badge links point to the correct URLs:

```bash
# No code changes were made, only documentation updates
```

## Code Quality

- [x] Code follows PEP 8 style guidelines
- [x] Functions have appropriate docstrings
- [x] Variable and function names are descriptive
- [x] Code is well-commented where necessary

## Documentation

- [x] Updated README.md if needed
- [ ] Updated CONTRIBUTING.md if needed
- [ ] Updated docstrings for new/modified functions
- [ ] Added examples for new features

## Backward Compatibility

- [x] Changes are backward compatible
- [ ] Breaking changes are documented
- [ ] Migration guide provided (if applicable)

## Checklist

- [x] I have read the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines
- [x] My code follows the project's coding standards
- [x] I have performed a self-review of my code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests pass locally with my changes

## Screenshots

Before:
[![CI](https://github.com/zenjiro/package_trial_zenjiro/workflows/CI/badge.svg)](https://github.com/zenjiro/package_trial_zenjiro/actions)
[![Issues](https://img.shields.io/github/issues/zenjiro/package_trial_zenjiro)](https://github.com/zenjiro/package_trial_zenjiro/issues)

After:
[![CI](https://github.com/zenjiro/package-trial/workflows/CI/badge.svg)](https://github.com/zenjiro/package-trial/actions)
[![Issues](https://img.shields.io/github/issues/zenjiro/package-trial)](https://github.com/zenjiro/package-trial/issues)

## Additional Notes

This PR fixes the broken badge links by updating the repository name in the URLs from `package_trial_zenjiro` to `package-trial` to match the actual repository name.