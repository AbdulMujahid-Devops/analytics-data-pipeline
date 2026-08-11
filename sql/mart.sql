-- Analytics KPI mart
SELECT
  event_date,
  service,
  COUNT(*) AS event_count,
  SUM(CASE WHEN status <> 'success' THEN 1 ELSE 0 END) AS failed_events,
  ROUND(AVG(duration_ms), 2) AS avg_duration_ms,
  ROUND(100.0 * SUM(CASE WHEN status <> 'success' THEN 1 ELSE 0 END) / COUNT(*), 2) AS error_rate_pct
FROM events
GROUP BY event_date, service
ORDER BY event_date, service;
