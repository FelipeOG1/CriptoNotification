from .criptoRequest import CoinsUtils
import os
import sys
from .database import Database
from .user import User
from .whatsapp_notification import WhatsappNotification
if __name__ == "__main__":
    db = Database("CriptoNotifier")
    user = User("Felipe","85793284","506")
    pending = db.get_notifications()
    
    
    
    #TODO:create the new user_workflow and later create the already registered coins worflow
       
    
