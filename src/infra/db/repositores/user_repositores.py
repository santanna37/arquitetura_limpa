from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user_entities import UsersEntities 


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name:str, age:int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_user = UsersEntities(
                    first_name = first_name,
                    last_name  = last_name,
                    age = age

                )
                database.add(new_user)
                database.commit()
                print(new_user)
                

            except Exception as exception: 
                database.rollback()
                print(exception)
                raise exception
                

            finally:
                print('acabou')
                database.close()


    @classmethod
    def select_user(cls, fisrt_name: str) -> any: 
        with DBConnectionHandler() as database: 
            try: 
                users = (
                    database.query(UsersEntities)
                    .filter(UsersEntities.first_name == first_name)
                    .all()
                )
                return users
            
            except Exception as exception: 
                database.rollback()
                print(exception)
                raise exception
                
            finally:
                print('acabou')
                database.close()