from datetime import datetime, timezone, timedelta
def unix_to_utc(unix_timestamp):
  dt_utc = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
  return dt_utc