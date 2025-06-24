# Package Trial Zenjiro

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-78%20passed-brightgreen.svg)](#testing)
[![CI](https://github.com/zenjiro/package-trial/workflows/CI/badge.svg)](https://github.com/zenjiro/package-trial/actions)
[![Status Checks](https://img.shields.io/badge/status%20checks-enabled-brightgreen.svg)](docs/status_checks.md)
[![Issues](https://img.shields.io/github/issues/zenjiro/package-trial)](https://github.com/zenjiro/package-trial/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

これはPythonパッケージをPyPIに登録するためのテストプロジェクトです。

## 🚀 機能

- **シンプルなAPI**: デモンストレーション用の単一関数 `add_one()`
- **100%テストカバレッジ**: 78のテストケースを含む包括的なテストスイート
- **最新のパッケージング**: `pyproject.toml`とhatchlingビルドバックエンドを使用
- **型サポート**: int、float、complex、Decimal、Fraction型に対応
- **本番環境対応**: エンタープライズレベルのテストと品質保証
- **🆕 強化されたStatus Checks**: 自動PR状況集約とインテリジェントガイダンス
- **最新のCI/CD**: セキュリティスキャンと品質チェックを含む包括的なCI/CDパイプライン
- **自動化されたセキュリティ**: CodeQL、Safety、Bandit、Semgrepによる毎日のセキュリティスキャン
- **品質保証**: 自動コードフォーマット、リンティング、型チェック
- **依存関係管理**: Dependabotによる自動依存関係更新

## 📦 インストール

```bash
# PyPIからインストール（公開後）
pip install package-trial-zenjiro

# ソースからインストール
pip install -e .

# テスト依存関係付きでインストール
pip install -e .[test]

# ビルド済みホイールからインストール
pip install dist/package_trial_zenjiro-0.0.7-py3-none-any.whl
```

## 🔧 使用方法

```python
from package_trial_zenjiro.main import add_one

# 基本的な使用法
result = add_one(5)
print(result)  # 出力: 6

# 様々な数値型に対応
print(add_one(3.14))    # 4.14
print(add_one(-1))      # 0
print(add_one(1+2j))    # (2+2j)
```

## 🧪 テスト

このプロジェクトには**100%コードカバレッジ**の包括的なテストスイートが含まれています。

### テストカテゴリ

- **コア機能** (18テスト): 基本操作と型処理
- **エッジケース** (14テスト): 境界条件と特殊値
- **高度なシナリオ** (21テスト): 複雑な型と数値安定性
- **パフォーマンス** (6テスト): 速度とメモリ効率
- **統合** (9テスト): パッケージ構造とインポート
- **品質保証** (11テスト): コード品質とドキュメント

### テスト実行

```bash
# カバレッジ付きですべてのテストを実行
PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro

# クイックテスト実行
PYTHONPATH=src python3 -m pytest tests/ -q

# HTMLカバレッジレポートを生成
PYTHONPATH=src python3 -m pytest tests/ --cov=src --cov-report=html
```

### テストステータス
- ✅ すべてのテストが成功
- ✅ 100%コードカバレッジ
- ✅ すべてのシナリオをカバーする6つのテストカテゴリ
- ✅ 包括的なエッジケース検証

## 🤖 強化されたStatus Checks

このプロジェクトでは、PRの状況を自動的に集約・分析する高度なStatus Checksシステムを導入しています。

### 主な機能

#### 📊 自動ステータス集約
- 全てのチェック結果をリアルタイムで収集
- 進捗率の自動計算と視覚的表示
- 各チェックの詳細状況を一覧表示

#### 💬 インテリジェントPRコメント
- PRに詳細なステータスレポートを自動投稿
- 失敗したチェックに対する具体的な修正方法を提示
- プッシュのたびに自動更新（スパム防止機能付き）

#### 🎯 アクショナブルガイダンス
```bash
# 失敗時に提示される具体的なコマンド例
black src/ tests/          # コードフォーマット修正
isort src/ tests/          # インポート順序修正
pytest tests/ -v           # ローカルテスト実行
safety check               # セキュリティチェック
```

#### 📈 プロジェクト健全性メトリクス
- **テストカバレッジ**: 100% (目標: 90%)
- **セキュリティスコア**: A+ (脆弱性なし)
- **コード品質**: 高品質 (フォーマット済み・リント済み)

詳細については [Status Checks ドキュメント](docs/status_checks.md) をご覧ください。

> **テスト更新**: このPRでは新しいStatus Checksワークフローの動作をテストしています。

## 📊 プロジェクト構造

```
package_trial_zenjiro/
├── src/package_trial_zenjiro/
│   ├── __init__.py
│   └── main.py                 # コア機能
├── tests/                      # 包括的なテストスイート
│   ├── conftest.py             # 共有フィクスチャ
│   ├── test_main.py            # コアテスト
│   ├── test_edge_cases.py      # エッジケーステスト
│   ├── test_advanced.py        # 高度なシナリオ
│   ├── test_performance.py     # パフォーマンステスト
│   ├── test_integration.py     # 統合テスト
│   └── test_documentation.py   # 品質テスト
├── htmlcov/                    # HTMLカバレッジレポート
├── pyproject.toml              # パッケージ設定
├── README.md                   # このファイル
├── README_TESTING.md           # 詳細なテストガイド
└── LICENSE                     # Apache 2.0ライセンス
```

## 🛠️ 開発

### ステータスチェック

このリポジトリはコード品質と機能性を確保するためにGitHubステータスチェックを使用しています：

- **クイックテスト**: 基本的な機能テスト
- **コード品質**: フォーマット、リンティング、型チェック
- **セキュリティチェック**: 脆弱性スキャン
- **ビルドチェック**: パッケージのビルドとインストール検証
- **Python互換性**: 複数のPythonバージョンでのテスト

詳細については[ステータスチェックのドキュメント](docs/status_checks.md)を参照してください。

### 要件
- Python 3.10+
- pytest (テスト用)
- pytest-cov (カバレッジ用)
- black, isort, flake8 (コード品質用)
- safety, bandit (セキュリティスキャン用)

### 開発環境のセットアップ
```bash
# リポジトリをクローン
git clone <repository-url>
cd package_trial_zenjiro

# 開発モードでインストール
pip install -e .[test]

# テストを実行
PYTHONPATH=src python3 -m pytest tests/
```

### 品質基準
- **テストカバレッジ**: 最低90%（現在100%）
- **テスト合格率**: 100%
- **コードスタイル**: PEP 8準拠
- **ドキュメント**: 包括的なインラインおよび外部ドキュメント

## 🔄 CI/CDパイプライン

### エンタープライズグレードの自動化
当社のCI/CDパイプラインは、最高水準の品質保証を目指した包括的な自動化を提供します：

#### **🧪 継続的インテグレーション**
- **マルチバージョンテスト**: すべてのプッシュ/PRでPython 3.10-3.13のマトリックステスト
- **100%テストカバレッジ**: 完全なカバレッジ検証を備えた78の包括的なテストケース
- **パフォーマンス検証**: 自動化されたパフォーマンスとメモリ効率のテスト
- **ビルド検証**: パッケージのビルドとインストールの検証

#### **🔍 コード品質保証**
- **Black**: 一貫したスタイルでの自動コードフォーマット
- **isort**: 適切なグループ化によるインポート整理（標準ライブラリ → サードパーティ → ローカル）
- **flake8**: PEP 8準拠とエラー検出（現在：0エラー）
- **mypy**: 信頼性向上のための静的型チェック
- **pylint**: 包括的なコード分析と品質メトリクス

#### **🛡️ セキュリティと脆弱性管理**
- **毎日のセキュリティスキャン**: 自動化された脆弱性検出
  - **Safety**: Python依存関係のCVEスキャン
  - **Bandit**: Pythonコードのセキュリティパターン分析
  - **Semgrep**: カスタムセキュリティルールによる静的分析
- **週次CodeQL分析**: GitHubのセマンティックセキュリティ分析
- **自動依存関係更新**: セキュリティパッチを含むDependabotの週次更新

#### **✅ プルリクエスト検証**
- **包括的なチェック**: マージ前にすべての品質ゲートに合格する必要あり
- **メタデータ検証**: PRのタイトルと説明の要件
- **破壊的変更の検出**: 潜在的に破壊的な変更の自動検出
- **セキュリティ検証**: すべてのPRでのマルチツールセキュリティ分析

### 📊 品質メトリクスと基準
- **テスト成功率**: 100%（78/78テスト合格）
- **コードカバレッジ**: 100%（自動的に維持）
- **リンティングエラー**: 0（CIによって強制）
- **セキュリティ脆弱性**: 0（継続的にモニタリング）
- **コード品質スコア**: A+（pylintで検証）

## 📚 ドキュメント

- **[テストガイド](README_TESTING.md)**: 包括的なテストドキュメント
- **[開発ガイドライン](.agent.md)**: 開発のベストプラクティス
- **[APIドキュメント](src/package_trial_zenjiro/main.py)**: 関数のドキュメント

## 🤝 貢献

1. リポジトリをフォーク
2. 機能ブランチを作成
3. 新機能のテストを追加
4. すべてのテストが100%カバレッジで合格することを確認
5. プルリクエストを提出

## 📄 ライセンス

このプロジェクトはApache License 2.0の下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 🎯 プロジェクト目標

このプロジェクトは以下を実証しています：
- 最新のPythonパッケージング手法
- 包括的なテスト戦略
- 品質保証の方法論
- ドキュメントのベストプラクティス
- オープンソースプロジェクト構造

Pythonのパッケージング、テスト、品質保証を学ぶのに最適です！🐍✨
## 🔄 GitHub Actionsのトリガー

GitHub Actionsワークフローは以下のイベントで自動的にトリガーされます：

- **Push**: メインブランチへのプッシュ時
- **Pull Request**: プルリクエスト作成/更新時
- **Schedule**: 毎日のセキュリティスキャン（午前2時UTC）
- **Workflow Dispatch**: 手動トリガー

手動でワークフローを実行するには：
1. リポジトリの「Actions」タブに移動
2. 左側のサイドバーから実行したいワークフロー（CI、Security Scan など）を選択
3. 「Run workflow」ボタンをクリック
4. 必要に応じてブランチを選択し、「Run workflow」をクリック

詳細については[GitHub Actionsのドキュメント](https://docs.github.com/en/actions)を参照してください。
