# BudgetWise AI - Directory Structure

## Overview
This document provides a comprehensive overview of the BudgetWise AI project structure, explaining the purpose of each directory and key files.

## Root Directory Structure

```
BudgetWise_AI/
├── .github/                      # GitHub configuration and templates
│   ├── ISSUE_TEMPLATE/          # Issue templates (bug reports, feature requests)
│   ├── PULL_REQUEST_TEMPLATE.md # Pull request template
│   └── workflows/               # CI/CD workflows (GitHub Actions)
│
├── app/                         # Main application code
│   ├── budgetwise_app.py       # Primary Streamlit application (2093 lines)
│   ├── streamlit_app.py        # Alternative entry point
│   ├── data_loader.py          # Data loading utilities
│   ├── csv_validator.py        # CSV validation module
│   └── __init__.py
│
├── src/                         # Source code for models and utilities
│   ├── models/                 # Model implementations
│   │   ├── baseline_models.py  # ARIMA, Prophet, Moving Average
│   │   ├── ml_models.py        # XGBoost, Random Forest, Linear Regression
│   │   ├── deep_learning_models.py  # LSTM, GRU, Bi-LSTM, CNN-1D
│   │   ├── transformer_models.py    # N-BEATS, Attention models
│   │   └── __init__.py
│   │
│   ├── preprocessing/          # Data preprocessing modules
│   │   ├── data_cleaner.py
│   │   ├── feature_engineering.py
│   │   └── __init__.py
│   │
│   ├── evaluation/             # Model evaluation utilities
│   │   ├── metrics.py
│   │   ├── visualization.py
│   │   └── __init__.py
│   │
│   ├── train_models.py         # Model training script
│   ├── config.py               # Configuration management
│   └── __init__.py
│
├── scripts/                     # Utility scripts
│   ├── data_generation/        # Data generation scripts
│   │   ├── generate_test_csv.py
│   │   ├── Synthetic_Data_Generator.py
│   │   └── __init__.py
│   │
│   ├── validation/             # Validation scripts
│   │   ├── validate_test_csv.py
│   │   └── __init__.py
│   │
│   ├── setup/                  # Setup scripts
│   │   ├── setup_ai_chat.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── tests/                       # Test suite
│   ├── fixtures/               # Test fixtures and mock data
│   │   └── __init__.py
│   │
│   ├── conftest.py             # Pytest configuration and shared fixtures
│   ├── test_data_validation.py # Data validation tests
│   ├── test_models.py          # Model testing (to be created)
│   ├── test_preprocessing.py   # Preprocessing tests (to be created)
│   └── __init__.py
│
├── utils/                       # Utility modules (organized)
│   ├── data/                   # Data utilities
│   │   ├── check_data_stats.py
│   │   ├── test_capping.py
│   │   ├── test_data_loading.py
│   │   └── __init__.py
│   │
│   ├── models/                 # Model utilities
│   │   ├── check_all_models.py
│   │   ├── debug_models.py
│   │   ├── test_streamlit_models.py
│   │   ├── get_model_results.py
│   │   └── __init__.py
│   │
│   ├── validation/             # Validation utilities
│   │   ├── verify_accuracy_metrics.py
│   │   ├── final_verification.py
│   │   └── __init__.py
│   │
│   ├── analysis/               # Analysis utilities
│   │   ├── analyze_daily_aggregation.py
│   │   ├── analyze_amounts.py
│   │   ├── analyze_ml_results.py
│   │   ├── capping_analysis.py
│   │   ├── enhancement_summary.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── data/                        # Data directory
│   ├── raw/                    # Raw data files
│   │   └── .gitkeep
│   ├── processed/              # Processed data files
│   │   └── .gitkeep
│   ├── features/               # Feature files
│   │   └── .gitkeep
│   └── budgetwise_finance_dataset.csv  # Primary dataset
│
├── models/                      # Saved models
│   ├── baseline/               # Baseline models (ARIMA, Prophet)
│   │   └── .gitkeep
│   ├── ml/                     # Machine learning models
│   │   └── .gitkeep
│   ├── deep_learning/          # Deep learning models
│   │   └── .gitkeep
│   └── transformer/            # Transformer models
│       └── .gitkeep
│
├── notebooks/                   # Jupyter notebooks
│   ├── data_Preprocessing.ipynb
│   ├── exploratory_analysis.ipynb  # To be created
│   └── model_experiments.ipynb     # To be created
│
├── docs/                        # Documentation
│   ├── user_guides/            # User documentation
│   │   ├── USER_MANUAL.md
│   │   ├── DEPLOYMENT_GUIDE.md
│   │   └── CSV_UPLOAD_GUIDE.md
│   │
│   ├── developer_guides/       # Developer documentation
│   │   ├── ARCHITECTURE.md
│   │   ├── API_REFERENCE.md   # To be created
│   │   └── MODEL_GUIDE.md     # To be created
│   │
│   ├── troubleshooting/        # Troubleshooting guides
│   │   ├── FIX_ZERO_PREDICTIONS.md
│   │   ├── CSV_UPLOAD_FEATURE_SUMMARY.md
│   │   └── COMMON_ISSUES.md   # To be created
│   │
│   ├── quick_references/       # Quick reference guides
│   │   └── CSV_UPLOAD_QUICK_REF.md
│   │
│   └── images/                 # Documentation images
│       └── architecture_diagram.png  # To be created
│
├── logs/                        # Application logs
│   └── .gitkeep
│
├── reports/                     # Generated reports
│   └── .gitkeep
│
├── .gitignore                   # Git ignore patterns (150+ lines)
├── .env.example                 # Environment variables template
├── README.md                    # Project overview and quick start
├── CHANGELOG.md                 # Version history and release notes
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Community code of conduct
├── LICENSE                      # Project license
├── Makefile                     # Build automation commands
├── requirements-complete.txt    # Production dependencies (25+ packages)
├── requirements-dev.txt         # Development dependencies
├── requirements.txt             # Minimal requirements (backwards compatibility)
├── restructure_project.py       # Project restructuring automation
├── PROJECT_STRUCTURE_ANALYSIS.md  # Comprehensive structure analysis
└── DIRECTORY_STRUCTURE.md      # This file

```

