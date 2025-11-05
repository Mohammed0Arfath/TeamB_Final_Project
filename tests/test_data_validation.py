"""
BudgetWise AI - Data Validation Tests

Tests for data loading, validation, and preprocessing functions.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime


class TestDataValidation:
    """Test suite for data validation functions"""
    
    def test_sample_data_structure(self, sample_expense_data, expected_columns):
        """Test that sample data has correct structure"""
        assert isinstance(sample_expense_data, pd.DataFrame)
        assert list(sample_expense_data.columns) == expected_columns
        assert len(sample_expense_data) == 366  # Full year including leap day
    
    def test_sample_data_values(self, sample_expense_data):
        """Test that sample data has valid values"""
        # No negative values
        numeric_cols = sample_expense_data.select_dtypes(include=[np.number]).columns
        assert (sample_expense_data[numeric_cols] >= 0).all().all()
        
        # No null values
        assert not sample_expense_data.isnull().any().any()
        
        # Date column is datetime
        assert pd.api.types.is_datetime64_any_dtype(sample_expense_data['date'])
    
    def test_csv_file_creation(self, sample_csv_file):
        """Test that CSV file is created correctly"""
        assert sample_csv_file.exists()
        
        df = pd.read_csv(sample_csv_file)
        assert len(df) == 366
        assert 'date' in df.columns
    
    def test_invalid_csv_detection(self, invalid_csv_file, expected_columns):
        """Test detection of invalid CSV files"""
        df = pd.read_csv(invalid_csv_file)
        
        # Check that required columns are missing
        missing_cols = set(expected_columns) - set(df.columns)
        assert len(missing_cols) > 0
    
    def test_empty_csv_detection(self, empty_csv_file):
        """Test detection of empty CSV files"""
        df = pd.read_csv(empty_csv_file)
        assert len(df) == 0
    
    def test_date_column_validation(self, sample_expense_data):
        """Test date column validation"""
        dates = pd.to_datetime(sample_expense_data['date'])
        
        # Check dates are sorted
        assert dates.is_monotonic_increasing
        
        # Check date range
        assert dates.min() == pd.Timestamp('2024-01-01')
        assert dates.max() == pd.Timestamp('2024-12-31')
    
    def test_total_calculations(self, sample_expense_data):
        """Test that totals are calculated correctly"""
        # Test daily total
        expense_cols = ['groceries', 'transportation', 'utilities', 
                       'entertainment', 'healthcare', 'dining_out', 
                       'shopping', 'education', 'other']
        
        manual_total = sample_expense_data[expense_cols].sum(axis=1)
        assert np.allclose(sample_expense_data['total_daily_expenses'], manual_total)
    
    def test_data_types(self, sample_expense_data):
        """Test that data types are correct"""
        # Date column should be datetime
        assert pd.api.types.is_datetime64_any_dtype(sample_expense_data['date'])
        
        # All other columns should be numeric
        numeric_cols = sample_expense_data.columns.drop('date')
        for col in numeric_cols:
            assert pd.api.types.is_numeric_dtype(sample_expense_data[col])
    
    def test_expense_ranges(self, sample_expense_data):
        """Test that expenses are within expected ranges"""
        # Groceries: 100-500
        assert sample_expense_data['groceries'].min() >= 100
        assert sample_expense_data['groceries'].max() <= 500
        
        # Transportation: 50-200
        assert sample_expense_data['transportation'].min() >= 50
        assert sample_expense_data['transportation'].max() <= 200
    
    @pytest.mark.parametrize("column", [
        'groceries', 'transportation', 'utilities', 
        'entertainment', 'healthcare', 'dining_out', 
        'shopping', 'education', 'other'
    ])
    def test_individual_columns_exist(self, sample_expense_data, column):
        """Test that each expense column exists"""
        assert column in sample_expense_data.columns
        assert len(sample_expense_data[column]) == 366


class TestDataPreprocessing:
    """Test suite for data preprocessing functions"""
    
    def test_missing_value_handling(self, sample_expense_data):
        """Test handling of missing values"""
        # Introduce missing values
        data_with_na = sample_expense_data.copy()
        data_with_na.loc[0, 'groceries'] = np.nan
        
        # Verify missing value is detected
        assert data_with_na['groceries'].isnull().any()
    
    def test_outlier_detection(self, sample_expense_data):
        """Test outlier detection in expense data"""
        # Add an outlier
        data_with_outlier = sample_expense_data.copy()
        data_with_outlier.loc[0, 'groceries'] = 10000  # Extreme value
        
        # Calculate z-score
        mean = data_with_outlier['groceries'].mean()
        std = data_with_outlier['groceries'].std()
        z_scores = np.abs((data_with_outlier['groceries'] - mean) / std)
        
        # Verify outlier is detected (z-score > 3)
        assert (z_scores > 3).any()
    
    def test_date_parsing(self):
        """Test date parsing from different formats"""
        date_formats = [
            '2024-01-01',
            '01/01/2024',
            '2024-01-01 00:00:00'
        ]
        
        for date_str in date_formats:
            try:
                parsed = pd.to_datetime(date_str)
                assert isinstance(parsed, pd.Timestamp)
            except Exception:
                pytest.fail(f"Failed to parse date: {date_str}")
    
    def test_data_normalization(self, sample_expense_data):
        """Test data normalization"""
        # Test min-max normalization
        col = 'groceries'
        normalized = (sample_expense_data[col] - sample_expense_data[col].min()) / \
                    (sample_expense_data[col].max() - sample_expense_data[col].min())
        
        assert normalized.min() >= 0
        assert normalized.max() <= 1


@pytest.mark.integration
class TestDataIntegration:
    """Integration tests for data pipeline"""
    
    def test_full_data_pipeline(self, sample_csv_file, expected_columns):
        """Test complete data loading and validation pipeline"""
        # Load data
        df = pd.read_csv(sample_csv_file)
        
        # Validate structure
        assert list(df.columns) == expected_columns
        
        # Parse dates
        df['date'] = pd.to_datetime(df['date'])
        
        # Validate data quality
        assert not df.isnull().any().any()
        assert (df.select_dtypes(include=[np.number]) >= 0).all().all()
        
        # Calculate statistics
        stats = df.describe()
        assert stats is not None
