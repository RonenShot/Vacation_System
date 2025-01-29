from src.utils.dal import DAL

class VacationLogic:
    def __init__(self):
        self.dal = DAL()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()
    def view_all_vacations(self):
        query = "select * from vacationsdatabase.vacations v inner join vacationsdatabase.countries c on v.country_id = c.country_id"
        result = self.dal.get_table(query)
        return result
    def view_all_vacations_in_country(self , country_name):
        query = "select * from vacationsdatabase.countries c where c.country_name = %s"
        params =(country_name,)
        result = self.dal.get_table(query ,params)
        
        if result == None:
            print("There are no vacations in this destenation.")
            return False
        
        id_dictionary = result[0]
        id = id_dictionary["country_id"]
        query = "select * from vacationsdatabase.vacations v inner join vacationsdatabase.countries c where v.country_id = c.country_id and v.country_id = %s"
        params = (id,)
        result = self.dal.get_table(query , params)
        return result
    def add_vacation(self , vacation_title , start_date , end_date , price  , country_id ,  image_url , description ):
        query = "insert into vacationsdatabase.vacations (vacation_title , start_date , end_date , price , total_likes ,country_id, image_url , description) values(%s , %s , %s , %s , %s , %s , %s , %s)"
        params = (vacation_title , start_date , end_date , price , 0 ,country_id , image_url , description)
        try:
          self.dal.insert(query , params) 
          return True
        except Exception as e:
            print(f"There was an error to add vacation: {e}")
            return False
    def delete_vacation(self , id):
        query = "delete from vacationsdatabase.vacations where vacation_id = %s"
        params = (id,)
        try:
            result = self.dal.delete(query , params)
            return True
        except Exception as e:
            print(f"There was an error deleting vacation {e}")
            return False 
    def edit_vacation(self, id, **kwargs):
        if not kwargs:
            return False
        clause = ", ".join([f"{k} = %s" for k in kwargs.keys()])

        params = tuple(kwargs.values()) + (id,)
        query = f"UPDATE vacationsdatabase.vacations SET {clause} WHERE vacation_id = %s"

        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating vacation: {e}")
            return False 
    def find_country(self , country_name):
        query = "select * from vacationsdatabase.countries where country_name = %s"
        params = (country_name,)
        result = self.dal.get_table(query , params)
        return result  
    
    def find_country_name(self, id):
        query = "select * from vacationsdatabase.countries where country_id = %s"
        params = (id,)
        result  = self.dal.get_table(query , params)
        return result
    
    def find_vacation(self , id):
        query = "select * from vacationsdatabase.vacations v where v.vacation_id =%s"
        params = (id,)
        result = self.dal.get_table(query , params)
        return result 
    def find_exists_vacation(self , vacation_title , start_date , end_date , price , country_id ,  image_url , description):
        query = "select * from vacationsdatabase.vacations v where v.vacation_title = %s and v.start_date = %s and v.end_date = %s and v.price = %s and v.country_id = %s and v.image_url = %s and v.description = %s"
        params1 = (vacation_title , start_date , end_date , price  , country_id ,  image_url , description)
        result = self.dal.get_table(query , params1)
        
        if len(result)==0:
            return False
        else: 
            return True
    
    
    

        

if __name__ == "__main__":
    v = VacationLogic()
    while True:
        
        while True:
            print("1.view all vacations")
            print("2.add vacation")
            print("3.edit vacation")
            print("4.delete vacation")
            print("5.find country")
            print("6.find country name")
            print("7.find vacation")
            print("8.find exist vacation")
            print("9.exit")
            try:
              op = int(input("please enter number of function: "))
              if op <1 or op >9:
                  print("not an exist function")
              else:
                  break
            except Exception as e:
                print("Not valid input")
        
        if op == 1:
            print(v.view_all_vacations())
        if op == 2:
            print(v.add_vacation("example vacation" , "2025-12-12" , "2025-12-13" , "5000" , 12 , "image example" , "description example"))
        if op==3:
            print(v.edit_vacation(vacation_title="example vacation1" , start_date="2025-12-13" , end_date="2025-12-14" , price="5001" , country_id=12 , image_url="image example1" , description="description example1"))
        if op==4:
            print(v.delete_vacation())
        if op ==5:
            print(v.find_country("USA"))
        if op == 6:
            print(v.find_country_name(12))
        if op ==7:
            print(v.find_vacation(1))
        if op ==8:
            print(v.find_exists_vacation(vacation_title="Ski Adventure" , start_date="2025-12-15" , end_date="2025-12-22" , price="2000" , country_id=2 , image_url="https://example.com/ski.jpg" , description="Enjoy skiing in the snowy mountains of Canada."))
        if op ==9:
            break
            
   