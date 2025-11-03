#!/usr/bin/env python3
"""
Analyze daily transaction volumes to understand aggregation
"""

import pandas as pd
import numpy as np

def analyze_daily_aggregation():
    print("🔍 Analyzing Daily Transaction Aggregation")
    print("=" * 50)
    
    # Load processed data
    print("📁 Loading processed train data...")
    train_df = pd.read_csv('data/processed/train_data.csv')
    
    # Load cleaned transactions
    print("📁 Loading cleaned transactions...")
    transactions_df = pd.read_csv('data/processed/cleaned_transactions.csv')
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])
    
    # Analyze daily transaction counts
    print(f"\n📊 Daily Transaction Volume Analysis:")
    daily_counts = transactions_df.groupby('date').size()
    print(f"   • Average transactions per day: {daily_counts.mean():.1f}")
    print(f"   • Median transactions per day: {daily_counts.median():.1f}")
    print(f"   • Max transactions per day: {daily_counts.max()}")
    print(f"   • Min transactions per day: {daily_counts.min()}")
    
    # Find days with highest transaction counts
    top_days = daily_counts.nlargest(10)
    print(f"\n🔝 Top 10 days by transaction count:")
    for date, count in top_days.items():
        daily_total = transactions_df[transactions_df['date'] == date]['amount'].sum()
        print(f"   • {date.strftime('%Y-%m-%d')}: {count} transactions, Total: ₹{daily_total:,.2f}")
    
    # Analyze amount distribution in processed data
    print(f"\n💰 Daily Total Analysis:")
    train_df['total_daily_expense'] = pd.to_numeric(train_df['total_daily_expense'], errors='coerce')
    print(f"   • Mean daily expense: ₹{train_df['total_daily_expense'].mean():,.2f}")
    print(f"   • Median daily expense: ₹{train_df['total_daily_expense'].median():,.2f}")
    print(f"   • 95th percentile: ₹{train_df['total_daily_expense'].quantile(0.95):,.2f}")
    print(f"   • 99th percentile: ₹{train_df['total_daily_expense'].quantile(0.99):,.2f}")
    print(f"   • Max daily expense: ₹{train_df['total_daily_expense'].max():,.2f}")
    
    # Check if any individual transactions are still above ₹1 lakh
    print(f"\n🎯 Transaction Capping Verification:")
    max_individual_amount = transactions_df['amount'].max()
    min_individual_amount = transactions_df['amount'].min()
    capped_transactions = transactions_df['amount_capped'].sum() if 'amount_capped' in transactions_df.columns else 0
    
    print(f"   • Max individual transaction: ₹{max_individual_amount:,.2f}")
    print(f"   • Min individual transaction: ₹{min_individual_amount:,.2f}")
    print(f"   • Total capped transactions: {capped_transactions:,}")
    
    # Find the day with maximum expense
    max_expense_idx = train_df['total_daily_expense'].idxmax()
    max_expense_date = train_df.loc[max_expense_idx, 'date']
    max_expense_amount = train_df.loc[max_expense_idx, 'total_daily_expense']
    
    print(f"\n🎯 Highest Expense Day Analysis:")
    print(f"   • Date: {max_expense_date}")
    print(f"   • Total expense: ₹{max_expense_amount:,.2f}")
    
    # Check transactions on that specific day
    max_day_transactions = transactions_df[transactions_df['date'] == pd.to_datetime(max_expense_date)]
    if len(max_day_transactions) > 0:
        print(f"   • Number of transactions: {len(max_day_transactions)}")
        print(f"   • Average per transaction: ₹{max_day_transactions['amount'].mean():,.2f}")
        print(f"   • Transactions at ₹1 lakh cap: {(max_day_transactions['amount'] == 100000).sum()}")
        
        # Show transaction breakdown
        print(f"   • Transaction amount distribution:")
        print(f"     - Under ₹10,000: {(max_day_transactions['amount'] < 10000).sum()}")
        print(f"     - ₹10,000-₹50,000: {((max_day_transactions['amount'] >= 10000) & (max_day_transactions['amount'] < 50000)).sum()}")
        print(f"     - ₹50,000-₹99,999: {((max_day_transactions['amount'] >= 50000) & (max_day_transactions['amount'] < 100000)).sum()}")
        print(f"     - Exactly ₹1,00,000: {(max_day_transactions['amount'] == 100000).sum()}")

if __name__ == "__main__":
    analyze_daily_aggregation()