# Changelog

All notable changes to BudgetWise AI - Personal Expense Forecasting Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-05

### 🎉 Initial Release

#### Added
- **Multi-Model Forecasting System**
  - Baseline models: Linear Regression, ARIMA, Prophet
  - Machine Learning: XGBoost (Champion), Random Forest
  - Deep Learning: LSTM, GRU, Bi-LSTM, CNN-1D
  - Transformer: N-BEATS

- **Interactive Streamlit Dashboard**
  - Real-time expense tracking
  - Model performance comparison
  - Multi-horizon predictions (1-30 days)
  - AI-powered chatbot assistant
  - Comprehensive insights and analytics

- **CSV Upload Feature**
  - Upload custom expense data
  - Column validation (13 required columns)
  - Data preview and summary statistics
  - Sample test CSV generator (100 rows)
  - Validation script for pre-upload checks

- **AI Chatbot Assistant**
  - Spending analysis and breakdown
  - Budget plan creation (50/30/20 rule)
  - Personalized savings tips
  - Trend analysis and forecasting
  - Category-specific insights
  - Natural language conversation

- **Advanced Features**
  - Feature engineering (221 features)
  - Data preprocessing pipeline
  - Model evaluation framework
  - Performance visualization
  - Confidence interval predictions

- **Documentation**
  - Comprehensive README
  - User manuals and guides
  - CSV upload documentation
  - AI chatbot guide
  - Deployment guide
  - Project objectives document
  - Technical reports

#### Fixed
- Zero predictions issue in Linear Regression model
  - Added data source parameter flow
  - Implemented validation for zero/NaN data
  - Added detection for negative predictions
  - Improved simulation fallback
  - Enhanced error messages

- Feature mismatch handling
  - Model expects 221 features, prediction creates 11
  - Automatic fallback to simulation
  - Clear user warnings

#### Technical Details
- **Accuracy**: 85.47% (XGBoost Champion)
- **MAPE**: 14.53% (below 15% target)
- **Data Quality**: 99.5%
- **Models Trained**: 13 total
- **Features Engineered**: 221
- **Startup Time**: 8.5 seconds

#### Known Limitations
- Feature engineering in predictions doesn't match full training pipeline
- Some models fall back to simulation mode
- Deep learning models require TensorFlow (optional dependency)
- Prophet model requires separate installation

---

## [Unreleased]

### Planned Features
- Multi-currency support
- Bank API integrations
- Mobile-responsive design
- Advanced data export (PDF, Excel)
- Proactive spending alerts
- Multi-user support
- Enterprise features

---

## Version History

### Version Numbering
- **Major (1.x.x)**: Breaking changes, major new features
- **Minor (x.1.x)**: New features, backward compatible
- **Patch (x.x.1)**: Bug fixes, minor improvements

### Support
- Latest version: 1.0.0
- Supported versions: 1.0.x
- Python compatibility: 3.8+

---

**Note**: For detailed technical changes, see individual commit messages and pull requests.

© 2025 Mohammed Arfath - BudgetWise AI
