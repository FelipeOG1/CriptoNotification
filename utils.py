from datetime import datetime, timezone, timedelta


def unix_to_cr(unix_timestamp):
  dt_utc = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
  costa_rica_tmz = dt_utc.astimezone(timezone(timedelta(hours=-6)))
  return costa_rica_tmz