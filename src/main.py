from src.facade.user_facade import UserFacade
from src.facade.vacation_facade import vacationFacade

class GeneralUser:
    def __init__(self):
        self.userFacade = UserFacade()
        self.data = None
        self.vacationFacade = vacationFacade()
    def Login(self):
        user_data = self.userFacade.login_user()
        dic = user_data[0]
        self.data = dic
    def Register(self):
        self.userFacade.register_user()
    def get_role(self):
        dic = self.data
        role = dic["role_id"]
        return role 
    def get_user_data(self):
        return self.data

class Admin(GeneralUser):
    def __init__(self , data):
        super().__init__() 
        self.data = data
    def add_vacation(self):
        self.vacationFacade.add_vacation()
    def edit_vacation(self):
        self.vacationFacade.update_vacation()
    def delete_vacation(self):
        self.vacationFacade.delete_vacation() 

class User(GeneralUser):
    def __init__(self , data):
        super().__init__()
        self.data = data
    def view_all_vacations(self):
        self.vacationFacade.view_all_vacations()
    def view_all_liked_vacations(self):
        dic = self.data
        self.vacationFacade.view_liked_vacations(dic["user_id"])
    def give_like(self):
        dic = self.data
        self.vacationFacade.give_like_to_vacation(dic["user_id"])
    def give_unlike(self):
        dic = self.data
        self.vacationFacade.give_unlike_to_vacation(dic["user_id"])
    

continue_program = True
loged = False
type_user = 0
while continue_program:
    if not loged:
        gUser = GeneralUser()
        print("Hello and welcome to our vacations system!! :)")
        print("Type the number next to the function you want to execute. ")
        print("1.Log in")
        print("2.Register")
        print("3.Exit system")
        print() 
        while True: 
            try:
              choise = int(input("Please enter your choise: "))
              if choise != 1 and choise!=2 and choise!=3:
                  raise ValueError
              break
            except Exception as e:
                print("Your choise must be nomeric 1 - 3")
        if choise == 1:   
          gUser.Login()
          loged = True
        elif choise == 2:
            gUser.Register() 
        else: 
            continue_program = False
    
    if loged:
        if gUser.get_role() == 2:
            user = User(gUser.get_user_data())
            type_user = 2
        else: 
            admin = Admin(gUser.get_user_data())
            type_user = 1
    
    if type_user == 2:
        print("\nYour functions (Type the number next to the function you want to execute, 1-5): ")
        print("1.View all vacations.")
        print("2.Like vacation.")
        print("3.Unlike vacation.")
        print("4.View your liked vacations.")
        print("5.Exit") 
        print()
        while True:
            try:
                choise = int(input("Please enter your choise: "))
                if choise <1 or choise > 5:
                    raise ValueError
                break
            except Exception as e:
                print("Your choise must be nomeric 1 or 2") 
        if choise ==1 :
            user.view_all_vacations()
        if choise == 2:
            user.give_like()
        if choise == 3:
            user.give_unlike()
        if choise == 4:
            user.view_all_liked_vacations()
        if choise == 5:
            type_user = 0 
            loged = False
    
    if type_user == 1:
        print("\nYour functions (Type the number next to the function you want to execute, 1-4): ")
        print("1.Add vacation.")
        print("2.Edit vacation.")
        print("3.Delete vacation.")
        print("4.Exit")
        print() 
        while True:
            try:
                choise = int(input("Please enter your choise: "))
                if choise <1 or choise > 5:
                    raise ValueError
                break
            except Exception as e:
                print("Your choise must be nomeric 1 or 2") 
        
        if choise == 1:
            admin.add_vacation()
        if choise == 2:
            admin.edit_vacation()
        if choise == 3:
            admin.delete_vacation()
        if choise == 4:
            type_user = 0
            loged = False
            
            
            
    
        

        
        





# class User:
#     def __init__(self):
#         self.user_facade = UserFacade()
#         self.data = {}
#     def Login(self):
#         res = self.user_facade.login_user()
#         self.data = res[0]  
#     def getData(self):
#         return self.data
        
# class Guest:
#     def __init__(self , data):
#         self.likesLogic = LikesLogic()
#         self.vacationLogic = VacationLogic()
#         self.data = data
#     def getLikedVacations(self):
#         res = self.likesLogic.view_user_liked_vacations(self.data["user_id"])
#         for vacation in res:
#             print(f"{vacation["vacation_title"]}")
#     def giveLike(self):
#         res = VacationLogic.view_all_vacations()
#         for vac in res:
#             print(f"{vac["vacation_title"]}")
        
#         vacation = input("Please enter vacation title you want to like: ")
#         while True:
#             if self.vacationLogic.find_vacation(vacation):
#                 self.likesLogic.like_vacation(self.data["user_id"] , vacation)
#                 break
#             else: 
#                 print("The vacation you entered is not valid.")
#                 vacation = input("Please enter vacation title you want to like: ")
#     def giveUnLike(self):
#         res = VacationLogic.view_all_vacations()
#         for vac in res:
#             print(f"{vac["vacation_title"]}")
#         vacation = input("Please enter vacation title you want to unlike: ")
#         while True:
#             if self.vacationLogic.find_vacation(vacation):
#                 self.likesLogic.unlike_vacation(self.data["user_id"] , vacation)
#                 break
#             else: 
#                 print("The vacation you entered is not valid.")
#                 vacation = input("Please enter vacation title you want to like: ")   
#     def viewAllVacations(self):
#         res = VacationLogic.view_all_vacations()
#         for vac in res:
#             print(f"{vac["vacation_title"]}") 
#     def viewAllLikedVacation(self):
#         res = LikesLogic.view_user_liked_vacations(self.data["user_id"])
#         for vac in res:
#             print(f"{vac["vacation_title"]}")

# print("Hello and welcome to our vacation system!")
# print()
# print("1.Login")
# print("2.Legister")
# print()

# while True:
#     try:
#         op = int(input("Please enter an option (1 or 2): "))
#         if op == 1 or op == 2:
#             break
#         else:
#             print("Enter the number next to the operation you want to execute (1 or 2).")
#     except ValueError:
#         print("Your choice must be numeric.") 
# if op ==1 :
#     user = User()
#     user.Login() 
#     role = user.getData()["role_id"]
    
#     if role == 1:
#         g = Guest(user.getData())
#         op = 0
#         print()
#         print("1.View all vacations.")
#         print("2.Like vacation.")
#         print("3.Unlike vacation.")
#         print("4.view all liked vacations.")
#         print("5.Log out")
#         print()
#         while True:
#          try:
#             op = int(input("Please enter your option (1-5): "))
            
#          except Exception as e:
#             print("Please enter the options presented infront of you.")
#          if op==1:
#             g.viewAllVacations()
#          if op==2:
#             g.giveLike()
#          if op == 3:
#             g.giveUnLike()
#          if op ==4:
#             g.viewAllLikedVacation()
    
    
    
        
    

