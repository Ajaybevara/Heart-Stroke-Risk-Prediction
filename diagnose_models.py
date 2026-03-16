#!/usr/bin/env python3
"""
Diagnostic script for Render deployment - checks model file availability
Run this in Render to debug model loading issues
"""

import os
import sys

def diagnose_model_files():
    """Diagnose model file availability in different locations"""
    print("🔍 Model File Diagnostic for Render")
    print("=" * 50)

    # Check current working directory
    cwd = os.getcwd()
    print(f"📂 Current working directory: {cwd}")

    # List contents of current directory
    try:
        contents = os.listdir('.')
        print(f"📂 Current directory contents: {contents}")
    except Exception as e:
        print(f"❌ Error listing current directory: {e}")

    # Check possible model locations
    possible_paths = [
        'saved_models',
        './saved_models',
        os.path.join(cwd, 'saved_models'),
        '/app/saved_models',
        os.path.join(os.path.dirname(__file__), 'saved_models'),
    ]

    print("\n🔍 Checking possible model locations:")
    for path in possible_paths:
        print(f"\nChecking: {path}")
        if os.path.exists(path):
            print(f"  ✅ Directory exists")
            try:
                files = os.listdir(path)
                print(f"  📂 Contents: {files}")

                # Check for specific model files
                model_files = ['stroke_model_A_original.pkl', 'stroke_model_B_synthetic.pkl', 'feature_info.pkl']
                for model_file in model_files:
                    file_path = os.path.join(path, model_file)
                    if os.path.exists(file_path):
                        size = os.path.getsize(file_path)
                        print(f"    ✅ {model_file} ({size} bytes)")
                    else:
                        print(f"    ❌ {model_file} - MISSING")

            except Exception as e:
                print(f"  ❌ Error accessing directory: {e}")
        else:
            print(f"  ❌ Directory does not exist")

    # Check environment variables
    print("\n🌍 Environment info:")
    print(f"  Python executable: {sys.executable}")
    print(f"  Python path: {sys.path}")
    print(f"  Current file location: {__file__}")

    # Try importing the app module
    print("\n🔄 Testing app import...")
    try:
        import app
        print("  ✅ App module imported successfully")
        try:
            models = app.load_models()
            print("  ✅ Models loaded successfully")
        except Exception as e:
            print(f"  ❌ Model loading failed: {e}")
    except Exception as e:
        print(f"  ❌ App import failed: {e}")

if __name__ == "__main__":
    diagnose_model_files()