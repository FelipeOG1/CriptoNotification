from pathlib import Path
import os
import sys
import sqlite3
from sqlite3 import Connection,Error
from typing import Optional,Union
from .user import User
from .notification import Notification 
class Database:
    def __init__(self,db_name:str):
        self.connection = self.start_connection(db_name)
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
    def _create_tables(self):
        self._execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT,
            username TEXT,
            phone_extension TEXT
        )
        """)
        self._execute("""
        CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        coin_name TEXT,
        sell INTEGER,
        buy INTEGER,
        notified int DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """)         
    def start_connection(self,db_name: str) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(f"{db_name}.db")
            conn.row_factory = sqlite3.Row
            return conn
        except Error as e:
            print(f"Error creating db {db_name}: {e}")
            raise

    def _execute(self,query:str,query_tuple:Optional[tuple] = None)->list:
        if query_tuple:
            self.cursor.execute(query,query_tuple)
        else:
            self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
        
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
        result = self._execute("INSERT INTO users (username, phone_number, phone_extension) VALUES (?, ?, ?);",user_values)
        self.connection.commit()
        
    def add_notification(self,notification:Notification)->None:
        if not isinstance(notification,Notification):
            raise TypeError(f"Expected a user and recived {type(notification).__name__}")
        noti_values = tuple(notification.__dict__.values())
        self._execute("INSERT into notifications (user_id,coin_name,sell,buy) VALUES(?,?,?,?)",noti_values)
        self.connection.commit()
        
    def get_pending_notifications(self)->list[dict]:
        res = self._execute("SELECT * from notifications where notified = 0")
        return res
    
    def get_phone_number(self,user_id:int)->Optional[str]:
        result = self._execute("SELECT phone_number,phone_extension from users where id = ?",(user_id,))
        if result:
           phone = result[0]["phone_number"]
           extension = result[0]["phone_extension"]
           result = f"{extension}{phone}"
           return result
       
    def get_all_users(self)->list:
      
      return self._execute("SELECT * FROM users")


    def get_all_notifications(self)->list:
        
      return self._execute("SELECT * FROM notifications")

        