## Directory Purposes

### Application Code (`app/`)
Contains the main Streamlit application and related modules:
- **budgetwise_app.py**: Primary application with 13 forecasting models, CSV upload, AI chatbot
- **data_loader.py**: Data loading and validation utilities
- **csv_validator.py**: CSV file validation with 13-column checking

### Source Code (`src/`)
Core functionality organized by purpose:
- **models/**: Model implementations for all 13 forecasting models
- **preprocessing/**: Data cleaning and feature engineering
- **evaluation/**: Model evaluation metrics and visualization
- **train_models.py**: Training pipeline for all models

### Scripts (`scripts/`)
Utility scripts organized by function:
- **data_generation/**: Generate synthetic test data
- **validation/**: Validate data and model outputs
- **setup/**: Environment and dependency setup

### Tests (`tests/`)
Comprehensive test suite:
- **conftest.py**: Pytest configuration with shared fixtures
- **test_data_validation.py**: Data loading and validation tests
- **fixtures/**: Test data and mock objects
- Target: 70%+ code coverage

### Utilities (`utils/`)
Helper utilities organized by category:
- **data/**: Data manipulation and statistics
- **models/**: Model debugging and result extraction
- **validation/**: Accuracy verification
- **analysis/**: Performance analysis and reporting

### Data (`data/`)
Data storage organized by processing stage:
- **raw/**: Original unprocessed data
- **processed/**: Cleaned and preprocessed data
- **features/**: Engineered feature sets
- **budgetwise_finance_dataset.csv**: Primary dataset (366 days, 13 columns)

### Models (`models/`)
Saved model artifacts organized by type:
- **baseline/**: ARIMA, Prophet, Moving Average models
- **ml/**: XGBoost, Random Forest, Linear Regression models
- **deep_learning/**: LSTM, GRU, Bi-LSTM, CNN-1D models
- **transformer/**: N-BEATS and attention-based models

### Documentation (`docs/`)
Comprehensive documentation organized by audience:
- **user_guides/**: End-user documentation and tutorials
- **developer_guides/**: Technical architecture and API docs
- **troubleshooting/**: Common issues and solutions
- **quick_references/**: Cheat sheets and quick guides

### GitHub Configuration (`.github/`)
GitHub-specific files:
- **ISSUE_TEMPLATE/**: Bug report and feature request templates
- **PULL_REQUEST_TEMPLATE.md**: PR template with checklists
- **workflows/**: CI/CD pipeline configurations (future)

## Key Files

### Configuration Files
- **.gitignore**: Comprehensive ignore patterns (Python, IDEs, data, models, logs)
- **.env.example**: Environment variable template (API keys, paths)
- **requirements-complete.txt**: Full dependency list with versions
- **requirements-dev.txt**: Development tools (pytest, black, flake8)
- **Makefile**: Build automation (install, test, lint, format, run)

### Documentation Files
- **README.md**: Project overview, quick start, features
- **CHANGELOG.md**: Version history with detailed release notes
- **CONTRIBUTING.md**: Contribution guidelines and coding standards
- **CODE_OF_CONDUCT.md**: Community standards and expectations
- **PROJECT_STRUCTURE_ANALYSIS.md**: Comprehensive structure audit and recommendations

### Build/Automation Files
- **restructure_project.py**: Automated project reorganization script
- **Makefile**: Build commands for common tasks

## File Counts by Category

| Category | Count | Description |
|----------|-------|-------------|
| Python Files | 82 | Application code, models, utilities |
| Test Files | 2+ | Pytest test suite (expanding) |
| Documentation | 15+ | User guides, developer docs, references |
| Configuration | 7 | Requirements, gitignore, environment |
| Scripts | 10+ | Utilities for data generation, validation |
| Notebooks | 1+ | Jupyter notebooks for analysis |

## Data Flow

```
Raw Data (CSV) 
    ↓
data_loader.py (Load & Validate)
    ↓
preprocessing/ (Clean & Engineer Features)
    ↓
models/ (Train & Predict)
    ↓
evaluation/ (Calculate Metrics)
    ↓
budgetwise_app.py (Visualize & Present)
```

## Model Organization

### 13 Forecasting Models:
1. **Baseline Models** (3):
   - ARIMA
   - Prophet
   - Moving Average

2. **Machine Learning Models** (3):
   - XGBoost (Champion: 14.53% MAPE)
   - Random Forest
   - Linear Regression

3. **Deep Learning Models** (4):
   - LSTM
   - GRU
   - Bi-LSTM
   - CNN-1D

4. **Transformer Models** (3):
   - N-BEATS
   - Attention-based models
   - Temporal Fusion Transformer

## Quality Standards

### Code Organization
- ✅ Clear separation of concerns (app, src, tests, utils)
- ✅ Modular structure with reusable components
- ✅ Comprehensive documentation in docs/

### Configuration
- ✅ Complete dependency management
- ✅ Environment variable template
- ✅ Git ignore patterns (150+ lines)

### Testing
- 🔄 Test suite structure created
- 🔄 Fixtures and configuration in place
- ⏳ Target: 70%+ code coverage

### Documentation
- ✅ User guides for all major features
- ✅ Troubleshooting documentation
- ⏳ API reference (to be created)
- ⏳ Architecture diagrams (to be created)

## Next Steps

### Immediate (Priority 1)
1. Execute `python restructure_project.py` to reorganize files
2. Run `make test` to validate test suite
3. Update import statements after restructuring

### Short Term (Priority 2)
1. Create additional test files (test_models.py, test_preprocessing.py)
2. Add API documentation
3. Create architecture diagrams

### Long Term (Priority 3)
1. Set up CI/CD workflows
2. Add performance benchmarking
3. Create deployment automation

## Maintenance

This structure document should be updated when:
- New directories are added
- Major files are moved or renamed
- New module categories are created
- Significant structural changes occur

**Last Updated**: 2025-01-05
**Version**: 1.0.0
