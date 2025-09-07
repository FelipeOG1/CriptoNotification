import threading
import time
from .criptoRequest import CoinsUtils
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
from .notification import Notification
from .criptoRequest import CoinsUtils

def get_notifications(pendings,prices,db):  
  for coin_name in prices:
    coin_price = prices[coin_name]["usd"]
    for pen in pendings:
      if pen["coin_name"] == coin_name:
        if coin_price>pen["sell"]:
            phone_number = db.get_phone_number(pen["user_id"])
            if phone_number:
                notification = WhatsappNotification(phone_number)
                notification.send_notification(coin_name,coin_price,"vender")
        elif coin_price<pen["buy"]:
            phone_number = db.get_phone_number(pen["user_id"])
            if phone_number:  
                notification = WhatsappNotification(phone_number)
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
        print("No se tienen notificaciones para enviar")
        
        
if __name__ == "__main__":
    db = Database("CriptoNotifier")
    r = db._execute("select * from users")
    s= db._execute("select * from notifications")
    db.add_user(User("Felipe","85793284","506"))
    db.add_user(User("Saul","85793304","506"))
    

    """
    h1 = threading.Thread(target = main_loop,args = (5,),daemon=True)  
    h1.start()
    
    while(True):
        time.sleep(300)
    
    """    
       
    
    
    
