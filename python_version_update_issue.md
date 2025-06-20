# Update Python Version Requirement to 3.10+

## 概要 / Overview

Python 3.8のサポート期間が2024年10月に終了するため、パッケージの最小要件をPython 3.10に更新する必要があります。

As Python 3.8 will reach its end of life (EOL) in October 2024, we need to update the minimum Python version requirement for the package to Python 3.10.

## 詳細 / Details

- Python 3.8: 2024年10月にEOL
- Python 3.9: 2025年10月にEOL
- Python 3.10: 2026年10月にEOL

現在の日付（2025年6月20日）では、Python 3.8はすでにEOLを過ぎており、Python 3.9も数ヶ月でEOLを迎えます。セキュリティとメンテナンスの観点から、最小バージョン要件をPython 3.10に更新することを提案します。

Given the current date (June 20, 2025), Python 3.8 has already reached EOL, and Python 3.9 will reach EOL in a few months. From a security and maintenance perspective, I propose updating the minimum version requirement to Python 3.10.

## 変更内容 / Changes Required

1. `pyproject.toml`の`requires-python`を`>=3.10`に更新
2. CI/CDワークフローをPython 3.10, 3.11, 3.12, 3.13をテストするように更新
3. ドキュメント（README.md, CONTRIBUTING.md, README_TESTING.md）を更新
4. バージョンを0.0.6に更新

## メリット / Benefits

- セキュリティの向上（EOLバージョンの排除）
- メンテナンスの簡素化
- Python 3.10の新機能（パターンマッチングなど）の活用可能性
- 将来的な互換性の確保

## 影響 / Impact

- Python 3.8または3.9のみを使用しているユーザーは、Pythonをアップグレードする必要があります
- CI/CDパイプラインが簡素化されます（テスト対象が減少）