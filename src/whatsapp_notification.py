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
    def send_notification(self,coin_name:str,coin_price:int,action:str)->None:
        assert action in ("vender,comprar"),f"accion {action} no es valida "
        base_url = f"https://graph.facebook.com/v22.0/{os.getenv('WHATSAPP_IDENTIFIER')}/messages"
        base_headers = {
                "Authorization": f"Bearer {os.getenv("WHATSAPP_KEY")}",
                "Content-Type": "application/json"
        }
        payload = {
        "messaging_product": "whatsapp",
        "to": self.phone_number,
        "type": "template",
        "template": {
            "name": "cripto_noti",   
            "language": {"code": "en"},  
            "components": [
                {
                    "type": "BODY",
                    "parameters": [
                        {"type": "text", "text": coin_name},   # {{1}}
                        {"type": "text", "text": coin_price},  # {{2}}
                        {"type": "text", "text": action} # {{3}}
                    ]
                }
            ]
        }
    }
        send_response = requests.post(base_url, json = payload,headers = base_headers)
        if send_response.status_code == 200:
            print(f"Notificacion enviada con exito al numero {self.phone_number}")
        
