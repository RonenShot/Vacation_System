from src.utils.dal import DAL

class LikesLogic:
    def __init__(self):
        self.dal = DAL()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()
    def like_vacation(self , user_id , vacation_id):
        query = "select * from vacationsdatabase.likes l where l.user_id = %s and l.vacation_id = %s"
        params = (user_id , vacation_id)
        result = self.dal.get_table(query , params)
        if len(result)!=0:
            print("This user already liked this vacation.")
            return False
            
        query = "select * from vacationsdatabase.vacations v where v.vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_table(query , params)
        
        current_likes_dic = result[0]
        current_likes = current_likes_dic["total_likes"]
        current_likes+=1
        
        query = "insert into vacationsdatabase.likes (user_id , vacation_id) values (%s , %s)"
        params = (user_id , vacation_id)
        self.dal.insert(query , params)
        
        query = "update vacationsdatabase.vacations v set v.total_likes = %s where v.vacation_id = %s"
        params = (current_likes , vacation_id)
        self.dal.update(query , params) 
        
    def unlike_vacation(self , user_id , vacation_id):
        query = "select * from vacationsdatabase.likes l where l.user_id = %s and l.vacation_id = %s"
        params = (user_id , vacation_id)
        result = self.dal.get_table(query , params)
        if len(result)==0:
            print("This user didn't gave a like for this vacation.")
            return False
            
        
        query = "select * from vacationsdatabase.vacations v where v.vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_table(query , params)
        
        current_likes_dic = result[0]
        current_likes = current_likes_dic["total_likes"]
        current_likes-=1
        
        query = "delete from vacationsdatabase.likes l where l.user_id = %s and l.vacation_id = %s"
        params = (user_id , vacation_id)
        self.dal.delete(query , params)
        
        query = "update vacationsdatabase.vacations v set v.total_likes = %s where v.vacation_id = %s"
        params = (current_likes , vacation_id)
        self.dal.update(query , params) 
    
    def view_user_liked_vacations(self , user_id):
        query = "select * from vacationsdatabase.likes l inner join vacationsdatabase.vacations v on l.vacation_id = v.vacation_id where l.user_id = %s"
        params = (user_id,)
        result = self.dal.get_table(query , params)
        return result


if __name__ == "__main__":
    l = LikesLogic()
    liked_vacations  = l.view_user_liked_vacations(12) 
    for like in liked_vacations:
        print(f"name: {like["vacation_title"]}")