from criptoRequest import CriptoRequest

if __name__ == "__main__":
  instance = CriptoRequest("usd","btc")
  print(instance.get_price())