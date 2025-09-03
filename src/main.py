from .criptoRequest import CoinsUtils
import os
import sys
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
if __name__ == "__main__":
   prices = CoinsUtils.get_current_price(["solana","bitcoin"])
   w = WhatsappNotification("50685793304")
   for elem in prices:
       key = elem
       price = elem["usd"]
       print(price)

