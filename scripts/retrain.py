# scripts/retrain.py
import pandas as pd
import glob, os
from prophet import Prophet
import joblib

UPLOAD_DIR = "data/uploads"
MODEL_PATH = "models/prophet_model.joblib"

def load_all_uploads():
    files = glob.glob(os.path.join(UPLOAD_DIR, "*.csv"))
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_csv(f))
        except:
            pass
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return pd.DataFrame()

def prepare(df):
    df.columns = [c.strip().lower().replace("/", " ").replace(" ", "_") for c in df.columns]
    date_col = [c for c in df.columns if 'date' in c or 'time' in c][0]
    amt_col = [c for c in df.columns if 'debit' in c or 'credit' in c or 'amount' in c][0]
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    df['amount'] = pd.to_numeric(df[amt_col], errors='coerce').fillna(0)
    df['month'] = df[date_col].dt.to_period('M').dt.to_timestamp()
    monthly = df.groupby('month')['amount'].sum().reset_index().rename(columns={'month':'ds','amount':'y'})
    return monthly

def main():
    df = load_all_uploads()
    if df.empty:
        print("No uploaded CSVs to train on.")
        return
    monthly = prepare(df)
    model = Prophet(yearly_seasonality=True)
    model.fit(monthly)
    joblib.dump(model, MODEL_PATH)
    print("Saved model to", MODEL_PATH)

if __name__ == "_main_":
    main()