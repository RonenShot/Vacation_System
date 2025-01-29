from src.logic.vacation_logic import VacationLogic
from src.logic.like_logic import LikesLogic
import datetime
class vacationFacade:
    def __init__(self):
        self.vacationLogic = VacationLogic()
        self.likesLogic = LikesLogic()
        
    def vacation_title(self):
      title  = input("enter a title for your vacation: ")
      while True:
        if title is not None:
            return title
        
    def vacation_image_url(self):
      url  = input("enter an image url: ")
      while True:
        if url is not None:
            return url
        
    def vacation_description(self):
      description  = input("enter a description for your vacation: ")
      while True:
        if description is not None:
            return description
     
        
    
    def start_date_check(self):
        cur_date = datetime.date.today()
        while True:
            try:
                start_date_input = input("Enter the vacation's beginning (YYYY-MM-DD):\n")
                start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
                
                count =0
                for ch in start_date_input:
                    if ch.isdigit():
                        count+=1
                if count!=8:
                    raise ValueError

                if start_date > cur_date:
                    
                    return start_date 
                else:
                    print("The start date must be in the future.")
                 
                

            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")

    def end_date_check(self, start_date):
        while True:
            try:
                end_date_input = input("Enter the vacation's end (YYYY-MM-DD):\n")
                end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()
                count =0
                for ch in end_date_input:
                    if ch.isdigit():
                        count+=1
                if count!=8:
                    raise ValueError

                if start_date < end_date:
                    return end_date
                else:
                    print("The end date must be after the start date.")
                    
                
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")

    def price_check(self):
      while True:
        price_input = input("Enter the price of the vacation: ")
        
        try:
            price = int(price_input) 
            if 1000 <= price <= 10000: 
                return price
            else:
                print("The price must be between 1000 and 10000.")
                 
            
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")
    
    def country_check(self):
      while True:
        country = input("Please enter the name of the country: ").strip()

        
        if not country.replace(" " ,"").isalpha():
            print("Invalid country name. Please enter a valid name.")
        else:
            
            result = self.vacationLogic.find_country(country)
            if len(result)>0:
                dic = result[0]
                return dic["country_id"] 
            else:
                print("Not exist country in the database.")
            
            
    def add_vacation(self):
        params = []
        params.append(self.vacation_title())
        params.append(self.start_date_check())
        params.append(self.end_date_check(params[-1]))
        params.append(self.price_check())
        params.append(self.country_check())
        params.append(self.vacation_image_url())
        params.append(self.vacation_description())
        if self.vacationLogic.find_exists_vacation(*params):
            print("This vacation already exists.")
            return False
        else:
          return self.vacationLogic.add_vacation(*params) 
    
    def delete_vacation(self):
        while True:
            try:
                id = int(input("Please enter id of vacation for delete: "))
                res = self.vacationLogic.find_vacation(id)
                if len(res) == 0:
                    print("Id nummber must represent exist vacation.")
                else:
                    valid_vacation = True
                    break
            except Exception as e:
                print("Id nummber must be numeric.")
        res =  self.vacationLogic.delete_vacation(id)
        
        if res:
            print("Vacation removed successfuly.")
        else: 
            print("Vacation didn't removed. might be wrong vacation id.")
    
    def update_vacation(self):
        valid_vacation = False
        while True:
            try:
                id = int(input("Please enter id of vacation for edit: "))
                res = self.vacationLogic.find_vacation(id)
                if len(res) == 0:
                    print("Id nummber must represent exist vacation.")
                else:
                    valid_vacation = True
                    break
            except Exception as e:
                print("Id nummber must be numeric.")
        if valid_vacation:
            valid_fields = ['vacation_title' , 'start_date' , 'end_date' , 'price' , 'country_id' , 'image_url' , 'description']
            params = {}
            while True:
                print("\nEnter the fields you want to update for the vacation:")
                print("Available fields: vacation_title, start_date, end_date, price, country_id,  image_url, description")
                print("To finish, just press Enter without typing anything.")
                field = input("Enter the field name (or press Enter to finish): ").strip()
                if not field:
                    break    
                if field not in valid_fields:
                    print(f"'{field}' is not a valid field. Please try again.")
                    continue  
                if field == "vacation_title":  
                    params["vacation_title"] = self.vacation_title()
                if field == "start_date" or field == "end_date":
                    params["start_date"] = self.start_date_check()
                    params["end_date"] = self.end_date_check(params["start_date"])
                if field == "price":
                    params["price"] = self.price_check()
                if field == "country_id":
                    params["country_id"] = self.country_check()
                if field == "image_url":
                    params["image_url"] = self.vacation_image_url()
                if field == "description":
                    params["description"] = self.vacation_description()
            if len(params) >0:
               return  self.vacationLogic.edit_vacation(id , **params)   
        
    
    def view_all_vacations(self):
        vacations =  self.vacationLogic.view_all_vacations()
        for vacation in vacations:
            print(f"ID vacation: {vacation["vacation_id"]}")
            print(f"Vacation title: {vacation["vacation_title"]}")
            print(f"Start date: {vacation["start_date"]}")
            print(f"End date: {vacation["end_date"]}")
            print(f"Price: {vacation["price"]}")
            print(f"Total likes: {vacation["total_likes"]}")
            res = self.vacationLogic.find_country_name(vacation["country_id"])
            dic = res[0]
            country = dic["country_name"]
            print(f"Country: {country}")
            print(f"Description: {vacation["description"]}\n")
    
    def give_like_to_vacation(self , id_user):
        valid_vacation = False
        while True:
            try:
                id = int(input("Please enter id of the vacation you want to like: "))
                res = self.vacationLogic.find_vacation(id)
                if len(res) == 0:
                    print("Id nummber must represent exist country.")
                else:
                    valid_vacation = True
                    break
            except Exception as e:
                print("Id nummber must be numeric ") 
        if valid_vacation:
            return self.likesLogic.like_vacation(id_user , id)
    
    def give_unlike_to_vacation(self , id_user):
        valid_vacation = False
        while True:
            try:
                id = int(input("Please enter id of the vacation you want to unlike: "))
                res = self.vacationLogic.find_vacation(id)
                if len(res) == 0:
                    print("Id nummber must represent exist country.")
                else:
                    valid_vacation = True
                    break
            except Exception as e:
                print("Id nummber must be numeric and represnt exist vacation.") 
        if valid_vacation:
            return self.likesLogic.unlike_vacation(id_user , id)
    
    def view_liked_vacations(self , id_user):
        vacations = self.likesLogic.view_user_liked_vacations(id_user)
        for vacation in vacations:
            print(f"ID vacation: {vacation["vacation_id"]}")
            print(f"Vacation title: {vacation["vacation_title"]}")
            print(f"Start date: {vacation["start_date"]}")
            print(f"End date: {vacation["end_date"]}")
            print(f"Price: {vacation["price"]}")
            print(f"Total likes: {vacation["total_likes"]}")
            res = self.vacationLogic.find_country_name(vacation["country_id"])
            dic = res[0]
            country = dic["country_name"]
            print(f"Country: {country}")
            print(f"Description: {vacation["description"]}\n")
        
            
             
