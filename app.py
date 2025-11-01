# app.py
import streamlit as st 
import hashlib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from prophet import Prophet
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import calendar
import warnings
warnings.filterwarnings('ignore')

# -------------------------------
# LOGIN PAGE IMPLEMENTATION
# -------------------------------
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# Dummy user credentials (replace or extend this for real users)
users = {
    "admin": make_hashes("admin123"),
    "user1": make_hashes("user123"),
    "santhiya": make_hashes("san123")
}

# Initialize session
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.set_page_config(page_title="Smart Expense AI | Login", page_icon="🔐", layout="centered")

    st.markdown("""
        <div style='text-align:center; margin-top:80px;'>
            <h1 style='color:#2563EB;'>🔐 Smart Expense AI Login</h1>
            <p style='color:gray;'>Please sign in to continue</p>
        </div>
    """, unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username in users:
            hashed_pswd = users[username]
            if check_hashes(password, hashed_pswd):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"✅ Welcome, {username}!")
                st.rerun()
            else:
                st.error("❌ Incorrect password")
        else:
            st.error("❌ User not found")
    st.stop()


# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Smart Expense AI", 
    layout="wide", 
    initial_sidebar_state="expanded",
    page_icon="💹"
)

# -------------------------------
# Perfect Color Theme - Professional Blue & Green
# -------------------------------
PRIMARY = "#2563EB"      # Professional Blue
SECONDARY = "#059669"    # Success Green
ACCENT = "#7C3AED"       # Purple Accent
NEUTRAL = "#64748B"      # Neutral Gray
WARNING = "#DC2626"      # Error Red
BG_GRADIENT = "linear-gradient(135deg, #F0F9FF 0%, #EFF6FF 100%)"
CARD_BG = "rgba(255, 255, 255, 0.95)"
SIDEBAR_BG = "rgba(255, 255, 255, 0.98)"

# -------------------------------
# Advanced CSS Styling
# -------------------------------
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .stApp {{
        background: {BG_GRADIENT};
        font-family: 'Inter', sans-serif;
    }}
    
    .main-header {{
        background: {CARD_BG};
        backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.1);
        border: 1px solid rgba(37, 99, 235, 0.1);
    }}
    
    .big-title {{
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }}
    
    .subtitle {{
        text-align: center;
        color: {NEUTRAL};
        font-size: 16px;
        margin-bottom: 0;
        font-weight: 400;
        # -------------------------------
        # 💰 Savings Estimator (uses filtered data)
        st.sidebar.markdown("### 💰 Savings Estimator")
        # Let user choose forecast months
        forecast_months = st.sidebar.slider("Forecast Next (Months)", 1, 12, 6)

        line-height: 1.5;
    }}
    
    .card {{
        background: {CARD_BG};
        backdrop-filter: blur(20px);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.08);
        border: 1px solid rgba(37, 99, 235, 0.1);
        margin-bottom: 20px;
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.15);
    }}
    
    .kpi-card {{
        text-align: center;
        padding: 20px 15px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(5, 150, 105, 0.05));
        border: 1px solid rgba(37, 99, 235, 0.1);
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .kpi-card:hover {{
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(5, 150, 105, 0.08));
        transform: scale(1.02);
    }}
    
    .kpi-value {{
        font-size: 24px;
        font-weight: 700;
        color: {PRIMARY};
        margin: 8px 0;
    }}
    
    .kpi-label {{
        font-size: 13px;
        color: {NEUTRAL};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .positive-change {{
        color: {SECONDARY};
        font-weight: 600;
    }}
    
    .negative-change {{
        color: {WARNING};
        font-weight: 600;
    }}
    
    .insight-card {{
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.03), rgba(5, 150, 105, 0.03));
        border-left: 4px solid {PRIMARY};
        padding: 16px;
        border-radius: 8px;
        margin: 8px 0;
        transition: all 0.2s ease;
    }}
    
    .insight-card:hover {{
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(5, 150, 105, 0.05));
        transform: translateX(4px);
    }}
    
    .section-header {{
        font-size: 20px;
        font-weight: 700;
        color: #1E293B;
        margin: 24px 0 16px 0;
        padding-bottom: 12px;
        border-bottom: 2px solid rgba(37, 99, 235, 0.1);
    }}
    
    .stSidebar {{
        background: {SIDEBAR_BG};
    }}
    
    .sidebar-header {{
        font-size: 18px;
        font-weight: 700;
        color: {PRIMARY};
        margin-bottom: 20px;
        padding-bottom: 12px;
        border-bottom: 2px solid rgba(37, 99, 235, 0.1);
    }}
    
    /* Custom file uploader */
    .stFileUploader > div > div {{
        background: {CARD_BG} !important;
        border: 2px dashed {PRIMARY} !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }}
    
    /* Custom buttons */
    .stDownloadButton button {{
        background: linear-gradient(135deg, {PRIMARY}, {SECONDARY}) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }}
    
    .stDownloadButton button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3) !important;
    }}
    
    /* Custom metric cards */
    [data-testid="metric-container"] {{
        background: {CARD_BG} !important;
        border: 1px solid rgba(37, 99, 235, 0.1) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
    }}
    
    /* Custom select boxes */
    .stSelectbox div div {{
        border-radius: 8px !important;
    }}
    
    /* Custom date input */
    .stDateInput div div {{
        border-radius: 8px !important;
    }}
    
    /* Custom multiselect */
    .stMultiSelect div div {{
        border-radius: 8px !important;
    }}
    
    /* Custom slider */
    .stSlider div div {{
        border-radius: 8px !important;
    }}
    
    /* Footer */
    .footer {{
        text-align: center;
        color: {NEUTRAL};
        font-size: 14px;
        margin-top: 40px;
        padding: 20px;
        border-top: 1px solid rgba(37, 99, 235, 0.1);
    }}
    
    /* Anomaly alert */
    .anomaly-alert {{
        background: rgba(220, 38, 38, 0.05);
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid {WARNING};
        border: 1px solid rgba(220, 38, 38, 0.1);
    }}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Enhanced Helpers
