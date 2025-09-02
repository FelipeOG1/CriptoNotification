import os
import requests
from dotenv import load_dotenv
from .utils.dates import unix_to_utc
load_dotenv()

HEADERS = {"x-cg-demo-api-key":os.getenv("CRIPTO_KEY"),"accept": "application/json"}
BASE_URL = os.getenv("CRIPTO_SIMPLE_URL")

class Coin():
  def __init__(self,cripto_id,base_currencie=None):
    self.base_currencie = base_currencie if base_currencie is not None else "usd"
    self.cripto_id = cripto_id 
    self.HEADERS = HEADERS
    self.BASE_URL = BASE_URL

  @staticmethod
  def _base_request(url, method = "get",data = None, params = None):
    try:
      response = None
      match(method.lower()):
        case "get":
          response = requests.get(url,headers = HEADERS,data = data ,params = params,timeout=5)
        case "post":
          response = requests.post(url,headers = HEADERS,data = data ,params = params,timeout = 5)
        case _:
          raise ValueError(f"Unsupported method: {method}")         
      if response.status_code == 200 or response.status_code ==202:     
        return {"status": response.status_code, "content":response.json()}
      else:
        return {"status": response.status_code, "content":response.text}

    except Exception as e:
        return {"status": 500, "content": str(e)}
  def get_current_price(self,coins:list):
    from urllib.parse import quote
    coins = [coin.capitalize() for coin in coins]
    cripto_names_encoded = quote(",".join(coins))
    price_url = f"{self.BASE_URL}?vs_currencies={self.base_currencie}&names={cripto_names_encoded}"
    response = Coin._base_request(price_url,"get")
    return response["content"]
  @staticmethod
  def coin_exist(coin_name:str)->bool:
    coin_name = coin_name.capitalize()
    URL = os.getenv("CRIPTO_COIN_LIST_URL")
    response = Coin._base_request(URL,method="get")
    if response["status"] == 200:
      probables  = set([coin["name"] for coin in response.get("content") if coin["name"].startswith(coin_name)])   
      if len(probables) == 0:
        print("No se encontro ninguna moneda con ese nombre")
        return False
      if coin_name in probables:return True

      print("No se encontro esa moneda")
      print(f"Monedas similares :f{probables} ")
      return False
    print(response)
    return False
  
  
