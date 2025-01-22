import mysql.connector
import os
class DAL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = os.getenv('DB_PASSWORD'),
            database = "vacationsdatabase",
            autocommit = True
            )
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            
            self.connection = None
    def validate_query_params(self,query , params):
        if not isinstance(query,str):
            raise ValueError("query must be a string")
        if params is not None and not isinstance(params,tuple):
            raise ValueError("params must be a tuple or None")
    
    def execute_query(self , query , params = None , fetchall=False , fetchone = False):
        self.validate_query_params(query , params)
        if self.connection:
            try:
                with self.connection.cursor(dictionary = True) as cursor:
                    print(f"executing query: {query}")
                    if params:
                        print(f"with parameters: {params}")
                    cursor.execute(query,params)
                    if fetchall:
                        result = cursor.fetchall()
                        print(f"fetched {len(result)} rows")
                        return result
                    if fetchone:
                        result = cursor.fetchone() 
                        print("fetched one row")
                        return result
                    else:
                        print(f"Query affected {cursor.rowcount} rows")     
            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")
    def get_table(self,query,params=None):
        return self.execute_query(query , params , fetchall=True)
    def get_scalar(self , query , params=None):
        return self.execute_query(query,params , fetchone=True)
    def insert(self,query , params=None):
        return self.execute_query(query , params)
    def update(self,query,params):
        return self.execute_query(query , params)
    def delete(self,query,params):
        return self.execute_query(query , params)
    def close(self):
        if self.connection:
            self.connection.close()
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.connection:
            self.close()
            print("connection closed!")
if __name__=="__main__":
    with DAL() as dal:
        print("\n===get tableexamples===")
        countries = dal.get_table("SELECT * FROM countries")
        users = dal.get_table("SELECT * FROM users")
        for country in countries:
            print(f"country name: {country["country_name"]}")
        for user in users:
            print(f"User name: {user["first_name"]} , Last name: {user["last_name"]}")
