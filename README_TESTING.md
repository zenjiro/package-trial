# テストガイド / Testing Guide

## 概要 / Overview

このプロジェクトには包括的なテストスイートが含まれており、`add_one`関数の品質と信頼性を確保しています。

This project includes a comprehensive test suite to ensure the quality and reliability of the `add_one` function.

## テスト構造 / Test Structure

```
tests/
├── __init__.py              # テストパッケージ初期化
├── conftest.py             # 共通フィクスチャとpytest設定
├── test_main.py            # メイン機能のテスト
├── test_edge_cases.py      # エッジケースと境界条件テスト
├── test_performance.py     # パフォーマンステスト
└── test_integration.py     # 統合テスト
```

## テストカテゴリ / Test Categories

### 1. 基本機能テスト (test_main.py)
- 正常系テスト（正の整数、負の整数、ゼロ）
- 浮動小数点数テスト
- 型エラーテスト
- パラメータ化テスト

### 2. エッジケーステスト (test_edge_cases.py)
- 非常に大きな数値
- 非常に小さな数値
- 無限大とNaN
- 浮動小数点精度の限界
- 数学的性質の検証

### 3. パフォーマンステスト (test_performance.py)
- 単一呼び出しの性能
- 大量呼び出しの性能
- メモリ効率性

### 4. 統合テスト (test_integration.py)
- パッケージインポート
- モジュール構造
- 関数アクセシビリティ
- クロスモジュール一貫性

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
pytest --cov=src/package_trial_zenjiro --cov-report=term-missing

# HTMLカバレッジレポート生成
pytest --cov=src/package_trial_zenjiro --cov-report=html
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

### カバレッジ目標 / Coverage Goals
- **行カバレッジ**: 90%以上
- **分岐カバレッジ**: 100%（該当する場合）
- **関数カバレッジ**: 100%

### テストケース数 / Test Case Count
- **基本テスト**: 15+ ケース
- **エッジケース**: 10+ ケース
- **パフォーマンステスト**: 5+ ケース
- **統合テスト**: 8+ ケース

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

## 継続的改善 / Continuous Improvement

### 新機能追加時 / When Adding New Features
1. 対応するテストケースを追加
2. カバレッジが90%以上を維持
3. 既存テストが全て通過することを確認

### テストメンテナンス / Test Maintenance
- 定期的なテスト実行
- 失敗したテストの迅速な修正
- テストコードのリファクタリング

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