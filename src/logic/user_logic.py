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
    while True:
        print("1.Register user")
        print("2.login user")
        print("3.find user")
        while True:
            try:
                op = int(input("Please enter number of function: "))
                if op <1 or op>3:
                    print("Not exist function")
                else:
                    break 
            except Exception as e:
                print("Not valid input")
            if op ==1:
                print(ul.user_register(first_name="example user" , last_name="example last name user" , email="userexample@gmail.com" , password="user123456" , date_of_birth="2020-12-12"))
            if op==2:
                print(ul.login_user("ronenuser@gmail.com" , "R123456"))
            if op==3:
                ul.find_user("ronenuser@gmail.com")
                
            