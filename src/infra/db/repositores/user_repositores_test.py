from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositores.user_repositores import UsersRepository


db_connection_handler = DBConnectionHandler()
conection = db_connection_handler.get_engine().connect()

def test_insert_user():
    fisrt_name = 'test_insert'
    last_name = 'test_last_inset'
    age = 44

    user_repositores = UsersRepository()
    user_repositores.insert_user(fisrt_name,last_name,age)

    sql =''' 
        SELECT * FROM users
        WHERE  first_name = '{}' 
    '''.format(fisrt_name)

    response = conection.execute(text(sql))
    registry = response.fetchall()

    print()
    print(registry)