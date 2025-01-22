from src.utils.dal import DAL
import bcrypt

class UserLogic:
     def __init__(self):
        self.dal = DAL() 
     def __enter__(self):
        return self
     def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()
     def user_register(self , first_name , last_name , email , password , date_of_birth ):
            if self.find_user(email) == True:
                print("This user already exists.")
                return False
            
            password = str(password)
            passwordb = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password = passwordb , salt = salt)
            
            query = """
            INSERT INTO vacationsdatabase.users 
            (first_name , last_name , email , password , date_of_birth ,role_id)
            VALUES 
            (%s, %s, %s, %s, %s , %s )
            """
            params = (first_name , last_name , email , hashed_password , date_of_birth , 2)
            try:
              self.dal.insert(query, params)
              return True
            except Exception as e:
                print(f"There was error to register: {e}")
                return False
            
     def find_user(self , email):
         try: 
             query = "SELECT * FROM vacationsdatabase.users where email = %s"
             params = (email,)
             result = self.dal.get_table(query , params)
             if result:
                 return True
             return False
         except Exception as err:
             print(f"There was an error: {err}")
             
     def login_user(self , email , password):
         if(self.find_user(email) == False):
             print("This user doesn't exists")
             return False
         query = "Select * from vacationsdatabase.users where email = %s"
         params = (email,)
         result = self.dal.get_table(query , params)
         dic = result[0]
         hashed_password = dic["password"].encode('utf-8')
         
         password = str(password)
         passwordb = password.encode('utf-8')
         
         if bcrypt.checkpw(passwordb , hashed_password):
             print("Loged in")
             return result
         
     def find_user_role(self, id):
         query = "select u.role_id from users u where u.user_id = %s"
         params = (id,)
         result = self.dal.get_table(query , params)
         return result
         
     
        
if __name__=="__main__":
    ul = UserLogic()
    #ul.user_register("bob" ,"taylor" ,"bob.taylor@example.com" , "hashed_password_4" , "1980-07-24" , "1")
    #ul.user_register("ronen" , "shotlender" , "ronenshot2006@gmail.com" , "R123456" , "2006-05-08")
    ul.login_user("ronenshot2006@gmail.com" , "R123456")