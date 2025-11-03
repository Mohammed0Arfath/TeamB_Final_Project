# 💰 **BudgetWise – AI Expense Forecaster**

## 📘 **Project Overview**

**BudgetWise** is an advanced **AI-powered financial forecasting and budget management system** designed to help users make informed financial decisions.
By combining **machine learning**, **deep learning**, and **time series forecasting techniques**, the system predicts future expenses and automatically suggests optimized budget allocations for each spending category.

This project aims to simplify **personal finance planning** by analyzing past spending patterns, identifying trends, and forecasting future expenses using intelligent algorithms.
The application integrates data visualization, predictive analytics, and budget optimization in a **user-friendly Streamlit dashboard**.

# ⚡ **Quick Start Guide — BudgetWise AI Expense Forecaster**

This section explains how to **set up, install dependencies, train models, and launch** the Streamlit dashboard for the BudgetWise AI project.

---

## 🧩 **1. Create a Virtual Environment**

```bash
python -m venv venv
```

### 🔍 Explanation:

* Creates a **virtual environment** named `venv` inside your project folder.
* It isolates your project’s dependencies from the system’s global Python packages.

✅ *Best practice: Always work inside a virtual environment to avoid version conflicts.*

---

## ⚙️ **2. Allow Execution of Scripts (Windows PowerShell)**

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 🔍 Explanation:

* Allows PowerShell to **temporarily run scripts** within this session.
* Without this, the virtual environment activation script may be blocked.

✅ *This change is temporary and applies only to the current terminal session.*

---

## ▶️ **3. Activate the Virtual Environment**

```bash
.\venv\Scripts\activate
```

### 🔍 Explanation:

* Activates the environment so that any Python commands now use the `venv` environment.
* You’ll see `(venv)` appear in your terminal, confirming activation.

✅ *Keep this environment active for all further steps.*

---

## 🧠 **4. Run Automated Setup**

```bash
python setup.py --install-all
```

### 🔍 Explanation:

* Executes the `setup.py` script which automatically:

  * Installs dependencies,
  * Sets up project directories,
  * Prepares configuration files.

✅ *This is a quick one-step setup process to initialize the environment.*

---

## 🚀 **5. Quick Start Execution**

```bash
python quick_start.py
```

### 🔍 Explanation:

* Automatically **trains forecasting models** on sample or provided data.
* **Launches the dashboard** after successful model training.

✅ *Best option for first-time users who want to see the complete system in action instantly.*

---

## 📦 **6. Install Required Dependencies (Manual Option)**

```bash
pip install -r requirements.txt
```

### 🔍 Explanation:

* Installs all Python libraries listed in the `requirements.txt` file, including ML/DL and visualization packages.

✅ *Use this step if the automated setup didn’t complete installation.*

---

## 🧮 **7. Train the Forecasting Models**

```bash
python train_models.py
```

### 🔍 Explanation:

* Loads your expense data and trains various **forecasting models** like:

  * Prophet
  * ARIMA
  * LSTM or GRU (if configured)
* Stores trained models in the designated directory for reuse.

✅ *After completion, your AI models will be ready for predictions.*

---

## 📊 **8. Install Plotly (Visualization Library)**

```bash
pip install plotly
```

### 🔍 Explanation:

* Installs **Plotly**, used for generating interactive charts and graphs in the dashboard.

✅ *Essential for rendering financial and forecasting visualizations.*

---

## 🌐 **9. Install Streamlit (Dashboard Framework)**

```bash
pip install streamlit
```

### 🔍 Explanation:

* Installs **Streamlit**, the web framework that powers the BudgetWise dashboard interface.

✅ *Required to launch and run the dashboard locally.*

---

## 🖥️ **10. Launch Streamlit Dashboard**

```bash
python -m streamlit run src/app.py
```

### 🔍 Explanation:

