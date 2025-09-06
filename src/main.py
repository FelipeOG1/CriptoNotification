from .criptoRequest import CoinsUtils
import os
import sys
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
from .notification import Notification
from .criptoRequest import CoinsUtils
def get_notifications(pendings,prices):  
  for coin_name in prices:
    coin_price = prices[coin_name]["usd"]
    for pen in pendings:
      if pen["coin_name"] == coin_name:
        if coin_price>pen["sell"]:
            phone_number = db.get_phone_number(pen["user_id"])
            if phone_number:
                notification = WhatsappNotification(phone_number,"sell")
                notification.send_notification(coin_name,coin_price)
        elif coin_price<pen["buy"]:
            phone_number = db.get_phone_number(pen["user_id"])
            if phone_number:  
                notification = WhatsappNotification(phone_number,"buy")
                notification.send_notification(coin_name,coin_price)
            continue    

if __name__ == "__main__":
    db = Database("CriptoNotifier")
    pendings = db.get_pending_notifications()
    coin_names = set([x["coin_name"] for x in pendings])
    prices = CoinsUtils.get_current_price(coin_names)
    print(prices)
    get_notifications(pendings,prices)
    
    
