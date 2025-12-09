import os, socket, psycopg
from flask import Flask, request, jsonify
from flask_cors import CORS
from simulator import simulate



DB_URL = os.getenv("DB_URL", "postgresql+psycopg://atc:atcpass@db:5432/adsb")
PORT = int(os.getenv("PORT", "8000"))

# psycopg connection string for 'psycopg' must not include the SQLAlchemy prefix
# so we normalize if the user passed postgresql+psycopg://
DB_URL_PG = DB_URL.replace("postgresql+psycopg://", "postgresql://")

app = Flask(__name__)
CORS(app)

def q(query, params=None, one=False):
    with psycopg.connect(DB_URL_PG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params or [])
            if cur.description:
                cols = [c.name for c in cur.description]
                rows = [dict(zip(cols, r)) for r in cur.fetchall()]
                return (rows[0] if rows else None) if one else rows
            return None

@app.get("/health")
def health():
    status = {
        "status": "ok",
        "database": {
            "url": DB_URL.split("@")[1].split("/")[0],  # Safe way to show host:port
            "resolved_ip": None,
            "error": None
        }
    }
    
    try:
        # Try to resolve DB hostname
        db_host = DB_URL.split("@")[1].split(":")[0]
        status["database"]["resolved_ip"] = socket.gethostbyname(db_host)
    except Exception as e:
        status["database"]["error"] = str(e)
        return jsonify(status), 503  # Service Unavailable
    
    return jsonify(status)


@app.get("/api/aircraft")
def get_aircraft():
    active_minutes = int(request.args.get("active_minutes", 5))
    rows = q("""
    SELECT callsign, icao_addr, lat, lon, ground_speed, heading, altitude, last_seen
    FROM aircraft_latest
    WHERE last_seen >= NOW() - make_interval(mins => %s)
    ORDER BY last_seen DESC
""", [active_minutes])

    return jsonify(rows)

@app.get("/api/aircraft/<icao>")
def get_one_aircraft(icao):
    since = request.args.get("since")    # ISO8601
    limit = int(request.args.get("limit", 300))

    latest = q("""
        SELECT callsign, icao_addr, lat, lon, ground_speed, heading, altitude, last_seen
        FROM aircraft_latest WHERE icao_addr = %s
    """, [icao.upper()], one=True)

    if since:
        positions = q("""
            SELECT icao_addr, ts, lat, lon, ground_speed, heading, altitude
            FROM aircraft_positions
            WHERE icao_addr = %s AND ts >= %s
            ORDER BY ts ASC
            LIMIT %s
        """, [icao.upper(), since, limit])
    else:
        positions = q("""
            SELECT icao_addr, ts, lat, lon, ground_speed, heading, altitude
            FROM aircraft_positions
            WHERE icao_addr = %s
            ORDER BY ts DESC
            LIMIT %s
        """, [icao.upper(), limit])

    return jsonify({"latest": latest, "positions": positions})

@app.get("/api/tracks/grouped")
def get_tracks_grouped():
    since = request.args.get("since")
    if not since:
        return {"error": "missing 'since' query param (ISO8601)"}, 400

    icao = request.args.get("icao")
    bbox = request.args.get("bbox")
    try:
        per_plane = min(int(request.args.get("per_plane", 50)), 2000)
    except ValueError:
        return {"error": "invalid 'per_plane' param"}, 400

    where = ["ap.ts >= %s::timestamptz"]
    params = [since]

    if icao:
        icao = icao.strip().upper()[:6]
        where.append("ap.icao_addr = %s")
        params.append(icao)

    if bbox:
        try:
            minLon, minLat, maxLon, maxLat = map(float, bbox.split(","))
        except Exception:
            return {"error": "invalid bbox; use minLon,minLat,maxLon,maxLat"}, 400
        if not (-180 <= minLon <= 180 and -180 <= maxLon <= 180 and -90 <= minLat <= 90 and -90 <= maxLat <= 90):
            return {"error": "bbox out of range"}, 400
        if minLat > maxLat:
            return {"error": "bbox minLat must be <= maxLat"}, 400

        if minLon <= maxLon:
            where.append("ap.lon BETWEEN %s AND %s AND ap.lat BETWEEN %s AND %s")
            params.extend([minLon, maxLon, minLat, maxLat])
        else:
            # crosses the anti-meridian
            where.append("""(
                (ap.lon BETWEEN %s AND 180 AND ap.lat BETWEEN %s AND %s)
                OR
                (ap.lon BETWEEN -180 AND %s AND ap.lat BETWEEN %s AND %s)
            )""")
            params.extend([minLon, minLat, maxLat, maxLon, minLat, maxLat])

    where_sql = " AND ".join(where)

    query = f"""
        WITH base AS (
            SELECT ap.icao_addr, ap.ts, ap.lat, ap.lon, ap.ground_speed, ap.heading, ap.altitude
            FROM aircraft_positions ap
            WHERE {where_sql}
        ),
        ranked AS (
            SELECT *,
                   ROW_NUMBER() OVER (PARTITION BY icao_addr ORDER BY ts ASC) AS rn
            FROM base
        )
        SELECT icao_addr, ts, lat, lon, ground_speed, heading, altitude
        FROM ranked
        WHERE rn <= %s
        ORDER BY icao_addr ASC, ts ASC
    """

    params_all = [*params, per_plane]
    rows = q(query, params_all)

    grouped = {}
    for r in rows:
        icao_addr = r.pop("icao_addr")
        grouped.setdefault(icao_addr, []).append(r)

    return jsonify(grouped)

from flask import request

@app.post("/api/aircraft/update")
def insert_aircraft_data():
    data = request.get_json(force=True)
    required = ["icao_addr", "lat", "lon", "altitude", "ground_speed", "heading", "ts"]
    if not all(k in data for k in required):
        return {"error": f"Missing fields; required: {required}"}, 400

    # Insert into aircraft_latest
    q("""
        INSERT INTO aircraft_latest (icao_addr, lat, lon, altitude, ground_speed, heading, last_seen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (icao_addr)
        DO UPDATE SET
            lat = EXCLUDED.lat,
            lon = EXCLUDED.lon,
            altitude = EXCLUDED.altitude,
            ground_speed = EXCLUDED.ground_speed,
            heading = EXCLUDED.heading,
            last_seen = EXCLUDED.last_seen
    """, [data["icao_addr"], data["lat"], data["lon"], data["altitude"],
          data["ground_speed"], data["heading"], data["ts"]])

    # Also store in aircraft_positions (history)
    q("""
        INSERT INTO aircraft_positions (icao_addr, ts, lat, lon, ground_speed, heading, altitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, [data["icao_addr"], data["ts"], data["lat"], data["lon"],
          data["ground_speed"], data["heading"], data["altitude"]])

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
