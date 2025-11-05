#!/usr/bin/env python3
"""
BudgetWise AI - Project Restructuring Script
Automates the reorganization of project files into professional structure

Run this script from the project root directory:
    python restructure_project.py
"""

import os
import shutil
from pathlib import Path

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_step(msg):
    print(f"{Colors.BLUE}[STEP]{Colors.END} {msg}")

def print_success(msg):
    print(f"{Colors.GREEN}[✓]{Colors.END} {msg}")

def print_warning(msg):
    print(f"{Colors.YELLOW}[!]{Colors.END} {msg}")

def print_error(msg):
    print(f"{Colors.RED}[✗]{Colors.END} {msg}")

def create_directory(path):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)
    return path

def move_file_safe(src, dst):
    """Move file safely, creating destination directory if needed"""
    try:
        if not os.path.exists(src):
            print_warning(f"Source not found: {src}")
            return False
        
        dst_path = Path(dst)
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        
        if os.path.exists(dst):
            print_warning(f"Destination exists, skipping: {dst}")
            return False
        
        shutil.move(src, dst)
        print_success(f"Moved: {src} → {dst}")
        return True
    except Exception as e:
        print_error(f"Failed to move {src}: {e}")
        return False

def main():
    """Main restructuring function"""
    
    print("\n" + "="*70)
    print("   BudgetWise AI - Project Restructuring Script")
    print("="*70 + "\n")
    
    # Confirm execution
    response = input("This will reorganize your project structure. Continue? (y/n): ")
    if response.lower() != 'y':
        print("Restructuring cancelled.")
        return
    
    print("\n")
    
    # Step 1: Create necessary directories
    print_step("Creating directory structure...")
    
    directories = [
        "scripts/data_generation",
        "scripts/validation",
        "scripts/setup",
        "docs/user_guides",
        "docs/developer_guides",
        "docs/troubleshooting",
        "docs/quick_references",
        "tests/fixtures",
        "utils/data",
        "utils/models",
        "utils/validation",
        "utils/analysis",
    ]
    
    for directory in directories:
        create_directory(directory)
        print_success(f"Created: {directory}/")
    
    print("\n")
    
    # Step 2: Move test/debug files
    print_step("Reorganizing test and debug files...")
    
    moves = [
        ("test_model_detection.py", "tests/test_model_detection.py"),
        ("debug_models.py", "utils/models/debug_models.py"),
    ]
    
    for src, dst in moves:
        move_file_safe(src, dst)
    
    print("\n")
    
    # Step 3: Move scripts
    print_step("Reorganizing scripts...")
    
    script_moves = [
        ("generate_test_csv.py", "scripts/data_generation/generate_test_csv.py"),
        ("validate_test_csv.py", "scripts/validation/validate_test_csv.py"),
        ("setup_ai_chat.py", "scripts/setup/setup_ai_chat.py"),
    ]
    
    for src, dst in script_moves:
        move_file_safe(src, dst)
    
    print("\n")
    
    # Step 4: Move documentation
    print_step("Reorganizing documentation...")
    
    doc_moves = [
        ("CSV_UPLOAD_GUIDE.md", "docs/user_guides/CSV_UPLOAD_GUIDE.md"),
        ("CSV_UPLOAD_QUICK_REF.md", "docs/quick_references/CSV_UPLOAD_QUICK_REF.md"),
        ("FIX_ZERO_PREDICTIONS.md", "docs/troubleshooting/FIX_ZERO_PREDICTIONS.md"),
        ("CSV_UPLOAD_FEATURE_SUMMARY.md", "docs/troubleshooting/CSV_UPLOAD_FEATURE_SUMMARY.md"),
    ]
    
    # Move from app/ if they exist there
    app_doc_moves = [
        ("app/USER_MANUAL.md", "docs/user_guides/USER_MANUAL.md"),
        ("app/DEPLOYMENT_GUIDE.md", "docs/user_guides/DEPLOYMENT_GUIDE.md"),
    ]
    
    for src, dst in doc_moves + app_doc_moves:
        move_file_safe(src, dst)
    
    print("\n")
    
    # Step 5: Organize utils
    print_step("Reorganizing utils directory...")
    
    utils_moves = [
        ("utils/analyze_daily_aggregation.py", "utils/analysis/analyze_daily_aggregation.py"),
        ("utils/analyze_amounts.py", "utils/analysis/analyze_amounts.py"),
        ("utils/analyze_ml_results.py", "utils/analysis/analyze_ml_results.py"),
        ("utils/capping_analysis.py", "utils/analysis/capping_analysis.py"),
        ("utils/enhancement_summary.py", "utils/analysis/enhancement_summary.py"),
        
        ("utils/check_data_stats.py", "utils/data/check_data_stats.py"),
        ("utils/test_capping.py", "utils/data/test_capping.py"),
        ("utils/test_data_loading.py", "utils/data/test_data_loading.py"),
        
        ("utils/check_all_models.py", "utils/models/check_all_models.py"),
        ("utils/test_streamlit_models.py", "utils/models/test_streamlit_models.py"),
        ("utils/get_model_results.py", "utils/models/get_model_results.py"),
        
        ("utils/verify_accuracy_metrics.py", "utils/validation/verify_accuracy_metrics.py"),
        ("utils/final_verification.py", "utils/validation/final_verification.py"),
    ]
    
    for src, dst in utils_moves:
        move_file_safe(src, dst)
    
    print("\n")
    
    # Step 6: Create __init__.py files
    print_step("Creating __init__.py files...")
    
    init_dirs = [
        "tests",
        "utils",
        "utils/data",
        "utils/models",
        "utils/validation",
        "utils/analysis",
        "scripts/data_generation",
        "scripts/validation",
        "scripts/setup",
    ]
    
    for directory in init_dirs:
        init_file = Path(directory) / "__init__.py"
        if not init_file.exists():
            init_file.write_text(f'"""BudgetWise AI - {directory.replace("/", ".")}"""\n')
            print_success(f"Created: {init_file}")
    
    print("\n")
    
    # Step 7: Create .gitkeep files for empty directories
    print_step("Creating .gitkeep files...")
    
    gitkeep_dirs = [
        "data/raw",
        "data/processed",
        "data/features",
        "models/baseline",
        "models/ml",
        "models/deep_learning",
        "models/transformer",
        "logs",
        "reports",
        "tests/fixtures",
    ]
    
    for directory in gitkeep_dirs:
        gitkeep_file = Path(directory) / ".gitkeep"
        if not gitkeep_file.exists():
            create_directory(directory)
            gitkeep_file.write_text("")
            print_success(f"Created: {gitkeep_file}")
    
    print("\n")
    
    # Step 8: Summary
    print("="*70)
    print("   Restructuring Complete!")
    print("="*70)
    print("\nNext Steps:")
    print("1. Review the changes")
    print("2. Update import statements in your code if needed")
    print("3. Run tests to ensure everything works: pytest")
    print("4. Update requirements.txt: pip freeze > requirements.txt")
    print("5. Commit the changes: git add . && git commit -m 'Restructure project'")
    print("\nFor detailed analysis, see: PROJECT_STRUCTURE_ANALYSIS.md")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nRestructuring cancelled by user.")
    except Exception as e:
        print_error(f"An error occurred: {e}")
        print("Please check PROJECT_STRUCTURE_ANALYSIS.md for manual instructions.")
