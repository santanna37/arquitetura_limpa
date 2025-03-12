from src.infra.db.tests.user_repository_test import UserRepositoryTest
from .user_register import UserRegister



def test_register():
    first_name = "ola"
    last_name = "last"
    age = 32 

    
    repo = UserRepositoryTest()
    user_register =UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    print("===")
    print(response)


