from typing import Dict

class UserFinderSpy:
    def __init__(self) -> None:
        self.atributes = {}

    def find(self, first_name: str) -> Dict:
        self.atributes["first_name"] = first_name 

        return {
            "type":"Users",
            "count": 1,
            "attributes": [{"first_name":first_name,
            "last_name": "lalala"}
            ]                                                                 
        }