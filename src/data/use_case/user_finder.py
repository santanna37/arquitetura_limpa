from src.domain.use_case.user_finder import UserFinder as UserFinderInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict, List
from src.domain.models.user_models import UserModels  # Certifique-se de importar UserModels corretamente

class UserFinder(UserFinderInterface):
    
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name=first_name)
        users = self.__search_user(first_name=first_name)
        response = self.__format_response(users=users)
        return response 

    @classmethod
    def __validate_name(cls, first_name: str):
        if not first_name.isalpha():
            raise Exception("Nome Inválido: números no nome")

        if len(first_name) > 18:
            raise Exception("Nome Inválido: Tamanho do nome excede o limite")

    def __search_user(self, first_name: str) -> List[UserModels]:
        users = self.__users_repository.select_user(first_name=first_name)  # Corrigido erro de atribuição
        if not users:
            raise Exception("Nome Inválido: Nome não encontrado")
        return users

    @classmethod
    def __format_response(cls, users: List[UserModels]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({
                "first_name": user.first_name,
                "age": user.age
            })

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes  # Corrigido nome do campo
        }

        return response
