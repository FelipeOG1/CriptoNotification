from typing import Optional

class User:
    "memory coins have is map with coin id as key and array with cell notifiation as index 0 and buy notification as  index 1 "
    def __init__(self,username:str,phone_number:str,phone_extension:str):
        self.username = username
        self.phone_number = phone_number
        self.phone_extension = phone_extension
        
