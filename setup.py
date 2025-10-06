"""
Budget Tool MVP - Setup and Quick Start Script
Automates the initial setup and provides guided quick start options.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import shutil

def print_banner():
    """Print welcome banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║               💰 Budget Tool MVP 💰                         ║
    ║                                                              ║
    ║        AI-Powered Expense Forecasting & Budget Tool         ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required!")
        print(f"   Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_directories():
    """Create necessary project directories."""
    print("📁 Creating project directories...")
    
    directories = [
        "data/raw",
        "artifacts/logs",
        "artifacts/models",
        "features/outputs",
        "recommendations",
        "logs"  # Fallback if not in artifacts
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✓ Created {directory}")
    
    print("✅ All directories created successfully!")

def install_dependencies(install_all=False):
    """Install Python dependencies."""
    print("📦 Installing dependencies...")
    
    # Basic requirements
    basic_deps = [
        "pandas>=2.0.0",
        "numpy>=1.24.0", 
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.15.0",
        "streamlit>=1.28.0",
        "pyyaml>=6.0",
        "joblib>=1.3.0"
    ]
    
    # Advanced ML/DL dependencies (optional)
    advanced_deps = [
        "xgboost>=1.7.0",
        "lightgbm>=4.0.0",
        "tensorflow>=2.13.0",
        "torch>=2.0.0",
        "prophet>=1.1.0",
        "statsmodels>=0.14.0"
    ]
    
    try:
        # Install basic dependencies
        print("   Installing basic dependencies...")
        for dep in basic_deps:
            subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                          check=True, capture_output=True)
        
        print("✅ Basic dependencies installed successfully!")
        
        if install_all:
            print("   Installing advanced ML/DL dependencies...")
            for dep in advanced_deps:
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                                  check=True, capture_output=True)
                    print(f"   ✓ Installed {dep}")
                except subprocess.CalledProcessError as e:
                    print(f"   ⚠️  Failed to install {dep}: {e}")
            
            print("✅ Advanced dependencies installation completed!")
        else:
            print("ℹ️  Use --install-all flag to install advanced ML/DL dependencies")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_sample_data():
    """Set up sample data if no data exists."""
    raw_data_path = Path("data/raw")
    
    # Check if user has their own data
    existing_files = list(raw_data_path.glob("*.csv"))
    
    if existing_files:
        print(f"✅ Found existing data files: {[f.name for f in existing_files]}")
        return True
    
    print("📊 Setting up sample data...")
    
    # Check if we have the original dataset
    original_files = [
        "data/budgetwise_finance_dataset.csv",
        "budgetwise_finance_dataset.csv",
        "../budgetwise_finance_dataset.csv"
    ]
    
    source_file = None
    for file_path in original_files:
        if Path(file_path).exists():
            source_file = Path(file_path)
            break
    
    if source_file:
        # Copy to raw data directory
        dest_file = raw_data_path / "budgetwise_finance_dataset.csv"
        shutil.copy2(source_file, dest_file)
        print(f"✅ Copied sample data to {dest_file}")
        return True
    else:
        print("⚠️  No sample data found. Please add your financial data to data/")
        print("   Supported format: CSV with columns like 'date', 'amount', 'category', 'transaction_type'")
        return False

def run_initial_setup():
    """Run initial data processing setup."""
    print("🔄 Running initial data processing...")
    
    try:
        # Add src to path
        sys.path.append(str(Path("src")))
        
        # Import and run components
        from components.data_ingestion import DataIngestion
        from components.data_preprocessing import DataPreprocessing
        from components.feature_engineering import FeatureEngineering
        from components.budget_recommendation import BudgetRecommendation
        
        # Initialize and run ingestion
        print("   Running data ingestion...")
        DATA_PATH = "data/budgetwise_finance_dataset.csv"
        if Path(DATA_PATH).exists():
            ingestion = DataIngestion(data_path=DATA_PATH)
            ingestion.initiate_data_ingestion()
        else:
            print("⚠️  Sample data not found. Skipping ingestion.")
            return False
        
        # Preprocessing
        print("   Running data preprocessing...")
        preprocessor = DataPreprocessing()
        preprocessor.initiate_preprocessing()
        
        # Feature engineering
        print("   Running feature engineering...")
        engineer = FeatureEngineering()
        engineer.initiate_engineering()
        
        # Budget recommendations
        print("   Generating budget recommendations...")
        recommender = BudgetRecommendation()
        recommender.initiate_recommendations()
        
        print("✅ Initial data processing completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error in initial setup: {e}")
        print("   You can run this manually later with: python src/components/data_ingestion.py")
        return False

