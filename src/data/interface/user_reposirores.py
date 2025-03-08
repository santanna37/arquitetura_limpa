from abc import ABC, abstractmethod
from typing import List
from src.domain.models.user_models import UserModels

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name:str, age:int) -> None: pass


    @abstractmethod
    def select_user(self, fisrt_name: str) -> List[UserModels]: pass
       