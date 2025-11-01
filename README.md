# Expense Forecast AI — Demo

Run locally:
1. python3 -m venv venv   # optional
2. source venv/bin/activate  # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. streamlit run app.py --server.port 8501

Upload your CSV with columns like: Date / Time, Debit/Credit/Amount, Category, Description.
If no file uploaded the app uses sample_expenses.csv.

Features:
- Auto-detect columns and clean the dataset
- Monthly aggregation and Prophet forecasting
- Anomaly detection (IsolationForest)
- Rule-based insights
- Download cleaned transactions and forecasts

Tips for judges demo:
- Show data preview -> monthly trend -> forecast -> anomalies -> download forecast CSV
- Switch CSV files to show how forecasts adapt to data