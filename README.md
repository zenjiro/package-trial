# Package Trial Zenjiro

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](htmlcov/index.html)
[![Tests](https://img.shields.io/badge/tests-78%20passed-brightgreen.svg)](#testing)

これはPythonパッケージをPyPIに登録するためのテストプロジェクトです。

This is a Python package trial project designed for testing PyPI registration with comprehensive test coverage and modern packaging standards.

## 🚀 Features / 機能

- **Simple API**: Single function `add_one()` for demonstration
- **100% Test Coverage**: Comprehensive test suite with 78 test cases
- **Modern Packaging**: Uses `pyproject.toml` and hatchling build backend
- **Type Support**: Works with int, float, complex, Decimal, Fraction types
- **Production Ready**: Enterprise-level testing and quality assurance

## 📦 Installation / インストール

```bash
# Install from source
pip install -e .

# Install with test dependencies
pip install -e .[test]
```

## 🔧 Usage / 使用方法

```python
from package_trial_zenjiro.main import add_one

# Basic usage
result = add_one(5)
print(result)  # Output: 6

# Works with different number types
print(add_one(3.14))    # 4.14
print(add_one(-1))      # 0
print(add_one(1+2j))    # (2+2j)
```

## 🧪 Testing / テスト

This project includes a comprehensive test suite with **100% code coverage**.

### Test Categories

- **Core Functionality** (18 tests): Basic operations and type handling
- **Edge Cases** (14 tests): Boundary conditions and special values
- **Advanced Scenarios** (21 tests): Complex types and numerical stability
- **Performance** (6 tests): Speed and memory efficiency
- **Integration** (9 tests): Package structure and imports
- **Quality Assurance** (11 tests): Code quality and documentation

### Running Tests

```bash
# Run all tests with coverage
PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro

# Quick test run
PYTHONPATH=src python3 -m pytest tests/ -q

# Generate HTML coverage report
PYTHONPATH=src python3 -m pytest tests/ --cov=src --cov-report=html
```

### Test Status
- ✅ All tests passing
- ✅ 100% code coverage
- ✅ 6 test categories covering all scenarios
- ✅ Comprehensive edge case validation

## 📊 Project Structure / プロジェクト構造

```
package_trial_zenjiro/
├── src/package_trial_zenjiro/
│   ├── __init__.py
│   └── main.py              # Core functionality
├── tests/                   # Comprehensive test suite
│   ├── conftest.py         # Shared fixtures
│   ├── test_main.py        # Core tests
│   ├── test_edge_cases.py  # Edge case tests
│   ├── test_advanced.py    # Advanced scenarios
│   ├── test_performance.py # Performance tests
│   ├── test_integration.py # Integration tests
│   └── test_documentation.py # Quality tests
├── htmlcov/                # HTML coverage reports
├── pyproject.toml          # Package configuration
├── README.md               # This file
├── README_TESTING.md       # Detailed testing guide
└── LICENSE                 # Apache 2.0 License
```

## 🛠️ Development / 開発

### Requirements
- Python 3.11+
- pytest (for testing)
- pytest-cov (for coverage)

### Setup Development Environment
```bash
# Clone the repository
git clone <repository-url>
cd package_trial_zenjiro

# Install in development mode
pip install -e .[test]

# Run tests
PYTHONPATH=src python3 -m pytest tests/
```

### Quality Standards
- **Test Coverage**: Minimum 90% (Currently 100%)
- **Test Pass Rate**: 100%
- **Code Style**: PEP 8 compliant
- **Documentation**: Comprehensive inline and external docs

## 📚 Documentation / ドキュメント

- **[Testing Guide](README_TESTING.md)**: Comprehensive testing documentation
- **[Development Guidelines](.agent.md)**: Development best practices
- **[API Documentation](src/package_trial_zenjiro/main.py)**: Function documentation

## 🤝 Contributing / 貢献

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass with 100% coverage
5. Submit a pull request

## 📄 License / ライセンス

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🎯 Project Goals / プロジェクト目標

This project demonstrates:
- Modern Python packaging practices
- Comprehensive testing strategies
- Quality assurance methodologies
- Documentation best practices
- Open source project structure

Perfect for learning Python packaging, testing, and quality assurance! 🐍✨
