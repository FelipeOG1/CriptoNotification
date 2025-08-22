import os
import requests
from dotenv import load_dotenv
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
    price_url = f"{self.BASE_URL}?vs_currencies={self.base_currencie}&symbols={self.cripto_code}"
    response = requests.get(price_url,self.HEADERS)
    print(price_url)
    return response.json().get(self.cripto_code).get(self.base_currencie)
  
  
    
