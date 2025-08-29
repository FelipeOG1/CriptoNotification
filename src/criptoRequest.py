import os
import requests
from dotenv import load_dotenv
from utils.dates import unix_to_utc
load_dotenv()

HEADERS = {"x-cg-demo-api-key":os.getenv("CRIPTO_KEY"),"accept": "application/json"}
BASE_URL = os.getenv("CRIPTO_SIMPLE_URL")

class CriptoRequest():
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
  def get_current_price(self):
    price_url = f"{self.BASE_URL}?vs_currencies={self.base_currencie}&ids={self.cripto_id}&include_last_updated_at=true"
    response = CriptoRequest._base_request(price_url,"get")
    if response["status"] not in {200,202} :return response["content"]
    res = response.get("content")
    id = self.cripto_id.lower()
    price = res.get(id).get(self.base_currencie)
    last_updated = res.get(id).get("last_updated_at")
    last_updated_utc = unix_to_utc(last_updated)
    fecha_str = last_updated_utc.strftime("%Y-%m-%d")  
    hora_str = last_updated_utc.strftime("%H:%M:%S")
    return {"Message":"Sucess","Price":price,"last_uptadted":f"{fecha_str} {hora_str}"}

  @staticmethod
  def find_coin_id(coin_name):
    coin_name = coin_name.capitalize()
    URL = os.getenv("CRIPTO_COIN_LIST_URL")
    response = CriptoRequest._base_request(URL,method="get")
    if response["status"] == 200:
      probables  = set([coin["id"] for coin in response.get("content") if coin["name"].startswith(coin_name)])
      message = "success"
      if len(probables) == 0:
        message = "No se encontro ninguna moneda con ese nombre"
      return {"Message":message,"status" : response["status"],"content":probables}
    return response
  
