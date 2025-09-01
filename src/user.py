from typing import Optional

class User:
    "memory coins have is map with coin id as key and array with cell notifiation as index 0 and buy notification as  index 1 "
    def __init__(self,username:str,phone_number:int,phone_extension:int):
        self.username = username
        self.phone_number = phone_number
        self.phone_extension = phone_extension
    def add_coin(self,coin_name,sell,buy)->Optional[list]:
        from .criptorequest import CriptoRequest
        from .databse import Database
        db = Database("coins_db")
        
        response = CriptoRequest.find_coin_id(coin_name)
        if response["status"] not in {200,202} :return response["content"]
        results = response["content"]
        if len(results)>0:
            if coin_name in results:
                "add to db"
                self.coins[coin_name] = {"sell":32131.3,"buy":30.000}
                print("Moneda agregada con exito")
                return self.coins
                pass
            print("No se encontro la moneda dentro de los probables, seguro la escribio bien?")
            print(f"Monedas similares: {results}")
            return None
        
        print(response["Message"])
        return None

    def show_coins(self):
        print(self.coins)
        

        
           
       

    

    
