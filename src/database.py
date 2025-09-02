from pathlib import Path
import os
import sys
import sqlite3
from sqlite3 import Connection,Error
from typing import Optional,Union
from .user import User
class Database:
    """
    db gonnaa have username,cellphone,registercoins,
    """
    def __init__(self,db_name):
       self.connection = self.start_connection(db_name)
       self.cursor = self.connection.cursor()
    def start_connection(self,db_name:str)->Optional[Connection]:
       try:
         return sqlite3.connect(f"{db_name}.db")
       except Error as e:
           print("Error creating db")
           return None
       
    def create_tables(self)->None:
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        phone_number INTEGER NOT NULL,
        phone_extension_code INTEGER
        )
        ''')
          
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin_id TEXT NOT NULL,
        sell REAL DEFAULT 0,
        buy REAL DEFAULT 0,
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
        return self.cursor.fetchall() 
    
    def get_user_id(self,username:str)->Optional[int]:
        user_id:int =self._execute("SELECT id FROM users WHERE username = ?;",(username,))[0][0]
        return user_id
    
    from .user import User
    def add_user_db(self,user:User)->None:
        if not isinstance(user,User):
            raise TypeError(f"Expected a user and recived {type(user).__name__}")
        if self.get_user_id(user.username)>0:
            print("user already exist")
            return 
        user_values = tuple(user.__dict__.values())
        result = self._execute("INSERT INTO users (username, phone_number, phone_extension_code) VALUES (?, ?, ?);",user_values)
        print("Usuario insertado de manera correcta")
    def add_coin_db(self,coin_id:str,username:str,sell:int,buy:int):
        pass
        
        
