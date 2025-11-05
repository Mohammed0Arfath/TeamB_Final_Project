# Contributing to BudgetWise AI

First off, thank you for considering contributing to BudgetWise AI! 🎉

It's people like you that make BudgetWise AI such a great tool for personal finance management.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## 🚀 Getting Started

### Types of Contributions

We welcome many types of contributions:

- 🐛 **Bug Reports**: Report issues you encounter
- 💡 **Feature Requests**: Suggest new features or improvements
- 📝 **Documentation**: Improve or add documentation
- 🧪 **Tests**: Add or improve test coverage
- 💻 **Code**: Fix bugs or implement features
- 🎨 **UI/UX**: Improve the user interface
- 📊 **Data**: Contribute datasets or preprocessing improvements
- 🤖 **Models**: Add new forecasting models or improve existing ones

### Before You Contribute

1. Check if the issue already exists in our [Issue Tracker](../../issues)
2. For major changes, open an issue first to discuss your proposal
3. Make sure your contribution aligns with project goals
4. Ensure your code follows our coding standards

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (venv, virtualenv, or conda)

### Setup Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/BudgetWise-AI.git
cd BudgetWise-AI

# 2. Create a virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 5. Verify installation
python -c "import pandas; print('Setup successful!')"

# 6. Run tests
pytest tests/
```

### Project Structure

```
BudgetWise-AI/
├── app/              # Streamlit applications
├── src/              # Core source code
├── scripts/          # Training and utility scripts
├── data/             # Data storage
├── models/           # Trained models
├── tests/            # Test suite
├── docs/             # Documentation
└── utils/            # Utility functions
```

---

## 🎯 How to Contribute

### Reporting Bugs

When reporting bugs, please include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Python version, OS, dependencies
- **Screenshots**: If applicable
- **Error Messages**: Full error traceback

**Bug Report Template**:
```markdown
**Describe the Bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
A clear description of what you expected to happen.

**Environment:**
- OS: [e.g., Windows 10, macOS 13]
- Python Version: [e.g., 3.9.7]
- BudgetWise Version: [e.g., 1.0.0]

**Additional Context**
Add any other context about the problem here.
```

### Suggesting Features

When suggesting features, please include:

- **Use Case**: Why is this feature needed?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other approaches you've considered
- **Additional Context**: Any relevant information

---

## 💻 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line Length**: 100 characters (not 79)
- **Quotes**: Use double quotes for strings
- **Imports**: Use absolute imports, group by standard lib, third-party, local

### Code Formatting

We use **Black** for code formatting:

```bash
# Format code
black app/ src/ scripts/ tests/

# Check formatting
black --check app/ src/
```

### Import Organization

Use **isort** to organize imports:

```bash
# Sort imports
isort app/ src/ scripts/ tests/

# Check import order
isort --check-only app/ src/
```

### Linting

Use **flake8** for linting:

```bash
# Run linting
flake8 app/ src/ scripts/ tests/
```

### Type Hints

Add type hints to function signatures:

```python
def calculate_total(expenses: List[float]) -> float:
    """Calculate total of expenses."""
    return sum(expenses)
```

### Docstrings

Use Google-style docstrings:

```python
def predict_expenses(days: int, model: str) -> Dict[str, Any]:
    """
    Predict future expenses using specified model.
    
    Args:
        days: Number of days to predict
        model: Model name to use for predictions
        
    Returns:
        Dictionary containing predictions and metadata
        
    Raises:
        ValueError: If days is negative or model not found
        
    Example:
        >>> predict_expenses(7, "XGBoost")
        {'predictions': [1000, 1050, ...], 'avg': 1025}
    """
    pass
```

---

## 🧪 Testing Guidelines

### Writing Tests

- Place tests in `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names
- One assertion per test when possible
- Use fixtures for common setup

**Example Test**:

```python
import pytest
from src.data_preprocessing import clean_data

def test_clean_data_removes_nulls():
    """Test that clean_data removes null values."""
    # Arrange
    data = pd.DataFrame({'amount': [100, None, 200]})
    
    # Act
    result = clean_data(data)
    
    # Assert
    assert result['amount'].isna().sum() == 0
    assert len(result) == 2
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov=app

# Run specific test file
pytest tests/test_data_preprocessing.py

# Run specific test
pytest tests/test_data_preprocessing.py::test_clean_data_removes_nulls

# Run with verbose output
pytest -v
```

### Test Coverage

Aim for:
- **Minimum**: 70% coverage
- **Target**: 80%+ coverage
- **Goal**: 90%+ coverage

---

## 📝 Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no code change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(csv-upload): add validation for column names

- Check for all 13 required columns
- Show clear error messages for missing columns
- Add preview of uploaded data

Closes #123

---

fix(predictions): resolve zero predictions issue

- Pass data_source through all prediction methods
- Add validation for zero/NaN historical data
- Improve simulation fallback

Fixes #456
```

---

## 🔄 Pull Request Process

### Before Submitting

1. ✅ Fork the repository
2. ✅ Create a feature branch (`git checkout -b feature/amazing-feature`)
3. ✅ Make your changes
4. ✅ Write/update tests
5. ✅ Ensure tests pass (`pytest`)
6. ✅ Update documentation
7. ✅ Format code (`black`, `isort`)
8. ✅ Lint code (`flake8`)
9. ✅ Commit changes with clear messages
10. ✅ Push to your fork
11. ✅ Open a Pull Request

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings

## Related Issues
Closes #(issue number)
```

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, your PR will be merged
4. Your contribution will be credited in CHANGELOG.md

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

---

## 📧 Questions?

- Open an issue for questions
- Check existing documentation
- Review closed PRs for examples

---

## 🙏 Thank You!

Your contributions make BudgetWise AI better for everyone!

© 2025 Mohammed Arfath - BudgetWise AI
