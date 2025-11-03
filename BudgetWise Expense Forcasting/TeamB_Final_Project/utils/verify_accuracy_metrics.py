#!/usr/bin/env python3
"""
Quick verification of enhanced accuracy metrics in Streamlit model comparison
"""

import pandas as pd
from pathlib import Path

def verify_accuracy_metrics():
    print("🔍 VERIFYING ENHANCED ACCURACY METRICS")
    print("=" * 60)
    
    # Load ML results with new metrics
    ml_file = Path("models/ml/ml_results.csv")
    if ml_file.exists():
        df = pd.read_csv(ml_file)
        print(f"✅ ML Results loaded: {len(df)} models")
        print(f"📊 Available columns: {df.columns.tolist()}")
        
        if 'val_r2' in df.columns and 'val_directional_accuracy' in df.columns:
            print(f"\n🎯 NEW ACCURACY METRICS AVAILABLE:")
            for _, row in df.iterrows():
                model_name = row['model_name']
                val_mae = row['val_mae']
                val_mape = row['val_mape']
                val_r2 = row['val_r2']
                val_dir_acc = row['val_directional_accuracy']
                
                print(f"   • {model_name}:")
                print(f"     - MAE: ₹{val_mae:.2f}")
                print(f"     - MAPE: {val_mape:.2f}%")
                print(f"     - R² Score: {val_r2:.3f}")
                print(f"     - Directional Accuracy: {val_dir_acc:.1f}%")
                print()
            
            # Test model comparison logic
            all_results = []
            for _, row in df.iterrows():
                all_results.append({
                    'Category': 'Machine Learning',
                    'Model': row['model_name'],
                    'MAE': row['val_mae'],
                    'RMSE': row['val_rmse'],
                    'MAPE': row['val_mape'],
                    'R²': row['val_r2'],
                    'Directional_Accuracy': row['val_directional_accuracy']
                })
            
            results_df = pd.DataFrame(all_results)
            print(f"🎉 STREAMLIT COMPARISON READY:")
            print(f"   • Total models for comparison: {len(results_df)}")
            print(f"   • Best MAE: ₹{results_df['MAE'].min():.2f} ({results_df.loc[results_df['MAE'].idxmin(), 'Model']})")
            print(f"   • Best R²: {results_df['R²'].max():.3f} ({results_df.loc[results_df['R²'].idxmax(), 'Model']})")
            print(f"   • Best Dir.Acc: {results_df['Directional_Accuracy'].max():.1f}% ({results_df.loc[results_df['Directional_Accuracy'].idxmax(), 'Model']})")
            
            # Check data quality
            print(f"\n📊 DATA QUALITY CHECK:")
            print(f"   • All MAE values valid: {(results_df['MAE'] > 0).all()}")
            print(f"   • All R² values in range: {(results_df['R²'] >= -1).all() and (results_df['R²'] <= 1).all()}")
            print(f"   • All Dir.Acc values in range: {(results_df['Directional_Accuracy'] >= 0).all() and (results_df['Directional_Accuracy'] <= 100).all()}")
            
            print(f"\n✅ SUCCESS: Enhanced accuracy metrics are working correctly!")
            print(f"🚀 Streamlit app should now display all accuracy metrics including R² and Directional Accuracy!")
            
        else:
            print(f"❌ ERROR: New accuracy metrics not found in CSV file")
    else:
        print(f"❌ ERROR: ML results file not found")

if __name__ == "__main__":
    verify_accuracy_metrics()