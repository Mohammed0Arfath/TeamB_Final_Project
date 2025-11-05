# 🚀 BudgetWise AI - Quick Start Guide

Get BudgetWise AI up and running in 5 minutes!

---

## ⚡ Super Quick Start (3 Commands)

```powershell
# 1. Install dependencies
pip install -r requirements-complete.txt

# 2. Run the application
streamlit run app/budgetwise_app.py

# 3. Open browser to http://localhost:8501
```

Done! The app is now running. 🎉

---

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.8+** installed
  ```powershell
  python --version  # Should show Python 3.8 or higher
  ```

- ✅ **pip** (Python package installer)
  ```powershell
  pip --version
  ```

- ✅ **Git** (optional, for cloning)
  ```powershell
  git --version
  ```

---

## 🎯 Step-by-Step Setup

### Step 1: Get the Code

**Option A: Clone from Git**
```powershell
git clone <repository-url>
cd BudgetWise_AI
```

**Option B: Already have the code?**
```powershell
cd c:\Users\moham\Infosys
```

### Step 2: Create Virtual Environment (Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows PowerShell

# You should see (venv) in your prompt now
```

### Step 3: Install Dependencies

**Option A: Using Makefile (Recommended)**
```powershell
make install
```

**Option B: Using pip directly**
```powershell
pip install -r requirements-complete.txt
```

This installs 25+ packages including:
- Streamlit (web interface)
- XGBoost, LightGBM (ML models)
- TensorFlow (deep learning)
- Plotly (visualizations)
- And more...

### Step 4: Generate Sample Data (Optional)

```powershell
# Using Makefile
make generate-data

# Or directly
python scripts/data_generation/generate_test_csv.py
```

This creates a test CSV file with realistic expense data.

### Step 5: Run the Application

**Option A: Using Makefile**
```powershell
make run
```

**Option B: Using Streamlit directly**
```powershell
streamlit run app/budgetwise_app.py
```

### Step 6: Open in Browser

The application will automatically open at:
```
http://localhost:8501
```

Or manually navigate to that URL in your browser.

---

## 🎮 Using the Application

### 1. Choose Data Source
- **Use Sample Data**: Built-in dataset with 366 days of expenses
- **Upload CSV**: Upload your own expense data (see format below)

### 2. Select Forecast Model
Choose from 13 models:
- **XGBoost** (Recommended - 14.53% MAPE)
- Random Forest
- LSTM, GRU, Bi-LSTM
- N-BEATS
- And more...

### 3. Set Forecast Period
- Days to forecast: 7, 30, 90, or custom
- Confidence intervals included

### 4. View Results
- **Predictions Chart**: Interactive Plotly visualization
- **Metrics**: MAPE, MAE, RMSE
- **Statistics**: Min, max, average predictions
- **Insights**: AI-generated analysis

### 5. Explore Other Pages
- 📊 **Dashboard**: Overview of all metrics
- 🤖 **AI Chat**: Ask questions about your finances
- 📈 **Analytics**: Deep dive into expense patterns

---

## 📤 CSV Upload Format

### Required Columns (13 total)
```csv
date,groceries,transportation,utilities,entertainment,healthcare,dining_out,shopping,education,other,total_daily_expenses,total_weekly_expenses,total_monthly_expenses
2024-01-01,250.50,75.00,120.00,50.00,0.00,80.00,150.00,0.00,45.00,770.50,5393.50,23265.00
2024-01-02,180.00,60.00,0.00,30.00,100.00,60.00,0.00,0.00,25.00,455.00,5183.50,22950.50
...
```

### Column Descriptions
1. **date**: Date in YYYY-MM-DD format
2. **groceries**: Daily grocery expenses (₹)
3. **transportation**: Transportation costs (₹)
4. **utilities**: Utility bills (₹)
5. **entertainment**: Entertainment expenses (₹)
6. **healthcare**: Medical expenses (₹)
7. **dining_out**: Restaurant/dining costs (₹)
8. **shopping**: Shopping expenses (₹)
9. **education**: Education costs (₹)
10. **other**: Other miscellaneous expenses (₹)
11. **total_daily_expenses**: Sum of all daily expenses
12. **total_weekly_expenses**: 7-day rolling sum
13. **total_monthly_expenses**: 30-day rolling sum

### Generate Sample CSV

```powershell
# Creates test_upload_sample.csv with 100 rows
python scripts/data_generation/generate_test_csv.py
```

---

## 🧪 Testing (For Developers)

### Run Tests

```powershell
# All tests
make test

# With coverage report
make test-cov

# Fast tests only (skip slow tests)
make test-fast
```

### Check Code Quality

```powershell
# Format code
make format

# Run linters
make lint

