from src.domain.models.user_models import UserModels
from typing import List



class UserRepositoryTest():
    
    def __init__(self) -> None:
        self.insert_user_atributes = {}
        self.select_user_atributes = {}

    def insert_user(self,first_name: str, last_name: str, age:int) -> None: 
        self.insert_user_atributes["first_name"] = first_name
        self.insert_user_atributes["last_name"] = last_name 
        self.insert_user_atributes["age"] = 10
        self.insert_user_atributes["id"] = 2
        return self.insert_user_atributes["first_name"] 


    def select_user(self, first_name: str) -> List[UserModels]:
        self.select_user_atributes["first_name"] = first_name
        return[
            UserModels(first_name= first_name, last_name= "test_repository_1", age= 21, id = 2),
            UserModels(first_name= first_name, last_name= "test_repository_2", age= 21, id = 3)
        ]