# -------------------------------
def clean_csv(df):
    """Enhanced CSV cleaning with better column detection"""
    df.columns = [c.strip().lower().replace(" ", "").replace("/", "") for c in df.columns]
    
    # Date column detection
    date_col = next((c for c in df.columns if "date" in c or "time" in c), None)
    if not date_col:
        st.error("❌ No date column found in CSV. Please ensure your file has a date column.")
        return pd.DataFrame(columns=['date','amount','category','description'])
    
    df['date'] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=['date'])
    
    # Amount column detection
    amount_col = next((c for c in df.columns if "debit" in c or "credit" in c or "amount" in c or "transaction" in c), None)
    if amount_col:
        df['amount'] = pd.to_numeric(df[amount_col], errors='coerce').fillna(0)
        # Handle credit/debit amounts
        if 'debit' in amount_col.lower():
            df['amount'] = df['amount'].abs()
        elif 'credit' in amount_col.lower():
            df['amount'] = -df['amount'].abs()
    else:
        df['amount'] = 0
    
    # Category detection
    cat_col = next((c for c in df.columns if "cat" in c or "category" in c or "type" in c), None)
    df['category'] = df[cat_col].fillna("Other") if cat_col else "Other"
    
    # Description detection
    desc_col = next((c for c in df.columns if "desc" in c or "remark" in c or "note" in c or "memo" in c), None)
    df['description'] = df[desc_col].fillna("") if desc_col else ""
    
    return df[['date','amount','category','description']].sort_values('date')

def monthly_aggregate(df):
    """Enhanced monthly aggregation"""
    df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
    monthly = df.groupby('month').agg({
        'amount': ['sum', 'mean', 'count'],
        'category': 'nunique'
    }).round(2)
    monthly.columns = ['total', 'avg_transaction', 'transaction_count', 'unique_categories']
    monthly = monthly.reset_index().rename(columns={'month': 'ds', 'total': 'y'})
    return monthly

def forecast_expense(df, periods=6):
    """Enhanced forecasting with confidence intervals"""
    monthly = monthly_aggregate(df)
    if len(monthly) < 3:
        st.warning("⚠ Need at least 3 months of data for forecasting")
        return monthly, pd.DataFrame()
    
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False,
        changepoint_prior_scale=0.05,
        seasonality_prior_scale=10
    )
    model.fit(monthly[['ds', 'y']])
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return monthly, forecast

