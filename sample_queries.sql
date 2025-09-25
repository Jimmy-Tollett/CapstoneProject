-- sample_queries.sql

-- Active aircraft (last 5 minutes)
-- SQLite:
-- SELECT * FROM aircraft_latest
-- WHERE last_seen >= datetime('now', '-5 minutes')
-- ORDER BY last_seen DESC;

-- PostgreSQL:
-- SELECT * FROM aircraft_latest
-- WHERE last_seen >= NOW() - INTERVAL '5 minutes'
-- ORDER BY last_seen DESC;

-- Track for one aircraft since a timestamp
-- SQLite:
-- SELECT * FROM aircraft_positions
-- WHERE icao_addr = :icao AND ts >= :since
-- ORDER BY ts ASC;

-- PostgreSQL:
-- SELECT * FROM aircraft_positions
-- WHERE icao_addr = $1 AND ts >= $2
-- ORDER BY ts ASC;

-- Bounding box filter
-- SQLite:
-- SELECT * FROM aircraft_positions
-- WHERE ts >= :since
--   AND lon BETWEEN :minLon AND :maxLon
--   AND lat BETWEEN :minLat AND :maxLat;

-- PostgreSQL:
-- SELECT * FROM aircraft_positions
-- WHERE ts >= $1
--   AND lon BETWEEN $2 AND $3
--   AND lat BETWEEN $4 AND $5;
