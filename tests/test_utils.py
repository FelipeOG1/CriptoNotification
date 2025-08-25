from datetime import datetime,timezone
from utils.dates import unix_to_utc
class TestUtils:
  def test_unixd_to_cr(self):
    sample  = datetime(2025, 8, 23, 5, 40, 0, tzinfo=timezone.utc)
    assert unix_to_utc(1755927600) == sample
    ""
    