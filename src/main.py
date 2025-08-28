from criptoRequest import CriptoRequest
from user import User
if __name__ == "__main__":
  cripto = CriptoRequest("Bitcoin")
  new_user =User("martin","+506 3313188") 
  print(new_user.add_coin("solana",33,33))
   

  
