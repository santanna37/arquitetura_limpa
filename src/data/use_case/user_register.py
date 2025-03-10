from src.domain.use_case.user_register import UserRegister as UserRegisterInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict, List
from src.domain.models.user_models import UserModels


class UserRegister(UserRegisterInterface):

    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = user_repository

    def register(self, first_name:str, last_name:str, age:int) -> Dict:
        self.__registry_user(first_name, last_name, age)
    
    def __registry_user(self, first_name:str, last_name:str, age:int) -> Dict:
        self.__users_repository.insert_user(
            first_name = first_name,
            last_name = last_name,
            age = age
            )
        


