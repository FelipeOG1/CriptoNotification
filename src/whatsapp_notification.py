#WHATSAPP DOCS:https://developers.facebook.com/docs/whatsapp/cloud-api/?locale=es_ES
from .criptoRequest import CoinsUtils
from dotenv import load_dotenv
from .notification import Notification
from typing import Union
import requests
import os
load_dotenv()
class WhatsappNotification:
    def __init__(self,phone_number:str,type_notification:str):
        self.phone_number = phone_number
        self.type_notification = type_notification
        
    def send_notification(self,coin_name:str,coin_price:int)->None:
        base_url = f"https://graph.facebook.com/v22.0/{os.getenv('WHATSAPP_IDENTIFIER')}/messages"
        base_headers = {
                "Authorization": f"Bearer {os.getenv("WHATSAPP_KEY")}",
                "Content-Type": "application/json"
        }
        match(self.type_notification):
         case "sell":
            message = f"Es buen momento para vender {coin_name} tiene un precio de {coin_price}"
         case "buy":
            message = f"Es buen momento para comprar ahora {coin_name} tiene un precio de {coin_price}"
         case _:
              print(f"No se soporta el evento {self.type_notification}")
              return 
        send_message_body = {
             "messaging_product": "whatsapp",
             "to":self.phone_number,
             "type":"text",
             "text":{
                 "body":message
            }
            }
        
        send_response = requests.post(base_url, json = send_message_body,headers = base_headers)
        print(send_response.status_code)   
         
        
         
        
        
