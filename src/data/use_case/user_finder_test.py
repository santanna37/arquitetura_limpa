from src.infra.db.tests.user_repository_test import UserRepositoryTest
from .user_finder import UserFinder


def test_find():
    first_name = 'MeuNome'
    repo = UserRepositoryTest()
    user_finder =UserFinder(repo)

    response = user_finder.find(first_name)

    print(response)

def test_find_erro_alpha(): 
    first_name = 'MeuNome123'
    repo = UserRepositoryTest()
    user_finder =UserFinder(repo)

    try: 
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome Inválido: números no nome"

def test_find_erro_len():
    first_name = "MeuNomeqwertyuiopçlkjgfds"
    repo = UserRepositoryTest()
    user_finder =UserFinder(repo)

    try: 
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome Inválido: Tamanho do nome excede o limite"

def test_find_erro_search():
    
    class UserRepositoryError(UserRepositoryTest):
        def select_user(self, first_name: str):
            return []

    first_name = "MeuNome"
    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try: 
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome Inválido: Nome não encontrado"