* Starts the Streamlit server and launches the **BudgetWise dashboard**.
* Opens automatically at:
  👉 **[http://localhost:8501/](http://localhost:8501/)**

---

## ✅ **Summary Table**

| Step | Command                                                      | Purpose                           |
| ---- | ------------------------------------------------------------ | --------------------------------- |
| 1    | `python -m venv venv`                                        | Create virtual environment        |
| 2    | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` | Allow PowerShell script execution |
| 3    | `.\venv\Scripts\activate`                                    | Activate the virtual environment  |
| 4    | `python setup.py --install-all`                              | Run automated setup and install   |
| 5    | `python quick_start.py`                                      | Train models & launch dashboard   |
| 6    | `pip install -r requirements.txt`                            | Install required dependencies     |
| 7    | `python train_models.py`                                     | Train forecasting models          |
| 8    | `pip install plotly`                                         | Install Plotly for visualization  |
| 9    | `pip install streamlit`                                      | Install Streamlit framework       |
| 10   | `python -m streamlit run src/app.py`                         | Launch interactive dashboard      |

---

## 🎯 **Objectives**

* 📈 **Forecast future expenses** based on historical data.
* 💡 **Optimize monthly budgets** to improve savings and spending efficiency.
* 📊 **Visualize spending patterns** interactively using an AI-powered dashboard.
* 🤖 **Compare multiple forecasting models** (Prophet, ARIMA, LSTM, Transformer) to evaluate accuracy and performance.
* 💬 **Provide actionable financial recommendations** using AI-based insights.

---

## ⚙️ **Key Features**

1. **Data Preprocessing Module**

   * Cleans, normalizes, and transforms raw expense data.
   * Handles missing values, outliers, and categorical encoding.
   * Generates time-series-ready datasets for modeling.

2. **Exploratory Data Analysis (EDA)**

   * Provides visual breakdowns of expenses by category, date, and source.
   * Includes dynamic visualizations such as bar charts, pie charts, and trend plots.
   * Enables quick insights into financial habits.

3. **Forecasting Engine**

   * Uses hybrid models such as:

     * **Prophet** for interpretability,
     * **ARIMA** for statistical forecasting,
     * **LSTM/GRU** for deep learning-based sequence prediction, and
     * **Transformers** for high-performance long-term forecasting.
   * Predicts future expenses for each category or total spending.

4. **Budget Optimization Module**

   * Suggests personalized budget allocations based on forecasted values and income constraints.
   * Uses optimization algorithms (linear programming / constraint satisfaction).
   * Aims to balance spending efficiency and savings goals.

5. **Interactive Streamlit Dashboard**

   * Allows users to upload CSV expense files.
   * Displays categorized spending trends and forecast visualizations.
   * Provides AI-generated recommendations for better financial planning.
   * Clean, responsive interface suitable for desktop and mobile use.

---

## 🧠 **Tech Stack**

| Category              | Tools / Libraries                                           |
| --------------------- | ----------------------------------------------------------- |
| **Language**          | Python 3.x                                                  |
| **Libraries (ML/DL)** | scikit-learn, TensorFlow / PyTorch, Prophet, ARIMA, XGBoost |
| **Data Processing**   | Pandas, NumPy, Scipy                                        |
| **Visualization**     | Matplotlib, Seaborn, Plotly                                 |
| **Dashboard**         | Streamlit                                                   |
| **Optimization**      | PuLP / SciPy Optimization                                   |
| **Version Control**   | Git / GitHub                                                |
| **Environment**       | Conda / Virtualenv                                          |

---

## 🧩 **Working Modules**

1. **Data Module (`data/`)**

   * Contains raw expense CSVs and cleaned datasets.
   * Supports automated data loading and version tracking.

2. **Notebook Module (`notebooks/`)**

   * Includes exploratory notebooks for data understanding and model experimentation.
   * Example: `eda.ipynb` visualizes category-wise spending patterns.

3. **Source Code Module (`src/`)**

   * **`preprocessing.py`** – handles data cleaning, encoding, and normalization.
   * **`models.py`** – defines ML/DL forecasting models and evaluation logic.
   * **`forecasting.py`** – performs time series prediction for all categories.
   * **`budget_optimizer.py`** – generates intelligent budget suggestions.
   * **`app.py`** – integrates Streamlit dashboard and backend processing.

4. **Testing Module (`tests/`)**

   * Contains unit tests to ensure accuracy, performance, and reliability of functions and models.

5. **Documentation and Requirements**

   * **`README.md`** – provides detailed project explanation, setup instructions, and usage guide.
   * **`requirements.txt`** – lists Python dependencies for easy environment setup.

---

## 📂 **Project Structure**

```
D:\ML_PROJECT_SESSION
│
├── data\                     # Raw & processed datasets
│
├── notebooks\                # Jupyter notebooks (EDA, model experiments)
│   └── eda.ipynb
│
├── src\                      # Source code
│   ├── preprocessing.py       # Data preprocessing and feature engineering
│   ├── models.py              # Machine learning and deep learning model definitions
│   ├── forecasting.py         # Forecasting engine using Prophet/ARIMA/LSTM
│   ├── budget_optimizer.py    # Optimization algorithms for budget allocation
│   └── app.py                 # Streamlit dashboard and app integration
│
├── tests\                    # Unit and functional test cases
│
├── README.md                 # Project documentation
│
└── requirements.txt          # Dependencies and environment setup
```

## 🧪 **Model Evaluation Metrics**

* Mean Absolute Error (MAE)
* Root Mean Square Error (RMSE)
* Mean Absolute Percentage Error (MAPE)
* R² Score (Model Accuracy)

Each model’s performance is compared, and the best-performing forecasting model is automatically selected for final predictions.

---

## 🚀 **Future Enhancements**

* Integration of **Transformers** for improved long-term forecasting.
* Addition of **AI-based expense category suggestions** (via NLP).
* Real-time **user authentication & personal dashboard**.
* Support for **bank API integration** to auto-import transactions.
* Deployment on **cloud platforms** for public accessibility.

---

## 🧭 **Conclusion**

**BudgetWise – AI Expense Forecaster** successfully demonstrates how artificial intelligence can enhance personal finance management through predictive analytics, data visualization, and optimization techniques.
The integration of ML, DL, and forecasting models provides users with actionable insights, empowering them to **plan smarter, spend better, and save more**.
