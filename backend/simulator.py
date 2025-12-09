import requests
import datetime as dt
import time
import random

API_URL = "http://localhost:8000/api/aircraft/update"

# ✈️ Dummy aircraft data (around Oklahoma City area)
# ✈️ Dummy aircraft data (around Oklahoma City area)
planes = [
    {
        "icao_addr": "GHJ120",
        "callsign": "ROCKET1",
        "lat": 35.52,
        "lon": -97.45,
        "lat": 35.52,
        "lon": -97.45,
        "altitude": 28000,
        "ground_speed": 290,
        "heading": 200
    },
    {
        "icao_addr": "NOP180",
        "callsign": "ZENIT18",
        "lat": 35.38,
        "lon": -97.60,
        "lat": 35.38,
        "lon": -97.60,
        "altitude": 26000,
        "ground_speed": 275,
        "heading": 175
    },
    {
        "icao_addr": "VWX222",
        "callsign": "SPIRIT3",
        "lat": 35.55,
        "lon": -97.35,
        "lat": 35.55,
        "lon": -97.35,
        "altitude": 36000,
        "ground_speed": 330,
        "heading": 270
    },
]

def simulate(num_cycles, interval):
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

if __name__ == "__main__":
    simulate(num_cycles=20, interval=5)