<<<<<<< HEAD
# 💰 Personal Expense Forecasting & Budget Optimization System  
**An AI-Powered Solution for Smart Financial Planning**

> 📊 *Predict, Plan, and Optimize your Personal Finances using Machine Learning, Deep Learning, and Transformer-based Forecasting.*

---

## 🧩 Project Overview

This project builds an **AI-driven personal expense forecasting system** that predicts and optimizes monthly expenses using **machine learning (ML)**, **deep learning (DL)**, and **transformer-based models**.  

The system analyzes historical financial data, identifies spending patterns, and provides **personalized budget recommendations** through an **interactive Streamlit dashboard**.

---

## 🎯 Objectives

- Predict future expenses (1, 3, and 6 months ahead) across multiple categories.  
- Identify key expense trends, seasonal patterns, and anomalies.  
- Suggest optimized budget allocations using intelligent algorithms.  
- Visualize and report financial performance in real time.  
- Deploy a user-friendly Streamlit web app for end users.

---

## 🧠 Skills Acquired

> **Skills Takeaway:**  
> Time Series Analysis • Feature Engineering • ML/DL Forecasting • LSTM • Transformers • Streamlit Development • Data Visualization • Financial Analytics

| Category | Skills |
|-----------|--------|
| **Data Science** | Data cleaning, preprocessing, EDA, feature engineering |
| **Machine Learning** | Random Forest, XGBoost, LightGBM, Prophet |
| **Deep Learning** | LSTM, GRU, Bi-LSTM, CNNs for time series |
| **Transformers** | Temporal Fusion Transformer (TFT), N-BEATS, Autoformer |
| **Visualization & App Dev** | Plotly, Streamlit, ReportLab, Dashboarding |
| **Finance Analytics** | Budget optimization, trend analysis, forecasting |

---

## 🧾 Problem Statement

> Managing personal finances effectively is a global challenge.

Most individuals rely on **static budgeting tools** that fail to adapt to lifestyle changes, seasonal spending, and income variations.  
This leads to:
- Overspending and unplanned debt 💸  
- Poor savings decisions 📉  
- Lack of visibility into financial trends 📊  

This project aims to build a **data-driven, predictive system** capable of:
- Forecasting future expenses across categories.  
- Providing intelligent budget recommendations.  
- Visualizing spending patterns in an interactive and actionable format.

---

## 🏦 Domain  
**Personal Finance Management & Predictive Analytics**

---

## 💼 Business Use Cases

| Sector | Use Case |
|--------|-----------|
| 🧍‍♀️ **Personal Finance** | Individuals can plan monthly budgets effectively. |
| 💡 **Financial Advisors** | Offer personalized insights for clients. |
| 🏦 **Banking** | Integrate predictive expense analysis in mobile apps. |
| 💳 **FinTech Apps** | Add forecasting & budget optimization features. |
| 🧮 **Credit & Loan Services** | Use expense behavior to evaluate credit risk. |

---

## ⚙️ Project Approach

