#!/bin/bash
# Activation script for the testing environment
# Usage: source activate_test_env.sh

# Activate the virtual environment
source ../venv/bin/activate

# Set environment variables for testing
export $(grep -v '^#' .env.test | xargs)

# Show current Python environment
echo "✅ Python virtual environment activated!"
echo "Python path: $(which python)"
echo "Python version: $(python --version)"
echo "Pip packages installed: $(pip list | wc -l) packages"

# Show available pytest commands
echo ""
echo "🧪 Available test commands:"
echo "  pytest tests/unit/              # Run unit tests"
echo "  pytest tests/integration/       # Run integration tests"
echo "  pytest tests/ -m unit           # Run only unit test markers"
echo "  pytest tests/ --cov=app         # Run with coverage"
echo "  pytest tests/ --html=report.html # Generate HTML report"
echo ""
echo "💡 To deactivate: deactivate"