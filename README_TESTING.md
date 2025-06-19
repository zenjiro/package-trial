# テストガイド / Testing Guide

## 概要 / Overview

このプロジェクトには包括的なテストスイートが含まれており、`add_one`関数の品質と信頼性を確保しています。

This project includes a comprehensive test suite to ensure the quality and reliability of the `add_one` function.

## テスト構造 / Test Structure

```
tests/
├── __init__.py              # テストパッケージ初期化
├── conftest.py             # 共通フィクスチャとpytest設定
├── test_main.py            # メイン機能のテスト (18 cases)
├── test_edge_cases.py      # エッジケースと境界条件テスト (14 cases)
├── test_advanced.py        # 高度なシナリオテスト (21 cases)
├── test_performance.py     # パフォーマンステスト (6 cases)
├── test_integration.py     # 統合テスト (9 cases)
└── test_documentation.py   # コード品質とドキュメントテスト (11 cases)
```

**総テストケース数: 78 (100% passing)**

## テストカテゴリ / Test Categories

### 1. 基本機能テスト (test_main.py) - 18 cases
- 正常系テスト（正の整数、負の整数、ゼロ）
- 浮動小数点数テスト
- 複素数テスト
- 型エラーテスト
- パラメータ化テスト
- 戻り値の型保持テスト

### 2. エッジケーステスト (test_edge_cases.py) - 14 cases
- 非常に大きな数値（10^100レベル）
- 非常に小さな数値（1e-300レベル）
- 無限大とNaN
- 浮動小数点精度の限界
- 数学的性質の検証
- 境界値テスト

### 3. 高度なシナリオテスト (test_advanced.py) - 21 cases
- Decimal型での高精度演算
- Fraction型での分数演算
- Boolean値の処理
- 数値安定性テスト
- 型保持の検証
- カスタム数値クラスのサポート
- スレッドセーフティシミュレーション

### 4. パフォーマンステスト (test_performance.py) - 6 cases
- 単一呼び出しの性能
- 大量呼び出しの性能（100-10,000回）
- メモリ効率性
- スケーラビリティテスト

### 5. 統合テスト (test_integration.py) - 9 cases
- パッケージインポート
- モジュール構造
- 関数アクセシビリティ
- モジュールリロード
- クロスモジュール一貫性
- 様々なコンテキストでの使用

### 6. コード品質・ドキュメントテスト (test_documentation.py) - 11 cases
- 関数シグネチャの検証
- ソースコード品質
- 数学的正確性
- エラーハンドリングの完全性
- パフォーマンス特性
- メモリ効率性
- ドキュメント可用性

## テスト実行方法 / How to Run Tests

### 基本実行 / Basic Execution
```bash
# 仮想環境をアクティベート
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# テスト依存関係をインストール
pip install -e .[test]

# 全テスト実行
pytest

# 詳細出力
pytest -v

# 特定のテストファイル実行
pytest tests/test_main.py
```

### カバレッジ付き実行 / With Coverage
```bash
# カバレッジレポート付きテスト実行
PYTHONPATH=src python3 -m pytest tests/ --cov=src/package_trial_zenjiro --cov-report=term-missing

# HTMLカバレッジレポート生成
PYTHONPATH=src python3 -m pytest tests/ --cov=src/package_trial_zenjiro --cov-report=html

# CI/CDと同じ設定でテスト実行
PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro --cov-report=xml --cov-fail-under=90
```

### 特定のテスト実行 / Running Specific Tests
```bash
# 特定のテストクラス
pytest tests/test_main.py::TestAddOne

# 特定のテストメソッド
pytest tests/test_main.py::TestAddOne::test_add_one_positive_integer

# パターンマッチング
pytest -k "test_add_one_positive"
```

## テスト設定 / Test Configuration

`pyproject.toml`に以下の設定が含まれています：

- **pytest設定**: テストディレクトリ、ファイルパターン、実行オプション
- **カバレッジ設定**: ソースディレクトリ、除外パターン、レポート形式
- **カバレッジ閾値**: 90%以上のカバレッジを要求

## フィクスチャ / Fixtures

`conftest.py`には以下の共通フィクスチャが定義されています：

