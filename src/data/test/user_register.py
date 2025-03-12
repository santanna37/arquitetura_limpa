from typing import Dict

class UserRegisterSpy:
    def __init__(self) -> None:
        self.atributes = {}

    def register(self, first_name: str, last_name: str, age:int) -> Dict:
        self.atributes["first_name"] = first_name
        self.atributes["last_name"] = last_name
        self.atributes["age"] = age
        self.atributes["id"] = 1

        return {
            "type":"Users",
            "count": 1,
            "attributes": [{"first_name":first_name,
            "last_name": last_name,
            "age": age
            }
            ]                                                                 
        }