-- schema.sqlite.sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS aircraft_latest (
  icao_addr     TEXT PRIMARY KEY,
  callsign      TEXT,
  lat           REAL NOT NULL CHECK (lat BETWEEN -90 AND 90),
  lon           REAL NOT NULL CHECK (lon BETWEEN -180 AND 180),
  ground_speed  REAL CHECK (ground_speed >= 0),
  heading       REAL CHECK (heading >= 0 AND heading < 360),
  altitude      REAL,
  last_seen     DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS aircraft_positions (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  icao_addr     TEXT NOT NULL,
  ts            DATETIME NOT NULL,
  lat           REAL NOT NULL CHECK (lat BETWEEN -90 AND 90),
  lon           REAL NOT NULL CHECK (lon BETWEEN -180 AND 180),
  ground_speed  REAL CHECK (ground_speed >= 0),
  heading       REAL CHECK (heading >= 0 AND heading < 360),
  altitude      REAL,
  FOREIGN KEY (icao_addr) REFERENCES aircraft_latest(icao_addr)
);

CREATE INDEX IF NOT EXISTS idx_positions_icao_ts
  ON aircraft_positions (icao_addr, ts);
