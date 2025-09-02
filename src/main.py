from .criptoRequest import Coin
import os
import sys
from .database import Database
from .user import User
if __name__ == "__main__":
    if Coin.coin_exist("chainlink"):
        coin = Coin("chainlink")
        print(coin.get_current_price(["solana","bitcoin"]))
  
  
