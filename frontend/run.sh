#!/bin/bash

# Air Traffic Control Frontend Startup Script

echo "🛫 Starting ATC Frontend Development Server..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the Flask development server
echo "Starting Flask server on http://localhost:5001"
echo "Press Ctrl+C to stop the server"
echo "----------------------------------------"

python app.py