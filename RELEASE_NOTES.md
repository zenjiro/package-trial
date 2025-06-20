# Release Notes

## Version 0.0.5 (Latest) - 2024-06-18

### 🔧 CI/CD Improvements
- **Modernized GitHub Actions**: Replaced deprecated actions with latest versions
  - `actions/create-release@v1` → `softprops/action-gh-release@v1`
  - Removed deprecated `actions/upload-release-asset@v1`
- **Enhanced Security**: Updated to latest action versions with improved security
- **Improved Release Process**: Streamlined asset upload with better file handling
- **Updated Documentation**: Comprehensive documentation updates

### 🛡️ Security Updates
- Updated supported versions in SECURITY.md
- Removed support for v0.0.1 (security reasons)
- Added support for v0.0.2, v0.0.3, v0.0.4, v0.0.5

### 📦 Package Updates
- Version bump to 0.0.5
- Maintained 100% test coverage
- All 78 test cases passing

## Version 0.0.4 - 2024-06-18

### 🧪 Testing Release
- Created for testing CI/CD workflow improvements
- Verified PyPI production publishing removal
- Validated release process functionality

## Previous Versions

### Version 0.0.3
- Enhanced testing framework
- Improved package structure

### Version 0.0.2
- Initial comprehensive testing implementation
- 100% code coverage achieved

### Version 0.0.1
- Initial release (deprecated for security reasons)

## How to Create a Release

### 1. Automatic Release (Recommended)
```bash
# Create and push a version tag
git tag v0.0.5
git push origin v0.0.5
```

### 2. Manual Release
```bash
# Use GitHub CLI
gh workflow run release.yml -f version=v0.0.5
```

### 3. Release Process
When a tag is pushed:
1. ✅ **Tests run** on all Python versions (3.10-3.13)
2. ✅ **Security scan** with safety
3. ✅ **Package builds** (wheel + source distribution)
4. ✅ **Installation test** verifies the package works
5. ✅ **GitHub Release** created with modern actions (softprops/action-gh-release@v1)
6. ✅ **Release assets** uploaded with improved file handling
7. ✅ **PyPI upload** (Test PyPI only - production publishing removed for safety)

### 4. PyPI Setup Required
Add these secrets to your GitHub repository:
- `TEST_PYPI_API_TOKEN`: Token for test.pypi.org
- `PYPI_API_TOKEN`: Token for pypi.org

### 5. Version Bumping
Update version in `pyproject.toml` before creating release:
```toml
version = "0.0.5"  # Update this
```

## Release Checklist
- [ ] Update version in `pyproject.toml`
- [ ] Update `README.md` if needed
- [ ] All tests passing locally
- [ ] Commit and push changes
- [ ] Create and push version tag
- [ ] Verify release workflow completes
- [ ] Check PyPI upload success