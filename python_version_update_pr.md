# Update Python Version Requirement to 3.10+

## 概要 / Overview

Python 3.8のサポート期間が2024年10月に終了したため、パッケージの最小要件をPython 3.10に更新しました。

Updated the minimum Python version requirement for the package to Python 3.10 as Python 3.8 reached its end of life (EOL) in October 2024.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [x] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [x] Documentation update
- [ ] Code refactoring
- [ ] Test improvements

## Related Issues

Fixes #7

## 変更内容 / Changes Made

- [x] Updated Python version requirement in `pyproject.toml` from `>=3.8` to `>=3.10`
- [x] Updated CI/CD workflows to test Python 3.10, 3.11, 3.12, and 3.13
- [x] Updated documentation to reflect new Python version requirements
- [x] Updated version to 0.0.6
- [x] Added specific Python version classifiers in `pyproject.toml`

## テスト / Testing

### Test Coverage
- [x] All tests pass locally
- [x] Code coverage remains at 100%
- [ ] Added tests for new functionality
- [ ] Updated existing tests if needed

### Manual Testing
```bash
# Verified package builds and installs correctly with Python 3.10+
python -m build
pip install dist/*.whl --force-reinstall
python -c "from package_trial_zenjiro.main import add_one; print(f'add_one(5) = {add_one(5)}')"
```

## Code Quality

- [x] Code follows PEP 8 style guidelines
- [x] Functions have appropriate docstrings
- [x] Variable and function names are descriptive
- [x] Code is well-commented where necessary

## Documentation

- [x] Updated README.md
- [x] Updated CONTRIBUTING.md
- [x] Updated README_TESTING.md
- [x] Updated RELEASE_NOTES.md

## 後方互換性 / Backward Compatibility

- [ ] Changes are backward compatible
- [x] Breaking changes are documented: Python 3.8 and 3.9 are no longer supported
- [x] Migration guide provided: Users need to upgrade to Python 3.10+

## Checklist

- [x] I have read the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines
- [x] My code follows the project's coding standards
- [x] I have performed a self-review of my code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [x] New and existing unit tests pass locally with my changes

## メリット / Benefits

- セキュリティの向上（EOLバージョンの排除）
- メンテナンスの簡素化
- Python 3.10の新機能（パターンマッチングなど）の活用可能性
- 将来的な互換性の確保

## 影響 / Impact

- Python 3.8または3.9のみを使用しているユーザーは、Pythonをアップグレードする必要があります
- CI/CDパイプラインが簡素化されます（テスト対象が減少）