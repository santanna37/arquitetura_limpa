from src.domain.use_case.user_finder import UserFinder as UserFinderInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict


class UserFinder(UserFinderInterface):
    
    def __init__(self,users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        
        if not first_name.isalpha():
            raise Exception("Nome invalido")
        
        if len(first_name) > 18:
            raise Exception("Nome grande")

        users == self.__users_repository.select_user(first_name)
        if users == []:
            raise Exception("Nome não encontrado")

        response ={
            "type": "Users",
            "count":len(users),
            "atributes": users  
        }

        retur response 