def detect_anomalies(df):
    """Enhanced anomaly detection"""
    if len(df) < 10:
        return pd.DataFrame()
    
    # Multiple anomaly detection methods
    iso = IsolationForest(contamination=0.05, random_state=42)
    df['amount_scaled'] = (df['amount'] - df['amount'].mean()) / df['amount'].std()
    df['anomaly_score'] = iso.fit_predict(df[['amount_scaled']])
    df['anomaly'] = df['anomaly_score'] == -1
    
    # Additional statistical anomalies
    Q1 = df['amount'].quantile(0.25)
    Q3 = df['amount'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df['statistical_anomaly'] = (df['amount'] < lower_bound) | (df['amount'] > upper_bound)
    df['final_anomaly'] = df['anomaly'] | df['statistical_anomaly']
    
    return df[df['final_anomaly'] == True]

def generate_insights(df, monthly, forecast):
    """Enhanced insights generation"""
    insights = []
    
    # Basic metrics
    total = df['amount'].sum()
    avg_month = monthly['y'].mean()
    top_cat = df.groupby('category')['amount'].sum().idxmax()
    top_cat_amount = df.groupby('category')['amount'].sum().max()
    
    insights.append(f"💰 Total spent: ₹{total:,.0f}")
    insights.append(f"📊 Average monthly spend: ₹{avg_month:,.0f}")
    insights.append(f"🏆 Highest spending category: {top_cat} (₹{top_cat_amount:,.0f})")
    
    # Trend analysis
    if len(monthly) >= 2:
        prev, last = monthly['y'].iloc[-2], monthly['y'].iloc[-1]
        change = (last-prev)/prev*100 if prev != 0 else 0
        trend_icon = "📈" if change > 0 else "📉"
        trend_class = "positive-change" if change > 0 else "negative-change"
        insights.append(f"{trend_icon} Last month vs previous: <span class='{trend_class}'>{change:+.1f}%</span>")
    
    # Forecast insights
    if not forecast.empty:
        next_val = forecast[forecast['ds'] > monthly['ds'].max()]['yhat'].iloc[0]
        current_avg = monthly['y'].mean()
        forecast_change = ((next_val - current_avg) / current_avg * 100) if current_avg != 0 else 0
        forecast_trend = "positive-change" if forecast_change > 0 else "negative-change"
        insights.append(f"🔮 Forecast next month: ₹{next_val:,.0f} (<span class='{forecast_trend}'>{forecast_change:+.1f}%</span>)")
    
    # Spending patterns
    if len(df) > 0:
        max_spend_day = df.groupby(df['date'].dt.day_name())['amount'].sum().idxmax()
        insights.append(f"📅 Highest spending day: {max_spend_day}")
        
        # Savings potential
        avg_daily = df['amount'].mean()
        if avg_daily > 0:
            monthly_savings_potential = avg_daily * 30 * 0.1  # Assume 10% savings potential
            insights.append(f"💡 Potential monthly savings: ₹{monthly_savings_potential:,.0f}")
    
    return insights

def create_sample_data():
    """Create comprehensive sample data"""
    dates = pd.date_range(start='2023-01-01', end='2024-02-01', freq='D')
    categories = ['Food & Dining', 'Transportation', 'Shopping', 'Entertainment', 'Bills & Utilities', 'Healthcare', 'Rent', 'Education', 'Travel', 'Other']
    
    data = []
    for date in dates:
        # Base daily transactions
        if np.random.random() > 0.3:  # 70% chance of transaction
            category = np.random.choice(categories, p=[0.2, 0.15, 0.12, 0.08, 0.15, 0.05, 0.1, 0.05, 0.05, 0.05])
            
            if category == 'Rent':
                if date.day == 1:  # Rent on 1st of month
                    amount = 15000
                    data.append({'date': date, 'amount': amount, 'category': category, 'description': 'Monthly Rent Payment'})
            elif category == 'Food & Dining':
                amount = np.random.normal(400, 150)
                descriptions = ['Restaurant Dinner', 'Grocery Shopping', 'Food Delivery', 'Coffee Shop', 'Lunch Outing']
                data.append({'date': date, 'amount': max(100, amount), 'category': category, 'description': np.random.choice(descriptions)})
            elif category == 'Bills & Utilities':
                if date.day in [1, 15]:  # Bills twice a month
                    amount = np.random.normal(2500, 800)
                    descriptions = ['Electricity Bill', 'Internet Bill', 'Mobile Recharge', 'Water Bill', 'Gas Bill']
                    data.append({'date': date, 'amount': max(800, amount), 'category': category, 'description': np.random.choice(descriptions)})
            else:
                amount = np.random.normal(800, 400)
                data.append({'date': date, 'amount': max(50, amount), 'category': category, 'description': f'{category} Expense'})
    
    return pd.DataFrame(data)

# -------------------------------
# App Layout
# -------------------------------
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.markdown('<div class="big-title">💹 Smart Expense AI Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Analytics & Predictive Insights for Your Financial Health</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# File Upload Section
upload_col1, upload_col2 = st.columns([2, 1])
with upload_col1:
    uploaded_file = st.file_uploader("📂 Upload Your Expenses CSV", 
                                   type=['csv'], 
                                   help="Upload CSV with columns: Date, Amount, Category, Description")

with upload_col2:
    use_sample = st.checkbox("Use Sample Data", 
                           value=True if not uploaded_file else False,
                           help="Load sample dataset for demonstration")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        st.stop()
elif use_sample:
    df = create_sample_data()
    st.info("📊 Using sample dataset for demonstration")
else:
    st.warning("Please upload a CSV file or use sample data to continue")
    st.stop()

# Data Cleaning
df_clean = clean_csv(df)

if not df_clean.empty:
    # Initialize df_filtered at the beginning
    df_filtered = df_clean.copy()
    
    # Sidebar with Enhanced Filters
    with st.sidebar:
        st.markdown('<div class="sidebar-header">🔧 Dashboard Controls</div>', unsafe_allow_html=True)
        
        # Date Range
        min_date = df_clean['date'].min().date()
        max_date = df_clean['date'].max().date()
        date_range = st.date_input(
            "📅 Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            help="Select the date range for analysis"
        )
        
        if len(date_range) == 2:
            start_date, end_date = date_range
        else:
            start_date, end_date = min_date, max_date
        
        # Category Filter
        categories = st.multiselect(
            "🏷 Categories",
            options=sorted(df_clean['category'].unique()),
            default=df_clean['category'].unique(),
            help="Select categories to include in analysis"
        )
        
        # Amount Range Filter
        min_amount, max_amount = st.slider(
            "💰 Amount Range (₹)",
            float(df_clean['amount'].min()),
            float(df_clean['amount'].max()),
            (float(df_clean['amount'].min()), float(df_clean['amount'].max())),
            help="Filter transactions by amount range"
        )
        
        # Analysis Period
        analysis_period = st.selectbox(
            "📈 Forecast Periods",
            options=[3, 6, 12],
            index=1,
            help="Number of months to forecast"
        )
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.info("""
        - Upload CSV with Date, Amount columns
        - Use filters to focus on specific data
        - Check anomalies for unusual spending
        - Download reports for offline analysis
        """)

    # Apply Filters
    df_filtered = df_clean[
        (df_clean['date'] >= pd.to_datetime(start_date)) & 
        (df_clean['date'] <= pd.to_datetime(end_date)) &
        (df_clean['category'].isin(categories)) &
        (df_clean['amount'] >= min_amount) &
        (df_clean['amount'] <= max_amount)
    ].copy()

    # Savings Estimator
    st.markdown('<div class="section-header">💰 Savings Estimator</div>', unsafe_allow_html=True)
    income = st.number_input("Monthly Income", min_value=0.0, format='%f')
    expenses = df_filtered['amount'].sum()
    
    if income > 0:
        savings = income - expenses
        savings_percent = (savings / income) * 100
        
        # Display savings metrics with custom styling
        st.markdown(f"""
            <div class="metric-card">
                <h3>Monthly Savings</h3>
                <p>₹{savings:,.2f}</p>
            </div>
            <div class="metric-card">
                <h3>Savings Rate</h3>
                <p>{savings_percent:.1f}%</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Enhanced KPI Cards
    st.markdown('<div class="section-header">📊 Key Performance Indicators</div>', unsafe_allow_html=True)
    
    total_spent = df_filtered['amount'].sum()
    months = df_filtered['date'].dt.to_period('M').nunique()
    avg_month = df_filtered.groupby(df_filtered['date'].dt.to_period('M'))['amount'].sum().mean()
    total_transactions = len(df_filtered)
    avg_transaction = df_filtered['amount'].mean()
    unique_categories = df_filtered['category'].nunique()

    kpi_cols = st.columns(5)
    kpi_data = [
        (f"₹{total_spent:,.0f}", "Total Spent"),
        (f"{months}", "Months Analyzed"),
        (f"₹{avg_month:,.0f}", "Avg Monthly"),
        (f"{total_transactions:,}", "Transactions"),
        (f"₹{avg_transaction:,.0f}", "Avg Transaction")
    ]
    
    for col, (value, label) in zip(kpi_cols, kpi_data):
        with col:
            st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-value'>{value}</div>
                <div class='kpi-label'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # Forecasting
    monthly, forecast = forecast_expense(df_filtered, periods=analysis_period)
    
    # Main Dashboard - Two Column Layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly Trend with Forecast
        st.markdown('<div class="section-header">📈 Expense Trends & Forecast</div>', unsafe_allow_html=True)
        if not forecast.empty:
            fig_trend = go.Figure()
            
            # Historical data
            fig_trend.add_trace(go.Scatter(
                x=monthly['ds'], y=monthly['y'],
                mode='lines+markers',
                name='Historical',
                line=dict(color=PRIMARY, width=3),
                marker=dict(size=6, color=PRIMARY)
            ))
            
            # Forecast
            fig_trend.add_trace(go.Scatter(
                x=forecast['ds'], y=forecast['yhat'],
                mode='lines',
                name='Forecast',
                line=dict(color=SECONDARY, width=3, dash='dash')
            ))
            
            # Confidence interval
            fig_trend.add_trace(go.Scatter(
                x=forecast['ds'].tolist() + forecast['ds'].tolist()[::-1],
                y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'].tolist()[::-1],
                fill='toself',
                fillcolor='rgba(5, 150, 105, 0.1)',
                line=dict(color='rgba(255, 255, 255, 0)'),
                name='Confidence Interval',
                showlegend=False
            ))
            
            fig_trend.update_layout(
                title="Monthly Expenses Trend & Forecast",
                xaxis_title="Month",
                yaxis_title="Amount (₹)",
                hovermode="x unified",
                template="plotly_white",
                height=400,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_trend, use_container_width=True)
        else:
            st.info("📊 Not enough data for forecasting. Need at least 3 months of data.")
        
        # Category-wise Spending
        st.markdown('<div class="section-header">🏷 Category Analysis</div>', unsafe_allow_html=True)
        
        cat_col1, cat_col2 = st.columns(2)
        
        with cat_col1:
            # Bar chart
            cat_sum = df_filtered.groupby('category')['amount'].sum().reset_index().sort_values('amount', ascending=False)
            fig_bar = px.bar(
                cat_sum.head(8), x='amount', y='category', 
                orientation='h',
                title="Top Spending Categories",
                color='amount',
                color_continuous_scale=['#EFF6FF', PRIMARY]
            )
            fig_bar.update_layout(
                height=300, 
                showlegend=False,
                xaxis_title="Amount (₹)",
                yaxis_title=""
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with cat_col2:
            # Pie chart
            fig_pie = px.pie(
                cat_sum, values='amount', names='category',
                title="Spending Distribution",
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.Blues_r
            )
            fig_pie.update_layout(height=300)
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Transaction Analysis
        st.markdown('<div class="section-header">💳 Transaction Details</div>', unsafe_allow_html=True)
        
        # Scatter plot of transactions
        fig_scatter = px.scatter(
            df_filtered, x='date', y='amount', color='category',
            size='amount', hover_data=['description'],
            title="Individual Transactions Over Time",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_scatter.update_layout(
            height=300, 
            showlegend=False,
            xaxis_title="Date",
            yaxis_title="Amount (₹)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Daily Spending Pattern
        st.markdown('<div class="section-header">📅 Daily Spending Patterns</div>', unsafe_allow_html=True)
        
        daily_pattern = df_filtered.groupby(df_filtered['date'].dt.day_name())['amount'].sum().reindex([
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])
        
        fig_daily = px.bar(
            x=daily_pattern.index, y=daily_pattern.values,
            title="Spending by Day of Week",
            color=daily_pattern.values,
            color_continuous_scale=['#EFF6FF', PRIMARY]
        )
        fig_daily.update_layout(
            height=300, 
            showlegend=False, 
            xaxis_title="Day", 
            yaxis_title="Amount (₹)"
        )
        st.plotly_chart(fig_daily, use_container_width=True)
    
    # Bottom Section - Full Width
    st.markdown('<div class="section-header">🔍 Deep Analysis</div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Anomaly Detection
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("⚠ Anomaly Detection")
        anomalies = detect_anomalies(df_filtered)
        
        if not anomalies.empty:
            st.write(f"Found {len(anomalies)} unusual transactions:")
            
            # Display top 5 anomalies
            for idx, row in anomalies.head(5).iterrows():
                st.markdown(f"""
                <div class="anomaly-alert">
                    <strong>📅 {row['date'].strftime('%Y-%m-%d')}</strong><br>
                    <strong>💰 ₹{row['amount']:,.0f}</strong> • {row['category']}<br>
                    <em>{row['description']}</em>
                </div>
                """, unsafe_allow_html=True)
            
            if len(anomalies) > 5:
                st.info(f"📋 ... and {len(anomalies) - 5} more anomalies detected")
        else:
            st.success("✅ No anomalies detected in your spending patterns!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        # Smart Insights
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 AI-Powered Insights")
        
        insights = generate_insights(df_filtered, monthly, forecast)
        for insight in insights:
            # Render HTML insights safely
            st.markdown(f'<div class="insight-card">{insight}</div>', unsafe_allow_html=True)
        
        # Additional advanced insights
        if len(df_filtered) > 30:  # Only show if sufficient data
            # Spending velocity
            days_span = (df_filtered['date'].max() - df_filtered['date'].min()).days
            daily_spend_rate = total_spent / days_span if days_span > 0 else 0
            st.markdown(f'<div class="insight-card">⚡ <strong>Daily spend rate:</strong> ₹{daily_spend_rate:,.0f}/day</div>', unsafe_allow_html=True)
            
            # Category diversity
            category_count = df_filtered['category'].nunique()
            st.markdown(f'<div class="insight-card">🎯 <strong>Spreading across:</strong> {category_count} categories</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Download Section
    st.markdown('<div class="section-header">💾 Export & Reports</div>', unsafe_allow_html=True)
    
    dl_col1, dl_col2, dl_col3 = st.columns(3)
    
    with dl_col1:
        csv_clean = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Filtered Data",
            csv_clean,
            "filtered_expenses.csv",
            "text/csv",
            help="Download the filtered transaction data as CSV"
        )
    
    with dl_col2:
        if not forecast.empty:
            csv_forecast = forecast[['ds','yhat','yhat_lower','yhat_upper']].to_csv(index=False).encode('utf-8')
            st.download_button(
                "📊 Download Forecast",
                csv_forecast,
                "expense_forecast.csv",
                "text/csv",
                help="Download the expense forecast data"
            )
        else:
            st.button("📊 Download Forecast", disabled=True, help="Not enough data for forecasting")
    
    with dl_col3:
        # Summary report
        summary_report = f"""
Smart Expense AI - Summary Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}
        
Period: {start_date} to {end_date}
Total Amount: ₹{total_spent:,.0f}
Transactions: {total_transactions:,}
Average Monthly: ₹{avg_month:,.0f}
Categories: {df_filtered['category'].nunique()}
        
Top Categories:
"""
        for cat, amount in df_filtered.groupby('category')['amount'].sum().nlargest(5).items():
            summary_report += f"\n- {cat}: ₹{amount:,.0f}"
        
        st.download_button(
            "📄 Download Summary",
            summary_report,
            "expense_summary.txt",
            "text/plain",
            help="Download a text summary of your expenses"
        )

else:
    st.error("""
    ❌ No valid data to display. 
    
    Please ensure your CSV file contains:
    - A date column (Date, Transaction Date, etc.)
    - An amount column (Amount, Transaction Amount, Debit, Credit, etc.)  
    - Optional: category and description columns
    """)

# Footer
st.markdown("""
<div class="footer">
    💹 Smart Expense AI Dashboard | Built with Streamlit | Advanced Financial Analytics
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Daily Expense Heatmap Calendar
# -------------------------------
st.markdown('<div class="section-header">🗓️ Daily Spending Heatmap</div>', unsafe_allow_html=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Prepare daily spending data
df_filtered['date'] = pd.to_datetime(df_filtered['date'])
daily = df_filtered.groupby('date')['amount'].sum().reset_index()

# Create calendar grid
daily['day'] = daily['date'].dt.day
daily['month'] = daily['date'].dt.month_name().str[:3]
pivot_table = daily.pivot_table(index='month', columns='day', values='amount')

# Sort months in calendar order
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
pivot_table = pivot_table.reindex(month_order)

# Plot the heatmap
plt.figure(figsize=(12, 5))
sns.heatmap(pivot_table, cmap="YlOrRd", linewidths=0.5, linecolor='gray', cbar_kws={'label': 'Total Spent (₹)'})
plt.title('Daily Expense Intensity Calendar', fontsize=16, weight='bold')
plt.xlabel('Day of Month')
plt.ylabel('Month')
st.pyplot(plt)



# -------------------------------
# Simple Text-based Chatbot
# -------------------------------
st.markdown('<div class="section-header">💬 Ask Smart Expense AI Assistant</div>', unsafe_allow_html=True)

# Chat input
user_query = st.text_input("💭 Ask your question (e.g., 'What is my highest expense category?')")

def chat_response(query, df_filtered, monthly, forecast):
    query = query.lower()
    response = "🤖 Sorry, I didn’t quite get that. Try asking about your expenses, categories, or forecast."

    try:
        if "total" in query and "spend" in query:
            response = f"💰 Your total spending for this period is ₹{df_filtered['amount'].sum():,.0f}."

        elif "average" in query and "month" in query:
            avg_month = monthly['y'].mean()
            response = f"📊 Your average monthly spending is ₹{avg_month:,.0f}."

        elif "highest" in query and "category" in query:
            top_cat = df_filtered.groupby('category')['amount'].sum().idxmax()
            top_amt = df_filtered.groupby('category')['amount'].sum().max()
            response = f"🏆 Your highest spending category is **{top_cat}**, totaling ₹{top_amt:,.0f}."

        elif "lowest" in query and "category" in query:
            low_cat = df_filtered.groupby('category')['amount'].sum().idxmin()
            low_amt = df_filtered.groupby('category')['amount'].sum().min()
            response = f"💡 Your lowest spending category is **{low_cat}**, with ₹{low_amt:,.0f} spent."

        elif "forecast" in query or "next month" in query:
            if not forecast.empty:
                next_month = forecast[forecast['ds'] > monthly['ds'].max()]['yhat'].iloc[0]
                response = f"🔮 Your forecasted spending for next month is approximately ₹{next_month:,.0f}."
            else:
                response = "⚠️ Not enough data to forecast expenses."

        elif "anomaly" in query or "unusual" in query:
            anomalies = detect_anomalies(df_filtered)
            if not anomalies.empty:
                count = len(anomalies)
                top_anomaly = anomalies.iloc[0]
                response = f"⚠️ Detected {count} unusual transactions. One example: ₹{top_anomaly['amount']:,.0f} on {top_anomaly['date'].strftime('%Y-%m-%d')} for {top_anomaly['category']}."
            else:
                response = "✅ No anomalies detected in your spending."

        elif "day" in query or "pattern" in query:
            top_day = df_filtered.groupby(df_filtered['date'].dt.day_name())['amount'].sum().idxmax()
            response = f"📅 You usually spend the most on **{top_day}s**."

        elif "category" in query:
            categories = ", ".join(sorted(df_filtered['category'].unique()))
            response = f"🏷 You have spending in the following categories: {categories}."

        elif "help" in query or "what can you do" in query:
            response = """🧠 I can help you with:
- Total or average spending
- Highest or lowest category
- Spending pattern by day
- Forecast for next months
- Detecting anomalies
Try asking: 'Show me forecast for next month' or 'Which category did I spend most on?'"""

    except Exception as e:
        response = f"⚠️ I ran into an issue: {e}"

    return response

if user_query:
    reply = chat_response(user_query, df_filtered, monthly, forecast)
    st.markdown(f"""
    <div class="card" style="margin-top:10px;">
        <strong>🧠 Smart Expense AI:</strong><br>
        {reply}
    </div>
    """, unsafe_allow_html=True)
