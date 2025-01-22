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
    
    # av = v.view_all_vacations()
    # for vacation in av:
    #     print(f"title: {vacation["vacation_title"]} , country_id: {vacation["country_id"] }, name:{vacation["country_name"]}")
    
    # country_vacations = v.view_all_vacations_in_country("USA")
