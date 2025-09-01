from typing import Optional

class User:
    "memory coins have is map with coin id as key and array with cell notifiation as index 0 and buy notification as  index 1 "
    def __init__(self,username:str,phone_number:int,phone_extension:int):
        self.username = username
        self.phone_number = phone_number
        self.phone_extension = phone_extension
        
    def add_coin(self,coin_name,sell,buy)->Optional[list]:
        from .criptorequest import CriptoRequest
        coin_is_valid = CriptoRequest.coin_is_valid()
        if coin_is_valid:   
            from .databse import Database
            db = Database("coins_db")
            db.add_coin()
        
    def _add_user_to_db(self):
        
        pass
           
       

    

    
