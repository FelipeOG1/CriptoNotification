from pathlib import Path
import os
from sqlite3 import sqlite3,Connection,Error
from typing import Optional
from ..user import User
class Database:
    """
    db gonnaa have username,cellphone,registercoins,
    """
    def __init__(self,db_name):
       self.conn = self.start_conn(db_name)
       self.cursor = self.conn.cursor()
        
    def start_conn(self,db_name:str)->Optional[Connection]:
       try:
         return sqlite3.connect(f"{db_name}.db")
         
       except Error as e:
           print("Error creating db")
           return None
       
    

