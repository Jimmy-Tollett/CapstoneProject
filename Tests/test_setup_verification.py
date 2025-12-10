#!/usr/bin/env python3
"""
Quick test to verify the testing environment is set up correctly
Run with: python test_setup_verification.py
"""

import sys
import subprocess
import importlib

def check_python_version():
    """Check Python version compatibility"""
    print(f"✅ Python version: {sys.version}")
    if sys.version_info >= (3, 8):
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python version should be 3.8 or higher")
        return False

def check_virtual_environment():
    """Check if running in virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        return True
    else:
        print("❌ Not running in virtual environment")
        return False

def check_required_packages():
    """Check if required testing packages are installed"""
    required_packages = [
        'pytest',
        'requests', 
        'psycopg2',
        'docker'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package.replace('-', '_'))
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def check_pytest_functionality():
    """Check if pytest can discover and run tests"""
    try:
        # Use the correct python executable path for the virtual environment
        python_path = sys.executable
        result = subprocess.run([python_path, '-m', 'pytest', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ pytest is working: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ pytest failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running pytest: {e}")
        return False

def main():
    """Run all verification checks"""
    print("🔍 Verifying test environment setup...\n")
    
    checks = [
        check_python_version(),
        check_virtual_environment(),
        check_required_packages(),
        check_pytest_functionality()
    ]
    
    if all(checks):
        print("\n🎉 Test environment is ready!")
        print("\n📝 Next steps:")
        print("1. Run: pytest tests/unit/test_parser.py -v")
        print("2. Start implementing the TODO items in test functions")
        print("3. Use: pytest tests/ --cov=app for coverage reporting")
    else:
        print("\n❌ Some issues found. Please fix them before proceeding.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())