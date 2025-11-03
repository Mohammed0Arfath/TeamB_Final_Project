#!/usr/bin/env python3
"""
Test the model loading and comparison logic from Streamlit app
"""

import pandas as pd
from pathlib import Path

def test_model_loading():
    print("🧪 TESTING STREAMLIT MODEL LOADING LOGIC")
    print("=" * 60)
    
    # Simulate the app's model loading
    model_results = {}
    
    result_paths = {
        'Baseline': 'models/baseline/baseline_results.csv',
        'Machine Learning': 'models/ml/ml_results.csv', 
        'Deep Learning': 'models/deep_learning/dl_results.csv',
        'Transformer': 'models/transformer/transformer_results.csv'
    }
    
    for category, file_path in result_paths.items():
        try:
            if Path(file_path).exists():
                if category in ['Machine Learning', 'Deep Learning']:
                    # These have model_name column
                    df = pd.read_csv(file_path)
                else:
                    # These use index as model name
                    df = pd.read_csv(file_path, index_col=0)
                
                model_results[category] = df
                print(f"✅ {category}: {len(df)} models loaded")
                if 'model_name' in df.columns:
                    print(f"   Models: {df['model_name'].tolist()}")
                else:
                    print(f"   Models: {df.index.tolist()}")
        except Exception as e:
            print(f"❌ {category}: Error - {e}")
    
    # Simulate the comparison logic
    print(f"\n🔍 TESTING COMPARISON LOGIC:")
    all_results = []
    
    for category, results_df in model_results.items():
        for model_name, row in results_df.iterrows():
            # Handle different file structures
            if 'model_name' in results_df.columns:
                model_display_name = row.get('model_name', model_name)
            else:
                model_display_name = model_name
            
            mae = row.get('val_mae', row.get('MAE', float('inf')))
            rmse = row.get('val_rmse', row.get('RMSE', float('inf')))
            mape = row.get('val_mape', row.get('MAPE', float('inf')))
            
            all_results.append({
                'Category': category,
                'Model': model_display_name,
                'MAE': mae,
                'RMSE': rmse,
                'MAPE': mape
            })
    
    results_df = pd.DataFrame(all_results)
    
    # Apply filtering logic
    print(f"   📊 Total models before filtering: {len(results_df)}")
    
    # Filter out only completely invalid values (new logic)
    results_df = results_df[results_df['MAE'] != float('inf')]
    results_df = results_df[~results_df['MAE'].isna()]
    results_df = results_df[~results_df['MAPE'].isna()]
    
    print(f"   📊 Total models after filtering: {len(results_df)}")
    
    if len(results_df) > 0:
        # Show extreme MAPE models
        extreme_mape_models = results_df[results_df['MAPE'] > 500]
        print(f"   ⚠️  Models with high MAPE (>500%): {len(extreme_mape_models)}")
        
        # Best model
        best_model_idx = results_df['MAE'].idxmin()
        best_model = results_df.loc[best_model_idx]
        
        print(f"\n🥇 BEST MODEL:")
        print(f"   • Name: {best_model['Model']} ({best_model['Category']})")
        print(f"   • MAE: ₹{best_model['MAE']:,.2f}")
        print(f"   • RMSE: ₹{best_model['RMSE']:,.2f}")
        print(f"   • MAPE: {best_model['MAPE']:.2f}%")
        
        print(f"\n📋 ALL MODELS SUMMARY:")
        for _, row in results_df.iterrows():
            print(f"   • {row['Model']} ({row['Category']}): MAE=₹{row['MAE']:,.2f}, MAPE={row['MAPE']:.1f}%")
        
        print(f"\n✅ SUCCESS: All {len(results_df)} models will be displayed in Streamlit!")
    else:
        print(f"\n❌ ERROR: No valid models found!")

if __name__ == "__main__":
    test_model_loading()