def create_quick_start_script():
    """Create a quick start script."""
    script_content = """#!/usr/bin/env python3
'''
Budget Tool MVP - Quick Start Script
'''

import subprocess
import sys
from pathlib import Path

def main():
    print("🚀 Budget Tool MVP Quick Start")
    print("=============================")
    
    # Run model training
    print("\\n1. Training models (this may take a while)...")
    subprocess.run([sys.executable, "src/models/baseline.py"], check=False)
    subprocess.run([sys.executable, "src/models/ml_model.py"], check=False)
    subprocess.run([sys.executable, "src/models/dl_model.py"], check=False)
    # Uncomment for transformers: subprocess.run([sys.executable, "src/models/transformers.py"], check=False)
    
    # Run evaluation
    print("\\n2. Evaluating models...")
    subprocess.run([sys.executable, "src/evaluation/model_evaluation.py"], check=False)
    
    # Start Streamlit dashboard
    print("\\n3. Starting Streamlit dashboard...")
    print("   Dashboard will open in your browser at http://localhost:8501")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=False)

if __name__ == "__main__":
    main()
"""
    
    script_path = Path("quick_start.py")
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make executable on Unix systems
    if os.name != 'nt':
        script_path.chmod(0o755)
    
    print(f"✅ Created quick start script: {script_path}")

def display_next_steps():
    """Display next steps for the user."""
    next_steps = """
    
    🎉 Setup Complete! Here are your next steps:
    
    📊 QUICK START (Recommended):
    ┌─────────────────────────────────────────────────────────────┐
    │  python quick_start.py                                      │
    └─────────────────────────────────────────────────────────────┘
    
    📝 MANUAL STEPS:
    
    1️⃣  Add your financial data:
       • Place CSV files in data/ directory
       • Required columns: date, amount, category, transaction_type
    
    2️⃣  Process data:
       • Ingestion: python src/components/data_ingestion.py
       • Preprocessing: python src/components/data_preprocessing.py
       • Feature Engineering: python src/components/feature_engineering.py
       • Recommendations: python src/components/budget_recommendation.py
    
    3️⃣  Train models:
       • Baseline: python src/models/baseline.py
       • ML: python src/models/ml_model.py
       • DL: python src/models/dl_model.py
       • Transformers: python src/models/transformers.py (requires PyTorch)
    
    4️⃣  Evaluate models:
       • python src/evaluation/model_evaluation.py
    
    5️⃣  Launch the dashboard:
       • streamlit run app.py
       • Opens at http://localhost:8501
    
    🔧 CONFIGURATION:
       • Edit config.yaml to customize settings
       • Adjust model parameters, data paths, etc.
    
    📚 DOCUMENTATION:
       • README.md - Complete project documentation
    
    ❓ NEED HELP?
       • Check artifacts/logs/ directory for detailed logs
       • Review artifacts/evaluation_results.csv for model results
    """
    
    print(next_steps)

def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(description="Budget Tool MVP Setup")
    parser.add_argument("--install-all", action="store_true", 
                       help="Install all dependencies including advanced ML/DL libraries")
    parser.add_argument("--skip-deps", action="store_true",
                       help="Skip dependency installation")
    parser.add_argument("--skip-data", action="store_true",
                       help="Skip initial data processing")
    
    args = parser.parse_args()
    
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not args.skip_deps:
        if not install_dependencies(args.install_all):
            print("⚠️  Dependency installation had issues. You may need to install manually.")
    
    # Setup sample data
    setup_sample_data()
    
    # Create quick start script
    create_quick_start_script()
    
    # Run initial setup
    if not args.skip_data:
        run_initial_setup()
    
    # Display next steps
    display_next_steps()
    
    print("🎉 Budget Tool MVP setup completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())