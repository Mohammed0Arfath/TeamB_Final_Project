#!/usr/bin/env python3
"""Get latest model performance results for README update"""

import pandas as pd
import numpy as np

def get_model_results():
    print('🏆 UPDATED MODEL PERFORMANCE RESULTS (With R² & Directional Accuracy)')
    print('=' * 80)

    try:
        # Load all model results
        baseline_df = pd.read_csv('models/baseline/baseline_results.csv')
        ml_df = pd.read_csv('models/ml/ml_results.csv')
        dl_df = pd.read_csv('models/deep_learning/dl_results.csv')
        transformer_df = pd.read_csv('models/transformer/transformer_results.csv')
        
        print('\n📊 BASELINE MODELS:')
        for _, row in baseline_df.iterrows():
            print(f'   • {row["model_name"]}: MAE=₹{row["val_mae"]:,.2f}, MAPE={row["val_mape"]:.2f}%, R²={row["val_r2"]:.3f}, Dir.Acc={row["val_directional_accuracy"]:.1f}%')
        
        print('\n🤖 MACHINE LEARNING MODELS:')
        for _, row in ml_df.iterrows():
            print(f'   • {row["model_name"]}: MAE=₹{row["val_mae"]:,.2f}, MAPE={row["val_mape"]:.2f}%, R²={row["val_r2"]:.3f}, Dir.Acc={row["val_directional_accuracy"]:.1f}%')
        
        print('\n🧠 DEEP LEARNING MODELS:')
        for _, row in dl_df.iterrows():
            mape_str = f'{row["val_mape"]:.2e}' if row["val_mape"] > 1000 else f'{row["val_mape"]:.2f}'
            print(f'   • {row["model_name"]}: MAE=₹{row["val_mae"]:.2f}, MAPE={mape_str}%, R²={row["val_r2"]:.3f}, Dir.Acc={row["val_directional_accuracy"]:.1f}%')
        
        print('\n🔮 TRANSFORMER MODELS:')
        for idx, row in transformer_df.iterrows():
            print(f'   • {idx}: MAE=₹{row["val_mae"]:,.2f}, MAPE={row["val_mape"]:.2f}%, R²={row["val_r2"]:.3f}, Dir.Acc={row["val_directional_accuracy"]:.1f}%')
        
        # Find best models by category
        best_models = []
        
        # Baseline
        if len(baseline_df) > 0:
            best_baseline = baseline_df.loc[baseline_df['val_mae'].idxmin()]
            best_models.append({
                'rank': 1, 'category': 'Baseline', 'name': best_baseline['model_name'],
                'mae': best_baseline['val_mae'], 'mape': best_baseline['val_mape'],
                'r2': best_baseline['val_r2'], 'dir_acc': best_baseline['val_directional_accuracy']
            })
        
        # ML
        if len(ml_df) > 0:
            best_ml = ml_df.loc[ml_df['val_mae'].idxmin()]
            best_models.append({
                'rank': 2, 'category': 'ML', 'name': best_ml['model_name'],
                'mae': best_ml['val_mae'], 'mape': best_ml['val_mape'],
                'r2': best_ml['val_r2'], 'dir_acc': best_ml['val_directional_accuracy']
            })
        
        # Deep Learning
        if len(dl_df) > 0:
            best_dl = dl_df.loc[dl_df['val_mae'].idxmin()]
            best_models.append({
                'rank': 3, 'category': 'Deep Learning', 'name': best_dl['model_name'],
                'mae': best_dl['val_mae'], 'mape': best_dl['val_mape'],
                'r2': best_dl['val_r2'], 'dir_acc': best_dl['val_directional_accuracy']
            })
        
        # Transformer
        if len(transformer_df) > 0:
            best_transformer = transformer_df.loc[transformer_df['val_mae'].idxmin()]
            best_models.append({
                'rank': 4, 'category': 'Transformer', 'name': best_transformer.name,
                'mae': best_transformer['val_mae'], 'mape': best_transformer['val_mape'],
                'r2': best_transformer['val_r2'], 'dir_acc': best_transformer['val_directional_accuracy']
            })
        
        # Sort by MAE (best performance)
        best_models.sort(key=lambda x: x['mae'])
        
        print('\n🏆 CHAMPION MODEL RANKING (by MAE):')
        emojis = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣']
        for i, model in enumerate(best_models):
            emoji = emojis[i] if i < len(emojis) else f'{i+1}️⃣'
            mae_str = f"₹{model['mae']:,.2f}"
            mape_str = f"{model['mape']:.2f}%" if model['mape'] < 1000 else f"{model['mape']:.2e}%"
            print(f'   {emoji} {model["name"]} ({model["category"]}): MAE={mae_str}, MAPE={mape_str}, R²={model["r2"]:.3f}, Dir.Acc={model["dir_acc"]:.1f}%')
        
        # Champion model details
        champion = best_models[0]
        print(f'\n🏆 CHAMPION MODEL: {champion["name"]}')
        print(f'   • MAE: ₹{champion["mae"]:,.2f}')
        print(f'   • MAPE: {champion["mape"]:.2f}%')
        print(f'   • R² Score: {champion["r2"]:.3f}')
        print(f'   • Directional Accuracy: {champion["dir_acc"]:.1f}%')
        print(f'   • Category: {champion["category"]}')
        
        return best_models
        
    except Exception as e:
        print(f'❌ Error loading results: {e}')
        return []

if __name__ == "__main__":
    results = get_model_results()