- `sample_numbers`: 様々なテスト用数値
- `invalid_inputs`: 無効な入力タイプ
- `special_float_values`: 特殊な浮動小数点値

## テスト品質指標 / Test Quality Metrics

### 現在の達成状況 / Current Achievement
- **総テストケース数**: 78 (100% passing)
- **行カバレッジ**: 100% (目標: 90%以上)
- **分岐カバレッジ**: 100% (該当する場合)
- **関数カバレッジ**: 100%
- **テスト成功率**: 100% (78/78)
- **CI/CD統合**: 完全自動化

### カテゴリ別テストケース数 / Test Cases by Category
- **基本機能テスト**: 18 ケース ✅
- **エッジケーステスト**: 14 ケース ✅
- **高度なシナリオテスト**: 21 ケース ✅
- **パフォーマンステスト**: 6 ケース ✅
- **統合テスト**: 9 ケース ✅
- **品質・ドキュメントテスト**: 11 ケース ✅

### CI/CD品質ゲート / CI/CD Quality Gates
- **自動テスト実行**: Python 3.8-3.12 マトリックス
- **コード品質チェック**: Black, isort, flake8 (0 errors)
- **セキュリティスキャン**: Safety, Bandit, Semgrep, CodeQL
- **カバレッジ検証**: 90%以上必須 (現在100%)
- **パフォーマンス検証**: 自動実行時間監視

## ベストプラクティス / Best Practices

### テスト作成時の指針 / Test Creation Guidelines
1. **AAA パターン**: Arrange, Act, Assert
2. **明確な命名**: テスト内容が分かる関数名
3. **独立性**: テスト間の依存関係を避ける
4. **再現性**: 常に同じ結果を返す
5. **適切な粒度**: 1つのテストで1つの機能をテスト

### エラーハンドリングテスト / Error Handling Tests
- 無効な入力タイプに対する`TypeError`
- 境界値での動作確認
- 特殊値（無限大、NaN）の処理

## CI/CD統合 / CI/CD Integration

### 自動化されたテスト実行 / Automated Test Execution
- **プッシュ時**: 全テストスイートが自動実行
- **プルリクエスト時**: 包括的な品質チェック
- **日次**: セキュリティスキャンとパフォーマンステスト
- **週次**: 依存関係更新とCodeQL分析

### 品質ゲート / Quality Gates
```yaml
# CI/CDで実行されるテストコマンド
PYTHONPATH=src python3 -m pytest tests/ -v \
  --cov=src/package_trial_zenjiro \
  --cov-report=xml \
  --cov-fail-under=90
```

### GitHub Actionsワークフロー / GitHub Actions Workflows
- **CI Tests**: 5つのPythonバージョンでマトリックステスト
- **Code Quality**: Black, isort, flake8による品質チェック
- **PR Validation**: プルリクエスト専用の包括的検証
- **Security Scan**: 複数ツールによるセキュリティ分析

## 継続的改善 / Continuous Improvement

### 新機能追加時 / When Adding New Features
1. 対応するテストケースを追加
2. カバレッジが90%以上を維持（現在100%）
3. 既存テストが全て通過することを確認
4. CI/CDパイプラインでの自動検証

### テストメンテナンス / Test Maintenance
- **自動実行**: CI/CDによる継続的テスト実行
- **品質監視**: 自動的な品質メトリクス追跡
- **セキュリティ**: 依存関係の脆弱性自動検出
- **パフォーマンス**: 実行時間の自動監視

## トラブルシューティング / Troubleshooting

### よくある問題 / Common Issues

1. **インポートエラー**
   ```bash
   # パスの問題の場合
   export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
   ```

2. **カバレッジが低い**
   ```bash
   # 詳細なカバレッジレポートを確認
   pytest --cov=src --cov-report=html
   # htmlcov/index.html を開いて詳細を確認
   ```

3. **テストが遅い**
   ```bash
   # 並列実行（pytest-xdistが必要）
   pip install pytest-xdist
   pytest -n auto
   ```

## 参考資料 / References

- [pytest公式ドキュメント](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [Pythonテストのベストプラクティス](https://docs.python-guide.org/writing/tests/)