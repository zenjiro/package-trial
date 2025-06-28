# Gemini CLI Project Notes

This file contains notes and configurations specific to the Gemini CLI's interaction with this project.

## Project Overview
This is a Python package trial project designed for testing PyPI registration. It uses `pyproject.toml` and hatchling as the build backend.

## Project-Specific Commands

- **Install in development mode:** `pip install -e .`
- **Build the package:** `PYTHONPATH=/home/zenjiro/.local/lib/python3.10/site-packages python3 -m build`
- **Test built package installation:** `pip install dist/package_trial_zenjiro-0.0.1-py3-none-any.whl --user --force-reinstall`
- **Run all tests with coverage:** `PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro`
- **Run quick tests:** `PYTHONPATH=src python3 -m pytest tests/ -q`
- **Generate HTML coverage report:** `PYTHONPATH=src python3 -m pytest tests/ --cov=src --cov-report=html`
- **Check package metadata:** `python -m pip show package_trial_zenjiro`
- **Linting/Type Checking:** `mypy src/` (from previous GEMINI.md)

## Conventions and Best Practices

- **Python Version:** Compatible with Python 3.8+ (previously 3.10 was listed, but 3.8+ is more accurate based on .agent.md).
- **Code Style:** Follows PEP 8.
- **Code Organization:** Main functionality in `src/package_trial_zenjiro/`.
- **Package Management:** Uses `venv/` for virtual environment; dependencies in `pyproject.toml`.
- **Version Management:** Update `pyproject.toml` following semantic versioning (MAJOR.MINOR.PATCH).
- **Testing:** Uses `pytest` for unit and integration tests; test files in `tests/` following `test_*.py` pattern. Achieves 100% code coverage.
- **Documentation:** Use docstrings for functions/classes; update `README.md` for new features.

## Areas of Focus

- **`src/package_trial_zenjiro/main.py`**: Main application logic.
- **`tests/`**: Contains all project tests, with comprehensive coverage (78+ test cases, 100% coverage).
- **`pyproject.toml`**: Project configuration and dependencies.