### **1️⃣ Data Collection**
- 🏦 **User Data:** Bank statements, card bills, UPI/Wallet exports (Paytm, GPay, PhonePe).  
- 📊 **Public Datasets:** [Kaggle: Personal Expense Transaction Data](https://www.kaggle.com/) and related sources.  
- 🧩 **Hybrid Dataset:** Combination of real + synthetic + external financial indicators.

### **2️⃣ Data Preprocessing**
- Categorize expenses using NLP on merchant names.  
- Handle missing values, duplicates, and outliers.  
- Create time-based features: week, month, season, holiday, etc.  
- Encode income patterns and demographic factors.  

### **3️⃣ Exploratory Data Analysis (EDA)**
- Category-wise expense trends & correlations.  
- Seasonality and cyclical behavior detection.  
- Identify overspending patterns and volatility.  

### **4️⃣ Feature Engineering**
- Rolling averages, lag features, trend differentials.  
- Category ratio and variance metrics.  
- Integration of inflation and economic indicators.  

### **5️⃣ Modeling**

| Type | Models Used | Description |
|-------|--------------|-------------|
| 🧮 **Baseline Models** | Linear Regression, ARIMA, SARIMA, Prophet | Foundational statistical forecasting |
| 🤖 **Machine Learning** | Random Forest, XGBoost, LightGBM | Handles non-linear dependencies |
| 🧠 **Deep Learning** | LSTM, GRU, Bi-LSTM, CNNs | Captures sequential temporal dependencies |
| ⚡ **Transformers (Advanced)** | Temporal Fusion Transformer (TFT), N-BEATS, Autoformer | State-of-the-art forecasting |
| 🔗 **Ensemble Models** | ML + DL hybrid | Combined predictions for higher accuracy |

### **6️⃣ Evaluation Metrics**
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- Mean Absolute Percentage Error (MAPE)  
- Directional Accuracy  
- Category-wise precision  

### **7️⃣ Deployment**
- 🎨 Interactive Streamlit Dashboard  
- 📉 Forecast Visualizations (Plotly Graphs)  
- 💡 Budget Optimization Insights  
- 📤 Report Export (Excel, PDF)  
- ☁️ Deploy on Streamlit Cloud / AWS / Heroku  

---



---

## 💻 Tech Stack & Dependencies

| Category | Tools |
|-----------|-------|
| **Languages** | Python |
| **Libraries** | Pandas, NumPy, Scikit-learn, XGBoost, LightGBM, Prophet, TensorFlow |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Frameworks** | Streamlit |
| **Deployment** | Docker, Streamlit Cloud |
| **Version Control** | Git, GitHub |
| **Reporting** | ReportLab, OpenPyXL |

---

Here is the complete project structure with brief descriptions for each file, presented in a visually clean format:

-----

## 📂 Personal Expense Forecasting Project Structure

```
PersonalExpenseForecasting/
├── app/
│   └── streamlit_app.py                # Web application interface
├── data/
│   ├── interim/
│   │   └── interim_cleaned_transactions.csv  # Transactions after initial cleaning
│   ├── processed/
│   │   └── processed_features_transactions.csv # Final features for modeling
│   └── raw/
│       ├── budgetwise_finance_dataset.csv      # Original raw dataset
│       └── budgetwise_synthetic_dirty.csv      # Secondary dirty dataset
├── models/
│   ├── bilstm_model.h5                 # Trained Bidirectional LSTM model
│   ├── cnn1d_model.h5                  # Trained 1D CNN model
│   ├── feature_columns.pkl             # Metadata for features used
│   ├── gru_model.h5                    # Trained GRU deep learning model
│   ├── lightgbm_model.pkl              # Trained LightGBM model
│   ├── linear_regression.pkl           # Trained Linear Regression model
│   ├── lstm_model.h5                   # Trained LSTM deep learning model
│   ├── random_forest.pkl               # Trained Random Forest model
│   ├── scaler.pkl                      # Fitted data scaler object
│   └── xgb_model.pkl                   # Trained XGBoost model
├── notebooks/                          # Exploratory Analysis (Jupyter Notebooks)
├── reports/                            # All project outputs and reports
│   ├── evaluation/
│   │   ├── best_model_summary.txt      # Text summary of best model
│   │   ├── metric_heatmap.png          # Visualization of model metrics
│   │   ├── r2_comparison.png           # R-squared score comparison plot
│   │   └── rmse_comparison.png         # RMSE score comparison plot
│   ├── figures/
│   │   ├── arima_forecast.png          # ARIMA model forecast plot
│   │   ├── autocorrelation_plot.png    # Autocorrelation function plot
│   │   ├── category_bar_chart.png      # Expense distribution bar chart
│   │   ├── category_pie_chart.png      # Expense distribution pie chart
│   │   ├── correlation_heatmap.png     # Feature correlation heatmap
│   │   ├── mae_horizon1.png            # MAE for first forecast horizon
│   │   ├── monthly_trend.png           # Plot of monthly expenses
│   │   ├── prophet_forecast.png        # Prophet model forecast plot
│   │   └── seasonal_decomposition.png  # Time series decomposition plot
│   └── forecasts/
│       ├── model_comparison.csv        # CSV of model performance metrics
│       └── model_results.csv           # Final forecast results
├── src/                                # Source code scripts
│   ├── data_preprocessing.py           # Functions for data cleaning
│   ├── eda_analysis.py                 # Scripts for EDA
│   ├── feature_engineering.py          # Logic for feature creation
│   ├── forecasting.py                  # Core prediction logic
│   ├── model_evaluation.py             # Script for model testing
│   ├── model_optimization.py           # Script for hyperparameter tuning
│   ├── model_training.py               # Script for model training
│   └── utils.py                        # General helper functions
├── .venv/                              # Python Virtual Environment
├── Dockerfile                          # Docker container configuration
└── requirements.txt                    # List of required packages
```
## 📈 Results & Model Performance

| Model         | MAE       | RMSE       | MAPE     | R²       | Observation               |
| ------------- | --------- | ---------- | -------- | -------- | ------------------------- |
| Prophet       | 12,540    | 17,620     | 14.8%    | 0.89     | Baseline trend accuracy   |
| Random Forest | 9,850     | 13,200     | 11.2%    | 0.93     | Strong performance        |
| **XGBoost**   | **7,420** | **10,150** | **8.4%** | **0.96** | ⭐ Best performer          |
| LSTM          | 8,150     | 11,870     | 9.1%     | 0.95     | Excellent long-term model |
---
#### ✅ Best Model: XGBoost
#### 📊 Overall Accuracy: ~91.6%
#### 📉 MAPE Improvement: ~43% better than baseline Prophet model.


---

  

# 💡 Insights from the Dashboard

#### Spending on Education dropped 82% (savings opportunity).

#### Miscellaneous category overspent 166% this month.

#### Suggested saving potential: ₹3,23,937 (~8.3%).

#### Recommended reallocation towards priority goals (housing, savings).

# 🧭 Future Enhancements

#### Integrate real-time APIs (Plaid, Razorpay) for live data ingestion.

#### Add transformer-based forecasting (TFT, N-BEATS).

#### Enable multi-user authentication and secure personal data vaults.

#### Build LangChain-based AI Assistant for conversational financial advice.

#### Integrate FastAPI microservice for backend scalability.

## 📜 License

#### This project is licensed under the MIT License.
#### You are free to use, modify, and distribute it with proper attribution.

## 👩‍💻 Author & Contact

#### Developed by: Sakshi Birajdar
####  📧 Email: sakshibirajdar34@gmail.com

#### 🔗 LinkedIn: linkedin.com/in/sakshibirajdar

## 🏁 Summary

#### Personal Expense Forecasting System combines AI forecasting, budget optimization, and visual analytics into a powerful, deployable web solution.
#### Built using Python, Streamlit, and advanced ML/DL models (XGBoost, LSTM, Prophet), it empowers users to make data-driven financial decisions with 90%+ accuracy.

## 🎯 “From Predicting to Planning — Your Finances, Smarter with AI.”

#### ⭐ If this project helped you, don’t forget to star it on GitHub!
=======
# 🏦 BudgetWise Personal Expense Forecasting & Budget Optimization

An AI-powered system for personal financial management that provides accurate expense forecasting, budget optimization, and actionable financial insights through an interactive dashboard.

## ✨ Features

### 🎯 Core Capabilities
- **Multi-Model Forecasting**: Combines baseline, ML, and deep learning models
- **Smart Budget Optimization**: AI-driven budget recommendations
- **Interactive Dashboard**: Real-time visualization and insights
- **Comprehensive Analysis**: Statistical and predictive analytics
- **Time Series Forecasting**: Advanced temporal pattern recognition

### 🤖 Machine Learning Pipeline
- **Baseline Models**: Linear Regression, ARIMA, Prophet
- **ML Models**: Random Forest, XGBoost, LightGBM with hyperparameter tuning
- **Deep Learning**: LSTM, GRU, CNN, Transformer architectures
- **Feature Engineering**: Lag features, rolling statistics, seasonal decomposition
- **Model Evaluation**: Comprehensive performance metrics and comparisons

### 📊 Interactive Features
- Real-time expense tracking and categorization
- Multi-horizon forecasting (1, 3, 6 months)
- Budget optimization with risk assessment
- Expense pattern analysis and anomaly detection
- Personalized financial insights and recommendations

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, Pandas, NumPy, Scikit-learn
- **Machine Learning**: XGBoost, LightGBM, TensorFlow, PyTorch
- **Time Series**: Prophet, ARIMA, Statsmodels
- **Web Framework**: Streamlit
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy, YAML
- **Development**: Jupyter, Git, pytest

## � Quick Start

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd BudgetWise-Forecasting
```

2. **Run automated setup**:
```bash
python setup.py --install-all
```

3. **Quick start** (trains models and launches dashboard):
```bash
python quick_start.py
```

### Manual Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Prepare your data**:
   - Place CSV files in `data/raw/` directory
   - Required columns: `date`, `amount`, `category`, `description`

3. **Train models**:
```bash
python train_models.py
```

4. **Launch dashboard**:
```bash
streamlit run app/streamlit_app.py
```

## �📁 Project Structure

```
BudgetWise-Forecasting/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── setup.py                 # Automated setup script
├── quick_start.py           # Quick start script
├── train_models.py          # Main training orchestrator
├── config/
│   └── config.yaml          # Configuration settings
├── data/
│   ├── raw/                 # Raw financial data
│   ├── processed/           # Cleaned and processed data
│   └── features/            # Engineered features
├── src/
│   ├── data_preprocessing.py    # Data cleaning and preparation
│   ├── feature_engineering.py  # Advanced feature creation
│   ├── models/
│   │   ├── baseline_models.py      # Statistical baseline models
│   │   ├── ml_models.py           # Machine learning models
│   │   └── deep_learning_models.py # Deep learning architectures
│   └── evaluation/
│       └── model_evaluator.py    # Comprehensive model evaluation
├── app/
│   └── streamlit_app.py     # Interactive web dashboard
├── models/                  # Trained model artifacts
├── reports/                 # Evaluation reports and visualizations
├── notebooks/               # Jupyter notebooks for exploration
└── tests/                   # Unit tests
```

## 🎯 Usage Guide

### Data Preparation
Your financial data should be in CSV format with these columns:
- `date`: Transaction date (YYYY-MM-DD format)
- `amount`: Transaction amount (positive numbers)
- `category`: Expense category (e.g., "Food", "Transportation")
- `description`: Transaction description (optional)

### Training Models

**Full Pipeline** (recommended):
```bash
python train_models.py
```

**Individual Steps**:
```bash
# Data preprocessing only
python train_models.py --step preprocess

# Feature engineering only  
python train_models.py --step features

# Train baseline models only
python train_models.py --step baseline

# Train ML models only
python train_models.py --step ml

# Train deep learning models only
python train_models.py --step dl

# Run evaluation only
python train_models.py --step evaluate
```

**Advanced Options**:
```bash
# Skip hyperparameter tuning (faster training)
python train_models.py --no-tune

# Skip specific model types
python train_models.py --skip-dl --skip-ml

# Force reprocessing of data
python train_models.py --force-reprocess
```

### Dashboard Features

Launch the interactive dashboard:
```bash
streamlit run app/streamlit_app.py
```

**Dashboard Sections**:
- **🏠 Dashboard**: Overview of expenses and key metrics
- **📊 Expense Analysis**: Detailed visualizations and trends
- **🔮 Forecasting**: Multi-horizon expense predictions
- **💰 Budget Optimizer**: AI-driven budget recommendations  
- **🎯 Model Performance**: ML model comparison and metrics

## ⚙️ Configuration

Edit `config/config.yaml` to customize:

```yaml
data:
  train_split: 0.7
  val_split: 0.15
  test_split: 0.15

feature_engineering:
  lag_periods: [1, 7, 14, 30]
  rolling_windows: [7, 14, 30]
  
models:
  baseline:
    linear_regression:
      fit_intercept: true
    
  ml_models:
    random_forest:
      n_estimators: [100, 200]
      max_depth: [10, 20]
    
  deep_learning:
    sequence_length: 30
    lstm:
      units: [64, 32]
      epochs: 100
```

## 📊 Model Performance

The system evaluates models using multiple metrics:

| Model Type | MAE | RMSE | MAPE | R² | Dir. Accuracy |
|------------|-----|------|------|-----|---------------|
| **Baseline Models** |
| Linear Regression | - | - | - | - | - |
| ARIMA | - | - | - | - | - |
| Prophet | - | - | - | - | - |
| **ML Models** |
| Random Forest | - | - | - | - | - |
| XGBoost | - | - | - | - | - |
| LightGBM | - | - | - | - | - |
| **Deep Learning** |
| LSTM | - | - | - | - | - |
| GRU | - | - | - | - | - |
| CNN | - | - | - | - | - |
| Transformer | - | - | - | - | - |

*Run training to populate performance metrics*

## 🎬 Demo & Examples

### Sample Output
After running the full pipeline, you'll see:

```
🏦 BUDGETWISE FORECASTING - QUICK EVALUATION SUMMARY
======================================================================

📊 Best Models by Category:
--------------------------------------------------
• Food                 | ml_random_forest         | MAE: 12.45
• Transportation       | baseline_prophet         | MAE: 8.73
• Entertainment        | dl_lstm                  | MAE: 15.22
• Healthcare           | ml_xgboost              | MAE: 22.18

🏆 Model Type Performance:
------------------------------
• ML         : 2 best models
• Baseline   : 1 best models
• DL         : 1 best models
```

### Dashboard Screenshots
The Streamlit dashboard provides:
- 📊 **Interactive Charts**: Plotly-powered visualizations
- 🔮 **Forecasting Interface**: Select categories and time horizons
- 💰 **Budget Optimizer**: AI-driven recommendations
- 🎯 **Model Comparison**: Performance metrics visualization
│   └── 06_model_comparison.ipynb
├── app/
│   ├── streamlit_app.py
│   ├── pages/
│   └── components/
├── models/                  # Saved model files
├── config/
│   └── config.yaml
├── tests/
├── reports/
└── requirements.txt
```

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mohammed0Arfath/BudgetWise-AI-based-Expense-Forecasting-Tool.git
cd BudgetWise-Forecasting
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. **Data Preprocessing**: Run the preprocessing pipeline
```bash
python src/data_preprocessing.py
```

2. **Feature Engineering**: Generate time-series features
```bash
python src/feature_engineering.py
```

3. **Train Models**: Train forecasting models
```bash
python src/models/train_models.py
```

4. **Launch App**: Start the Streamlit application
```bash
streamlit run app/streamlit_app.py
```

## 📊 Model Performance

| Model | MAE | RMSE | MAPE | Directional Accuracy |
|-------|-----|------|------|---------------------|
| LSTM | 245.32 | 387.45 | 12.8% | 78.9% |
| XGBoost | 289.76 | 421.33 | 14.2% | 76.4% |
| Prophet | 312.44 | 445.21 | 15.7% | 74.1% |
| Ensemble | 221.89 | 359.12 | 11.4% | 81.2% |

## 📈 Key Insights

- Housing and transportation expenses show strong seasonal patterns
- Food expenses have high volatility but predictable weekly cycles
- Income correlation significantly improves forecast accuracy
- Ensemble methods outperform individual models by 15-20%

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Mohammed Arfath** - *Initial work* - [Mohammed0Arfath](https://github.com/Mohammed0Arfath)

## 🙏 Acknowledgments

- Kaggle community for financial datasets
- Streamlit team for the amazing framework
- Open source contributors for ML libraries

---

⭐ **Star this repo if you found it helpful!**
>>>>>>> b50393eb3518db5ccd89dd25167a6e1f57dbf3b3
