"""
BudgetWise AI - Pytest Configuration and Shared Fixtures

This file contains shared pytest fixtures and configuration for the test suite.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


@pytest.fixture
def sample_expense_data():
    """Generate sample expense data for testing"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'date': dates,
        'groceries': np.random.uniform(100, 500, len(dates)),
        'transportation': np.random.uniform(50, 200, len(dates)),
        'utilities': np.random.uniform(100, 300, len(dates)),
        'entertainment': np.random.uniform(50, 150, len(dates)),
        'healthcare': np.random.uniform(0, 200, len(dates)),
        'dining_out': np.random.uniform(50, 250, len(dates)),
        'shopping': np.random.uniform(100, 400, len(dates)),
        'education': np.random.uniform(0, 300, len(dates)),
        'other': np.random.uniform(50, 200, len(dates))
    }
    
    df = pd.DataFrame(data)
    df['total_daily_expenses'] = df.iloc[:, 1:10].sum(axis=1)
    df['total_weekly_expenses'] = df['total_daily_expenses'].rolling(window=7).sum()
    df['total_monthly_expenses'] = df['total_daily_expenses'].rolling(window=30).sum()
    
    return df


@pytest.fixture
def sample_csv_file(tmp_path, sample_expense_data):
    """Create a temporary CSV file with sample data"""
    csv_path = tmp_path / "test_expenses.csv"
    sample_expense_data.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def invalid_csv_file(tmp_path):
    """Create an invalid CSV file (missing required columns)"""
    data = {
        'date': pd.date_range(start='2024-01-01', periods=10),
        'groceries': np.random.uniform(100, 500, 10),
        'transportation': np.random.uniform(50, 200, 10)
    }
    csv_path = tmp_path / "invalid_expenses.csv"
    pd.DataFrame(data).to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def empty_csv_file(tmp_path):
    """Create an empty CSV file"""
    csv_path = tmp_path / "empty_expenses.csv"
    csv_path.write_text("date,groceries,transportation,utilities,entertainment,healthcare,dining_out,shopping,education,other\n")
    return csv_path


@pytest.fixture
def mock_model_path(tmp_path):
    """Create a mock model directory path"""
    model_dir = tmp_path / "models"
    model_dir.mkdir()
    return model_dir


@pytest.fixture
def expected_columns():
    """List of expected columns in expense data"""
    return [
        'date', 'groceries', 'transportation', 'utilities', 
        'entertainment', 'healthcare', 'dining_out', 'shopping', 
        'education', 'other', 'total_daily_expenses',
        'total_weekly_expenses', 'total_monthly_expenses'
    ]


@pytest.fixture
def sample_predictions():
    """Generate sample prediction data"""
    future_dates = pd.date_range(start='2025-01-01', periods=30, freq='D')
    
    return {
        'date': future_dates,
        'predictions': np.random.uniform(1000, 3000, len(future_dates)),
        'confidence_lower': np.random.uniform(800, 1500, len(future_dates)),
        'confidence_upper': np.random.uniform(1500, 3500, len(future_dates))
    }


@pytest.fixture(autouse=True)
def reset_random_seed():
    """Reset random seed before each test for reproducibility"""
    np.random.seed(42)
    yield


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers"""
    for item in items:
        # Add unit marker to all tests by default
        if "integration" not in item.keywords and "slow" not in item.keywords:
            item.add_marker(pytest.mark.unit)
