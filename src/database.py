from pathlib import Path
import os
import sys
import sqlite3
from sqlite3 import Connection,Error
from typing import Optional
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
        username TEXT NOT NULL,
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
    
   
    def _execute(self,query:str,query_tuple = None)->bool:
        
        status = False
        last_row :int = self.cursor.lastrowid
        self.cursor.execute(query,query_tuple)
        new_last_row :int = self.cursor.lastrowid
        return [last_row,new_last_row]
        if new_last_row > last_row:
            
            status = True
        
        self.connection.commit()
        return status

    def add_user(self,user)->None:
         
        print(user.username)
        
        
        pass
     


