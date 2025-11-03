import requests
import datetime as dt
import time
import random

API_URL = "http://localhost:8000/api/aircraft/update"

# ✈️ Dummy aircraft data
planes = [
    {
        "icao_addr": "GHJ120",
        "callsign": "ROCKET1",
        "lat": 42.28,
        "lon": -83.74,
        "altitude": 28000,
        "ground_speed": 290,
        "heading": 200
    },
    {
        "icao_addr": "NOP180",
        "callsign": "ZENIT18",
        "lat": 36.85,
        "lon": -76.29,
        "altitude": 26000,
        "ground_speed": 275,
        "heading": 175
    },
    {
        "icao_addr": "VWX222",
        "callsign": "SPIRIT3",
        "lat": 25.79,
        "lon": -80.29,
        "altitude": 36000,
        "ground_speed": 330,
        "heading": 270
    },
]


num_cycles = 1
interval = 5   

for i in range(num_cycles):
    print(f"\nCycle {i+1}/{num_cycles}")
    for plane in planes:
        # Slightly move each plane
        plane["lat"] += random.uniform(-0.01, 0.01)
        plane["lon"] += random.uniform(-0.01, 0.01)
        plane["altitude"] += random.uniform(-50, 50)
        plane["ts"] = dt.datetime.utcnow().isoformat() + "Z"

        try:
            response = requests.post(API_URL, json=plane)
            if response.status_code == 200:
                print(f"✅ Updated {plane['callsign']} | lat={plane['lat']:.3f}, lon={plane['lon']:.3f}, alt={plane['altitude']:.0f}")
            else:
                print(f"❌ Error updating {plane['callsign']} ({response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
    time.sleep(interval)

print("\n🏁 Simulation complete. All cycles finished.")
