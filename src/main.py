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
    noti = Notification(1,"Solana",198,200)
    pendings = db.get_pending_notifications()
    coin_names = set([x["coin_name"] for x in pendings])
    prices = CoinsUtils.get_current_price(coin_names)
    def get_notifications(pendings,prices):  
        for coin_name in prices:
            coin_price = prices[coin_name]["usd"]
            for pen in pendings:
                if pen["coin_name"] == coin_name:
                    if pen["sell"]>coin_price:
                        print('vendeee')
                        print(f"precio a vender {pen['sell']}")
                        print(f"precio actual de {coin_name}: {coin_price}")
                    elif pen["buy"]<coin_price:
                        print("compraaa")
                        
    
    get_sell_notifications(pendings,prices)
       
