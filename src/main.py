from criptoRequest import CriptoRequest
if __name__ == "__main__":
  cripto = CriptoRequest("Bitcoin")
  print(cripto.get_current_price())
  print("mama")
  print(cripto.find_coin_id("Solana"))