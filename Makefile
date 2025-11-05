# BudgetWise AI - Makefile
# Build automation for development, testing, and deployment

.PHONY: help install install-dev clean test test-cov lint format check run docs build

# Default target
help:
	@echo "BudgetWise AI - Available Commands"
	@echo "=================================="
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install development dependencies"
	@echo "  make clean          - Remove build artifacts and cache"
	@echo "  make test           - Run tests with pytest"
	@echo "  make test-cov       - Run tests with coverage report"
	@echo "  make lint           - Run code quality checks (flake8, pylint)"
	@echo "  make format         - Format code with Black and isort"
	@echo "  make check          - Run all checks (lint, format-check, test)"
	@echo "  make run            - Run the Streamlit app"
	@echo "  make docs           - Build documentation"
	@echo "  make build          - Build package for distribution"
	@echo "  make restructure    - Reorganize project structure"

# Installation targets
install:
	@echo "Installing production dependencies..."
	pip install -r requirements-complete.txt

install-dev: install
	@echo "Installing development dependencies..."
	pip install -r requirements-dev.txt

# Cleaning targets
clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".coverage" -delete
	rm -rf build/ dist/ htmlcov/ .coverage coverage.xml
	@echo "Clean complete!"

# Testing targets
test:
	@echo "Running tests..."
	pytest tests/ -v

test-cov:
	@echo "Running tests with coverage..."
	pytest tests/ -v --cov=app --cov=src --cov=utils --cov-report=html --cov-report=term

test-fast:
	@echo "Running fast tests only (excluding slow tests)..."
	pytest tests/ -v -m "not slow"

# Code quality targets
lint:
	@echo "Running flake8..."
	flake8 app/ src/ utils/ tests/ --max-line-length=88 --extend-ignore=E203
	@echo "Running pylint..."
	pylint app/ src/ utils/ --max-line-length=88 || true

format:
	@echo "Formatting code with Black..."
	black app/ src/ utils/ tests/
	@echo "Sorting imports with isort..."
	isort app/ src/ utils/ tests/

format-check:
	@echo "Checking code formatting..."
	black app/ src/ utils/ tests/ --check
	isort app/ src/ utils/ tests/ --check-only

type-check:
	@echo "Running type checks with mypy..."
	mypy app/ src/ utils/ --ignore-missing-imports

# Comprehensive check
check: format-check lint type-check test
	@echo "All checks passed!"

# Running targets
run:
	@echo "Starting BudgetWise AI..."
	streamlit run app/budgetwise_app.py

run-alt:
	@echo "Starting BudgetWise AI (alternative entry point)..."
	streamlit run app/streamlit_app.py

# Documentation targets
docs:
	@echo "Building documentation..."
	@echo "Documentation build not yet configured"

# Build targets
build: clean
	@echo "Building package..."
	python -m build

# Project structure
restructure:
	@echo "Restructuring project..."
	python restructure_project.py

# Development setup
setup: install-dev
	@echo "Setting up development environment..."
	@echo "Installing pre-commit hooks..."
	pre-commit install || echo "pre-commit not available"
	@echo "Setup complete!"

# Data generation
generate-data:
	@echo "Generating test data..."
	python scripts/data_generation/generate_test_csv.py

# Model training
train:
	@echo "Training models..."
	python src/train_models.py

# Utility commands
validate:
	@echo "Validating project structure..."
	@test -f README.md || (echo "README.md missing!" && exit 1)
	@test -f requirements-complete.txt || (echo "requirements-complete.txt missing!" && exit 1)
	@test -f .gitignore || (echo ".gitignore missing!" && exit 1)
	@test -d app/ || (echo "app/ directory missing!" && exit 1)
	@test -d tests/ || (echo "tests/ directory missing!" && exit 1)
	@echo "Project structure validated!"

# Quick start for new developers
quickstart: install-dev generate-data
	@echo "========================================"
	@echo "  BudgetWise AI - Quick Start Complete!"
	@echo "========================================"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Review README.md for project overview"
	@echo "  2. Check docs/ for detailed documentation"
	@echo "  3. Run 'make test' to ensure everything works"
	@echo "  4. Run 'make run' to start the application"
	@echo ""
	@echo "Happy coding! 🚀"
