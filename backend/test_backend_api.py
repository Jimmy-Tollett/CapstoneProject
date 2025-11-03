import requests
import datetime as dt
from zoneinfo import ZoneInfo

API = "http://localhost:8000"
API_KEY = ""

headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}

def to_cst(utc_str):
    """Convert RFC 1123 or ISO UTC time string to CST (America/Chicago)."""
    try:
        # Handle RFC 1123 format: 'Mon, 13 Oct 2025 15:25:51 GMT'
        utc_time = dt.datetime.strptime(utc_str, "%a, %d %b %Y %H:%M:%S GMT")
        utc_time = utc_time.replace(tzinfo=dt.timezone.utc)
        return utc_time.astimezone(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    except Exception:
        try:
            # Handle ISO format fallback: '2025-10-13T15:25:51Z'
            utc_time = dt.datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
            return utc_time.astimezone(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
        except Exception:
            return utc_str  # if it’s some unexpected format, just return as-is

def get_aircraft(active_minutes=10080):  
    r = requests.get(f"{API}/api/aircraft",
                     params={"active_minutes": active_minutes},
                     headers=headers)
    r.raise_for_status()
    return r.json()

def get_grouped_tracks(minutes=10080, per_plane=50):  
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=minutes)).isoformat()
    r = requests.get(f"{API}/api/tracks/grouped",
                     params={"since": since, "per_plane": per_plane},
                     headers=headers)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    print("🛩 Active aircraft:")
    aircraft = get_aircraft()
    for plane in aircraft:
        if "last_seen" in plane:
            plane["last_seen"] = to_cst(plane["last_seen"])
        print(plane)

    print("\n📡 Grouped tracks:")
    grouped = get_grouped_tracks()
    for callsign, points in grouped.items():
        print(f"\n✈️ {callsign}")
        for p in points:
            p["ts"] = to_cst(p["ts"])
            print(p)