# Run all checks (format, lint, tests)
make check
```

---

## 🐛 Troubleshooting

### Issue: "Streamlit not found"
**Solution**:
```powershell
pip install streamlit==1.31.0
```

### Issue: "Module not found" errors
**Solution**: Install complete dependencies
```powershell
pip install -r requirements-complete.txt
```

### Issue: "TensorFlow not found"
**Solution** (Windows CPU version):
```powershell
pip install tensorflow==2.15.0
```

### Issue: "Port 8501 already in use"
**Solution**: Use different port
```powershell
streamlit run app/budgetwise_app.py --server.port 8502
```

### Issue: Zero predictions (₹0.00)
**Solution**: Check data source
- Ensure CSV has all 13 columns
- Verify no NaN or zero values in expense columns
- See `docs/troubleshooting/FIX_ZERO_PREDICTIONS.md` for details

### Issue: CSV validation fails
**Solution**: Check CSV format
- Ensure all 13 columns are present
- Date format: YYYY-MM-DD
- No negative values
- See `docs/user_guides/CSV_UPLOAD_QUICK_REF.md`

---

## 📚 Next Steps

### For Users
1. **Upload your data**: Follow CSV format above
2. **Explore models**: Try different forecasting models
3. **Adjust parameters**: Change forecast period
4. **Read documentation**: `docs/user_guides/USER_MANUAL.md`

### For Developers
1. **Read CONTRIBUTING.md**: Learn development workflow
2. **Set up dev environment**: `make install-dev`
3. **Run tests**: `make test`
4. **Check code quality**: `make check`
5. **Read ARCHITECTURE.md**: Understand the system

### For Contributors
1. **Read CODE_OF_CONDUCT.md**: Community guidelines
2. **Check open issues**: Find something to work on
3. **Follow PR template**: `.github/PULL_REQUEST_TEMPLATE.md`
4. **Write tests**: Maintain 70%+ coverage

---

## 🔧 Advanced Setup

### Development Environment

```powershell
# Install development dependencies
make install-dev

# Or directly
pip install -r requirements-dev.txt
```

This installs:
- pytest (testing)
- black (formatting)
- flake8 (linting)
- mypy (type checking)
- And more...

### Pre-commit Setup

```powershell
# Install pre-commit hooks
pip install pre-commit
pre-commit install
```

This runs checks automatically before each commit.

### Docker (Future)

```powershell
# Build Docker image (when available)
docker build -t budgetwise-ai .

# Run container
docker run -p 8501:8501 budgetwise-ai
```

---

## 🎯 Makefile Commands Reference

```powershell
make help           # Show all available commands
make install        # Install production dependencies
make install-dev    # Install development dependencies
make test           # Run tests
make test-cov       # Run tests with coverage
make lint           # Run code quality checks
make format         # Format code with Black
make check          # Run all checks
make run            # Start Streamlit app
make clean          # Remove cache and build artifacts
make validate       # Validate project structure
make quickstart     # Complete new developer setup
```

---

## 📞 Getting Help

### Documentation
- **User Manual**: `docs/user_guides/USER_MANUAL.md`
- **CSV Upload Guide**: `docs/user_guides/CSV_UPLOAD_GUIDE.md`
- **Troubleshooting**: `docs/troubleshooting/`
- **Architecture**: `docs/developer_guides/ARCHITECTURE.md`

### Resources
- **README.md**: Project overview
- **CONTRIBUTING.md**: Development guidelines
- **CHANGELOG.md**: Version history
- **PROJECT_STRUCTURE_ANALYSIS.md**: Detailed analysis

### Support
- 🐛 **Report bugs**: Use `.github/ISSUE_TEMPLATE/bug_report.md`
- 💡 **Request features**: Use `.github/ISSUE_TEMPLATE/feature_request.md`
- 📧 **Email**: [Your contact email]
- 💬 **Discussions**: [GitHub Discussions link]

---

## ✅ Success Checklist

After setup, verify everything works:

- [ ] Python 3.8+ is installed
- [ ] Dependencies are installed (25+ packages)
- [ ] Virtual environment is activated (if using)
- [ ] Streamlit app runs without errors
- [ ] Browser opens to http://localhost:8501
- [ ] Sample data loads successfully
- [ ] At least one model generates predictions
- [ ] CSV upload works with test file
- [ ] No error messages in terminal

If all checked, you're ready to go! 🎉

---

## 🎊 You're All Set!

**BudgetWise AI is now running on your system!**

**What you can do now:**
1. ✅ Upload your expense data (CSV format)
2. ✅ Generate forecasts with 13 different models
3. ✅ Analyze spending patterns
4. ✅ Chat with AI about your finances
5. ✅ Export predictions and insights

**Need help?** Check the troubleshooting section above or read the full documentation in `docs/`.

**Ready to contribute?** Read `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.

---

**Happy Forecasting! 📈💰**

*Last Updated: 2025-01-05*  
*Version: 1.0.0*
