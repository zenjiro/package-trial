# Contributing to Package Trial Zenjiro

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git
- pytest and pytest-cov for testing

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/package_trial_zenjiro.git
   cd package_trial_zenjiro
   ```

2. **Install in development mode**
   ```bash
   pip install -e .[test]
   ```

3. **Run tests to ensure everything works**
   ```bash
   PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro
   ```

## 🧪 Testing

### Running Tests
```bash
# Run all tests with coverage
PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro --cov-report=term-missing

# Run specific test file
PYTHONPATH=src python3 -m pytest tests/test_main.py -v

# Generate HTML coverage report
PYTHONPATH=src python3 -m pytest tests/ --cov=src --cov-report=html
```

### Test Requirements
- All tests must pass
- Maintain 100% code coverage
- Add tests for new functionality
- Follow existing test patterns

## 📝 Code Style

### Python Code
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings for functions and classes
- Keep functions simple and focused

### Test Code
- Use descriptive test names that explain what is being tested
- Follow AAA pattern (Arrange, Act, Assert)
- Test both normal and edge cases
- Include error condition testing

## 🔄 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following the style guidelines
   - Add or update tests as needed
   - Update documentation if necessary

3. **Test your changes**
   ```bash
   # Run tests
   PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/package_trial_zenjiro
   
   # Test package build
   python3 -m build
   pip install dist/*.whl --force-reinstall
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

5. **Push and create pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Guidelines
- Provide a clear description of the changes
- Reference any related issues
- Ensure all CI checks pass
- Update documentation if needed
- Add tests for new functionality

## 🐛 Bug Reports

When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce the issue
- Expected vs actual behavior
- Error messages (if any)

## 💡 Feature Requests

For feature requests, please:
- Describe the feature and its use case
- Explain why it would be valuable
- Consider backward compatibility
- Be open to discussion about implementation

## 📋 Development Guidelines

### Adding New Features
1. Discuss the feature in an issue first
2. Keep changes focused and atomic
3. Maintain backward compatibility
4. Add comprehensive tests
5. Update documentation

### Code Review Process
- All changes require review
- Address feedback promptly
- Be respectful in discussions
- Learn from the review process

### CI/CD Guidelines
- **GitHub Actions**: Use latest action versions for security
- **Testing**: All CI tests must pass before merging
- **Security**: Follow security best practices in workflows
- **Release Process**: Use modernized release workflow (softprops/action-gh-release@v1)
- **Documentation**: Update docs when changing CI/CD processes

## 🎯 Project Goals

Remember that this project aims to demonstrate:
- Modern Python packaging practices
- Comprehensive testing strategies
- Quality assurance methodologies
- Documentation best practices
- Open source collaboration

## 📞 Getting Help

- Open an issue for questions
- Check existing documentation
- Review test examples for usage patterns

## 📄 License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

Thank you for contributing! 🎉