if __name__ == "__main__":
    vf = vacationFacade()
    while True:
        print("1.vacation title")
        print("2.vacation image url")
        print("3.vacation description")
        print("4.start date")
        print("5.end date")
        print("6.price")
        print("7.country check")
        print("8.add vacation")
        print("9.update vacation")
        print("10.delete vacatio")
        print("11.view all vacations")
        print("12.give like")
        print("13.give unlike")
        print("14.view liked vacations")
        print("15.exit")
        while True:
            try: 
                op = int(input("Please enter number of function to execute: "))
                if op<1 or op>15:
                    print("not exist function")
                else:
                    break
            except Exception as e:
                print("not valid input") 
        if op ==1:
            print(vf.vacation_title())
        if op ==2:
            print(vf.vacation_image_url())
        if op ==3:
            print(vf.vacation_description())
        if op ==4:
            print(vf.start_date_check())
        if op ==5:
            print(vf.end_date_check(vf.start_date_check()))
        if op ==6:
            print(vf.price_check())
        if op ==7:
            print(vf.country_check())
        if op ==8:
            print(vf.add_vacation())
        if op ==9:
            print(vf.update_vacation())
        if op ==10:
            print(vf.delete_vacation())
        if op ==11:
            print(vf.view_all_vacations())
        if op ==12:
            print(vf.give_like_to_vacation(104))
        if op==13:
            print(vf.give_unlike_to_vacation(104))
        if op ==14:
            print(vf.view_liked_vacations(104))
        if op ==15:
            break
    
