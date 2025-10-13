from flask import Flask, render_template, jsonify, send_from_directory
import random
import time
import math
import os

app = Flask(__name__)

# Path for offline map tiles
TILES_DIR = os.path.join(os.path.dirname(__file__), 'tiles')

# Mock aircraft data for development
def generate_mock_aircraft():
    """Generate mock aircraft data for frontend testing"""
    aircraft = []
    callsigns = ["AAL123", "UAL456", "DAL789", "SWA101", "JBU234", "VRD567", "ANZ890", "BAW111"]
    
    # Generate aircraft around a central area (roughly around DFW airport coordinates)
    center_lat = 32.8998
    center_lon = -97.0403
    
    for i, callsign in enumerate(callsigns):
        # Random position within ~50 mile radius
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0.1, 0.8)  # degrees
        
        aircraft.append({
            "id": i + 1,
            "callsign": callsign,
            "latitude": center_lat + distance * math.cos(angle),
            "longitude": center_lon + distance * math.sin(angle),
            "altitude": random.randint(15000, 40000),
            "speed": random.randint(200, 500),
            "heading": random.randint(0, 359),
            "aircraft_type": random.choice(["B737", "A320", "B777", "A350", "CRJ9", "E190"]),
            "timestamp": int(time.time())
        })
    
    return aircraft

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/aircraft')
def get_aircraft():
    """API endpoint to get current aircraft data"""
    return jsonify(generate_mock_aircraft())

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "service": "atc-frontend"})

@app.route('/tiles/<int:z>/<int:x>/<int:y>.png')
def serve_tiles(z, x, y):
    """Serve map tiles from local directory"""
    try:
        tile_path = os.path.join(TILES_DIR, str(z), str(x))
        return send_from_directory(tile_path, f'{y}.png')
    except Exception as e:
        # Return 404 if tile not found - frontend will fallback to online
        print(f"Tile not found: {z}/{x}/{y}.png - {e}")
        return '', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)