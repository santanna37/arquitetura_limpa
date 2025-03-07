from src.domain.use_case.user_finder import UserFinder as UserFinderInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict


class UserFinder(UserFinderInterface):
    
    def __init__(self,user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def find(self, first_name: str) -> Dict:
        pass 