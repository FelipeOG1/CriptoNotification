from pathlib import Path
import os
import sqlite3
class Database:
    """
    db gonnaa have username,cellphone,registercoins,
    """
    def __init__(self,db_name):
       self.conn = self.start_conn(db_name)
       self.cursor = self.conn.cursor()
        
    def start_conn(self,db_name):
       conn = sqlite3.connect(f"{db_name}.db")
       return conn
   
   def create_tables(self,user):
       self.cursor.execute()
       
   

       
    


  
        
            
            
        
        



               

        
       



