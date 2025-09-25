-- retention.sql
-- Delete old rows (older than 24 hours by default)

-- SQLite:
-- DELETE FROM aircraft_positions
-- WHERE ts < datetime('now', '-24 hours');

-- PostgreSQL:
-- DELETE FROM aircraft_positions
-- WHERE ts < NOW() - INTERVAL '24 hours';
