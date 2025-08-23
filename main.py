from criptoRequest import CriptoRequest
from utils import unix_to_utc
if __name__ == "__main__":
  instance = CriptoRequest("usd","btc")
  print(instance.get_price())