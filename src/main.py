import threading
import time
from .criptoRequest import CoinsUtils
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
from .notification import Notification
from .criptoRequest import CoinsUtils
import sqlite3
import os
def get_notifications(pendings,prices,db:Database):  
  for coin_name in prices:
    coin_price = prices[coin_name]["usd"]
    for pending in pendings:
      if pending["coin_name"] == coin_name:
        if coin_price>pending["sell"]:
            phone_number = db.get_phone_number(pending["user_id"])
            if phone_number:
                notification = WhatsappNotification(phone_number,pending["id"])
                notification.send_notification(coin_name,coin_price,"vender")
        elif coin_price<pen["buy"]:
            phone_number = db.get_phone_number(pending["user_id"])
            if phone_number:  
                notification = WhatsappNotification(phone_number,pending["id"])
                notification.send_notification(coin_name,coin_price,"comprar")
        continue 

def main_loop(time_sleep:int):
    while(True):
        time.sleep(time_sleep)
        db = Database("CriptoNotifier")
        pendings = db.get_pending_notifications()
        if pendings:
            coin_names = set([x["coin_name"] for x in pendings])
            prices = CoinsUtils.get_current_price(coin_names)
            get_notifications(pendings,prices,db)
        else:
            print("No existen notificaiones pendintes")
            
if __name__ == "__main__":
    print(f"Initating process with id {os.getpid()}")
    db = Database("CriptoNotifier")
    h1 = threading.Thread(target = main_loop,args = (5,),daemon=True)  
    h1.start()
    print("thread iniciado")
    while(True):
        time.sleep(300)
    
     
       
    
    
    
