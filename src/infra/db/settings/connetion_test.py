from .connection import DBConnectionHandler
from sqlalchemy import text




def test_create_engine_database():
    db_connection = DBConnectionHandler()

    engine = db_connection.get_engine()

    # conn = engine.connect()
    # conn.execute(
    #     text("insert into users(first_name, last_name, age ) values ('test_conexcao', 'teste', 32 )")
    # )

    # conn.commit()


    print ('=======')
    print(' ')

    print(engine)

