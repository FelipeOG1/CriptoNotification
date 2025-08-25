import os
import requests
from dotenv import load_dotenv
from utils.dates import unix_to_utc
load_dotenv()

HEADERS = {"x-cg-demo-api-key":os.getenv("CRIPTO_KEY"),"accept": "application/json"}
BASE_URL = os.getenv("CRIPTO_SIMPLE_URL")

class CriptoRequest():
  def __init__(self,cripto_code,base_currencie=None):
    self.base_currencie = base_currencie if base_currencie is not None else "usd"
    self.cripto_code = cripto_code
    self.HEADERS = HEADERS
    self.BASE_URL = BASE_URL 

  def get_price(self):
    price_url = f"{self.BASE_URL}?vs_currencies={self.base_currencie}&symbols={self.cripto_code}&include_last_updated_at=true"
    try:
      response = requests.get(price_url,self.HEADERS,timeout=5)
    except Exception as e:
      print(f"exception happened {e}")
    if response.status_code == 200:
      res = response.json()
      price = res.get(self.cripto_code).get(self.base_currencie)
      last_updated = res.get(self.cripto_code).get("last_updated_at")
      last_updated_utc = unix_to_utc(last_updated)
      fecha_str = last_updated_utc.strftime("%Y-%m-%d")  
      hora_str = last_updated_utc.strftime("%H:%M:%S")
      return {"Message":"Sucess","Price":price,"last_uptadted":f"{fecha_str} {hora_str}"}
    else:
      return {"Mesasge":response.text,"status":response.status_code} 
  

   
  
  
    
