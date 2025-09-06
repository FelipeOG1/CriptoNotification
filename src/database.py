from pathlib import Path
import os
import sys
import sqlite3
from sqlite3 import Connection,Error
from typing import Optional,Union
from .user import User
from .notification import Notification 


    def get_user_id(self,phone_number:str)->Optional[int]:
        user_id = self._execute("SELECT id FROM users WHERE phone_number = ?;",(phone_number,))
        if user_id:
            return user_id[0][0]
        return None
    from .user import User
    def add_user(self,user:User)->None:
        if not isinstance(user,User):
            raise TypeError(f"Expected a user and recived {type(user).__name__}")
        if self.get_user_id(user.username):
            print("user already exist")
            return 
        user_values = tuple(user.__dict__.values())
        result = self._execute("INSERT INTO users (username, phone_number, phone_extension_code) VALUES (?, ?, ?);",user_values)
        print("Usuario insertado de manera correcta")
        
    def add_notification(self,notification:Notification)->None:
        if not isinstance(notification,Notification):
            raise TypeError(f"Expected a user and recived {type(notification).__name__}")
        noti_values = tuple(notification.__dict__.values())
        self._execute("INSERT into notifications (user_id,coin_name,sell,buy) VALUES(?,?,?,?)",noti_values)
    def get_pending_notifications(self)->list[dict]:
        res = self._execute("SELECT * from notifications where notified = 0")
        return res
    
    def get_phone_number(self,user_id:int)->Optional[str]:
        result = self._execute("SELECT phone_number,phone_extension_code from users where id = ?",(user_id,))
        if result:
           phone = result[0]["phone_number"]
           extension = result[0]["phone_extension_code"]
           result = f"{extension}{phone}"
           return result
       
    
      
        
