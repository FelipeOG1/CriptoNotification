from .criptoRequest import CriptoRequest
import os
import sys
from .database import Database
from .user import User
if __name__ == "__main__":
  db = Database("coins_db")
  user = User("martin",394930903,1)
  mama = "mama"
  db.add_user(user)
  
