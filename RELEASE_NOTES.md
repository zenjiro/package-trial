# Release Notes

## How to Create a Release

### 1. Automatic Release (Recommended)
```bash
# Create and push a version tag
git tag v0.0.2
git push origin v0.0.2
```

### 2. Manual Release
```bash
# Use GitHub CLI
gh workflow run release.yml -f version=v0.0.2
```

### 3. Release Process
When a tag is pushed:
1. ✅ **Tests run** on all Python versions (3.8-3.12)
2. ✅ **Security scan** with safety
3. ✅ **Package builds** (wheel + source distribution)
4. ✅ **Installation test** verifies the package works
5. ✅ **GitHub Release** created with artifacts
6. ✅ **PyPI upload** (Test PyPI first, then production)

### 4. PyPI Setup Required
Add these secrets to your GitHub repository:
- `TEST_PYPI_API_TOKEN`: Token for test.pypi.org
- `PYPI_API_TOKEN`: Token for pypi.org

### 5. Version Bumping
Update version in `pyproject.toml` before creating release:
```toml
version = "0.0.2"  # Update this
```

## Release Checklist
- [ ] Update version in `pyproject.toml`
- [ ] Update `README.md` if needed
- [ ] All tests passing locally
- [ ] Commit and push changes
- [ ] Create and push version tag
- [ ] Verify release workflow completes
- [ ] Check PyPI upload success