-- schema.postgres.sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS aircraft_latest (
  icao_addr     CHAR(6) PRIMARY KEY,
  callsign      TEXT,
  lat           DOUBLE PRECISION NOT NULL CHECK (lat BETWEEN -90 AND 90),
  lon           DOUBLE PRECISION NOT NULL CHECK (lon BETWEEN -180 AND 180),
  ground_speed  DOUBLE PRECISION CHECK (ground_speed >= 0),
  heading       DOUBLE PRECISION CHECK (heading >= 0 AND heading < 360),
  altitude      DOUBLE PRECISION,
  last_seen     TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS aircraft_positions (
  id            BIGSERIAL PRIMARY KEY,
  icao_addr     CHAR(6) NOT NULL REFERENCES aircraft_latest(icao_addr) ON DELETE CASCADE,
  ts            TIMESTAMPTZ NOT NULL,
  lat           DOUBLE PRECISION NOT NULL CHECK (lat BETWEEN -90 AND 90),
  lon           DOUBLE PRECISION NOT NULL CHECK (lon BETWEEN -180 AND 180),
  ground_speed  DOUBLE PRECISION CHECK (ground_speed >= 0),
  heading       DOUBLE PRECISION CHECK (heading >= 0 AND heading < 360),
  altitude      DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS idx_positions_icao_ts
  ON aircraft_positions (icao_addr, ts DESC);
