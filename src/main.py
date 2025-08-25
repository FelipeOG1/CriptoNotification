from criptoRequest import CriptoRequest


if __name__ == "__main__":
  cripto = CriptoRequest("btc")
  print(cripto.get_price())
  