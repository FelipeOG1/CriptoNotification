from .criptoRequest import CoinsUtils
import os
import sys
from .database import Database
from .user import User
if __name__ == "__main__":
        print(CoinsUtils.get_current_price(["solana","bitcoin"]))
        

    #TODO : create notification class 
