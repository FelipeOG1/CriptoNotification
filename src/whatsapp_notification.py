#WHATSAPP DOCS:https://developers.facebook.com/docs/whatsapp/cloud-api/?locale=es_ES
from .criptoRequest import CoinsUtils
from dotenv import load_dotenv
from .notification import Notification
from typing import Union
import requests
import os

    
load_dotenv()
class WhatsappNotification:
    def __init__(self,phone_number:str):
        self.phone_number = phone_number
        self.base_url = f"https://graph.facebook.com/v22.0/{os.getenv('WHATSAPP_IDENTIFIER')}/messages"
        self.base_headers = {
                "Authorization": f"Bearer {os.getenv("WHATSAPP_KEY")}",
                "Content-Type": "application/json"
        } 
    def send_message(self,message:str):
         send_message_body = {
             "messaging_product": "whatsapp",
             "to":self.phone_number,
             "type":"text",
             "text":{
                 "body":message
            }
            }
         send_response = requests.post(self.base_url, json = send_message_body,headers = self.base_headers)
         print(send_response.text)
         print(self.base_headers)
    from .user import User
    from .database import Database
    def create_notification(user_message:dict,user:User)->None:
       db = Database("CriptoNotifier")
       user_id = db.get_user_id(user.username)
      
        
        
        
        
         
        
       
        
        
