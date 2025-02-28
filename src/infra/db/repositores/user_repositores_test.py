from src.infra.db.repositores.user_repositores import UsersRepository


def test_insert_user():
    fisrt_name = 'test_insert'
    last_name = 'test_last_inset'
    age = 44

    user_repositores = UsersRepository()
    user_repositores.insert_user(fisrt_name,last_name,age)