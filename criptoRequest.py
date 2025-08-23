import os
import requests
from dotenv import load_dotenv
from utils import unix_to_utc
load_dotenv()

HEADERS = {"x-cg-demo-api-key":os.getenv("CRIPTO_KEY"),"accept": "application/json"}
BASE_URL = os.getenv("CRIPTO_SIMPLE_URL")
class CriptoRequest:
  def __init__(self,base_currencie,cripto_code):
    self.base_currencie = base_currencie
    self.cripto_code = cripto_code
    self.HEADERS = HEADERS
    self.BASE_URL = BASE_URL
  def get_price(self):
    price_url = f"{self.BASE_URL}?vs_currencies={self.base_currencie}&symbols={self.cripto_code}&include_last_updated_at=true"
    response = requests.get(price_url,self.HEADERS)
    res = response.json()
    price = res.get(self.cripto_code).get(self.base_currencie)
    #TODO: fix unix_to_cr
    last_updated = res.get(self.cripto_code).get("last_updated_at")
    print(unix_to_utc(last_updated))
    return {"price":price,"last_uptadted":last_updated}    
  
  
    
