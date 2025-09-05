from pathlib import Path
import os
import sys
import sqlite3
from sqlite3 import Connection,Error
from typing import Optional,Union
from .user import User
from .notification import Notification 

class Database:
    """
    db gonnaa have username,cellphone,registercoins,
    """
    def __init__(self,db_name):
       self.connection = self.start_connection(db_name)
       self.cursor = self.connection.cursor()
      
    def start_connection(self,db_name:str)->Optional[Connection]:
       try:
         conn = sqlite3.connect(f"{db_name}.db") 
         conn.row_factory = sqlite3.Row
         return conn
       except Error as e:
           print("Error creating db")
           
           return None
       
    def create_tables(self)->None:
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        phone_number TEXT NOT NULL,
        phone_extension_code TEXT NOT NULL
        )
        ''')
          
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin_name TEXT NOT NULL,
        sell INT DEFAULT 0,
        buy INT DEFAULT 0,
        notified BOOLEAN DEFAULT 0,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')       
        self.connection.commit()
    
    def _execute(self,query:str,query_tuple = None)->list:
        status = False
        if query_tuple:
            self.cursor.execute(query,query_tuple)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_user_id(self,phone_number:str)->Optional[int]:
        user_id:int =self._execute("SELECT id FROM users WHERE phone_number = ?;",(phone_number,))
        if user_id:
            return user_id[0][0]
        return user_id
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
        self._execute("INSERT into notifications (user_id,coin_id,sell,buy) VALUES(?,?,?,?)",noti_values)
    
    def get_pending_notifications(self)->list[tuple[Notification,...]]:
        res = self._execute("SELECT * from notifications where notified = 0")
        return res
        
    
    
      
        
