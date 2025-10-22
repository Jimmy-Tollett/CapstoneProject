"""
Flask Backend for ATC Desktop Application
This is the backend API server that provides aircraft data and serves the web UI

Responsibilities:
- Serve HTML templates for the dashboard UI
- Provide REST API endpoints for aircraft data
- Generate mock aircraft data for development/testing
- Serve map tiles for offline capability
- Health check endpoint for Electron to verify server is running

In production, this would connect to a real ASTERIX data source
Currently uses mock data for demonstration purposes

Author: Andrew Moore
Course: Capstone Project - FAA ATC System
"""

# Import Flask modules
from flask import Flask, render_template, jsonify, send_from_directory
# Flask: Main application class
# render_template: Renders Jinja2 HTML templates
# jsonify: Converts Python dictionaries to JSON responses
# send_from_directory: Serves static files from a directory path

import random  # For generating random aircraft positions and attributes
import time    # For generating timestamps
import math    # For trigonometric calculations (circular distribution of aircraft)
import os      # For file path operations

# Create the Flask application instance
# __name__ tells Flask where to find templates and static files
app = Flask(__name__)

# Path for offline map tiles
# Tiles are stored in a 'tiles' directory next to this file
# Structure: tiles/{z}/{x}/{y}.png (z=zoom, x/y=tile coordinates)
TILES_DIR = os.path.join(os.path.dirname(__file__), 'tiles')

# ============================================================================
# Mock Data Generation (Development Only)
# In production, this would be replaced with real ASTERIX data integration
# ============================================================================

def generate_mock_aircraft():
    """
    Generate mock aircraft data for frontend testing
    Creates 8 realistic aircraft positioned around DFW Airport

    Returns:
        list: Array of aircraft dictionaries with position, speed, altitude, etc.
    """
    aircraft = []

    # Real airline callsigns for realism
    # AAL=American Airlines, UAL=United, DAL=Delta, SWA=Southwest,
    # JBU=JetBlue, VRD=Virgin, ANZ=Air New Zealand, BAW=British Airways
    callsigns = ["AAL123", "UAL456", "DAL789", "SWA101", "JBU234", "VRD567", "ANZ890", "BAW111"]

    # Center point: DFW Airport coordinates (Dallas-Fort Worth International Airport)
    center_lat = 32.8998   # Latitude (North-South position)
    center_lon = -97.0403  # Longitude (East-West position)

    # Generate one aircraft for each callsign
    for i, callsign in enumerate(callsigns):
        # Distribute aircraft randomly in a circle around DFW
        # Using polar coordinates (angle + distance) for circular distribution
        angle = random.uniform(0, 2 * math.pi)  # Random angle 0-360° (in radians)
        distance = random.uniform(0.1, 0.8)     # Random distance 0.1-0.8 degrees (~11-88 km)

        # Create aircraft dictionary with all required fields
        aircraft.append({
            "id": i + 1,  # Unique ID (1-8)
            "callsign": callsign,  # Flight identifier

            # Position: Convert polar coordinates (angle, distance) to lat/lon
            # cos(angle) gives x-offset (latitude), sin(angle) gives y-offset (longitude)
            "latitude": center_lat + distance * math.cos(angle),
            "longitude": center_lon + distance * math.sin(angle),

            # Flight parameters with realistic ranges
            "altitude": random.randint(15000, 40000),  # 15,000-40,000 feet (cruise altitude)
            "speed": random.randint(200, 500),         # 200-500 knots (airspeed)
            "heading": random.randint(0, 359),         # 0-359 degrees (compass heading)

            # Common commercial aircraft types
            "aircraft_type": random.choice(["B737", "A320", "B777", "A350", "CRJ9", "E190"]),

            # Current Unix timestamp (seconds since Jan 1, 1970)
            "timestamp": int(time.time())
        })

    return aircraft

# ============================================================================
# Flask Routes (API Endpoints and Web Pages)
# ============================================================================

@app.route('/')
def index():
    """
    Main dashboard page route
    Renders the ATC dashboard HTML template

    Returns:
        str: Rendered HTML from templates/index.html
    """
    # render_template() looks for 'index.html' in the 'templates' directory
    # Flask uses Jinja2 templating engine to process the HTML
    return render_template('index.html')


@app.route('/api/aircraft')
def get_aircraft():
    """
    API endpoint to get current aircraft data
    Called by the frontend every 5 seconds to refresh aircraft positions

    Returns:
        JSON: Array of aircraft objects with position, speed, altitude, etc.
    """
    # Generate fresh mock data and convert to JSON response
    # jsonify() sets the Content-Type header to application/json
    # In production, this would query a real data source instead
    return jsonify(generate_mock_aircraft())


@app.route('/health')
def health():
    """
    Health check endpoint
    Used by Electron main process to verify Flask server is running
    Electron polls this endpoint during startup to know when to create the window

    Returns:
        JSON: Status object indicating server is healthy
    """
    return jsonify({"status": "ok", "service": "atc-frontend"})


@app.route('/tiles/<int:z>/<int:x>/<int:y>.png')
def serve_tiles(z, x, y):
    """
    Serve map tiles from local directory
    Enables offline map functionality by serving pre-downloaded tiles

    URL structure matches standard tile server format:
    /tiles/{zoom}/{x}/{y}.png

    Args:
        z (int): Zoom level (0-19)
        x (int): Tile X coordinate
        y (int): Tile Y coordinate

    Returns:
        File: PNG image if found, 404 error if not found
    """
    try:
        # Build the path to the tile file
        # Example: tiles/9/128/256.png
        tile_path = os.path.join(TILES_DIR, str(z), str(x))
        # send_from_directory() safely serves files from a directory
        # It prevents directory traversal attacks (e.g., ../../etc/passwd)
        return send_from_directory(tile_path, f'{y}.png')
    except Exception as e:
        # If tile not found (file doesn't exist), return 404
        # Frontend will detect this and fallback to online tiles
        print(f"Tile not found: {z}/{x}/{y}.png - {e}")
        return '', 404  # Empty response with 404 status code


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    # This block only runs when executing this file directly (not when imported)
    # Start the Flask development server
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces (allows Electron to connect)
        port=5001,       # Port number (must match FLASK_PORT in electron/main.js)
        debug=True       # Enable debug mode (auto-reload on code changes, detailed errors)
    )
    # Note: In production, use a proper WSGI server like Gunicorn or uWSGI
    # The built-in Flask server is not designed for production use