from src.domain.use_case.user_finder import UserFinder as UserFinderInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict, List
from src.errors.types import HttpBadRequest, HttpNotFound


class UserFinder(UserFinderInterface):
    
    def __init__(self,users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name = first_name)
        users = self.__search_user(first_name = first_name)
        response = self.__formart_response(users = users)
        return response 

    @classmethod
    def __validate_name(cls, first_name: str):
        if not first_name.isalpha():
            raise HttpBadRequest("Nome Inválido: números no nome")

        if len(first_name) > 18:
            raise HttpBadRequest("Nome_invalido: Tamanho do nome")
        
    def __search_user(self, first_name: str) -> List:
        users = self.__users_repository.select_user(first_name = first_name)
        if users == []:
            raise HttpNotFound("Nome Inválido: Nome não encontrado")
        return users

    @classmethod
    def __formart_response(cls, users: List) -> Dict:
        atributes = []
        for user in users:
            atributes.append({
                "first_name": user.first_name,
                "age": user.age
            })

        response = {
            "type": "Users",
            "count": len(users),
            "atributes": atributes
        }

        return response 