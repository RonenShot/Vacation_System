from src.logic.user_logic import UserLogic
import re
import datetime
class UserFacade:
    def __init__(self):
        self.params = []
        self.UserLogic = UserLogic()
    def getFirstName(self):
        valid = False
        while not valid:
            check = True
            name = input("Please enter your first name: ")
            if len(name)<=1:
                check = False
            for ch in name:
                if ch.isalpha() == False:
                    check = False
            valid = check
            if not valid:
                print("Your name can only consist alphbetic letters and at least two chars")
            else:
                return name
           
            
    def getLastName(self):
        valid = False
        while not valid:
            check = True
            name = input("Please enter your last name: ")
            if len(name)<=1:
                check = False
            for ch in name:
                if ch.isalpha() == False:
                    check = False
            valid = check
            if not valid:
                print("Your name can only consist alphbetic letters and at least two chars")
            else: 
                return name
            
            
    def email_check(self):
      Email = input("Enter your email: ")
      regex = r'\b[A-Za-z0-9.%+-]+@+[A-Za-z0-9.%+-]+.com\b'
      while True:
        if re.fullmatch(regex, Email):  # Check if the email matches the pattern
            return Email
        print("Your email is not correct.")
        Email = input("Enter your email again: ")
        
    def password_check(self):
      while True:
        password = input("Enter your password: ")
        upperCase = False
        number = False
        for ch in password:
            if ch.isupper():  
                upperCase = True
            elif ch.isdigit():  
                number = True
        if upperCase and number and len(password) > 5:
            return password  
        else:
            print("Password is invalid. It must contain at least one uppercase letter, one number, and be longer than 5 characters.")
            
    def date_of_birth_check(self):
      cur_date = datetime.date.today()  
    
      while True:
        try:
            
            birthday_input = input("Enter your birthday (YYYY-MM-DD):\n")
            birthday = datetime.datetime.strptime(birthday_input, "%Y-%m-%d").date()  
            
            count =0
            for ch in birthday_input:
                if ch.isdigit():
                    count+=1
            if count!=8:
                raise ValueError
            
            if birthday <= cur_date :
                
                return birthday  
            else:
                print("Your birthday cannot be in the future. Please enter a valid date.")
        
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
    
    def register_user(self):
        params = []
        params.append(self.getFirstName())
        params.append(self.getLastName())
        params.append(self.email_check())
        params.append(self.password_check())
        params.append(self.date_of_birth_check()) 
        
        if self.UserLogic.find_user(params[2]):
            print("This user already exists.")
            return False
        
        return self.UserLogic.user_register(*params)
    def login_user(self):
        while True:
          id = self.email_check()
          if not self.UserLogic.find_user(id):
              print("This user don't exist.")
          else:
             while True:
                try:
                    password = self.password_check()  
                    res = self.UserLogic.login_user(id, password) 

                    if len(res) == 1:
                        return res  
                    else:
                        print("Login failed. Please try again.")  

                except Exception as e:
                    print(f"Wrong password.")  
    
        
                            
                        
                   
        
        
                
    
                    
                    
if __name__ == "__main__":
    uf = UserFacade()
    while True:
        while True:
            print("1.get first name")
            print("2.get last name")
            print("3.get email")
            print("4.get password")
            print("5.get date of birth")
            print("6.register")
            print("7.login")
            print("8.exit")
            try:
                op = int(input("Please enter number of function to execute: "))
                if op <1 or op>8:
                    print("not exitst function")
                else:
                    break
            except Exception as e:
                print("Not valid input")
        if op ==1:
            print(uf.getFirstName())
        if op==2:
            print(uf.getLastName())
        if op==3:
            print(uf.email_check())
        if op==4:
            print(uf.password_check())
        if op==5:
            print(uf.date_of_birth_check())
        if op ==6:
            print(uf.register_user())
        if op ==7:
            print(uf.login_user())
        if op ==8:
            break
            
    
    
    