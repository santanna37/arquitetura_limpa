from abc import ABC, abstractclassmethod
from typing import Dict


class UserRegister(ABC):

    @abstractclassmethod
    def register(
        self,
        fisrt_name:str,
        last_name: str,
        age: int

        ) -> Dict: pass 