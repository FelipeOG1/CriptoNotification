from .criptoRequest import CoinsUtils
import os
import sys
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
from .notification import Notification
from .criptoRequest import CoinsUtils
if __name__ == "__main__":
    db = Database("CriptoNotifier")
    user = User("Felipe","85793284","506")
    
    """
    coin_names = set([x[1] for x in pendings])
    prices = CoinsUtils.get_current_price(coin_names)
    user_id = 5
    coin_name = 1
    buy_price = 2
    sell_price = 3
    print(pendings)
    pending_notis = {}
    for elem in pendings:
        uid = elem[user_id]
        coin = elem[coin_name]
        prices = (elem[buy_price], elem[sell_price])
        if uid not in pending_notis:
            pending_notis[uid] = {}          
        pending_notis[uid][coin] = prices
    """
        
   
